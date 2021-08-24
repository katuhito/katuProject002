from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    #サインアップページのビューの呼び出し
    #「http(s)://<ホスト名>/signup/」へのアクセスに対して、
    #viewsモジュールのSignUpViewをインスタンス化する
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('signup_success/', views.SignUpSuccessView.as_view(), name='signup_success'),
]