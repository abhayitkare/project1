from django import forms


# how to create Form

class form1(forms.Form):
    name = forms.CharField()
    surname = forms.CharField()
    age = forms.IntegerField()
    email = forms.EmailField()

class form2(forms.Form):
    name = forms.CharField()
    surname = forms.CharField()
    email = forms.EmailField()

class form3(forms.Form):
    name = forms.CharField()
    surname = forms.CharField()
    age = forms.IntegerField()
    email = forms.EmailField()

# Form field argument 

class form4(forms.Form):
    name = forms.CharField(label='Your Name')
    surname = forms.CharField(label_suffix=" ")
    age = forms.IntegerField(help_text="don't enter age more than 50")
    location = forms.CharField(required=False)
    email = forms.EmailField(initial='abhay@gmail.com')
    gender = forms.CharField(disabled=True)
    password = forms.CharField(widget=forms.PasswordInput)
    msg = forms.CharField(widget=forms.Textarea)
    box = forms.CharField(widget=forms.CheckboxInput)
    file = forms.CharField(widget=forms.FileInput)


# how to get form data

class form5(forms.Form):
    name = forms.CharField()
    surname = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class form6(forms.Form):
    name = forms.CharField()
    surname = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


# From field type CharField,booleanField,Integerfield,DecimalField,SlugField etc
# and we use in-build validation for Form here using max_length = 2,min_length=10 etc in this field

class form7(forms.Form):
    name = forms.CharField(min_length=3,max_length=10) # we validate this field using max,min 
    surname = forms.CharField(empty_value="itkare") # surname takal nhi tri default "itkare" yeil error yenar nhi
    email = forms.EmailField(error_messages={'required':'enter email and ends with @gmail.com'})  # apn lihilela error msg disel default vala n dista
    roll = forms.IntegerField(min_value=101,max_value=110) # 101  to 110 madhe roll no dya lagel
    fee = forms.DecimalField(min_value=5,max_value=50,max_digits=4,decimal_places=2) # 4 length asel ani point nantr 2 no lenght asel
    price = forms.FloatField(min_value=5,max_value=50)  # decimal point nantr kiti pn no jamat DecimalField chya yevji he field use jast karychi
    agree = forms.BooleanField(label="I Agree",label_suffix='')  # check box yete BooleanField mule


# we use coustom validation for Form single field

class form8(forms.Form):
    name = forms.CharField()
    surname = forms.CharField()

    def clean_name(self):                 # jya field la validation lavych tyach nav us karych clean_name()
        val = self.cleaned_data['name']
        if len(val) <= 3:
            raise forms.ValidationError("enter name using more than 3 char")
        return val
    
    def clean_surname(self):
        val = self.cleaned_data['surname']
        if len(val) <= 4:
            raise forms.ValidationError("Plz enter name using more than 4 char")
        else:
            return val
    
 # we use coustom validation for all Form field

class form9(forms.Form):
    name = forms.CharField()
    surname = forms.CharField()
 

    def clean(self):
        cleaned_data =  super().clean()
        valn = self.cleaned_data['name']
        vals = self.cleaned_data['surname']
       

        if len(valn) <= 3:
            raise forms.ValidationError("plz enter name using greater than 3 char")
        
        if len(vals) < 4:
            raise forms.ValidationError("plz enter surname using greater than 4 char")
        
# build in validators 2 way
from django.core import validators

class form10(forms.Form):
    name = forms.CharField(validators=[validators.MaxLengthValidator(10)])
    surname = forms.CharField()
    roll = forms.IntegerField(validators=[validators.MaxValueValidator(10)]) # less than 10 roll no dya lagtil


# custom validators

def start_a(val):        # we defind coustom validator here and we use this validator in Form field
    if val[0] != "a":
        raise forms.ValidationError("plz starts with a")
    
class form11(forms.Form):
    name = forms.CharField(validators=[start_a])   # we use here name 'a' pasun start honar liha lagel
    surname = forms.CharField()
    roll = forms.IntegerField() 


# match password and re-enter password field

class form12(forms.Form):
    name = forms.CharField()  
    surname = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    rpassword = forms.CharField(widget=forms.PasswordInput,label='password(again)') 

    def clean(self):
        cleaned_data = super().clean()
        p1 = self.cleaned_data['password']
        p2 = self.cleaned_data['rpassword']

        if p1 != p2:
            raise forms.ValidationError("password does not match")
        


class form13(forms.Form):
    name = forms.CharField()
    surname = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

# ModelForm
# now we don't want to write same code as models.py
from .models import table3

class form14(forms.ModelForm):
    class Meta:
        model = table3
        fields = ['name','surname','password']

# in-built validation in ModelForm
from .models import table4

class form15(forms.ModelForm):
    # name = forms.CharField(max_length=10,required=False)  # asa pn yeka validate karu shakto
    class Meta:
        model = table4
        fields = ['name','surname','password']
        labels = {'name':'Enter Name','surname':'Enter Surname','password':'Enter Password'}
        error_messages = {'name':{'required':'plz enter your name'},
                          'password':{'required':'plz enter tour surname'}}
        widgets = {'password':forms.PasswordInput}

from .models import table5

class form16(forms.ModelForm):
    class Meta:
        model = table5
        fields = ['name','surname','password']

# create Registration Form using UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class singupform(UserCreationForm):
    password2 = forms.CharField(label='confirm password (again)',widget=forms.PasswordInput)  # all ready ahe mhanun ethe validation lava lagat ahe
    class Meta:
        model = User             # in-build model use kel 
        fields = ['username','first_name','last_name','email']  # ya extra fields add karnya sathi apan asa code lihila
        labels = {'email':'Email'}


















# another way of writing model form

from .models import table6


class form17(forms.ModelForm):
    class Meta:
        model = table6
        fields = "__all__"          # ya mule all fields distil
       # exclude = ['surname']       # ya mule surname field disnar nhi


