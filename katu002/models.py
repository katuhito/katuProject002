from django.db import models
#accountsアプリのmodelsモジュールからCustomUserをインポート
from accounts.models import CustomUser

class Category(models.Model):
    #カテゴリ名のフィールド
    title = models.CharField(verbose_name = 'カテゴリ', max_length=20)

    def __str__(self):
        """オブジェクトを文字列にして返す
        Returns(str):カテゴリ名"""
        return self.title

class PhotoPost(models.Model):
    """モデルクラス"""
    # CustomUserモデル(のUser_id)とPhotoPostモデルを
    # 一体多の関係で結びつける
    # CustomUserが親でPhotoPostが子の関係になる
    #verbose_name:管理画面のフィールドのタイトルを設定
    #on_delete=models.CSACADE：ユーザーを削除する際にはそのユーザー投稿データもすべて削除する
    user = models.ForeignKey(CustomUser, verbose_name = 'ユーザー', on_delete=models.CASCADE)

    # Categoryモデル(のtitle)とPhotoPostモデルを
    # 1対多の関係で結びつける
    # Categoryが親でPhotoPostが子の関係になる
    category = models.ForeignKey(
        Category,
        #フィールドのタイトル(管理画面)
        verbose_name = 'カテゴリ',
        #カテゴリに関連付けられた投稿データが存在する場合には
        #そのカテゴリを削除できないようにする
        on_delete = models.PROTECT
    )

    #タイトル用のフィールド
    title = models.CharField(
        verbose_name = 'タイトル',
        max_length = 200   #最大文字数200
    )

    # コメント用のフィールド
    comment = models.TextField(
        verbose_name = 'コメント',
    )

    #イメージのフィールド1
    image1 = models.ImageField(
        verbose_name = 'イメージ1',
        upload_to = 'photos',   #MEDIA_ROOT以下のphotosにファイルを保存
        blank = True,    #フィールド値の設定は必須でない
        null = True    #データベースにnullが保存されることを許容  
    )

    #イメージのフィールド2
    image2 = models.ImageField(
        verbose_name = 'イメージ2',
        upload_to = 'photos',   #MEDIA_ROOT以下のphotosにファイルを保存
        blank = True,    #フィールド値の設定は必須でない
        null = True    #データベースにnullが保存されることを許容  
    )

    #投稿日時のフィールド
    posted_at = models.DateTimeField(
        verbose_name = '投稿日時',
        auto_now_add = True    #日時を自動追加
    )

    def __str__(self):
        """オブジェクトを文字列で返す
        Returns(str):投稿記事のタイトル
        """
        return self.title

