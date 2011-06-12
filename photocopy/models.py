from django.db import models
import urllib

class Photocopy(models.Model):
    title = models.CharField(max_length=4096)
    url = models.CharField(max_length=4096)
    description = models.TextField()
    article_content = models.TextField()
    save_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
       ordering = ["-update_date"]

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.fetch_content();
        super(Photocopy, self).save(*args, **kwargs) # Call the "real" save() method.

    def fetch_content(self):
        print self.url
        self.article_content = urllib.urlopen(self.url).read()
        print self.article_content
