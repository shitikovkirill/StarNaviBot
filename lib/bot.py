from lib.user import User
from lib.post import Post
import random
from faker import Faker
fake = Faker()


class Bot:

    users = []
    posts = []
    likes = []

    def __init__(self, number_of_users, max_posts_per_user, max_likes_per_user, url):
        self.number_of_users = number_of_users
        self.max_posts_per_user = max_posts_per_user
        self.max_likes_per_user = max_likes_per_user
        self.url = url

    def register_users(self):
        for _ in range(int(self.number_of_users)):
            user = User(
                name=fake.user_name(),
                password=fake.password(length=16, special_chars=True, digits=True, upper_case=True, lower_case=True),
                email=fake.email()
            )
            code, data = user.sing_up(self.url + 'api/users/')
            if code == 201:
                self.users.append(user)
        return self.users

    def create_posts(self):
        for user in self.users:
            for _ in range(random.randint(1, int(self.max_posts_per_user))):
                post = Post(
                    title=fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None),
                    text=fake.text(max_nb_chars=250, ext_word_list=None)
                )
                code, data = user.login(self.url + 'api/token/')
                if code == 200:
                    post.publish(self.url + 'api/posts/', user.token)
                    self.posts.append(post)
        return self.posts

    def add_likes(self):
        for user in self.users:
            random.shuffle(self.posts)
            for index in range(random.randint(1, int(self.max_likes_per_user))):
                post = self.posts[index]
                post.like(self.url + 'api/posts/{}/like/', user.token)
                self.likes.append(post)
        return self.likes
