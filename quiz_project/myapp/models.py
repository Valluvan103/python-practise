from django.db import models

# Create your models here.
class Quiz(models.Model):
	question=models.CharField(max_length=250)

	option1=models.BooleanField(default=False)
	option2=models.BooleanField(default=False)
	option3=models.BooleanField(default=False)
	option4=models.BooleanField(default=False)

	answer=models.CharField(max_length=50)