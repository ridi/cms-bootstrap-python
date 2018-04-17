''' Tag API example

Make sure to run `make cms-up` before you test this example.

The API offers read-only operations with the tags.
Writing operations can only be made in CMS-Admin service(http://localhost/super/tags).
'''

from ridi.cms.config import Config
from ridi.cms.cms_client import AdminUser
from ridi.cms.cms_client import AdminMenu
from ridi.cms.cms_client import AdminTag

config = Config()
config.RPC_URL = 'http://localhost'

admin_user = AdminUser(config)
admin_tag = AdminTag(config)
admin_menu = AdminMenu(config)
user = admin_user.getUser('admin')

print('\n#Get all tags assigned to the user\n')
tag_ids = admin_user.getAdminUserTag(user.id)
print(tag_ids)

print('\n#Get tag objects from tag ids\n')
tags = admin_tag.getAdminTags(tag_ids)
print(tags)

print('\n#Get menu urls under the tag\n')
if tag_ids:
    menu_ids = admin_tag.getAdminTagMenus(tag_ids[0])
    menus = admin_menu.getMenus(menu_ids)
    urls = list(map(lambda m: m.menu_url, menus))
    print(urls)

print('\n#Get users who use the tag\n')
user_ids = admin_tag.getAdminIdsFromTags(tag_ids)
for user_id in user_ids:
    user = admin_user.getUser(user_id)
    print(user)
