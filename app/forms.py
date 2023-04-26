# from django import forms
# from .models import House, Category

# class HouseForm(forms.ModelForm):
#     categories = forms.ModelMultipleChoiceField(
#         queryset=Category.objects.all(),
#         widget=forms.CheckboxSelectMultiple,
#     )

#     class Meta:
#         model = House
#         fields = ['name', 'address', 'price', 'categories']
