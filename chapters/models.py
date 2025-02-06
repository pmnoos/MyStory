from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from tinymce.models import HTMLField as richtext


class Chapter(models.Model):
    title = models.CharField(max_length=255, blank=False)
    subtitle = richtext(blank=True)
    content = richtext(blank=True)
    cover_image = models.ImageField(upload_to='images/', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Track updates
    order = models.IntegerField(default=999)  # Field to control display order

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title) if self.title else slugify("chapter-" + str(self.pk or "new"))
        super().save(*args, **kwargs)

    def clean(self):
        # Validate title field
        if not self.title:
            raise ValidationError("Title cannot be blank.")

    def __str__(self):
        return self.title
