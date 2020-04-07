from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
    feeling_good = models.BooleanField(default=True)

#to help with admin viewing 
    def __str__(self):
        '''
        Its one of those magic functions!
        This is how to show the name up in the admin page
        '''
        return self.title


#to add polish create functions within your model class that do specifics
    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

