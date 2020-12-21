from django.core.files.storage import FileSystemStorage


class OverwriteMixin:
    def get_available_name(self, name, max_length=None):
        self.delete(name)
        return name


class OverwriteFileSystemStorage(OverwriteMixin, FileSystemStorage):
    pass
