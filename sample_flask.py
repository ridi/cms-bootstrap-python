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

# inject user menu data before every template rendering
@app.context_processor
def inject_user_menu_data():
    user = g.get('user', None)
    admin_menus = admin_auth.getAdminMenu(user.getAdminId())
    menu_data = list(map(lambda admin_menu: admin_menu.__dict__, admin_menus))
    return dict(menu_data=menu_data)

# The app route path can be customized in './cms/.env'
@app.route('/example/home/')
def index():
    return render_template('index.html', content='Hello CMS!')

if __name__ == "__main__":
    # If the port changes, './cms/.env' file also needs to be updated.
    app.run(host="127.0.0.1", port=8080, threaded=True)
