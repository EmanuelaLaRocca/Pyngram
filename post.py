from datetime import datetime
from user import User
import funzioni

## classe POST
all_posts = []  # ROADMAP DIZIONARIO POST
all_post_tot =[]

class Post:
    def __init__(self, text, user):
        self.text = text
        self.user = user

    # metodo per pubblicare un post
    def add_post(self):
        global all_posts
        all_posts.append(self)
        C_user =funzioni.name_object(self.user)
        if User.getter__profile_privacy(C_user)=="public":
            all_post_tot.append(self)