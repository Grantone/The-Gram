from django import forms


class InstagramLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name', max_length=30)
    email = forms.EmailField(label='Email')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('posts', 'gender')


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user']
