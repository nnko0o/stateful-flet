from typing import (
  Optional,
  Union,
  Dict,
  Callable,
  T
  )

from .exceptions import StateValueError

# class StateValueError(ValueError): pass

class ReducerAction:
    def __init__(
      self,
      type_:str,
      data:Optional[T] = None,
    ):
        self.type = type_
        self.data = data

    def __str__(self):
        return f"ReducerAction(type={self.type})"

    def __repr__(self):
        return self.__str__()

class Reduce:
    def __init__(
      self,
    ):
        self.reducer = self.__reducer
        self.reducers: Dict[str, Callable] = {}

    def __reducer(self, state:type[T], action:ReducerAction) -> Optional[T]:
        if len(self.reducers) <= 0:
            return state

        if action.type not in self.reducers:
            return state

        reducer_hanlder = self.reducers.get(action.type)
        return reducer_hanlder(state, action)

    @staticmethod
    def reduce(action_type: str):
        def decdector(func: Callable):
            def wrapper(*args, **kwargs):
                self: Reduce = args[0]
                self.reducers.update({
                  action_type: func,
                })
                result = func(*args, **kwargs)
                return result

            return wrapper

        return decdector

class Reducer:
    def __init__(
      self,
      value: T,
      reducer: Union[Callable[[..., T, ReducerAction], None], Reduce],
      type_chack: Optional[Union[T, bool]] = True,
      on_state_update: Optional[Callable] = None,
    ):
        self.__value = value
        self.on_state_update = on_state_update
        self.reducer = reducer

        if type_chack is True:
            self.type = type(self.__value)

        elif (type_chack is False) or (type_chack is None):
            self.type = None

        else:
            self.type = type_chack
   
        self.effects = []

    def get(self) -> Optional[T]:
        return self.__value

    def dispatch(
      self,
      action: ReducerAction
    ) -> Optional[T]:
        if isinstance(action, str):
            action = ReducerAction(action)

        elif not isinstance(action, ReducerAction):
            raise ValueError(f"{self.__class__.__name__}.dispatch({action}) - action must be implemented `str` or `ReduceAction`")

        result = self.__invoke(self.get(), action)
        return result

    def __set(self, value: Optional[T]) -> None:
        if self.type:
            if not isinstance(value, self.type):
                raise StateValueError(type(value), self.type)

            self.__value = value
        else:
            self.__value = value

        if self.on_state_update:
            self.on_state_update()

        if len(self.effects) > 0:
            for effect in self.effects:
                effect.execute()

    def __invoke(
      self,
      state: Optional[T],
      action: ReducerAction
    ) -> Optional[T]:
        handler = self.reducer
        if isinstance(handler, Callable):
            result = handler(state, action)
            self.__set(result)
            return result

        elif isinstance(handler, Reduce):
            result = handler.reducer(state, action)
            self.__set(result)
            return result

        else:
            raise ValueError(f"{self.__class__.__name__}.__invoke() - invalid reducer must be implemented `Callbale` or class isinstance `Reduce`")

