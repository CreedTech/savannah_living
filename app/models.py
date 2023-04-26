from django.db import models
from autoslug import AutoSlugField
from django.template.defaultfilters import slugify
from django.core.validators import FileExtensionValidator
# Create your models here.

LEARNING_DISABILITIES = 'Learning disabilities'
AUTISM = 'Autism'
PHYSICAL_DISABILITIES = 'Physical disabilities'
ACQUIRED_BRAIN_INJURIES = 'Acquired brain injuries'
MENTAL_HEALTH = 'Mental health'
HOMELESSNESS = 'Homelessness'
YOUNG_PEOPLE = 'Young People'
# Define your categories as choices here
CATEGORIES_CHOICES = [
    (LEARNING_DISABILITIES, 'Learning disabilities'),
    (AUTISM, 'Autism'),
    (PHYSICAL_DISABILITIES, 'Physical disabilities'),
    (ACQUIRED_BRAIN_INJURIES, 'Acquired brain injuries'),
    (MENTAL_HEALTH, 'Mental health'),
    (HOMELESSNESS, 'Homelessness'),
    (YOUNG_PEOPLE, 'Young People'),
    # Add more categories as needed
]


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
    slug = AutoSlugField(
        unique=True, populate_from='title', sep='-', null=True)

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class House(models.Model):

    # Add any other fields you need for the house model here
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    description = models.TextField(null=True, blank=True)
    # Create a ManyToManyField for the categories/tags
    categories = models.ManyToManyField('Category')
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
    slug = AutoSlugField(
        unique=True, populate_from='name', sep='-', null=True)

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Category(models.Model):
    name = models.ForeignKey(LivingOptions, on_delete=models.CASCADE)

    slug = AutoSlugField(
        unique=True, populate_from='name', sep='-', null=True)

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
