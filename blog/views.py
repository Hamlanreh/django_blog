from django.shortcuts import render
from .models import Post, Category, Comment
from .forms import CommentForm

# Create your views here.

def post_index(request):
    posts = Post.objects.filter( status = 1 ).order_by('-created_on')
    all_categories = Category.objects.all()
    recent_posts = posts[:5]
    context = {
        'posts': posts,
        'categories': all_categories,
        'recent_posts': recent_posts
    }
    return render(request, 'post_index.html', context)



def post_detail(request, slug):
    post = Post.objects.get( slug = slug )
    all_categories = Category.objects.all()
    recent_posts = Post.objects.filter( status = 1 ).order_by('-created_on')[:5]

    if request.method == 'POST':
        form = CommentForm(request.POST)    

        if form.is_valid():
            comment = Comment(
                author = form.cleaned_data["author"],
                content = form.cleaned_data["content"],
                post = post
            )
            comment.save() 

    else:
        form = CommentForm()


    comments = Comment.objects.filter(post = post)
        
    context = {
        'post': post,
        'categories': all_categories,
        'comments': comments,
        'form': CommentForm(),
        'recent_posts': recent_posts
    }
    return render(request, 'post_detail.html', context)



def post_category(request, category):
    category = Category.objects.get(name=category)
    all_categories = Category.objects.all()
    posts = Post.objects.filter( category__name__contains = category.name, status = 1 ).order_by('-created_on')
    recent_posts = posts[:5]
    context = {
        'category': category,
        'posts': posts,
        'categories': all_categories,
        'recent_posts': recent_posts
    }
    return render(request, 'post_category.html', context)