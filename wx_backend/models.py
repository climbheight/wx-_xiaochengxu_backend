from django.db import models

class Welcome(models.Model):
    # upload_to 图片上传后，放到 media文件夹下的welcome文件夹下
    # 必须安装pillow   pip3 install pillow
    img = models.ImageField(upload_to='welcome', default='welcome/slash.png')
    order = models.IntegerField()
    # 这个字段以后不用传，会自动把上传图片的时间存到数据库
    create_time = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)