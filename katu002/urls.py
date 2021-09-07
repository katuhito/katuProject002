from django.urls import path
from . import views

# URLパターンを逆引きできるように名前を付ける
app_name = 'katu002'

#URLパターンを登録するための変数
#katu002アプリへのアクセスはviewsモジュールのIndexViewにリダイレクトする
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    #写真投稿ページへのアクセスはviewsモジュールのCreatePhotoViewを実行
    path('post/', views.CreatePhotoView.as_view(), name='post'), 
    #投稿完了ページへのアクセスはviewsモジュールのpostSuccessViewを実行
    path('post_done/', views.PostSuccessView.as_view(), name='post_done'),
]