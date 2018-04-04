from flask import g, Flask, redirect, request, render_template
from ridi.cms.config import Config as CmsConfig
from ridi.cms.cms_client import AdminAuth
from ridi.cms.login_session import LoginSession, COOKIE_CMS_TOKEN

config = CmsConfig()
config.RPC_URL = 'http://localhost'
admin_auth = AdminAuth(config)

app = Flask(__name__, static_url_path='/example/static')

@app.before_request
def authorize():
    # Serve static files without authorization.
    if request.path.startswith('/example/static') and request.method == 'GET':
        return None

    # Once login is successful, a login cookie is set by CMS.
    # App should provide the token from the cookie.
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

# Retrieve menus for the user.
@app.route('/example/user/menus/')
def menu():
    user = g.get('user', None)
    menu_items = admin_auth.getAdminMenu(user.getAdminId())
    return render_template('index.html', menu_items=list(map(lambda x: x.__dict__, menu_items)))

if __name__ == "__main__":
    # If the port changes, './cms/.env' file also needs to be updated.
    app.run(host="127.0.0.1", port=8080, threaded=True)
