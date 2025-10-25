import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from django.contrib.auth.models import User

users = User.objects.all()
print(f"\n{'=' * 60}")
print(f"Total Users: {users.count()}")
print(f"{'=' * 60}\n")

for user in users:
    print(f"ID: {user.id}")
    print(f"Username: {user.username}")
    print(f"Email: {user.email}")
    print(f"Superuser: {user.is_superuser}")
    print(f"Staff: {user.is_staff}")
    print(f"Active: {user.is_active}")
    print(f"Joined: {user.date_joined}")
    print("-" * 60)
