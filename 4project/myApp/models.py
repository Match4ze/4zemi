from django.conf import settings
from django.db import models

class login(models.Model):
   picture = models.ImageField(upload_to='images/', default='images/initial.jpeg')
   name = models.CharField(max_length=10) #自分の名前（本名)
   password = models.CharField(max_length=8) #パスワード
   mail = models.EmailField(max_length=240) #メールアドレス
   birth = models.CharField(max_length=8) #生年月日
   school_name = models.CharField(max_length=50) #大学名
   school_grade = models.CharField(max_length=1, choices=[('1','1年生'),('2', '2年生'),('3','3年生'), ('4','4年生'),('大学院','大学院生')]) #学年
   sexuality = models.CharField(max_length=5, choices=[('男','男'),('女', '女'),('その他','その他')])#性別
   insta_ID = models.CharField(max_length=50, null=True, blank=True) #インスタのアカウント名
   twitter_ID = models.CharField(max_length=50, null=True, blank=True) #Twitterのアカウント名
   SNS_name1 = models.CharField(max_length=50, null=True, blank=True) #その他SNSの種類
   SNS_ID1 = models.CharField(max_length=50, null=True, blank=True) #その他SNSのアカウント名
   SNS_name2 = models.CharField(max_length=50, null=True, blank=True) #その他SNSの種類
   SNS_ID2 = models.CharField(max_length=50, null=True, blank=True) #その他SNSのアカウント名

   def publish(self):
        self.save()

   def __str__(self):
        return self.name
