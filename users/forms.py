from django import forms
from django.contrib import auth
from django.contrib.auth.models import User
from users.models import UserInfo

class LoginForm(forms.Form):
    username = forms.CharField(label='username', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'please enter user name'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter Password'}))

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        user = auth.authenticate(username=username, password=password)
        if user is None:
            raise forms.ValidationError('Username or password is incorrect')
        else:
            self.cleaned_data['user'] = user
        return self.cleaned_data

class RegForm(forms.Form):
    username = forms.CharField(label='username',max_length=30,min_length=3,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please enter 3-30 usernames'}))
    email = forms.EmailField(label='email', widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'email-id'}))
    password = forms.CharField(label='password', min_length=6,widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'password'}))
    password_again = forms.CharField(label='Re-enter password', min_length=6,widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username already exists')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('email already exits')
        return email

    def clean_password_again(self):
        password = self.cleaned_data['password']
        password_again = self.cleaned_data['password_again']
        if password != password_again:
            raise forms.ValidationError('Inconsistent password entered twice')
        return password_again

class UserDetailForm(forms.Form):
    # user_name= forms.CharField(label=u'Username ',widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':' Enter your username again'}))
    # user_first_name= forms.CharField(label=u'Name ',widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':' Enter your Name'}))
    user_phone = forms.CharField(label=u'cellphone number',widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':' Phone Number'}))
    car_number = forms.CharField(label=u'number plate',widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please enter the license plate number'}))
    car_type = forms.CharField(label=u'Model',widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please enter the model'}))
    # car_color = forms.CharField(label=u'Car color',widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':' enter the car color'}))
    # car_kind = forms.CharField(label=u'car type',widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please enter the type of vehicle'}))
    # car_company = forms.CharField(label=u'car Company',widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Please enter the Company of vehicle'}))


    def clean(self):
        # user_name= self.cleaned_data['user_name']
        user_phone = self.cleaned_data['user_phone']
        car_number = self.cleaned_data['car_number']
        car_type = self.cleaned_data['car_type']
        # car_color = self.cleaned_data['car_color']
        # car_kind = self.cleaned_data['car_kind']
        # user_first_name= self.cleaned_data['user_first_name']
        # car_company= self.cleaned_data['car_company']
        return self.cleaned_data    
    # def clean_user_phone(self):
    #     user_phone = self.cleaned_data['user_phone']
    #     if UserInfo.objects.filter(user_phone=user_phone).exists():
    #         raise forms.ValidationError('用户名')