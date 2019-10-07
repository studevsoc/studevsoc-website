from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.decorators import method_decorator


from .models import Post
from .forms import PostForm, CommentForm, TagForm, BlogTypeForm

#Post List View
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-updated_on')
    template_name = 'blog.html'
    paginate_by = 4

class PostListPub(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-updated_on')
    template_name = 'new_tag.html'
    paginate_by = 4

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
    def get_context_data(self, **kwargs):
        context = super(PostDetail , self).get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(status=1).order_by('-updated_on')
        return context

@method_decorator(login_required, name='dispatch')
class PostUpdateView(generic.UpdateView):
    model = Post
    fields = ('content','tags',)
    template_name = 'edit_post.html'
    SlugField = 'slug'
    context_object_name = 'post'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.updated_on = timezone.now()
        post.status = 0
        post.save()
        return redirect('post_detail', slug=post.slug )


@login_required
def new_tag(request):
    posts = Post.objects.filter(status=1).order_by('-updated_on')
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            tag = form.save(commit=False)
            tag.save()
            return redirect('new_post')
    else:
        form = TagForm()
    return render(request, 'new_tag.html', {'form':form,'posts': posts})


#new post view
@login_required
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_date = timezone.now()
            post.status = 0
            post.save()
            return redirect('post_detail',slug=post.slug)
    else:
        form = PostForm()
    return render(request, 'new_post.html', {'form':form})

#new_tag view


#new categories
@login_required
def new_blogtype(request):
    if request.method == 'POST':
        form = BlogTypeForm(request.POST)
        if form.is_valid():
            blogtype = form.save(commit=False)
            blogtype.save()
            return redirect('new_post')
    else:
        form = BlogTypeForm
    return render(request, 'new_tag.html', {'form':form})

#add comment
@login_required
def add_new_comment(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()
    return render(request, 'comment.html', {'form':form})
