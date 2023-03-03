from django.forms import ModelForm

from apps.blog.models import Comments


class CommentForm(ModelForm):

    class Meta:
        model = Comments
        fields = '__all__'
