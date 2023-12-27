from django.db import models
from autoslug import AutoSlugField
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 80, null = False, blank = False)
    slug = AutoSlugField(populate_from = 'name', unique = True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Pdf(models.Model):
    pdf = models.FileField(upload_to="pdfs/")
    category = models.ForeignKey(
        Category, related_name = 'pdftools',
        on_delete = models.SET_NULL,
        blank = True,
        null = True
        )
    
    def __str__(self):
        return f"{self.pdf}"
    