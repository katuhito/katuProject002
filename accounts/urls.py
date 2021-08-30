from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    #サインアップページのビューの呼び出し
    #「http(s)://<ホスト名>/signup/」へのアクセスに対して、
    #viewsモジュールのSignUpViewをインスタンス化する
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('signup_success/', views.SignUpSuccessView.as_view(), name='signup_success'),

    #ログインページの表示
    # 「http(s)://<ホスト名>/login/」へのアクセスに対して、
    # django,contrib.auth.views.LoginViewをインスタンス化して、ログインページを表示する
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    #ログアウトを実行
    # 「http(s)://<ホスト名>/login/」へのアクセスに対して、
    # django,contrib.auth.views.LoginViewをインスタンス化して、ログアウトさせる。
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]