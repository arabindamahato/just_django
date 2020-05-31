from django.db.models import Count, Q 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 
from django.shortcuts import render, get_object_or_404, redirect, reverse
from posts.models import Post
from marketing.models import SignUp
from posts.forms import CommentForm, PostCreateForm

def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query)  |   Q(overview__icontains=query)
        ).distinct()
    context = {
        'queryset' : queryset,
    }
    return render(request, 'search_results.html', context)



def get_category_count():
    queryset = Post.objects.values('categories__title').annotate(Count('categories'))
    return queryset

def index(request):
    featured = Post.objects.filter(featured = True)
    latest = Post.objects.order_by('-timestamp')[0:3]

    if request.method == 'POST':
        email = request.POST["email"]
        new_signup = SignUp()
        new_signup.email = email
        new_signup.save()
    context={
        'object_list' : featured,
        'latest' : latest, 
        }    
    return render(request, 'index.html', context)


def blog(request):
    category_count = get_category_count()
    # print('*'*100)
    # print(category_count)
    # print('*'*100)    
    most_recent = Post.objects.order_by('-timestamp')[:3]
    post_list = Post.objects.all() 
    paginator = Paginator(post_list, 4) # Paginator() accepts 2 args post_list and no's of page to show
    page_request_var = 'page'  # localhost:8000/?page=1
    page = request.GET.get(page_request_var) # request.GET gets the querystring
    try:
        paginated_queryset = paginator.page(page) # results comes according to querystring 
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1) # If querystring is not an integer then it will return 1st page
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages) # if querystring is empty then will return all pages

    context = {
        'queryset':paginated_queryset,
        'most_recent':most_recent,
        'page_request_var':page_request_var,
        'category_count':category_count,
    }
    return render(request, 'blog.html', context)

def post(request, id):
    category_count = get_category_count()
    most_recent = Post.objects.order_by('-timestamp')[:3]
    post = get_object_or_404(Post, id=id)
    form = CommentForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = post 
            form.save()
            return redirect(reverse("post_detail", kwargs={'id': post.pk}))
    context = {
        'form':form,
        'post':post,
        'most_recent':most_recent,
        'category_count':category_count, 
    }
    return render(request, 'post.html', context)


def post_create(request):
    form = PostCreateForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse("post_detail", kwargs={
                'id' : form.instance.id
                }))
    context = {
        'form': form
    }
    return render(request, "post_create.html", context)


def post_update(request, id):
    pass


def post_delete(request, id):
    pass

    