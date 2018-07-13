from flask import g, Flask, redirect, request, render_template
from ridi.cms.config import Config as CmsConfig
from ridi.cms.cms_client import AdminAuth
from ridi.cms.login_session import COOKIE_CMS_TOKEN, COOKIE_ADMIN_ID
from ridi.cms.thrift.Errors.ttypes import *

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
    # App should provide the token to authenticate the user.
    token = request.cookies.get(COOKIE_CMS_TOKEN)

    try:
        # Tag is similar to the concept of role or permission.
        # Each endpoint should have required tags.
        # When users access to the endpoint with the required tags, the user can succeed the authorization.
        required_tag_names = ['example']

        # See if the user has the required tags by inspecting the user's token.
        admin_auth.authorizeByTag(token, required_tag_names)
    except (ExpiredTokenException, NoTokenException, MalformedTokenException, UnauthorizedException) as e:
        print(e)
        login_url = admin_auth.getAuthorizeUrl(return_url=request.path)
        return redirect(login_url)
    except (TException) as e:
        raise e

    return None

# Inject user menu data before every template rendering
@app.context_processor
def inject_user_menu_data():
    # Retrieve AdminMenu list
    admin_id = request.cookies.get(COOKIE_ADMIN_ID)
    admin_menus = admin_auth.getAdminMenu(admin_id)

    # Convert each AdminMenu to dict so that it can be serialized to JSON.
    menu_data = list(map(lambda admin_menu: admin_menu.__dict__, admin_menus))

    # By returning this, menu_data is accessible inside any template.
    return dict(menu_data=menu_data)

# The app route path can be customized in './cms/.env'
@app.route('/example/home/')
def index():
    return render_template('index.jinja2', content='Hello CMS!')

if __name__ == "__main__":
    # If the port changes, './cms/.env' file also needs to be updated.
    app.run(host="127.0.0.1", port=8080, threaded=True, debug=True)
