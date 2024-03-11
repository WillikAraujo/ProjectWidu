import flet as ft


class TopMenu(ft.Container):

    def __init__(self, name_user: str, img_profile_user: str):
        super().__init__(
            expand=True,
            shadow=ft.BoxShadow(
                blur_radius=3,
                color="#A2A2A2",
                spread_radius=0.1,
                blur_style=ft.ShadowBlurStyle.OUTER,
            ),
            padding=ft.padding.only(45, 15, 45, 15),
        )
        self.content = ft.Container(
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.Container(
                        content=ft.Image(
                            src="imgs/logo.png",
                            width=87,
                            height=48,
                        )
                    ),
                    ft.Row(
                        spacing=39,
                        controls=[
                            ft.Text(
                                value=name_user,
                                font_family="Poppins-Regular",
                                size=16,
                            ),
                            ft.Container(
                                border=ft.border.all(2, "#000000"),
                                border_radius=50,
                                width=50,
                                height=50,
                                content=ft.Image(
                                    src=img_profile_user,
                                    fit=ft.ImageFit.FIT_WIDTH,
                                    error_content=ft.Container(
                                        border_radius=50,
                                        width=50,
                                        height=50,
                                        bgcolor="#861D7B",
                                        content=ft.Row(
                                            controls=[
                                                ft.Text(
                                                    value="WP",
                                                    size=20,
                                                    font_family="Poppins-Bold",
                                                    color="white",
                                                )
                                            ],
                                            alignment=ft.MainAxisAlignment.CENTER,
                                        ),
                                    ),
                                ),
                            ),
                        ],
                    ),
                ],
            )
        )
