from flask import abort
class Post():

    POSTS = [
        {'id':1, 'title': 'First Post', 'Content':'This is my First post'},
        {'id':2, 'title': 'Second Post', 'Content':'This is my Second post'},
        {'id':3, 'title': 'Third Post', 'Content':'This is my Third post'},
        {'id':4, 'title': 'fourth Post', 'Content':'This is my fourth post'} ,   
    ]
    @classmethod
    def all(cls):
        """return all posts"""
        return cls.POSTS


    @classmethod 
    def find (cls, id):

        """return the selected post"""

        try:
            return cls.POSTS[int(id) - 1]
        
        except IndexError:
            abort(404)

    