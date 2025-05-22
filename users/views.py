from django.shortcuts import render , redirect
from django.views.generic import ListView,DetailView,FormView,UpdateView ,DeleteView
from django.views import View


#works with function based views
from django.contrib.auth.decorators import login_required , permission_required

#works with class based viewws
from django.contrib.auth.mixins import LoginRequiredMixin ,PermissionRequiredMixin
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from library.forms import UserUpdateForm,profileupdateform,AddUserForm ,addform
from django.contrib import messages
from django.urls import reverse_lazy
from library.models import issuedbooks ,reservedbooks
from django.utils.timesince import timesince
from datetime import datetime,timedelta
from django.utils import timezone
import requests


# Create your views here.
@login_required
def profile(request):	
	
	# url = "https://andruxnet-random-famous-quotes.p.rapidapi.com/"
	# querystring = {"cat":"famous","count":"1"}
	# headers = {
	# "X-RapidAPI-Host": "andruxnet-random-famous-quotes.p.rapidapi.com",
	# "X-RapidAPI-Key": "key"
	# }
	
	# response = requests.request("POST", url, headers=headers, params=querystring)
	# q = response.json()

	return render(request,'users/profile.html',{

		# 'response':response,
		# 'qoute' :q
		#'author':q['author']


		})



class forgotpassword(View):
	model = User
	template_name = 'user/passwordresetview.html'
	
@login_required
def profile_edit(request,**kwargs):
	if request.method == 'POST':
		form = UserUpdateForm(request.POST ,instance = request.user)
		profile_form = profileupdateform(request.POST,request.FILES ,instance = request.user.profile)

		if form.is_valid() and profile_form.is_valid():
			form.save()
			profile_form.save()
			messages.success(request,f'Your profile has been updated')
			return redirect('profile')
		

	else:
		form = UserUpdateForm(instance = request.user)
		profile_form = profileupdateform(instance = request.user.profile)

		context = {
        'update_form':form,
        'profile_form':profile_form 
    }
		return render(request,'users/profile_edit.html',context)


class userslistview(PermissionRequiredMixin, LoginRequiredMixin,ListView):
	raise_exception =  False
	permission_required = 'user.view_users'
	permission_denied_message = ""
	login_url = '/books/'
	redirect_field_name ='next'

	model = User
	template_name = 'users/users.html'
	context_object_name = 'users'
	paginate_by =  5


@login_required
def adduser(request):
    if request.method == 'POST':
      form =  AddUserForm(request.POST)
      formtwo =addform(request.POST)

    
      if form.is_valid():
             form.save()
          
             username = form.cleaned_data.get('username')
             messages.success(request, f'Account for {username} has been Successfully Created')
             return redirect('users')
    else:
        form = AddUserForm()
    return render(request ,'users/register.html',{'form':form})


class UserDetailView(LoginRequiredMixin, DetailView):
	model = User
	template_name = 'users/userdetail.html'
	context_object_name = 'usersinfo'


class UserAccountListView(LoginRequiredMixin, ListView):
	model = issuedbooks
	template_name = 'users/user_account.html'
	context_object_name = 'useracc'
	
	def get_queryset(self,**kwargs):

		return issuedbooks.objects.filter(userid_id = self.request.user.id)

	def get_context_data(self, ** kwargs):
		ctx = super().get_context_data( ** kwargs)
		ctx['today'] = timezone.now()
		ctx['rsvdbooks'] = reservedbooks.objects.filter(userid_id =  self.request.user.id)
		return ctx




