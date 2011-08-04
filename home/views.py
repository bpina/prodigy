from django.shortcuts import render, render_to_response
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from home.forms import UserForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User

def index(request):
  return render(request, 'home/index.html')

@csrf_protect
def register(request):
  if request.method == 'GET':
    user_form = UserForm()
    return render(request, 'home/register.html', {'user_form': user_form})
  else:
    post = request.POST
    user_form = UserForm(post)
    if user_form.is_valid():
      if post['password_one'] == post['password_two']:
        user = User.objects.create_user(post['username'], post['email'], post['password_one'])
        return HttpResponseRedirect('/users/' + user.username)
      else:
        errors = {'error': 'passwords do not match'}
        return render(request, 'home/register.html', {'user_form': user_form, 'errors': errors})
    else:
      return render(request, 'home/register.html', {'user_form': user_form})
