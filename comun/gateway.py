from typing import TypeVar

from django.db.models import Manager, Model

T = TypeVar("T", bound=Model)


class ModelManager(Manager):
    def __init__(self) -> None:
        temp = self.model
        super().__init__()
        self.model = temp

    def __init_subclass__(cls, model: T) -> None:
        cls.model = model
        return super().__init_subclass__()
