from django.db import models

# Create your models here.
class resume_study(models.Model):
    title=models.CharField("Title", max_length=100,null=True,blank=True)
    icon=models.CharField("Write Icon Name", max_length=100,null=True,blank=True)
    time=models.CharField("Collage Timeline Date", max_length=100,null=True,blank=True)
    collage=models.CharField("Collage Name", max_length=100,null=True,blank=True)
    degree=models.CharField("Collage Course", max_length=100,null=True,blank=True)
    des=models.TextField("Description About Degree",null=True,blank=True)

    class Meta:
        verbose_name_plural = "Resume Study"

    def __str__(self):
        return self.collage

class work_history(models.Model):
    title=models.CharField("Title", max_length=100,null=True,blank=True)
    icon=models.CharField("Write Icon Name", max_length=100,null=True,blank=True)
    time=models.CharField("Job Duration", max_length=100,null=True,blank=True)
    place=models.CharField("Company Name", max_length=100,null=True,blank=True)
    post=models.CharField("Position", max_length=100,null=True,blank=True)
    des=models.TextField("Description About Job",null=True,blank=True)

    class Meta:
        verbose_name_plural = "Work History"

    def __str__(self):
        return self.place

class cv_download(models.Model):
    link=models.TextField("Link Of Your Resume",null=True,blank=True)


class Skill(models.Model):
    name=models.CharField("Skill Name", max_length=100,null=True,blank=True)
    value=models.CharField("Rate Your Skill", max_length=100,null=True,blank=True)
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Skill"

class Technical(models.Model):
    name=models.CharField("Technical Skill Name", max_length=100,null=True,blank=True)
    value=models.CharField("Rate Your Skill", max_length=100,null=True,blank=True)
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Technical Skill"