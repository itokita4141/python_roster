from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return str(self.__dict__)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.__dict__)

# from django.db import models
#
#
# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#
#
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)

# #-------------------------------------------------
# #テーブル作成予定
# #=====
# # user
# #=====
# # id
# # name
# # address
# # tell
# # sex
# # contract
# # delteFlag
# # updateTime
# # addTime
# #=====
# # attendance
# #=====
# # id
# # userId
# # yearMonth
# # day
# # startTime
# # endTime
# # restStartTime
# # restEndTime
# # updateTime
# # addTime
# #-------------------------------------------------
# from django.db import models
# #
# # # Create your models here.
# from django.conf import settings
# from django.db import models
# from django.utils import timezone
#
# class user(models.Model):
#     # __tablename__ = "user"
#     userId = models.IntegerField(null=False, blank=False,primary_key=True,verbose_name="ユーザーID")
#     name = models.CharField(max_length=20,verbose_name="名前")
#     address = models.CharField(max_length=100,verbose_name="住所")
#     tell = models.CharField(max_length=20,null=True,blank=True,verbose_name="電話番号")
#     sex = models.CharField(max_length=1,verbose_name="性別(m:男性,f:女性)")
#     contract = models.CharField(max_length=100,null=False,blank=False,verbose_name="社員パートなど")
#     deleteFlag = models.BooleanField(default=True,verbose_name="削除フラグ")
#     updateTime = models.DateTimeField(blank=False,null=False,default=timezone.now,verbose_name="更新日時")
#     addTime = models.DateTimeField(blank=False,null=False,default=timezone.now,verbose_name="追加日時")
#     def __str__(self):
#         return str(self.userId) + " " + str(self.name)
#     # id以外のカラム名のインスタンス変数を作成(idはDBに登録される際に自動で割り振られるので不要)
#     # def __init__(self, userId, name, address, tell, sex, contract, deleteFlag, updateTime, addTime):
#     #     self.userId = userId
#     #     self.name = name
#     #     self.address = address
#     #     self.tell = tell
#     #     self.sex = sex
#     #     self.contract = contract
#     #     self.deleteFlag = deleteFlag
#     #     self.updateTime = updateTime
#     #     self.addTime = addTime
#     # def userInfo(self):
#     #     return "{self.userId} {self.name} {self.address} {self.tell} {self.sex} {self.contract}"
#
# class attendance(models.Model):
#     attendanceId = models.IntegerField(null=False,blank=False,primary_key=True,verbose_name="出勤ID")
#     userId = models.IntegerField(null=False,blank=False,verbose_name="ユーザーID")
#     yearMonth = models.CharField(max_length=6,null=True,blank=True,verbose_name="対象年月")
#     day = models.CharField(max_length=2,null=True,blank=True,verbose_name="対象日")
#     startTime = models.CharField(max_length=8,blank=True,null=True,verbose_name="勤務開始時間")
#     endDateTime = models.DateTimeField(blank=True,null=True,verbose_name="勤務終了時間")
#     restStartTime = models.DateTimeField(blank=True,null=True,verbose_name="休憩開始時間")
#     restEndTime = models.DateTimeField(blank=True,null=True,verbose_name="休憩終了時間")
#     deleteFlag = models.BooleanField(default=True,verbose_name="削除フラグ")
#     updateTime = models.DateTimeField(blank=True,null=True,default=timezone.now,verbose_name="更新時間")
#     addTime = models.DateTimeField(blank=True,null=True,default=timezone.now,verbose_name="追加時間")
#     def __str__(self):
#         return str(self.attendanceId) + " " + str(self.userId) + " " + str(self.yearMonth) + str(self.day)
#
# #######
# # test
# #######
# class Post(models.Model):
#     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     title = models.CharField(max_length=200)
#     text = models.TextField()
#     created_date = models.DateTimeField(default=timezone.now)
#     published_date = models.DateTimeField(blank=True, null=True)
#     def publish(self):
#         self.published_date = timezone.now()
#         self.save()
#     def __str__(self):
#         return self.title
#
#     # ===============================================================
#     # (参考) https://qiita.com/okoppe8/items/4cc0f87ea933749f5a49
#     # ===============================================================
#     # from django.db import models
#     #
#     # # from users.models import
#     #
#     # class Item(models.Model):
#     #     """
#     #     データ定義クラス
#     #       各フィールドを定義する
#     #     参考：
#     #     ・公式 モデルフィールドリファレンス
#     #     https://docs.djangoproject.com/ja/2.1/ref/models/fields/
#     #     """
#     #
#     #     # サンプル項目1 文字列
#     #     sample_1 = models.CharField(
#     #         verbose_name='サンプル項目1_文字列',
#     #         max_length=20,
#     #         blank=True,
#     #         null=True,
#     #     )
#     #
#     #     # サンプル項目2 数値
#     #     sample_2 = models.IntegerField(
#     #         verbose_name='サンプル項目2_数値',
#     #         blank=True,
#     #         null=True,
#     #     )
#     #
#     #     # サンプル項目3 ブール値
#     #     sample_3 = models.BooleanField(
#     #         verbose_name='サンプル項目3_ブール値',
#     #     )
#     #
#     #     # サンプル項目4 選択肢
#     #     sample_choice = (
#     #         (1, '選択１'),
#     #         (2, '選択２'),
#     #         (3, '選択３'),
#     #     )
#     #
#     #     sample_4 = models.IntegerField(
#     #         verbose_name='サンプル項目4_選択肢',
#     #         choices=sample_choice,
#     #         blank=True,
#     #         null=True,
#     #     )
#     #
#     #     # サンプル項目5 日付
#     #     sample_5 = models.DateField(
#     #         verbose_name='サンプル項目5 日付',
#     #         blank=True,
#     #         null=True,
#     #     )
#     #
#     #     # 以下、管理項目
#     #
#     #     # 作成者(ユーザー)
#     #     created_by = models.ForeignKey(
#     #         # User,
#     #         verbose_name='作成者',
#     #         blank=True,
#     #         null=True,
#     #         related_name='CreatedBy',
#     #         on_delete=models.CASCADE,
#     #         editable=False,
#     #     )
#     #
#     #     # 作成時間
#     #     created_at = models.DateTimeField(
#     #         verbose_name='作成時間',
#     #         blank=True,
#     #         null=True,
#     #         editable=False,
#     #     )
#     #
#     #     # 更新者(ユーザー)
#     #     updated_by = models.ForeignKey(
#     #         # User,
#     #         verbose_name='更新者',
#     #         blank=True,
#     #         null=True,
#     #         related_name='UpdatedBy',
#     #         on_delete=models.CASCADE,
#     #         editable=False,
#     #     )
#     #
#     #     # 更新時間
#     #     updated_at = models.DateTimeField(
#     #         verbose_name='更新時間',
#     #         blank=True,
#     #         null=True,
#     #         editable=False,
#     #     )
#     #
#     #     def __str__(self):
#     #         """
#     #         リストボックスや管理画面での表示
#     #         """
#     #         return self.sample_1
#     #
#     #     class Meta:
#     #         """
#     #         管理画面でのタイトル表示
#     #         """
#     #         verbose_name = 'サンプル'
#     #         verbose_name_plural = 'サンプル'
