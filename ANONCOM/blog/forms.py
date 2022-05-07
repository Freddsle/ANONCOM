from django import forms
from .models import Comments, AnonComments
from .models import Post


# Update Image
class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'post_image']


class CommentsForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'Comment here',
        'rows': '4',
    }))

    class Meta:
        model = Comments
        fields = ('content', )


class AnonCommentsForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'Comment here',
        'rows': '4',
    }))

    class Meta:
        model = AnonComments
        fields = ('content', )