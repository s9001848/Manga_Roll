from django.contrib.auth.forms import UserCreationForm
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from django.forms import ModelForm
from mangaRoll_app.models import Chat
from django import forms
from django.contrib.auth.models import User
from . import models

class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ('message', )