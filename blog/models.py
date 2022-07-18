
from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Category(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    create = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    


     


class Blog(models.Model):
    title = models.CharField(_("Post Title"), max_length=255)
    tags = models.CharField(_("Tag"), max_length=50)
    category = models.CharField(_("Category"), max_length=50)
    desc = models.TextField(_("Description"))

    def __str__(self):
        return self.title
    
