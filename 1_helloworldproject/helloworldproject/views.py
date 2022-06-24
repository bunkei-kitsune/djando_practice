from django.http import HttpResponse
from django.views.generic import TemplateView
from pathlib import Path


# この関数は、requestオブジェクトを受け取って、responseオブジェクトを返す
# helloworldfunctionはurls.pyファイルからrequestオブジェクトを受け取るので、引数を1つ設定
# 引数名はなんでもいいけど、requestにしておく
def helloworldfunction(request):
    returnedobject = HttpResponse('<h1>Hello world<h1>') # htmlタグつけられる
    # HttpResponse は Djangoが用意しているクラス
    return returnedobject
    
class HelloWorldClass(TemplateView):
    # htmlファイルの場所を指示する
    template_name = 'hello.html'

