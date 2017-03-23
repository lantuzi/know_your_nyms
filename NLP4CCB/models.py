from __future__ import unicode_literals
from django import forms
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class WordRelationshipForm(forms.Form):
	word = forms.CharField(
		max_length=100,
		widget=forms.TextInput()
	)

class UserStat(models.Model):
	user = models.OneToOneField(User)
	rounds_played = models.IntegerField()
	total_score = models.FloatField()

class Relation(models.Model):
	type = models.CharField(max_length=50)
	base_word = models.CharField(max_length=50)
	input_word = models.CharField(max_length=50)
	word_net_score = models.FloatField()
	model_score = models.FloatField()

	def __str__(self):
		return ', '.join([self.type, self.base_word, self.input_word])

class UserInput(models.Model):
	user = models.ForeignKey(User)
	round_number = models.IntegerField()
	round_time = models.IntegerField()
	relation = models.ForeignKey(Relation)
	word_score = models.FloatField()
	challenge = models.BooleanField()
