#-------------------------------------------------
#テーブル作成予定
#=====
# user
#=====
# id
# name
# address
# tell
# sex
# contract
# delteFlag
# updateTime
# addTime
#=====
# attendance
#=====
# id
# userId
# yearMonth
# day
# startTime
# endTime
# restStartTime
# restEndTime
# updateTime
# addTime
#-------------------------------------------------
from django.db import models
#
# # Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone

class user(models.Model):
    userId = models.IntegerField('userId', null=True, blank=False)
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    tell = models.IntegerField('tell',null=True,blank=False)
    sex = models.CharField(max_length=1)
    contract = models.IntegerField('contrach',null=False,blank=False)
    deleteFlag = models.IntegerField('deleteFlag',null=False,blank=False)
    updateTime = models.DateTimeField(blank=False,null=False)
    addTime = models.DateTimeField(blank=False,null=False)
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title

class attendance(models.Model):
    attendanceId = models.IntegerField('attendanceid',null=False,blank=False)
    userId = models.IntegerField('userId',null=False,blank=False)
    yearMonth = models.IntegerField(null=False,blank=False)
    day = models.IntegerField(null=False,blank=False)
    startTime = models.DateTimeField(blank=False,null=False)
    endTime = models.DateTimeField(blank=False,null=False)
    restStartTime = models.DateTimeField(blank=False,null=False)
    restEndTime = models.DateTimeField(blank=False,null=False)
    updateTime = models.DateTimeField(blank=False,null=False)
    addTime = models.DateTimeField(blank=False,null=False)
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title
#######
# test
#######
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title

    # ===============================================================
    # (参考) https://qiita.com/okoppe8/items/4cc0f87ea933749f5a49
    # ===============================================================
    # from django.db import models
    #
    # # from users.models import
    #
    # class Item(models.Model):
    #     """
    #     データ定義クラス
    #       各フィールドを定義する
    #     参考：
    #     ・公式 モデルフィールドリファレンス
    #     https://docs.djangoproject.com/ja/2.1/ref/models/fields/
    #     """
    #
    #     # サンプル項目1 文字列
    #     sample_1 = models.CharField(
    #         verbose_name='サンプル項目1_文字列',
    #         max_length=20,
    #         blank=True,
    #         null=True,
    #     )
    #
    #     # サンプル項目2 数値
    #     sample_2 = models.IntegerField(
    #         verbose_name='サンプル項目2_数値',
    #         blank=True,
    #         null=True,
    #     )
    #
    #     # サンプル項目3 ブール値
    #     sample_3 = models.BooleanField(
    #         verbose_name='サンプル項目3_ブール値',
    #     )
    #
    #     # サンプル項目4 選択肢
    #     sample_choice = (
    #         (1, '選択１'),
    #         (2, '選択２'),
    #         (3, '選択３'),
    #     )
    #
    #     sample_4 = models.IntegerField(
    #         verbose_name='サンプル項目4_選択肢',
    #         choices=sample_choice,
    #         blank=True,
    #         null=True,
    #     )
    #
    #     # サンプル項目5 日付
    #     sample_5 = models.DateField(
    #         verbose_name='サンプル項目5 日付',
    #         blank=True,
    #         null=True,
    #     )
    #
    #     # 以下、管理項目
    #
    #     # 作成者(ユーザー)
    #     created_by = models.ForeignKey(
    #         # User,
    #         verbose_name='作成者',
    #         blank=True,
    #         null=True,
    #         related_name='CreatedBy',
    #         on_delete=models.CASCADE,
    #         editable=False,
    #     )
    #
    #     # 作成時間
    #     created_at = models.DateTimeField(
    #         verbose_name='作成時間',
    #         blank=True,
    #         null=True,
    #         editable=False,
    #     )
    #
    #     # 更新者(ユーザー)
    #     updated_by = models.ForeignKey(
    #         # User,
    #         verbose_name='更新者',
    #         blank=True,
    #         null=True,
    #         related_name='UpdatedBy',
    #         on_delete=models.CASCADE,
    #         editable=False,
    #     )
    #
    #     # 更新時間
    #     updated_at = models.DateTimeField(
    #         verbose_name='更新時間',
    #         blank=True,
    #         null=True,
    #         editable=False,
    #     )
    #
    #     def __str__(self):
    #         """
    #         リストボックスや管理画面での表示
    #         """
    #         return self.sample_1
    #
    #     class Meta:
    #         """
    #         管理画面でのタイトル表示
    #         """
    #         verbose_name = 'サンプル'
    #         verbose_name_plural = 'サンプル'
