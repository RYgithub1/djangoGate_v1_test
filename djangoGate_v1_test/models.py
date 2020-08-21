from django.db import models
from django.utils import timezone


# pythonでのmodel定義は、modelsファイル作成して自分で定義
# $ rails g model post author title textに相当
# プロパティの型の宣言が必要
# Post モデルが、DB（SQLite）に作成
# $ python3 manage.py makemigrations djangoGate_v1_test
# $ python3 manage.py migrate djangoGate_v1_test
# $ python3 manage.py showmigrate
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
