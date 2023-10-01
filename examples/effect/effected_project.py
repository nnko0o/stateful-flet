import flet as ft
from stateful_flet import Effect
from stateful_flet import StatefulUC

class App(StatefulUC):
    def __init__(self):
        super().__init__()
        # make new state and make the value is `True`
        self.myState = self.state(True)
        # setup the effect to print the value of state when changes
        self.effect = Effect(lambda: print('State Changed to : ', self.myState.get()), [self.myState])

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
        App()
    )

if __name__=='__main__':
        ft.app(
            target=main,
            view=ft.AppView.WEB_BROWSER
        )