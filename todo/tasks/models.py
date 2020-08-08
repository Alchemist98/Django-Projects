from django.db import models

# Create your models here.
class Task(models.Model):
	task = models.CharField(max_length=200)
	complete = models.BooleanField(default=False)
	created_on = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-created_on']

	def __str__(self):
		return self.task