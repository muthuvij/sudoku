from django import forms

from .models import Blog



class BlogForm(forms.ModelForm):
    name = forms.CharField(label='Enter your name',
                           widget=forms.TextInput(attrs={"placeholder": "Your name"}))
    class Meta:
        model = Blog
        fields = [
            'name',
            'age',
            'goal'
        ]
    def clean_name(self, *args, **kwargs):
        name = self.cleaned_data.get("name")
        if "sus" not in name:
            return name
        else:
            raise forms.ValidationError("Your name is kinda sussy")

    def clean_age(self, *args, **kwargs):
        age = self.cleaned_data.get("age")
        if age >= 18:
            return age
        else:
            raise forms.ValidationError("Go away kid")



class RawBlogForm(forms.Form):
    name=forms.CharField(label='Enter name')
    age=forms.DecimalField(initial=18)
    goal=forms.CharField(required=True,
                         widget=forms.Textarea(     #Textarea ()->optional
                             attrs={
                                    #"class": "new-class-name two",
                                    "rows": 20,
                                    "cols": 50
                                 }
                             )
                         )
