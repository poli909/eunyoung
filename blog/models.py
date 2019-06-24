from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Blog(models.Model):

    title = models.CharField(max_length=200)  # CharField에 최대 200글자까지의 제목 저장
    pub_date = models.DateTimeField('date published')  # 작성한 날짜
    body = models.TextField()  # TextFeld 조금 긴 글 저장

    def __str__(self):  # 타이틀에 직접 입력한 제목 설정
        return self.title

    def summary(self):  # 글자수 100개까지만 보여주고 그 뒤에는 detail안에 들어가서 볼수있게함
        return self.body[:100]


class Comment(models.Model):
    post = models.ForeignKey(
        Blog, on_delete=models.CASCADE, related_name="comments")  # Blog객체에 기본키를 줘서
    # on_delte 부모가 없는 댓글 다 지워
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=500)  # 최대 글 500안넘게 댓글내용
