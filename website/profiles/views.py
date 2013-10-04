from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from forms import CreateUserForm, LoginForm, ProfileForm, UserSearchForm
from models import SiteUser
from posts.models import Post


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
  if request.user.is_authenticated():
    return HttpResponseRedirect(reverse(landing))
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
  following = request.user.following.all().values_list('followee')
  following = [user[0] for user in following]
  following.append(request.user.id)
  return render_to_response('home.html', RequestContext(request, {
    'posts': Post.objects.filter(author__in=following).order_by('-timestamp')
  }))


@login_required
def profile(request):
  form = ProfileForm(request.POST or None, request.FILES or None,
      instance=request.user)
  if form.is_valid():
    user = form.save()
    return HttpResponseRedirect(reverse(landing))
  return render_to_response('profiles/profile.html', RequestContext(request, {
    'profile_form': form
  }))


@login_required
def logout_user(request):
  logout(request)
  return HttpResponseRedirect(reverse(login_user))


@login_required
def search_user(request):
  form = UserSearchForm(data=request.POST or None)
  if form.is_valid():
    q = form.cleaned_data['q']
    users = SiteUser.objects.filter(Q(username__icontains=q) |
        Q(first_name__icontains=q) | Q(last_name__icontains=q))
    return render_to_response('profiles/search_user.html',
        RequestContext(request, {'users': users}))
