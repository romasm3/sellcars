import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from django.contrib.auth.models import User

# Create superuser
username = "admin"
email = "admin@sellcars.com"
password = "admin123"

if User.objects.filter(username=username).exists():
    print(f"❌ User '{username}' already exists!")
else:
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f"✅ Superuser '{username}' created successfully!")
    print(f"   Email: {email}")
    print(f"   Password: {password}")
    print("\n🔐 You can login at: http://127.0.0.1:8000/accounts/login/")
    print("🛠️  Or admin panel: http://127.0.0.1:8000/admin/")
