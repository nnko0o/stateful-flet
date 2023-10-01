from typing import List, Optional, Union, T, Callable
from enum import Enum

import logging
from asyncio import create_task
from flet import UserControl, Control, Page

from .exceptions import StateValueError

class State:
    def __init__(
        self,
        value: T,
        type_chack: Optional[Union[T, bool]] = False,
        on_state_update: Optional[Callable] = None,
    ):
        self.value = value
        self.on_state_update = on_state_update
        if type_chack is True:
            self.type = type(self.value)

        elif (type_chack is False) or (type_chack is None):
            self.type = None

        else:
            self.type = type_chack
        
        self.effects = []

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

        if self.on_state_update:
            self.on_state_update()
        
        if len(self.effects) != 0:
            for effect in self.effects:
                effect.execute()

    

    def __str__(self):
        return (
            f"State{self.type if self.type else '<T>'}({self.value})"
        )

    def __repr__(self):
        return (
            f"State{self.type if self.type else '<T>'}({self.value})"
        )
