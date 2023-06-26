from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

# Create your models here.


class posts(models.Model):

    header = models.CharField(verbose_name='Heading',max_length=100,blank=False)
    tag = models.CharField(verbose_name='Tag',default='All',max_length=100)
    date = models.DateField(auto_now=True,editable=False)
    description = models.TextField(verbose_name='description',max_length=5000,blank=False,default='')
    image = models.ImageField(verbose_name='Image')
    slug = models.SlugField()


    def __str__(self) -> str:
        return self.header

    def slug_creater(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.header)

        return super().save(*args,**kwargs)

        
    def get_absolute_url(self):
        return reverse("post", kwargs={"slug":self.slug,"pk": self.pk})

    def tags(self):
        if self.tag:
            a = self.tag.split(' ')
            l = []
            l.append(a)

        return l

