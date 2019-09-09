from configuration import CONFIG
from lib.bot import Bot

bot = Bot(
    CONFIG["bot"]["number_of_users"],
    CONFIG["bot"]["max_posts_per_user"],
    CONFIG["bot"]["max_likes_per_user"],
    CONFIG["url"],
)

users = bot.register_users()
print("Added {} users!".format(len(users)))
#print(users)

posts = bot.create_posts()
print("Added {} posts!".format(len(posts)))
#print(posts)

likes = bot.add_likes()
print("Added {} likes!".format(len(likes)))
#print(likes)
