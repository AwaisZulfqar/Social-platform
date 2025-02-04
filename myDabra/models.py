from django.db import models

# Create your models here.


# creating User Model
class User(models.Model):
   
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=40)
    password = models.CharField(max_length=16,blank=True)
    profile_pic = models.ImageField(upload_to="profile_pics/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    


    
    
