from django.db import models

# Create your models here.

# どのようなデータを扱うかを指定(フィールドの指定)
# Todomodelにはtitleとmemoという2つの情報を入れていく
class Todomodel(models.Model):
    # todoモデルのオブジェクト(1つ1つのデータ)を作るとき、タイトルをまず入れるからtitile
    # CharFieldは大・小サイズの文字列情報を扱うフィールド
    title = models.CharField(max_length=100) # 引数max_lengthは必ず指定
    # 次にメモを書くのでmemo
    # TextFieldは多量のテキストを扱うフィールド
    memo = models.TextField()