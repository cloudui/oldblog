from django.apps import AppConfig
from watson import search as watson


class PostsConfig(AppConfig):
    name = 'posts'
    def ready(self):
        post_model = self.get_model("Post")
        watson.register(post_model)
        