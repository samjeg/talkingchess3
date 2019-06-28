# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import UserProfileInfo, Chessboard, ChessboardComment

admin.site.register(UserProfileInfo)
admin.site.register(Chessboard)
admin.site.register(ChessboardComment)
