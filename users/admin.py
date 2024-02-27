from django.contrib import admin
from users.models import *

admin.site.register(UserModel)
admin.site.register(VerificationCodeModel)
admin.site.register(FollowersModel)