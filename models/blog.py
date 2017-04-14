from models.post import Post
from database import Database
import uuid, datetime
class Blog(object):
    def __init__(self, author, title, description, id=None):
        self.author = author
        self.title = title
        self.description = description
        # self.created_date = now
        self.id = uuid.uuid4().hex if id is None else id


    def new_post(self):
        title = raw_input("Enter Post Title:")
        content = raw_input("Enter Content:")
        date = str(raw_input("Enter post date or leave blank for today (MMDDYYYY):"))
        dateStr=datetime.datetime.strptime(date, '%m%d%Y')
        post = Post(blog_id=self.id,
                    title=title,
                    content=content,
                    author=self.author,
                    date=dateStr)
        post.save_to_mongo()

    def get_posts(self):
        return  Post.from_blog(self.id)

    def save_to_mongo(self):
        Database.insert(collection='blogs', query=self.json())

    def json(self):
        return {
            'author': self.author,
            'title': self.title,
            'description': self.description,
            'id': self.id
        }

    @classmethod
    def from_mongo(cls, id): #cls = currentClass
        blog_data = Database.find_one(collection='blogs', query={'id': id})
        return cls(author=blog_data['author'],
                   title=blog_data['title'],
                   description =blog_data['description'],
                   id=blog_data['id'])