# Effect

A Hook used for eun some function when some stateful object *(state, context reducer, etc...)* change's and re-render the page

Doesn't care about the page type for running your function

## Usage

```python
import flet as ft
```

...

Make static application using StatefulUC like the "first step" page

and add new effect and he will get's two arguments:

### `Effect(func: Callable, states: List[StatefulObject])` .

  •  func: `lambad: print("hi")` or `self.effectHanlder`

  •  states: `[self.myfState, ...]`

So we enter `lambda: print('State Changed to : ', self.myState.get())` as func

and enter `self.myState` to the states argument

When the user click the button and change the state the func of state will called in the background


#### and that's all after some time i will complete the other class and make it more perfect i can
