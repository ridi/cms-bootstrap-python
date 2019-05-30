# CMS Bootstrap for DRF(django rest framework) Middleware

This template is designed for more ease of use when using django rest framework authentication with CMS-RPC

You will see three files in the current directory. 
- cms.py
- permissions.py
- authentication.py

**What is cms.py**
The cms.py file preconfigures cms-sdk with RPC url.

**What is permissions.py and authentication.py?**
These files are responsible for authentication and permissions based on the cms-sdk by preconfigured cms.py.

If you want to understand this more, check out the [basic drf authentication and permissions](https://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/).


# How to use
1. Save the files to the appropriate path in the project.
- cms.py
- permissions.py
- authentication.py

2. Override the hardcorded string in the files.

```python
# permissions.py
from ${PROJECT_PATH}.cms  import admin_auth

# authentication.py
from ${PROJECT_PATH}.cms import admin_user, admin_auth

# cms.py
config.RPC_URL = 'https://YOUR_CMS_RPC_HTTPS_DOMAIN'
```

3. Defines the variables to use for authentication

```python
# settings.py

...

REST_FRAMEWORK = {
    ...
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'PROJECT_PATH.authentication.CmsOpenAuthentication',
    ),
    ...
}

...

CMS_TEST_ID = os.getenv('TEST_ID', 'admin')
CMS_RPC_URL = os.getenv('CMS_RPC_URL', 'http://localhost')
CMS_AUTH_DISABLE = os.environ.get('CMS_AUTH_DISABLE', False)
...

```

4. Enjoy it! example 

```python
class UserListCreateAPIView(generics.ListCreateAPIView):
    required_tags = ["example",] # Minimum permissions to access this API View
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes=(IsAuthenticated,)
```
