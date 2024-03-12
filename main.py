import flet as ft
from TopMenu import TopMenu
from MenuLateral import MenuLateral
from LandingPage import LandingPage


def main(page: ft.Page):
    page.padding = 0
    page.fonts = {
        "Poppins-Regular": "fonts/Poppins-Regular.ttf",
        "Poppins-Bold": "fonts/Poppins-Bold.ttf",
        "Poppins-Light": "fonts/Poppins-Light.ttf",
    }
    page.window_center()
    page.scroll = "always"

    
    landing_page = LandingPage()
    menu_lateral = MenuLateral(landing_page)
    page.add(
        ft.Column([
            ft.ResponsiveRow([TopMenu(name_user="Willik, Pimenta",img_profile_user="imgs/img_profile.jpeg")]),
            ft.Row(
                vertical_alignment="start",
                controls=[
                    menu_lateral,
                    ft.VerticalDivider(width=30, color="transparent"),
                    landing_page,
                ],
            ),
        ]))


ft.app(main)
