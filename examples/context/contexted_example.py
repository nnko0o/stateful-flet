import flet as ft
from stateful_flet import StatefulUC
from stateful_flet import Context

print('Started..!')
class App(StatefulUC):
    def __init__(self, theme: Context):
        super().__init__()
        # init the Context in the `StatefulUC`
        self.theme = theme
        self.theme.subscribe(self)

    def build(self):
        self._content = ft.Container(
            content = ft.Column(
                controls=[
                    ft.Text(
                        value='StatfulUC ..1',
                        # Color will change when value of theme Context changes
                        color = ft.colors.WHITE24 if self.theme.get() else ft.colors.BLUE_GREY_800,
                    ),
                    ft.IconButton(
                        # icon will change with the theme context change
                        # when the user click the icon he will change the theme
                        icon=ft.icons.MODE_NIGHT_OUTLINED if self.theme.get() else ft.icons.LIGHT_MODE,
                        on_click=lambda e: self.theme.set(lambda v: not v),
                        icon_color=ft.colors.LIGHT_BLUE_700,
                    ),
                    ft.Text(
                        # Color will change when value of theme Context changes
                        # Text will be 'Dark' when the theme is dark(True) if the theme is light(False) write 'Light'
                        value=('Theme is ')+ ('Dark' if self.theme.get() else 'Light'),
                        color = ft.colors.WHITE24 if self.theme.get() else ft.colors.BLUE_GREY_800,

                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            # Will change with the Context
            bgcolor=ft.colors.BLACK87 if self.theme.get() else ft.colors.GREY_500,

            # Some desin
            height=self.height,
            width=self.width,
            alignment=ft.alignment.center,
            padding=18,
            margin=35,
            border_radius=14
        )

        return self._content

class other_us(StatefulUC):
    def __init__(self, theme: Context):
        super().__init__()
        # init the Context in the `StatefulUC`
        self.theme = theme
        self.theme.subscribe(self)

    def build(self):
        self._content = ft.Container(
            content = ft.Column(
                controls=[
                    ft.Text(
                        value='StatfulUC 2',
                        # Color will change when value of theme Context changes
                        color = ft.colors.WHITE24 if self.theme.get() else ft.colors.BLUE_GREY_800,
                    ),
                    ft.IconButton(
                        # icon will change with the theme context change
                        # when the user click the icon he will change the theme
                        icon=ft.icons.MODE_NIGHT_OUTLINED if self.theme.get() else ft.icons.LIGHT_MODE,
                        on_click=lambda e: self.theme.set(lambda v: not v),
                        icon_color=ft.colors.LIGHT_BLUE_700,
                    ),
                    ft.Text(
                        # Color will change when value of theme Context changes
                        # Text will be 'Dark' when the theme is dark(True) if the theme is light(False) write 'Light'
                        value=('Theme is ')+ ('Dark' if self.theme.get() else 'Light'),
                        color = ft.colors.WHITE24 if self.theme.get() else ft.colors.BLUE_GREY_800,

                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            # Will change with the Context
            bgcolor=ft.colors.BLACK87 if self.theme.get() else ft.colors.GREY_500,

            # Some desin
            height=self.height,
            width=self.width,
            alignment=ft.alignment.center,
            padding=18,
            margin=35,
            border_radius=14
        )

        return self._content

def main(page: ft.Page):
    page.vertical_alignment   = 'center'
    page.horizontal_alignment = 'center'
    
    # make the `Context` and set True as a value (Dark = True)
    # if you want add type chacking dont add it like that: `Context(True, True)` but like the code to makr the code more readful
    theme = Context(True, type_chack=True)
    
    page.add(
        App(theme),
        other_us(theme),
        other_us(theme),
    )

if __name__=='__main__':
        ft.app(
            target=main,
            port=8007,
            view=ft.AppView.WEB_BROWSER
        )