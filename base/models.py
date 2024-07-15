from django.db import models
from django.contrib.auth.models  import User



class Topic (models.Model):
    name=models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    



class Room(models.Model):
    host=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    topic=models.ForeignKey(Topic,on_delete=models.SET_NULL,null=True)
    name=models.CharField(max_length=200)
    description=models.TextField(null=True,blank=True)
    updated =models.DateTimeField(auto_now=True)
    participants=models.ManyToManyField(User,related_name='participants',blank=True)
    #everytime the model is updated keep track of the time
    created=models.DateTimeField(auto_now_add=True)#when the model is created keep track of the time
    class Meta:
        ordering=['-updated','-created'] #sort the rooms by the time they were created in a descending order without - is in the ascending order
    def __str__(self):
        return self.name
    
    
class Message(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    room=models.ForeignKey(Room, on_delete=models.CASCADE)
    body=models.TextField()
    updated =models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)#when the model is created keep track of the time
    def __str__(self):
        return self.body[0:50]
    