from django import forms
from .models import books,category,issuedbooks ,searchedcontent
from users.models import profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.forms import UserCreationForm used for creating a user

class Dateinput(forms.DateInput):
	input_type = 'date'

class AddBookForm(forms.ModelForm):
	title = forms.CharField(
		label="Your Title Here",
		widget=forms.TextInput(attrs={'placeholder': 'Your Title Here'}),
		min_length=4,
		required=True)
	#publication_date =forms.DateField(widget=Dateinput)
	

	class Meta:
		model = books
		fields = "__all__"
		widgets = {'publication_date':Dateinput()}



class AddCategoryForm(forms.ModelForm):
	category = forms.CharField(min_length=3,required=True)

	class Meta:
		model = category
		fields = ['id']

		#def clean_category(self):

		#	for instance in category.objects.all():
		#		if instance.category_name == category:
		#			raise forms.ValidationError(category + ' is already created')
		#	return category
class UserUpdateForm(forms.ModelForm):

	email = forms.EmailField()
	username = forms.CharField(required=True,widget=forms.TextInput(attrs={

		"readonly":'readonly'
		}))

	class Meta:
		model = User
		fields = ['email','username','first_name','last_name']


class profileupdateform(forms.ModelForm):
	class Meta:
		model = profile
		fields = ['image']



class AddUserForm(UserCreationForm):
	username = forms.CharField(required=True)
	email = forms.EmailField(required= True)

	class Meta:
		model = User
		fields = ['first_name','last_name','username','email','password1','password2']


		def clean(self):
			email=self.cleaned_data.get('email')
			if User.objects.filter(email=email).exists():
				raise ValidationError("email exists")
			return self.cleaned_data

class addform(forms.ModelForm):

	class Meta:
		model = profile
		fields = "__all__"


class issuebookform(forms.ModelForm):
	booksid = forms.IntegerField(required=True)


	class Meta:
		model = issuedbooks
		fields = "__all__"




class searchedcontentform(forms.ModelForm):
		class Meta:
    			
				model = searchedcontent
				fields = ['searchedinfo']
		













#