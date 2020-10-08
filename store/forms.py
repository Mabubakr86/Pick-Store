from django import forms
from .models import ProductReviw


class ReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReviw
        fields = ['review', 'score']