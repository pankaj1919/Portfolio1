from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    phone=models.CharField("Write Phone Name", max_length=100,null=True,blank=True)
    # image=models.ImageField("Upload Client Image", upload_to="profile/",null=True,blank=True)
    image2=models.ImageField("Upload Client Image", upload_to="user/",null=True,blank=True)
    gender=models.CharField("Write gender", max_length=100,null=True,blank=True)
    position=models.CharField("Designation", max_length=100,null=True,blank=True)

    class Meta:
        verbose_name_plural = "Profile"

    def __str__(self):
        return f'{self.user.username} Profile'


    # def save(self, force_insert=False):
    #     super().save(force_insert)

    #     img = Image.open(self.image.path)

    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)       

        