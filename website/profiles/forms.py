from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import ContentType
from django.contrib.auth.models import Permission
from django.utils.translation import ugettext as _

from models import SiteUser
from posts.models import Post


def _add_post_permissions(site_user):
  """Adds post add/edit/delete permissions to the user object given.

  Args:
    site_user: SiteUser object.

  Returns:
    Updated user object with post permissions.
  """
  post_content_type = ContentType.objects.get_for_model(Post)
  post_permissions = ['add', 'change', 'delete']
  for post_permission in post_permissions:
    permission = Permission.objects.get(
        content_type=post_content_type, codename='%s_post' % post_permission)
    site_user.user_permissions.add(permission)
  site_user.save()
  return site_user


class CreateUserForm(UserCreationForm):
  email = forms.EmailField(required=True)

  class Meta:
    model = SiteUser
    fields = ('username',)

  def __init__(self, *args, **kwargs):
    super(CreateUserForm, self).__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.form_id = 'id-signupFrom'
    self.helper.form_method = 'post'
    self.helper.form_action = '/signup/'
    self.helper.add_input(Submit('submit', _('Sign up')))


  def clean_username(self):
    """
    Checks for unique username.
    """
    username = self.cleaned_data['username']
    if SiteUser.objects.filter(username=username).exists():
      raise forms.ValidationError(_('User with this username already exists.'))
    return username

  def clean_email(self):
    """
    Checks for unique email address.
    """
    email = self.cleaned_data['email']
    if SiteUser.objects.filter(email=email).exists():
      raise forms.ValidationError(_('User with this email id already exists.'))
    return email

  def save(self, *args, **kwargs):
    """
    Creates user and adds post permissions.
    """
    site_user = SiteUser.objects.create_user(
        self.cleaned_data['username'], self.cleaned_data['email'],
        self.cleaned_data['password1'])
    return _add_post_permissions(site_user)


class LoginForm(AuthenticationForm):

  def __init__(self, *args, **kwargs):
    super(LoginForm, self).__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.form_id = 'id-loginForm'
    self.helper.form_method = 'post'
    self.helper.form_action = '/login/'
    self.helper.add_input(Submit('submit', _('Sign in')))


class ProfileForm(forms.ModelForm):
  class Meta:
    model = SiteUser
    fields = ('first_name', 'last_name', 'bio', 'gender', 'photo', 'website')

  def __init__(self, *args, **kwargs):
    super(ProfileForm, self).__init__(*args, **kwargs)
    self.fields['bio'].widget = forms.Textarea(attrs={'rows': 4})
    self.helper = FormHelper()
    self.helper.form_id = 'id-profileForm'
    self.helper.form_method = 'post'
    self.helper.form_action = '/profile/'
    self.helper.add_input(Submit('submit', _('Save')))
