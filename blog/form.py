from django import forms
from . models import Blog


class BlogPost(forms.ModelForm):  # modleForm기반 입력 공간
    class Meta:
        model = Blog
        fields = ['title', 'body']  # 입력받을 항목들
