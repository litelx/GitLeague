import datetime
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse_lazy
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.utils.encoding import escape_uri_path
from django.views.generic import View
from django.views.generic.edit import FormView, UpdateView
from django.views.generic.list import ListView
from core.forms import *
from core.github_content import *
from core.models import *


class LoginView(FormView):
    form_class = LoginForm
    template_name = "login.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect('core:list')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])

        if user is not None and user.is_active:
            login(self.request, user)
            if self.request.GET.get('from'):
                return redirect(self.request.GET['from'])  # SECURITY: check path
            return redirect('core:list')

        form.add_error(None, "Invalid user name or password")
        return self.form_invalid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("login")


class LoggedInMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            url = reverse("login") + "?from=" + escape_uri_path(request.path)
            return redirect(url)
        return super().dispatch(request, *args, **kwargs)


class GroupListView(LoggedInMixin, ListView):
    page_title = 'groups list'
    model = Group

    def get_context_data(self, **kwargs):
        context = super(GroupListView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return super().get_queryset().filter(owner=self.request.user)


class CreateGroupView(LoggedInMixin, FormView):
    page_title = 'create group'
    form_class = GroupForm
    template_name = "core/group_form.html"
    success_url = reverse_lazy('core:list')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.created_at = datetime.datetime.now()
        form.save()
        return super().form_valid(form)


class CreateGitUserView(LoggedInMixin, FormView):
    page_title = 'Add user'
    form_class = GitUserForm
    template_name = "core/git_form.html"
    success_url = reverse_lazy('core:u_list')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user_name = form.instance.username
        exist = GitUser.objects.filter(username=user_name)
        if exist:
            # if self.request.user in exist[0].user:
            messages.error(self.request, 'The github user "{}" is already in database. Please add another github user.'.format(user_name))
            return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))
            # exist[0].user.add(self.request.user)
            # form.instance.user = self.request.user
            # form.save()
        if is_git_user(user_name):
            form.save()
            i = add_user_data(user_name)
            gu = GitUser.objects.filter(username=user_name)
            gu.email = i[1]
            gu.user.add(self.request.user)
            messages.success(self.request, 'A new git user has been recorded with {} commits'.format(i[0]))
        else:
            messages.error(self.request, 'There is no github user with username "{}". Sorry, try again'.format(user_name))
            return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))
        return super().form_valid(form)


class UpdateGroupView(LoggedInMixin, UpdateView):
    page_title = 'Edit group'
    form_class = GroupForm
    model = Group
    template_name = "core/group_edit.html"

    success_url = reverse_lazy('core:list')

    def get_object(self, queryset=None):
        return Group.objects.get(id=self.kwargs['pk'])

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Group: {}, has been updated'.format(form.instance.name))
        return redirect('core:list')


class UpdateGitUserView(LoggedInMixin, UpdateView):
    page_title = 'Edit git user'
    form_class = GitUserForm
    model = GitUser
    template_name = 'core/git_user_edit.html'
    success_url = reverse_lazy('core:u_list')

    def get_initial(self):
        return super().get_initial()

    def get_object(self, queryset=None):
        return GitUser.objects.get(id=self.kwargs['pk'])

    def form_valid(self, form):
        user_name = form.instance.username
        form.save()
        i = add_user_data(user_name)
        messages.success(self.request, 'Git user: {}, has been updated'.format(form.instance.username))
        return redirect('core:u_list')


class GitUserListView(LoggedInMixin, ListView):
    page_title = 'Git users list'
    model = GitUser

    def get_context_data(self, **kwargs):
        context = super(GitUserListView, self).get_context_data(**kwargs)
        return context

    # def get_queryset(self):
    #     return super().get_queryset().filter(user=self.request.user)


class DataListView(LoggedInMixin, ListView):
    page_title = 'Data list'
    model = Data

    def get_object(self):
        return Group.objects.get(id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(DataListView, self).get_context_data(**kwargs)
        q = self.request.GET.get("browse")
        context['input'] = q
        return context

    def get_queryset(self):
        users_data_list = last_50(id=self.kwargs['pk'])[:50]
        if self.request.GET.get("browse"):
            selection = self.request.GET.get("browse")
            if selection == "1":
                users_data_list = last_50(id=self.kwargs['pk'])
                return users_data_list[:50]
            elif selection == "2":
                users_data_list = last_5_commits(id=self.kwargs['pk'])
                return users_data_list
            elif selection == "3":
                users_data_list = top_commit_user(self.kwargs['pk'])
                return users_data_list
            elif selection == "4":
                return users_data_list[:4]
        return users_data_list


def delete_group(request, id):
    Group.objects.get(pk=id).delete()
    messages.success(request, 'The group was deleted successfully')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def delete_git_user(request, id):
    delete_user_data(GitUser.objects.get(pk=id).username)
    GitUser.objects.get(pk=id).delete()
    messages.success(request, 'The github user was deleted successfully')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def last_50(id):
    users_data_list = Data.objects.filter(
        gitUser=Group.objects.get(id=id).git_users.all()[0])

    for t in Group.objects.get(id=id).git_users.all():
        users_data_list |= Data.objects.filter(gitUser=t)

    users_data_list = users_data_list.order_by('-created_at')
    users_data_list = users_data_list

    return users_data_list


def last_5_commits(id):
    users_data_list = Data.objects.filter(
        gitUser=Group.objects.get(id=id).git_users.all()[0])[:5]
    return users_data_list


def top_commit_user(id):

    q1 = '''
    SELECT id, gitUser_id, created_at, COUNT(description) as 'commits' FROM core_data GROUP BY gitUser_id, created_at
    '''
    q = """
    SELECT core_data.id, core_data.gitUser_id, core_data.created_at, COUNT(description) as 'commits'
    FROM core_data, core_group_git_users
    WHERE core_group_git_users.group_id={} and
          core_group_git_users.gituser_id=core_data.gitUser_id
    GROUP BY core_data.gitUser_id, created_at
    """.format(id)
    q2 = '''
    SELECT * FROM core_data
    '''
    users_data_list = Data.objects.raw(q)
    # con = sqlite3.connect('Django default')
    # cur = con.cursor()
    #
    # cur.execute(q)
    # row = cur.fetchone()
    return users_data_list


class UserDataListView(LoggedInMixin, ListView):
    page_title = 'Data list'
    model = Data

    def get_queryset(self):
        u = GitUser.objects.get(pk=self.kwargs['id'])
        users_data_list = Data.objects.filter(gitUser=u).all()
        return users_data_list


class AddUserView(LoggedInMixin, View):

    def post(self, request, *args, **kwargs):
        assert False, (kwargs['pk'], request.POST.get('username'))


