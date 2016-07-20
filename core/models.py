from django.contrib import auth
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext as _


class GitUser(models.Model):
    user = models.ManyToManyField(auth.models.User,
                              related_name='user',
                              verbose_name=_("user"))
    username = models.CharField(_('username'), max_length=40)
    email = models.EmailField(_('EMail'), null=True, blank=True)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        # return "/edit_git_user/%i/" % self.pk
        return reverse("core:git_user", args=[str(self.pk)])


class Group(models.Model):
    owner = models.ForeignKey(auth.models.User,
                             related_name='owener',
                             verbose_name=_("owener"))
    name = models.CharField(_('name'), max_length=40)
    created_at = models.DateField(_('created_at'))
    git_users = models.ManyToManyField(GitUser, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("core:group", args=[str(self.pk)])


class Data(models.Model):
    gitUser = models.ForeignKey(GitUser)
    created_at = models.DateField(_('created_at'))
    event_type = models.CharField(_('event_type'), max_length=30)
    repository = models.CharField(_('repository'), max_length=70)
    description = models.TextField(_('description'), null=True, blank=True)

    def __str__(self):
        return "User: {}, created at: {}. Event: {}".format(
            self.gitUser, self.created_at, self.event_type)
