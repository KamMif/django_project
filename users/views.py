from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm

def logout_view(request):
  """Closing session"""
  logout(request)
  return HttpResponseRedirect(reverse('djangos_ll:index'))

def register(request):
  """Registrate new user"""
  if request.method != 'POST':
    #Display blank registration form
    form = UserCreationForm()
  else:
    #Form processing
    form = UserCreationForm(data=request.POST)
    if form.is_valid():
      new_user = form.save()
      #LogIn and redirect home page
      authenticate_user = authenticate(username=new_user.username, password=request.POST['password1'])
      login(request, authenticate_user)
      return HttpResponseRedirect(reverse('djangos_ll:index'))

  context = {'form': form}
  return render(request, 'users/register.html', context)