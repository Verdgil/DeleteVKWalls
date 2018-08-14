#!/usr/local/bin/python3
#https://github.com/Verdgil/DeleteVKWalls.git

import vk
import time

app_id = 3020234
login = ""
passwd = ""
session = vk.AuthSession(app_id=str(app_id), user_login=login, user_password=passwd, scope='wall')
api = vk.API(session)
count = api.wall.get(version=5.80, count=1)[0]
for i in range(count):
    try:
        post = api.wall.get(version=5.80, count=1)
        res = api.wall.delete(post_id=post[1]['id'], version=5.80)
    except:
        time.sleep(1)
print("Done")