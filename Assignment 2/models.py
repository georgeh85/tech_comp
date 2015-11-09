
import time
from datetime import date
import PIL
from PIL import Image

class Content(object):
    # list to keep track of all pieces of content
    existing_content = []

    def __init__(self, year, month, day, contributors):
        # log each piece of content as existing upon creation
        self.existing_content.append(self)

        # TODO: Delete the following line and replace it with a line
        # that stores the year, month, and day (hint: check out datetime.date)
        self.creation_date = date(year, month, day)

        # list of contirbutors
        self.contributors = contributors

    # this defines a show method that has nothing in it, to be overridden later
    def show(self):
        return 'This content was created on {0}/{1}/{2} by {3}.'.format(self.creation_date.month, 
            self.creation_date.day, self.creation_date.year, self.contributors)


# TODO: Define an Article class that extends the Content class
class Article(Content):

    def __init__(self, year, month, day, contributors, headline, content):
        super(Article, self).__init__(year, month, day, contributors)
        self.headline = headline
        self.content = content

    def show(self):
        return '{0}\nby {1}\n\n{2}/{3}/{4}\n{5}'.format(self.headline,
            self.contributors, self.creation_date.month, self.creation_date.day, 
            self.creation_date.year, self.content)

# TODO: Define an Picture class that extends the Content class
class Picture(Content):
    def __init__(self, year, month, day, contributors, title, caption, path):
    	super(Picture, self).__init__(year, month, day, contributors)
        self.title = title
        self.caption = caption
        self.path = path

    def show(self):
        im = Image.open("sexy.gif")
        im.show()
        return '{0} \nTitle: {1} \n{2} \n{3}'.format(super(Picture.self).show(), 
            self.path, self.caption)