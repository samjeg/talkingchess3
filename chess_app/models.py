# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class UserProfileInfo(models.Model):
	user = models.OneToOneField(User, related_name='userprofileinfos', on_delete=models.CASCADE, blank=True, null=True, default=1)
	picture = models.ImageField(upload_to='profile_images', blank=True, null=True)

	def __str__(self):
		return self.user.username

	def get_absolute_url(self):
		return reverse('chess_app:profile_detail', kwargs={'pk':self.pk})

class Chessboard(models.Model):
	player = models.OneToOneField(UserProfileInfo, on_delete=models.CASCADE, blank=True, null=True, default=1)
	user_input_state = models.CharField(max_length=1000)

	def __str__(self):
		return self.user_profile.username

	def get_absolute_url(self):
		return reverse('chess_app:chess_detail', kwargs={'pk':self.pk})

class ChessboardComment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
	chessboard = models.ForeignKey(Chessboard, related_name="comments", on_delete=models.CASCADE, blank=True, null=True)
	comment = models.CharField(max_length=140)
	comment_picture_path = models.CharField(max_length=20, blank=True, null=True)

	def __str__(self):
		return self.user.username