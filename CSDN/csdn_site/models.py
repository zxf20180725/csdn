from django.db import models


class CsdnUser(models.Model):
    username = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'csdn_user'

    def __str__(self):
        return self.username


class Data(models.Model):
    username = models.CharField(max_length=256,null=False,default="")
    post_time = models.BigIntegerField()
    num_comments = models.IntegerField()
    num_likes = models.IntegerField()
    csdn_article_id = models.BigIntegerField()
    csdn_article_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'data'
