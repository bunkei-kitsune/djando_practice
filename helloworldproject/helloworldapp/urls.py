from django.urls import path
from .views import helloworldappview
# .viewsは同じ階層のviewsというファイルという意味
# そこから、helloworldappviewを呼び出す

urlpatterns = [
    path('helloworldapp', helloworldappview), #path('url',呼び出すviewファイル名)
    # projectのurls.py のurlpetterns に'app/'と書いてあって、こちらでも'app/helloworldapp'と書くと、app/が重複する
    # ページのurlが app/app/helloworldapp になる
]