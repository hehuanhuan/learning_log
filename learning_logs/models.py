from django.db import models

# Create your models here.
class Topic(models.Model):
    #用户学习的主题
    text=models.CharField(max_length=200)
    date_add=models.DateTimeField(auto_now_add=True)

    def _str_(self):
        #返回模型的字符串表示
        return self.text

