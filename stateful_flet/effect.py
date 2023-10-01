from typing    import List, Optional, Union, TypeVar, Callable

from threading import Thread
from time      import sleep

from asyncio import get_event_loop, new_event_loop
from inspect import iscoroutinefunction as isasync

from .state import State

T = TypeVar("T")

class Effect:
    def __init__(
      self,
      func: Callable,
      states: List[State] = [],
      *func_args,
      **func_kwargs
    ):
        self.func     = func
        self.func_arg = (
             func_args  or (),
            func_kwargs or {},
        )
        self.states = states
        for s in self.states:
            s.effects.append(self)

    def execute(self):
        if self.func is None:
            return

        if isasync(self.func):
            try:
                loop = get_event_loop()
                loop.create_task(
                    func(*self.func_arg[0], **self.func_arg[1],)
                )

            except RuntimeError: # when theres no loop in the thread or task
                loop = new_event_loop()
                loop.create_task(
                    func(*self.func_arg[0], **self.func_arg[1],)
                )
        else:
            runner_thread = Thread(
                target=self.func,
                args=self.func_arg[0],
                kwargs=self.func_arg[1],
            )
            runner_thread.start()
