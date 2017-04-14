__author__ = 'jmgamao'
import uuid, datetime
from database import Database

class Post(object): #this post comes from an object

    def __init__(self, blog_id, title, content, author, date=datetime.datetime.utcnow(), id=None): #default - only in the end
        self.blog_id = blog_id
        self.title =  title
        self.content = content
        self.author = author
        self.id = uuid.uuid4().hex if id is None else id #randomly,32char
        self.created_date = date

        # post = Post(


    #what can a post do
    #insert in table Posts with the following JSON
    def save_to_mongo(self):
        Database.insert(collection='posts',
                        query=self.json())

    # get JSON/DATA
    def json(self):
        return {
            'id': self.id,
            'blog_id':self.blog_id,
            'title': self.title,
            'content': self.content,
            'author': self.author,
            'id': self.id,
            'created_date': self.created_date

        }
        #creates a json representation


    # get a specific data : find_one , return an object
    @classmethod
    def from_mongo(cls, id):
        # Post.from_mongo('123')
        post_data = Database.find_one(collection='posts',query={'id': id})
        return cls(blog_id = post_data['blog_id'],
                   title=post_data['title'],
                   content=post_data['content'],
                   author=post_data['author'],
                   date=post_data['created_date'],
                   id=post_data['id'])


    @staticmethod
    def from_blog(id):
        return [post for post in Database.find(collection='posts', query={'blog_id': id})]



