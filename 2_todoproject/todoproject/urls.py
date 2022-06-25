
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # 今回はパスに何も入力しない。
    # adminという情報がない場合はいつもtodoアプリのurls.pyファイルの情報を参照する
    path('', include('todo.urls')),
]
