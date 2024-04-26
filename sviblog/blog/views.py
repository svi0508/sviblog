from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import Http404
#from django.core.paginator import Paginator

def post_detail(request, id):
    post = get_object_or_404(Post,
                             id=id,
                             status=Post.Status.PUBLISHED,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})

def post_list(request):
    posts = Post.published.all()
    # Постраничная разбивка с 3 постами на страницу
    #paginator = Paginator(post_list, 3)
    #page_number = request.GET.get('page', 1)
    #posts = paginator.page(page_number)
    return render(request,
                  'blog/post/list.html',
                  {'posts': posts})
# Create your views here.
