from django.shortcuts import render
from django.utils import timezone
# .models の . は カレントディレクトリ、もしくは、カレントアプリケーション を表す
from .models import Post


# ビュー（コントローラー）作成
def test(request):
    # モデルPostから参照して変数postsに格納 ->テンプレート（ビュー）で活用
    posts = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    # return render(request, 'djangoGate_v1_test/templates/test.html', {'posts': posts})
    return render(request, 'test.html', {'posts': posts})
