from django.db import models

# Create your models here.


class System(models.Model):

    system = models.CharField(max_length=128, verbose_name='操作系统')
    type = models.CharField(max_length=128, verbose_name='机器类型')


class Performance(models.Model):

    mem = models.FloatField(null=True,blank=True,verbose_name='内存')
    cpu = models.IntegerField(null=True,blank=True,verbose_name="处理器")
    disk = models.FloatField(null=True,blank=True,verbose_name="硬盘")
    nic = models.CharField(max_length=128,verbose_name="网络地址")
    system = models.ForeignKey('System',null=True,blank=True,verbose_name="操作系统",on_delete=models.SET_NULL)
    username = models.CharField(max_length=128,verbose_name="账号",default="root")
    password = models.CharField(max_length=128,default="123456",verbose_name="密码")

