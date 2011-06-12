from django.db import models

class Photocopy(models.Model):
	url = models.CharField(max_length=4096)
	description = models.TextField()
	save_date = models.DateTimeField(auto_now_add=True)
	update_date = models.DateTimeField(auto_now=True)

