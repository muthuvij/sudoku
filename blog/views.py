from django.http import Http404

from django.shortcuts import render, get_object_or_404, redirect

from .forms import *

from .models import Blog
# Create your views here.



def ppl_create_view_dj(request):
    my_form = RawBlogForm()
    
    if request.method == 'POST':
        my_form = RawBlogForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            Blog.objects.create(**my_form.cleaned_data)
            my_form = RawBlogForm()
        else:
            print(my_form.errors)
    
    context = {
        'form': my_form   
    }
    return render(request, "templates/people_create_dj.html", context)



def ppl_create_view_own(request):
    #print(request.GET)
    #print(request.POST)
    if request.method == 'POST':
        new_name=request.POST.get('name')
        print(new_name)
        #Blog.objects.create(name=new_name)
    
    context = {
        
    }
    return render(request, "templates/people_create_own.html", context)




def ppl_create_view(request):

    initial_data = {
            'name': 'My name'
            
        }

    obj = Blog.objects.get(id=1)
    
    form = BlogForm(request.POST or None, initial = initial_data, instance = obj)

    if form.is_valid():
        form.save()
        form = BlogForm()
    
    context = {
        'form' : form
        
    }
    return render(request, "templates/people_create.html", context)




def ppl_detail_view(request):
    obj = Blog.objects.get(id=1)
    context = {
        'name' : obj.name,
        'object' : obj
    }
    return render(request, "templates/people_details.html", context)



def dynamic_lookup_view(request, my_id):
    #obj = Blog.objects.get(id=my_id)
    #obj = get_object_or_404(Blog, id=my_id)
    try:
        obj = Blog.objects.get(id=my_id)
    except Blog.DoesNotExist:
        raise Http404
    context = {
            "object": obj
        }
    
    return render(request, "templates/people_details.html", context)



def blog_delete_view(request, my_id):
    obj = get_object_or_404(Blog, id=my_id)
    
    if request.method == "POST":
        #confirming delete
        obj.delete()
        return redirect('../../')
        
    context = {
            "object": obj
        }
    
    return render(request, "templates/blog_delete.html", context)








