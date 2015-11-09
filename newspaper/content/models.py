from django.db import models


class Content(models.Model):
    title = models.CharField(max_length=500)
    subtitle = models.CharField(max_length=500)
    contributors = models.ManyToManyField('Contributor', related_name='content')
    pub_date = models.DateTimeField('date published')


class Article(Content):
    text = models.TextField()
    def show(self):
    	return 'This content was created on {0}/{1}/{2} by {3}.'.format(self.pub_month, 
            self.pub_date.day, self.pub_date.year, self.contributors) 


class Image(Content):
    path = models.FilePathField()
    def info():
    	return '/"{0}/": {1}'.format(self.title, self.subtitle)


class Contributor(models.Model):
    first_name = models.CharField(max_length=500)
  	last_name = models.CharField(max_length=500)
  	content = models.ManyToManyField(Article, related_name='contributor')
  	def die(self):
      del(self)
