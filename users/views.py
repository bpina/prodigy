from django.shortcuts import render_to_response, render

def show(request, username):
  user = User.objects.filter(username=username)
  return render_to_response('users/show.html', {'user': user})
