from cmssdk.Config import Config
from cmssdk.CmsClient import AdminUser
from cmssdk.CmsClient import AdminMenu
from cmssdk.CmsClient import AdminTag

config = Config()
config.RPC_URL = 'http://localhost'
admin_user = AdminUser(config)
user = admin_user.getUser('admin')
print('\n#User info\n')
print(user)

admin_menu = AdminMenu(config)
menus = admin_menu.getAllMenuList()
print('\n#All Menus\n')
print(menus)

admin_tag = AdminTag(config)
tag = admin_tag.getAdminTagMenus(1)
print('\n#Get Tag menu ids\n')
print(tag)
