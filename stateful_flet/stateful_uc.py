from typing import List, Optional, Union, T, Callable
from enum import Enum

import logging
from asyncio import get_event_loop
from inspect import iscoroutinefunction as isasync

from flet import UserControl, Control

from .state import State
from .reducer import Reducer

class StatePageType(Enum):
    ASYNC: str = "async"
    SYNC: str = "sync"

class StatefulUC(UserControl):
    def __init__(
        self,
          page_type : StatePageType = StatePageType.SYNC,
        before_build: Callable = None,
        after_build : Callable = None,

        # UserControl args
        *us_args,
        **us_kwargs
    ):
        super().__init__(*us_args, **us_kwargs, )
        if isinstance(page_type, StatePageType):
            self.type = page_type.value
        elif isinstance(page_type, str):
            if page_type.lower().strip() not in ["async", "sync"]:
                raise ValueError(
                    f"StatefulUC(type={page_type}) invaild `type` must be implemented `sync`, `async` Or a `StatePageType`"
                )
            self.type = page_type.lower().strip()
        else:
            raise ValueError(
                f"StatefulUC(type={page_type}) invaild `type` must be implemented `sync`, `async` Or a `StatePageType` not {type(page_type)}"
            )

        self.before_build = before_build
        self.after_build = after_build

        if (self.before_build is not None and not isinstance(self.before_build, Callable)) and \
           (self.after_build  is not None and not isinstance(self.after_build , Callable)):
            raise ValueError(
                f'{self.__class__.__name__} - `before_build` and `after_build` must be implemented `Callable`'
            )

        self.states:  List[State] = []
        self.effects: List[Effect] = []
        self.reduces: List[Reducer] = []

    def state(
        self,
        value: T,
        type_chack: Optional[Union[T, bool]] = True,
    ) -> State:
        state = State(
            value=value, type_chack=type_chack, on_state_update=self.re_render
        )
        self.states.append(state)

        return state
    
    def reducer(
        self,
        value: T,
        reducer: Union[Callable[[..., T, ReducerAction], None], Reduce],
        type_chack: Optional[Union[T, bool]] = True,
    ):
        reducer_ = Reducer(value, reducer, type_chack, self.re_render)
        self.reduces.append(
            reducer_
        )
        return reducer_

    def re_render(self, update:bool=True):
        print(f"{self.__class__.__name__}.re_render({update})")
        logging.debug(f"{self.__class__.__name__}.re_render()")
        print(self.states)
        self._build()

        # update
        # here we going to chack its a async or sync page, by the Your Input page_type : StatePageType
        if update:
            if self.type == StatePageType.ASYNC.value:  # async
                try:
                    loop = get_event_loop()
                    loop.create_task(self.update_async())
                except NotImplementedError:
                    raise ValueError(
                        f"{self.__class__.__name__}.update_async() - The Page Is A `sync` Page not `async`"
                    )

            else:  # sync
                try:
                    self.update()
                except NotImplementedError:
                    raise ValueError(
                        f"{self.__class__.__name__}.update() - The Page Is A `async` Page not `sync`"
                    )
    
    def build(self) -> Union[Control, List[Control]]:
        pass

    def _build(self):
        if self.before_build:
            self.before_build()
        content = self.build()
        if isinstance(content, Control):
            self.controls = [content]
        elif isinstance(content, List) and all(
            isinstance(control, Control) for control in content
        ):
            self.controls = content
        else:
            raise Exception(
                f"{self.__class__.__name__}.build() method must be implemented and returning either Control or List[Control]."
            )
        if  self.after_build:
            self.after_build()
