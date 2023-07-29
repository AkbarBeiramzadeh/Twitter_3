from django.shortcuts import render
from django.views import View


class PostsView(View):
    template_name = 'posts/posts.html'

    def get(self, request):
        render(request, self.template_name)
