import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "events_afro.users"
    verbose_name = _("Users")

    def ready(self):
        with contextlib.suppress(ImportError):
            import events_afro.users.signals  # noqa: F401
