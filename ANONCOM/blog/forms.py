from django import forms
from .models import Comments
from .models import Post

#
# # Update Image
# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ['post_image']


class CommentsForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'Comment here',
        'rows': '4',
    }))

    class Meta:
        model = Comments
        fields = ('content', )