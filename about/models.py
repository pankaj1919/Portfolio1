from django.db import models

# Create your models here.
class About(models.Model):
    description=models.TextField("Write About You",null=True,blank=True)
    image=models.ImageField("Upload Your Image", upload_to="about/",null=True,blank=True)

    class Meta:
        verbose_name_plural = "About"

    def __str__(self):
        return self.description

class Service(models.Model):
    service=models.CharField("Title Of Your Service", max_length=100,null=True,blank=True)
    service_icon=models.CharField("Write Icon Name", max_length=100,null=True,blank=True)
    service_des=models.TextField("Service Detail",null=True,blank=True)

    class Meta:
        verbose_name_plural = "Service"

    def __str__(self):
        return self.service


class Client(models.Model):
    client_name=models.CharField("Name Of Client", max_length=100,null=True,blank=True)
    image=models.ImageField("Upload Client Image/Logo", upload_to="client/",null=True,blank=True)
    link=models.TextField("Link Of Client",null=True,blank=True)

    class Meta:
        verbose_name_plural = "Client"

    def __str__(self):
        return self.client_name


class Facts(models.Model):
    fact_icon=models.CharField("Write Icon Name", max_length=100,null=True,blank=True)
    fact_title=models.CharField("Fact Title",max_length=100,null=True,blank=True)
    count=models.CharField("Fact total Number", max_length=100,null=True,blank=True)

    class Meta:
        verbose_name_plural = "Fact"

    def __str__(self):
        return self.fact_title

class Profile(models.Model):
    name=models.CharField("Write Client Name", max_length=100,null=True,blank=True)
    image=models.ImageField("Upload Client Image", upload_to="testonomial/",null=True,blank=True)
    position=models.CharField("Designation", max_length=100,null=True,blank=True)
    des=models.TextField("Client Words",null=True,blank=True)

    class Meta:
        verbose_name_plural = "Profile"

    def __str__(self):
        return self.name