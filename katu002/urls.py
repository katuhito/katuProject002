from django.urls import path
from . import views

# URLパターンを逆引きできるように名前を付ける
app_name = 'katu002'

#URLパターンを登録するための変数
#katu002アプリへのアクセスはviewsモジュールのIndexViewにリダイレクトする
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]