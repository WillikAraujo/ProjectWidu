import flet as ft
from TopMenu import TopMenu
from MenuLateral import MenuLateral
from LadingPage import LadingPage


def main(page: ft.Page):
    page.padding = 0
    page.fonts = {
        'Poppins-Regular': 'fonts/Poppins-Regular.ttf',
        'Poppins-Bold': 'fonts/Poppins-Bold.ttf',
        'Poppins-Light': 'fonts/Poppins-Light.ttf'
    }
    page.window_center()
    page.add(
        ft.Column(
            [
                ft.ResponsiveRow(
                    [
                        TopMenu(
                            name_user="Willik, Pimenta",
                            img_profile_user="imgs/img_profile.jpeg",
                        )
                    ]
                ),
                
                ft.Row(
                    vertical_alignment='start',
                    controls=
                    [
                        MenuLateral(),
                        ft.VerticalDivider(width=30,color="transparent"),
                        LadingPage(1),
                    ]
                )
            ]
        )
    )


ft.app(main)
