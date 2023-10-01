import concurrent.futures

from typing import List, Optional, Union, T, Callable
from enum import Enum


from asyncio import create_task
from flet import UserControl, Control, Page

from .exceptions import StateValueError


class Context:
    def __init__(
        self,
        value: T,
        type_chack: Optional[Union[T, bool]] = False,
    ):
        self.value = value
        if type_chack is True:
            self.type = type(self.value)

        elif (type_chack is False) or (type_chack is None):
            self.type = None

        else:
            self.type = type_chack

        self.effects = []
        self.subscribers: List[Callable] = []

    def subscribe(self, func: Callable):
        if func in self.subscribers:
            self.unsubscribe(func)

        if isinstance(func, UserControl):  # StatefulUC
            try:
                func = func.re_render
            except AttributeError:
                raise ValueError(f"")  # TODO: write good error

        self.subscribers.append(func)

    def unsubscribe(self, func: Callable):
        try:
            self.subscribers.remove(func)
        except ValueError:
            return

    def get(self) -> Optional[T]:
        return self.value

    def set(self, value: Union[T, Callable[..., T]]):
        if self.type:
            if isinstance(value, Callable):
                data = value(self.get())
                if not isinstance(data, self.type):
                    raise StateValueError(type(data), self.type)

                self.value = data

            elif isinstance(value, self.type):
                self.value = value
            else:
                raise StateValueError(type(value), self.type)
        else:
            if isinstance(value, Callable):
                data = value(self.get())
                self.value = data

            else:
                self.value = value

        if len(self.subscribers) > 0:
            self.__post()

        if len(self.effects) != 0:
            for effect in self.effects:
                effect.execute()

    def __post(self):
        batch_size = 5
        num_batches = (len(self.subscribers) + batch_size - 1) // batch_size

        with concurrent.futures.ThreadPoolExecutor(max_workers=num_batches) as executor:
            batches = [
                self.subscribers[i : i + batch_size]
                for i in range(0, len(self.subscribers), batch_size)
            ]

            for batch in batches:
                print(batch)
                results = executor.map(lambda func: func(True), batch)

    def __str__(self):
        return f"Context{self.type if self.type else '<T>'}({self.value})"

    def __repr__(self):
        return f"Context{self.type if self.type else '<T>'}({self.value})"
