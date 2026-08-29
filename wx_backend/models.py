from django.db import models

# 轮播图表
class Banner(models.Model):
    img = models.ImageField(upload_to='banner', default='banner-1.png', verbose_name='图片')
    order = models.IntegerField(verbose_name='顺序')
    create_time = models.DateTimeField(auto_now=True, verbose_name='创建时间')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        verbose_name_plural = '轮播图'

    def __str__(self):
        return str(self.img)
class Notice(models.Model):
    title = models.CharField(max_length=64, verbose_name='公告标题')
    content = models.TextField(verbose_name='公告内容')
    img = models.ImageField(upload_to='notice', default='notice.png', verbose_name='公告图片')
    create_time = models.DateTimeField(auto_now=True, verbose_name='创建时间')

    class Meta:
        verbose_name_plural = '公告表'

    def __str__(self):
        return self.title

class Welcome(models.Model):
    # upload_to 图片上传后，放到 media文件夹下的welcome文件夹下
    # 必须安装pillow   pip3 install pillow
    img = models.ImageField(upload_to='welcome', default='welcome/slash.png')
    order = models.IntegerField()
    # 这个字段以后不用传，会自动把上传图片的时间存到数据库
    create_time = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)
    class Meta:
        verbose_name_plural = "欢迎表"
    def __str__(self):
        return str(self.img)
### 采集表
class Collection(models.Model):
    name = models.CharField(max_length=32, verbose_name='采集人员姓名')
    name_pinyin = models.CharField(max_length=32, verbose_name='姓名拼音', null=True)
    avatar = models.ImageField(upload_to='collection/%Y/%m/%d/', default='default.png', verbose_name='头像')
    create_time = models.DateTimeField(auto_now=True, verbose_name='采集时间')
    area = models.ForeignKey(to='Area', null=True, verbose_name='网格区域', on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "采集表"
    def __str__(self):
        return self.name
###区域表
class Area(models.Model):
    name = models.CharField(max_length=32, verbose_name='网格区域名')
    desc = models.CharField(max_length=32, verbose_name='网格简称')
    user = models.ForeignKey(to='UserInfo', on_delete=models.CASCADE, null=True, verbose_name="负责用户")

    class Meta:
        verbose_name_plural = '区域表'
    def __str__(self):
        return self.name
class UserInfo(models.Model):
    name = models.CharField(verbose_name="姓名", max_length=32)
    avatar = models.FileField(verbose_name="头像", max_length=128, upload_to='avatar')
    create_date = models.DateField(verbose_name="日期", auto_now_add=True)
    score = models.IntegerField(verbose_name="积分", default=0)

    class Meta:
        verbose_name_plural = '用户表'

    def __str__(self):
        return self.name
