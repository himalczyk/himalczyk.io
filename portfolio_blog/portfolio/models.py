from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    status = models.BooleanField(default=False)
    image = models.ImageField(upload_to="images/")
    url = models.URLField(default='placeholder')
    
    def __str__(self):
        return self.title

