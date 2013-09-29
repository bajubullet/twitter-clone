from django.conf import settings
from django.contrib.auth import authenticate, login
from django.shortcuts import render_to_response
from django.template import RequestContext

from forms import CreateUserForm


def signup(request):
  form = CreateUserForm(request.POST or None)
  if form.is_valid():
    user = form.save()
    user = authenticate(username=request.POST['username'],
                        password=request.POST['password1'])
    if user is not None:
      if user.is_active:
        login(request, user)
        # Redirect to success page.
      else:
        # Return disabled account error msg.
        pass
    else:
      # Return an 'invalid login' error msg.
      pass
  return render_to_response('profiles/signup.html', RequestContext(request, {
      'login_form': form,
  }))


def home(request):
  return render_to_response('base.html', RequestContext(request, {}))