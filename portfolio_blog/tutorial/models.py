from django.db import models

# Create your models here.
class Tutorial(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    content = models.TextField(default="full content of the article")
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to="images/")
    
    def __str__(self):
        return self.title