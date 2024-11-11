from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField
from django.utils.text import slugify

class News(models.Model):
    news_topic = models.CharField(max_length=300)
    news_desc = HTMLField()
    news_slug = AutoSlugField(populate_from='news_topic', unique=True, null=True, default=None)

    # Code to chane AutoSLug if edited from templates

    def save(self, *args, **kwargs):
        # If the news_topic changes, regenerate the news_slug manually
        if self.pk:  # If the instance already exists (i.e., not a new object)
            old_instance = News.objects.get(pk=self.pk)
            if old_instance.news_topic != self.news_topic:
                # Manually regenerate the slug
                self.news_slug = slugify(self.news_topic)  # Use slugify to generate the new slug
        
        # Save the model instance as usual
        super(News, self).save(*args, **kwargs)

    def __str__(self):
        return self.news_topic
