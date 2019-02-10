from django.shortcuts import render,get_object_or_404

from .models import blog
# Create your views here.

def allblogs(request):

    allblogs = blog.objects.all()
    #print(allblogs)
    return render(request,"blog/allblogs.html",{"allblogs":allblogs})

def getBlog(request,blogId):

    detailblog = get_object_or_404(blog, pk=blogId)
    print(detailblog)
    return render(request, 'blog/detail.html', {'blog':detailblog})
