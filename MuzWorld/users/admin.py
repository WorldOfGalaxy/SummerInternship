from django.contrib import admin

from .models import Musician
from .models import Genre
from .models import Audio
from .models import Comment
from .models import Point


admin.site.register(Musician)
admin.site.register(Genre)
admin.site.register(Audio)
admin.site.register(Comment)
admin.site.register(Point)