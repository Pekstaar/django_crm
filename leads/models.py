from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save

# Create your models here.


# Custom user class
class User(AbstractUser):
    pass  # No fields are added all are inherited from django


class UserProfiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Lead(models.Model):
    first_name = models.CharField(max_length=20)  # reps string in python
    # string of 20 characters maximum length
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)  # age of int type
    # if lead is deleted the lead is deleted
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organisation = models.ForeignKey(UserProfiles, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email

# function to listen when user is saved in database to create user profile


def post_user_created_signal(sender, instance, created, **kwargs):
    print("saved on signal instance: ", instance, created)

    if created:
        UserProfiles.objects.create(user=instance)


post_save.connect(post_user_created_signal, sender=User)

#   # tuple of choices
#     SOURCE_CHOICES = (
#         ('YouTube', 'YouTube'),
#         ('Google', 'Goolge')
#         ('Newsletter', 'Newsletter')
#     )
# phoned = models.BooleanField(default=False)
# source = models.CharField(choices=SOURCE_CHOICES,
#                           max_length=100)  # soure of lead
# profile_picture = models.ImageField(blank=True, null=True)
# special_files = models.FileField(
#     blank=True, null=True)  # specifies file storage
