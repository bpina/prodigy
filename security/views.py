from django.shortcuts import render_to_response, render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def login(request):
  if request.method == 'GET':
    login_form = AuthenticationForm()
    return render(request, 'security/login.html', {'login_form': login_form})
  else:
    post = request.POST
    login_form = AuthenticationForm(data=post)

    if login_form.is_valid():
      user = auth.authenticate(username=post['username'], password=post['password'])
      if user is not None:
        auth.login(request, user)
        if request.is_ajax():
          return HttpResponse()
        else:
          return HttpResponseRedirect('/user')
      else:
        return render(request, 'security/login.html', {'login_form': login_form})
    else:
      print login_form.errors
      return render(request, 'security/login.html', {'login_form': login_form, 'errors': login_form.errors})

def logout(request):
  auth.logout(request)
  return HttpResponseRedirect('/')
