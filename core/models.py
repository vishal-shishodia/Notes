from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Profile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	mobile=models.CharField(max_length=10)
	address=models.CharField(max_length=50,blank=True,null=True)

	def __str__(self):
		return self.user.username

	@property
	def note_count(self):
		return Note.objects.filter(profile=self).count()

class Note(models.Model):
	profile=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='notes')
	title=models.CharField(max_length=250)
	content=models.TextField()
	uploaded=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('detail_note', kwargs={'pk': self.pk})


class Image(models.Model):
	note=models.ForeignKey(Note,on_delete=models.CASCADE,related_name='images')
	image=models.ImageField(upload_to='image')

	def __str__(self):
		return self.note.title



	