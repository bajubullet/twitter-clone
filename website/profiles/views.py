from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from forms import CreateUserForm, LoginForm, ProfileForm


def signup(request):
  form = CreateUserForm(request.POST or None)
  if form.is_valid():
    user = form.save()
    user = authenticate(username=request.POST['username'],
                        password=request.POST['password1'])
    if user is not None:
      if user.is_active:
        login(request, user)
        return HttpResponseRedirect(reverse(landing))
      else:
        # Return disabled account error msg.
        pass
    else:
      # Return an 'invalid login' error msg.
      pass
  return render_to_response('profiles/signup.html', RequestContext(request, {
      'signup_form': form,
  }))


def login_user(request):
  form = LoginForm(data=request.POST or None)
  if form.is_valid():
    login(request, form.get_user())
    return HttpResponseRedirect(reverse(landing))
  return render_to_response('profiles/login.html', RequestContext(request, {
    'login_form': form,
  }))


def landing(request):
  if not request.user.is_authenticated():
    return HttpResponseRedirect(reverse(signup))
  return render_to_response('home.html', RequestContext(request, {}))


@login_required
def profile(request):
  form = ProfileForm(data=request.POST or None, instance=request.user)
  if form.is_valid():
    user = form.save()
    return HttpResponseRedirect(reverse(landing))
  return render_to_response('profiles/profile.html', RequestContext(request, {
    'profile_form': form
  }))
