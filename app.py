__author__ = 'jmgamao'
import pymongo
from models.post import Post
from database import Database
from models.blog import Blog
from menu import Menu


Database.initialize()
# post = Post(blog_id='123',
#             title='Another great post',
#             content='This is something',
#             author='Joenabie Gamao',
#             )
#
# post.save_to_mongo()
# posts = Post.from_mongo('55bff1ec19f646d3969402cb486f4184')
# print(posts)
# for post in posts:
#     print (post)

#mongo db client


# blog = Blog(
#     author="Abz",
#     title="Sample Title",
#     description="Some description here",
# )
#
# blog.new_post()
# blog.save_to_mongo()
# from_database = Blog.from_mongo(blog.id)
# print (blog.get_posts())


menu = Menu()
menu.run_menu()