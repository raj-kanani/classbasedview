
from django.views import View

from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from .forms import todoform
from .models import Todos
from .forms import userform
from django.views.generic.base import TemplateView, RedirectView


### classs based view  simple demo

class Home(View):
    name = 'raj-kanani'
    def get(self, request):

        return HttpResponse(self.name)

class Child(Home):
    def get(self, request):
        return HttpResponse(self.name)

class Newform(View):
    def get(self, request):
        form = userform()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = userform(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse('thanks for all')

class New(View):
    f = 'form.html'
    def get(self, request):
        context = {'info': 'hello india whats up '}
        return render(request, self.f, context)


#####templateview
class Home(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'raj'
        context['roll'] = '101'
        return context


##### redirect view
class Index(RedirectView):
    url = 'https://www.google.com'

class Index1(RedirectView):
    pattern_name = 'index' #index page in redirect using pattern_name...

class Raj(RedirectView):
    pattern_name = 'raj1'
    permanent = True
    '''status code define (266) terminal'''
    query_string = True
    '''same as false output but show user type (12?defbgdscdv) in url'''

    def get_redirect_url(self, *args, **kwargs):
        print(kwargs)
        kwargs['post'] = 'RAJ-KANANI'
        '''server url ma user kai pan lakhe to raj-kakani show thy html page ma.'''
        return super().get_redirect_url(*args, **kwargs)


######## CRUD with class based view........

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


