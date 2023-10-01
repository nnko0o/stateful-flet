import flet as ft
from stateful_flet import StatefulUC
from stateful_flet import Reducer, ReducerAction, Reduce

class MyReducer(Reduce):
    def __init__(self):
        super().__init__()
    
    @Reduce.reduce("pls")
    def pls(self, state:int, action: ReducerAction) -> int:
        return state + 1
    
    @Reduce.reduce("min")
    def min(self, state:int, action:ReducerAction) -> int:
        if state == 0: 
            return state
        return state - 1
    
    @Reduce.reduce("del")
    def del__(self, _, __) -> int:
        return 0

print("app reloaded..!")
class App(StatefulUC):
    def __init__(self):
        super().__init__()
        # make new reducer and add self.reducer as handler and 0 as a value
        self.myReducer = self.reducer(0, MyReducer)

    def build(self):
        self._content = ft.Column(
            controls=[
                ft.ElevatedButton(
                    text     = 'Click' if self.myReducer.get() == 0 else f"clicked, {self.myReducer.get()}",
                    # when the user click, we will dispatch to reducer "pls"
                    on_click = lambda e: self.myReducer.dispatch("pls"),
                    # when the user long press, we will going to dispatch to the reducer "min"
                    on_long_press= lambda e: self.myReducer.dispatch("min"),

                    # some design
                    bgcolor  = ft.colors.BLUE_GREY_800 ,
                    width=150,
                    height=150,
                ),
                ft.IconButton(
                    icon=ft.icons.REMOVE_CIRCLE_OUTLINE,
                    # when the user click, we will to dispatch to reducer "reset"
                    on_click = lambda e: self.myReducer.dispatch('reset'),
                    icon_color="#B43131"
                )
            ],
            horizontal_alignment="center",
            alignment="center",
        )

        return self._content

def main(page: ft.Page):
    page.vertical_alignment   = 'center'
    page.horizontal_alignment = 'center'

    page.add(
        App()
    )

if __name__=='__main__':                                                                                                      ft.app(
            target=main,
        )
