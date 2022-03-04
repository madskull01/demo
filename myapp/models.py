from django.db import models

# Create your models here.
class Emp(models.Model):
    
    id=models.AutoField(primary_key=True)
    teamname=models.CharField(max_length=255)
    teamlogo=models.ImageField(upload_to='images/',default="a.png")
    player1name=models.CharField(max_length=255)
    player1image=models.ImageField(upload_to='images/',default="a.png")
    player2name=models.CharField(max_length=255)
    player2image=models.ImageField(upload_to='images/',default="a.png")
    player3name=models.CharField(max_length=255)
    player3image=models.ImageField(upload_to='images/',default="a.png")
    player4name=models.CharField(max_length=255)
    player4image=models.ImageField(upload_to='images/',default="a.png")
    player5name=models.CharField(max_length=255,blank=True,default='')
    player5image=models.ImageField(upload_to='images/',default="a.png",blank=True)
    player6name=models.CharField(max_length=255,blank=True,default='')
    player6image=models.ImageField(upload_to='images/',default="a.png",blank=True)
    
    
   

    def __str__(self):
        return self.teamname

class Register(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    username=models.CharField(max_length=255)
    password=models.CharField(max_length=255)


    def __str__(self):
        return self.name


class Login(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=255)
    password=models.CharField(max_length=255)

    
    def __str__(self):
        return self.name