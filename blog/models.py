from django.db import models

# Create your models here.
class blog(models.Model):
    title = models.CharField(max_length=20)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def summaybody(self):
        return self.body[:10]

    def pub_date_format(self):
        return self.pub_date.strftime('%b %e %Y')
