from configuration import CONFIG
from lib.bot import Bot

print(CONFIG)

bot = Bot(
    CONFIG["bot"]["number_of_users"],
    CONFIG["bot"]["max_posts_per_user"],
    CONFIG["bot"]["max_likes_per_user"],
    CONFIG["url"],
)

users = bot.register_users()
print(users)

posts = bot.create_posts()
print(posts)