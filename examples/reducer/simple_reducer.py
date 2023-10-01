import flet as ft
from stateful_flet import StatefulUC
from stateful_flet import Reducer, ReducerAction

print("app reloaded..!")
class App(StatefulUC):
    def __init__(self): 
        super().__init__()
        # make new reducer and add self.reducer as handler and 0 as a value
        self.myReducer = self.reducer(0, self.reduce, on_state_update=self.re_render)

    def reduce(self, state: int, action: ReducerAction):
        # if the action type(name) is (*) do:*
        if action.type == "pls":
            return state + 1
        elif action.type == "min":
            return state - 1
        elif action.type == "reset":
            return 0 
    
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

if __name__=='__main__':
        ft.app(
            target=main,
        )