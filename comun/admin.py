import inspect
from django.db.models import Model
from django.contrib import admin


def register(container):
    for _, klass in inspect.getmembers(container):
        # Think discrete here (Model && META => NO ABSTRACT && ADMIN => ModelAdmin)
        if (
            inspect.isclass(klass)
            and issubclass(klass, Model)
            and getattr(klass, "Admin", False)
            and issubclass(klass.Admin, admin.ModelAdmin)
        ):
            # noinspection PyBroadException
            try:
                admin.register(klass)(getattr(klass, "Admin"))
            except Exception:
                print(f"Model {klass.__name__} tried to be on admin but was ignored.")
