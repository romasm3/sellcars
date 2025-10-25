from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.accounts"  # ✅ svarbu, kad būtų "apps.accounts"
    verbose_name = "Accounts"
