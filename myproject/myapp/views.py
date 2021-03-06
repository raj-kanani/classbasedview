from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.views import View, generic
from django.views.generic.base import TemplateView, RedirectView
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from .forms import registerform, todoform, editform, editadminform
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .models import Todos


# 1. class based view  simple demo
#
# class Home(View):
#     name = 'raj-kanani'
#
#     def get(self, request):
#         return HttpResponse(self.name)

# class Child(Home):
#     def get(self, request):
#         return HttpResponse(self.name)
#
#
# class Newform(View):
#     def get(self, request):
#         form = userform()
#         return render(request, 'form.html', {'form': form})
#
#     def post(self, request):
#         form = userform(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data['name'])
#             return HttpResponse('thanks for all')
#
#
# class New(View):
#     f = 'form.html'
#
#     def get(self, request):
#         context = {'info': 'hello india whats up '}
#         return render(request, self.f, context)
#
#
# # 2.template view
# class Home(TemplateView):
#     template_name = 'home.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['name'] = 'raj'
#         context['roll'] = '101'
#         return context
#
#
# # 3. redirect view
# class Index(RedirectView):
#     url = 'https://www.google.com'
#
#
# class Index1(RedirectView):
#     pattern_name = 'index'
#     '''index page in redirect using pattern_name..'''
#
#
# class Raj(RedirectView):
#     pattern_name = 'raj1'
#     permanent = True
#     '''status code define (266) terminal'''
#     query_string = True
#     '''same as false output but show user type (12?defbgdscdv) in url'''
#
#     def get_redirect_url(self, *args, **kwargs):
#         print(kwargs)
#         kwargs['post'] = 'RAJ-KANANI'
#         '''server url ma user kai pan lakhe to raj-kakani show thy html page ma.'''
#         return super().get_redirect_url(*args, **kwargs)


# 4. CRUD with class based view........(templateview, redirectview, view)


# Create your views here.

def register(request):
    if request.method == 'POST':
        fm = registerform(request.POST)
        if fm.is_valid():
            messages.success(request, 'account created')
            fm.save()
            return HttpResponseRedirect('/loggin/')
    else:
        fm = registerform()
    return render(request, 'register.html', {'form': fm})


def loggin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                username = fm.cleaned_data['username']
                password = fm.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'login user  !!!!!')
                    return HttpResponseRedirect('/index/')

        else:
            fm = AuthenticationForm()
        return render(request, 'login.html', {'form': fm})
    else:
        return HttpResponseRedirect('/index/')


def loggout(request):
    logout(request)
    return HttpResponseRedirect('/loggin/')

@login_required(login_url='loggin')
def index(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.user.is_superuser == True:
                fm = editadminform(request.POST, instance=request.user)

            else:
                fm = editform(request.POST, instance=request.user)
            if fm.is_valid():
                fm.save()
                messages.success(request, 'data update')
        else:
            if request.user.is_superuser == True:
                fm = editadminform(instance=request.user)
            else:
                fm = editform(instance=request.user)
        return render(request, 'index.html', {'name': request.user.username, 'form': fm})
    else:
        return HttpResponseRedirect('/loggin/')


class Todoview(TemplateView):
    template_name = 'todo.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        blog = todoform()
        context = {'blog': blog}
        return context

    def post(self, request):
        blog = todoform(request.POST)
        if blog.is_valid():
            print(blog)
            blog.save()
        return HttpResponseRedirect('/tododetail/')


class Tododetailview(TemplateView):
    template_name = 'todo_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        st = Todos.objects.all()
        context = {'st': st}
        return context


class Deleteview(RedirectView):
    url = '/tododetail/'

    def get_redirect_url(self, *args, **kwargs):
        print('delete-data', kwargs)
        d = kwargs['id']
        Todos.objects.get(id=d).delete()
        ''' obj = Todos.objects.get(id=kwargs['id'])'''
        '''obj.delete()'''
        return super().get_redirect_url(*args, **kwargs)


class Updateview(View):
    def get(self, request, id):
        s = Todos.objects.get(id=id)
        print(s.details)
        fm = todoform(instance=s)
        return render(request, 'update.html', {'st': fm})

    def post(self, request, id):
        s = Todos.objects.get(id=id)
        fm = todoform(request.POST, instance=s)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/tododetail/')

