from django.db import models
from autoslug import AutoSlugField
from django.template.defaultfilters import slugify
from django.core.validators import FileExtensionValidator
# Create your models here.
class LivingOptionsCategory(models.Model):
   name = models.CharField(max_length=150)
   short_description = models.TextField(max_length=200, null=True, blank=True)
   description = models.TextField(null=True, blank=True)
   single_image = models.ImageField(
      upload_to='living_options/single_images',
      max_length=500,
      validators=[
             FileExtensionValidator(
            allowed_extensions=[
               'png', 'jpg', 'jpeg', 'webp'
            ]
         )
      ],
   )
   slug = AutoSlugField(unique=True, populate_from='name', sep='-', null=True)
   date_created = models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return self.name

   def save(self, *args, **kwargs):
      self.slug = slugify(self.name)
      super().save(*args, **kwargs)

   class Meta:
      verbose_name_plural = "LivingOptions Categories"

class LivingOptions(models.Model):
   title = models.CharField(max_length=255)
   description = models.TextField(null=True, blank=True)
   image = models.ImageField(
      upload_to='living_options/images',
      max_length=500,
      validators=[
             FileExtensionValidator(
            allowed_extensions=[
               'png', 'jpg', 'jpeg', 'webp'
            ]
         )
      ],
   )
   date_posted = models.DateTimeField(auto_now_add=True)
   last_updated = models.DateField(auto_now=True)
   slug = AutoSlugField(unique=True, populate_from='title', sep='-', null=True)

   def __str__(self):
      return f'{self.title} on {self.date_posted}'
      
   def save(self, *args, **kwargs):
      self.slug = slugify(self.title)
      super().save(*args, **kwargs)