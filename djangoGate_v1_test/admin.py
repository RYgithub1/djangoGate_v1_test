from django.contrib import admin
from .models import Post

# 作成したモデルを指定する
# DBの内容を確認したいときは、サーバ起動して、Django adminでアクセスして確認
admin.site.register(Post)
