from rest_framework.versioning import NamespaceVersioning


class CustomNamespaceVersioning(NamespaceVersioning):
    # noinspection SpellCheckingInspection
    def get_versioned_viewname(self, viewname: str, request):
        if "#" in viewname:
            view, version = viewname.split("#", maxsplit=1)
            return f"{version}:{view}"
        return super().get_versioned_viewname(viewname, request)
