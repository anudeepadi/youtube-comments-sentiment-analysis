from django import forms

class CommentForm(forms.Form):
    link = forms.URLField()
    no_of_comments = forms.IntegerField()
    additional_params = forms.CharField(required=False)
