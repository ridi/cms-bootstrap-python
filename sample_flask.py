from flask import g, Flask, redirect, request
from ridi.cms.Config import Config as CmsConfig
from ridi.cms.CmsClient import AdminAuth
from ridi.cms.LoginSession import LoginSession, COOKIE_CMS_TOKEN

config = CmsConfig()
config.RPC_URL = 'http://localhost'
admin_auth = AdminAuth(config)

app = Flask(__name__)


@app.before_request
def authorize():
    # Once login is successful, a login cookie is set by CMS.
    # App should provide the token in cookies.
    token = request.cookies.get(COOKIE_CMS_TOKEN)
    user = LoginSession(config, token)
    setattr(g, 'user', user)

    # Authorize the user with the token and see if the user is allowed for the path.
    if not admin_auth.authorize(user, request.path):
        login_url = admin_auth.getLoginUrl(request.path)
        return redirect(login_url)
    return None

# The app route path can be customized in './cms/.env'
@app.route('/example/home/')
def index():
    return 'Hello CMS!'

# Retrieve munus for the user.
@app.route('/example/user/menus/')
def menu():
    user = g.get('user', None)
    menus = admin_auth.getAdminMenu(user.getAdminId())
    return str(list(map(lambda m: (m.menu_title, m.menu_url), menus)))

if __name__ == "__main__":
    # If the port changes, './cms/.env' file also needs to be updated.
    app.run(host="127.0.0.1", port=8080, threaded=True)
