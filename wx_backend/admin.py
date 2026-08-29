from django.contrib import admin
# 导入Django自带的后台管理功能

from .models import Welcome,Banner,Notice,UserInfo,Area,Collection
# 从当前目录的models.py里，导入所有模型类

admin.site.register(Welcome)      # 把Welcome表注册到后台
admin.site.register(Banner)       # 把Banner表注册到后台
admin.site.register(Notice)       # 把Notice表注册到后台
admin.site.register(Collection)   # 把居民采集表注册到后台
admin.site.register(UserInfo)     # 把用户表注册到后台
admin.site.register(Area)         # 把网格区域表注册到后台
