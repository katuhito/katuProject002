from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import PhotoPostForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class IndexView(TemplateView):
    #index.htmlwをレンダリングする
    template_name = 'index.html'

#デコレーターにより、CreatePhotoViewへのアクセスはログインユーザーに限定される
#ログイン状態で無ければsettings.pyのLOGIN_URLにリダイレクトされる
@method_decorator(login_required, name='dispatch')
class CreatePhotoView(CreateView):
    """写真投稿ページのビュー
    PhotoPostFormで定義されているモデルとフィールドを連携して
    投稿データベースに登録する

    Attributes:
        form_class: モデルとフィールドが登録されたフォームクラス
        template_name: レンダリングするテンプレート
        success_url: データベース登録完了後のリダイレクト先
    """
    
    
