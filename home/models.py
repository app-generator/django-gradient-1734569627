# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    id = models.IntegerField(null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    date_joined = models.DateTimeField(blank=True, null=True, default=timezone.now)
    avatar = models.CharField(max_length=255, null=True, blank=True)
    auth_provider = models.CharField(max_length=255, null=True, blank=True)
    bio = models.TextField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Conversation(models.Model):

    #__Conversation_FIELDS__
    id = models.IntegerField(null=True, blank=True)
    user = models.CharField(max_length=255, null=True, blank=True)
    input_text = models.TextField(max_length=255, null=True, blank=True)
    translated_text = models.TextField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Conversation_FIELDS__END

    class Meta:
        verbose_name        = _("Conversation")
        verbose_name_plural = _("Conversation")


class Usage Analytics(models.Model):

    #__Usage Analytics_FIELDS__
    user = models.CharField(max_length=255, null=True, blank=True)
    chats_used = models.IntegerField(null=True, blank=True)
    last_used_at = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Usage Analytics_FIELDS__END

    class Meta:
        verbose_name        = _("Usage Analytics")
        verbose_name_plural = _("Usage Analytics")



#__MODELS__END
