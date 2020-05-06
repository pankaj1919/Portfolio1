from django.db import models
from project.utils import unique_slug_generator
from django.db.models.signals import pre_save, post_save

class Category(models.Model):
    title=models.CharField("Category Name", max_length=100,null=True,blank=True,unique=True)

    class Meta:
        verbose_name_plural = "Portfolio Category"

    def __str__(self):
        return self.title

class portfolio(models.Model):
    category = models.ForeignKey(Category,null=True,blank=True,on_delete=models.CASCADE)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    thumbnail= models.ImageField("Upload Image", upload_to="portfolio/",null=True,blank=True)
    link=models.CharField("Project Link", max_length=100,null=True,blank=True)
    title=models.CharField("Project Name", max_length=100,null=True,blank=True)
    icon=models.CharField("Write Icon Name", max_length=100,null=True,blank=True)

    class Meta:
        verbose_name_plural = "Portfolio"

    def __str__(self):
        return self.title
        

def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(rl_pre_save_receiver, sender=portfolio)