from ridi.cms.config import Config
from ridi.cms.cms_client import AdminUser
from ridi.cms.cms_client import AdminMenu
from ridi.cms.cms_client import AdminTag

config = Config()
config.RPC_URL = 'http://localhost'

admin_user = AdminUser(config)
admin_tag = AdminTag(config)
user = admin_user.getUser('admin')

print('\n#Get all tags assigned to the user\n')
tag_ids = admin_user.getAdminUserTag(user.id)
print(tag_ids)

print('\n#Get tag objects from tag ids\n')
tags = admin_tag.getAdminTags(tag_ids)
print(tags)

print('\n#Get menus under the tags\n')
for tag_id in tag_ids:
    menu_ids = admin_tag.getAdminTagMenus(tag_id)
    print(menu_ids)

print('\n#Get users who use the tag\n')
user_ids = admin_tag.getAdminIdsFromTags(tag_ids)
for user_id in user_ids:
    user = admin_user.getUser(user_id)
    print(user)
