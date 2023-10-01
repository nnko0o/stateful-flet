 `<div align="center">`
   `<a href="https://github.com/nnko0o/statful-flet">`
   `<img src="https://github.com/nnko0o/stateful-flet/images/Icon-512.png" width="180" height="180" alt="Stateful Flet Library">`
  `</a>`

**State Management for Flet**

</div>

# Stateful Flet

Flet library, makes flet more stateful BY adding state management close to React
Easy, Speed and Strong

# Installation (BETA)

Install From Git Branch:

```bash
pip3 install -U git+https://github.com/nnko0o/stateful-flet.git
```

# Basic Usage

```python
import flet as ft
from stateful_flet import StatefulUC

class App(StatefulUC):
    def __init__(self):
        super().__init__()
        # make new state and make the value is `True`
        self.myState = self.state(True)

    def build(self):
        self._content = ft.Column(
            controls=[
                ft.ElevatedButton(
                    text     = 'State: '+str(self.myState.get()),
                    # when the user click, thge state wull change
                    on_click = lambda e: self.myState.set(lambda v: not v),

                    # Color will changes when state change and re-render the page
                    bgcolor  = ft.colors.BLACK if self.myState.get() else ft.colors.BLUE_GREY_800 ,
                    color    = ft.colors.WHITE24 if self.myState.get() else ft.colors.BLUE_GREY_50
                )
            ]
        )

        return self._content

def main(page: ft.Page):
    page.vertical_alignment   = 'center'
    page.horizontal_alignment = 'center'
  
    page.add(
        App(page)
    )

if __name__=='__main__':
        ft.app(
            target=main,
        )
```

# Philosophy

flet missing a state management from make it more smoothly `<br />`
so i get React State Management and make it more pythonic and work perfectly with flet `<br />`
ِAnd make it fast as possible with minimal use of hardware resources `<br />`
By remove the multiple loops in the threads in `Effect` and make it work by add the effect function in the Stateful Objects

# TODO:

- ~~_State_ - work hand by hand with flet.~~
- ~~_SattfulUserControl(StatdfulUC)_  - statful control can rerender and make `State` and `Context` easy.~~
- ~~Effect - simple stateful hook run some function when some Stateful Object changes.~~
- ~~Context - State but in multiple StatdfulUC, change from one place, and all place's will be rerender.~~
- Add String Docs for all function and classes.
- Add Full API Reference and Docs for all the library.
- Make A Class and UI helpers for customize re-rendering for make your application more faster and stable.

# Contact Me:

[Telegram](https://t.me/nnk0o)
