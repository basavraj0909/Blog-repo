import uuid
import random
import string
from django.db import models
from django.utils import timezone


class User(models.Model):
    user_id = models.CharField(max_length=14, unique=True, blank=True, editable=False)

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=15, unique=True)

    is_active = models.BooleanField(default=True)
    is_phone_verified = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

    def generate_user_id(self):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(12))

    def save(self, *args, **kwargs):
        # Only generate user_id if it doesn't already exist
        if not self.user_id:
            # Generate a UUID and format it as desired
            self.user_id = self.generate_user_id()
            self.user_id = f"{self.user_id[:4]}-{self.user_id[4:8]}-{self.user_id[8:]}"

        # Call the parent class's save method
        super(User, self).save(*args, **kwargs)
