from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm,UsernameField #  we have to modified form
from django import forms
from django.contrib.auth.models import User # we have used this inbuild model 
from django.utils.translation import ugettext_lazy as _
from . models import Post


# singup form 
class SingUpForm(UserCreationForm):
    password1=forms.CharField(label='password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Confirm password(again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        label={'first_name':'First Name','last_name':'Last Name','email':'Email'}
        widgets={'username':forms.TextInput(attrs={'class':'form-control'}),
        'first_name':forms.TextInput(attrs={'class':'form-control'}),
        'last_name':forms.TextInput(attrs={'class':'form-control'}),
        'email':forms.EmailInput(attrs={'class':'form-control'}),
        }

# login form
class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))    
    password = forms.CharField(label=_("password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'})) 

# form for update

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields=['title','Desc']
        labels={'title':'Title','Desc':'Description'}
        widgets={'title':forms.TextInput(attrs={'class':'form-control'}),
        'Desc':forms.Textarea(attrs={'class':'form-control'}), }



