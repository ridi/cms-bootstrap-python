from ridi.cms.Config import Config
from ridi.cms.CmsClient import AdminUser
from ridi.cms.CmsClient import AdminMenu
from ridi.cms.CmsClient import AdminTag

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
