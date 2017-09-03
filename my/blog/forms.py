from django import forms
from .models import *
from django.db import models

class PostForm(forms.ModelForm):

        class Meta:
            model = Post
            fields = ('title', 'text','video','published_date'
                                                                              ''
                                                                              ''
                                                                              ''
                                                                              '')

            created_date = models.DateTimeField(
                default=timezone.now)
            published_date = models.DateTimeField(
                blank=True, null=True)

        def publish(self):
                self.published_date = timezone.now()
                self.save()

        def __str__(self):
            return "%s,%s" % (self.id, self.title)

