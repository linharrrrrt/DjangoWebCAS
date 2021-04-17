from django import forms

class UserForm(forms.Form):
    username = forms.CharField(label="姓名", max_length=128)
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField(label="姓名，例如 “张三”", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    groupname = forms.CharField(label="党小组名，例如 “第三组”", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="确认密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class QaingdaForm(forms.Form):
    username = forms.CharField(label="姓名", max_length=128, widget=forms.HiddenInput(attrs={'class': 'form-control'}))
    groupname = forms.CharField(label="党小组", max_length=128, widget=forms.HiddenInput(attrs={'class': 'form-control'}))
