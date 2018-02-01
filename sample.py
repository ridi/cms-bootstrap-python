from cmssdk.Config import Config
from cmssdk.CmsClient import AdminUser

config = Config()
config.RPC_URL = 'http://localhost'
admin_user = AdminUser(config)
user = admin_user.getUser('admin')
print(user)