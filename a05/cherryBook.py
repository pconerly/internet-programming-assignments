import cherrypy
from jinja2 import Environment #, PackageLoader
from jinja2 import FileSystemLoader
from bookdb import BookDB


class Book(object):
    def index(self):
        books = BookDB()
        env = Environment(loader=FileSystemLoader('templates'))
        tmpl = env.get_template('booklist.html')
        
        return tmpl.render(books=books.titles())
    index.exposed = True

    def BookDetail(self, id):
        books = BookDB()
        env = Environment(loader=FileSystemLoader('templates'))
        tmpl = env.get_template('bookdetail.html')

        return tmpl.render(detail=books.title_info(id))
    BookDetail.exposed = True

    detail = BookDetail

cherrypy.quickstart(Book(), '/', 'tutorial.conf')

