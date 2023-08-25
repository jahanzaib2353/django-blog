from django.shortcuts import render, redirect

from django.views import generic

from django.views.generic import CreateView, UpdateView
from .models import Post
from .models import Sidebar

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'slug', 'content', 'image']
    template_name = 'post_create.html'

    def form_valid(self, form):
        post = form.save()
        return redirect(post.get_absolute_url())

class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'slug', 'content', 'image']
    template_name = 'post_update.html'

    def form_valid(self, form):
        post = form.save()
        return redirect(post.get_absolute_url())



class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')[:2]
    template_name = 'index.html'
    context_object_name = "posts"

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = "post"





def sidebar_view(request):
    # Assuming there is only one entry in the Sidebar model, you can retrieve it like this:
    sidebar = Sidebar.objects.first()

    context = {
        'sidebar_image': sidebar.image_name if sidebar else 'default_image.jpg', # Provide a default image name if no entry is found
    }

    return render(request, 'sidebar.html', context)



def show_all_posts(request):
    # Retrieve all the posts from the database, ordered by the latest created_on
    all_posts = Post.objects.filter(status=1).order_by('-created_on')
    return render(request, 'all_posts.html', {'posts': all_posts})

    