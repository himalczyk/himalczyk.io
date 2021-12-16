from django.db import models
# from django.utils.text import slugify

# Create your models here.

class User(models.Model):
    first_name = models.TextField(blank=True, null=True)
    last_name = models.TextField(blank=True, null=True)
    age = models.IntegerField()
    email = models.EmailField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    # def save(self (*args, **kwargs)):
    #     if not self.slug:
    #         self.slug = slugify(self.title)

    #     super(User).save(*args, **kwargs)

