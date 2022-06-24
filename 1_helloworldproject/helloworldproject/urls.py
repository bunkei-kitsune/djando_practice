from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from .views import HelloWorldClass, helloworldfunction
# .viewsは同じ階層のviewsというファイルという意味
# そこから、helloworldfunctionを呼び出す

urlpatterns = [
    path('admin/', admin.site.urls),
    path('helloworld/', helloworldfunction),
    # ClassBasedViewの場合は as_view()をつける必要がある
    # クラスからオブジェクトを作成する、メソッド・関数に変えていくイメージ
    path('helloworld2/', HelloWorldClass.as_view()),
    # 最初が空欄だと、上記のURL以外を受け取った場合は helloworldapp.urls を呼び出すという意味になる?->ならなかったっぽい
    path('app/', include('helloworldapp.urls')), # 作成したhelloworldappのurls.pyファイルを呼び出す
]
