from django.db import models
from django.utils import timezone #djangoではdatetime.nowの代わりにtimezone.nowを使う


class Day(models.Model):
    title = models.CharField('タイトル', max_length=200)
     #CharFieldは一行で収まる物(titleなど、、、)
    text = models.TextField('本文')
     #TextFieldは複数行の文字列に保存したいものに使う
    date = models.DateTimeField('日付', default=timezone.now)
     #DateTimeFieldは日付と時間を扱うもの
     
    def __str__(self):
         return self.title

'''
    モデルを作成したらプロンプトにてデータベースに反映する必要がある。
        py manage.py makemigrations diary
            migrationは移動という意味
            このコマンドでdjangoフレームワークに作成や変更したよと伝えている。

        py manage.py migrate
            migrateをすることで実際に反映を行う。
            
'''