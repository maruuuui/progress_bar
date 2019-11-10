from django.db import models


class Progress(models.Model):
    """進捗管理モデル"""

    now = models.IntegerField("現在の進捗", default=0)
    total = models.IntegerField("全ステップ数", default=100)
