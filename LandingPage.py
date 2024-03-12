import flet as ft
from viagens_list import viagens


class LandingPage(ft.Column):
    def __init__(self):
        self.lista_vianges = []
        for propriedade in viagens:
            self.lista_vianges.append(CardsViagem(propriedade["cidade"],propriedade["caminho_img"],propriedade["periodo_viagem"]))
            print(propriedade["cidade"])
        print(self.lista_vianges)
        
        self.pagina_inicial = ft.Column(
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.END,
                    controls=[
                        ft.Container(
                            alignment=ft.alignment.center_right,
                            expand=True,
                            padding=ft.padding.only(0, 10, 18, 10),
                            margin=ft.margin.only(0, 0, 37, 0),
                            content=ft.Image(
                                src="imgs/edit_deactive.png", width=19, height=18
                            ),
                        )
                    ],
                ),
                ft.Container(
                    animate=ft.animation.Animation(200, "EASE-IN"),
                    padding=ft.padding.only(left=24, right=150),
                    content=ft.Column(
                        controls=[
                            ft.Text(
                                value="Página inicial",
                                font_family="Poppins-Bold",
                                size=32,
                            ),
                            ft.Divider(height=30, color="transparent"),
                            ft.Text(
                                value="Sobre mim",
                                font_family="Poppins-Regular",
                                size=24,
                            ),
                            ft.Divider(height=10, color="transparent"),
                            ft.Text(
                                value="Aqui terá um texto sobre você, na qual poderá editar clicando no lado superior direito.",
                                font_family="Poppins-Regular",
                                size=14,
                            ),
                        ]
                    ),
                ),
                ft.Divider(height=30,color='transparent'),
                ft.Row(controls=self.lista_vianges),
            ]
        )

        self.viagens = ft.Column(
            [
                ft.Row(
                    alignment=ft.MainAxisAlignment.END,
                    controls=[
                        ft.Container(
                            alignment=ft.alignment.center_right,
                            expand=True,
                            padding=ft.padding.only(0, 10, 18, 10),
                            margin=ft.margin.only(0, 0, 37, 0),
                            content=ft.Image(
                                src="imgs/edit_deactive.png", width=19, height=18
                            ),
                        )
                    ],
                ),
                ft.Container(
                    animate=ft.animation.Animation(200, "EASE-IN"),
                    padding=ft.padding.only(left=24, right=150),
                    content=ft.Column(
                        controls=[
                            ft.Text(
                                value="Viagens",
                                font_family="Poppins-Bold",
                                size=32,
                            ),
                            ft.Divider(height=30, color="transparent"),
                            ft.Text(
                                value="Sobre as viagens",
                                font_family="Poppins-Regular",
                                size=24,
                            ),
                            ft.Divider(height=10, color="transparent"),
                            ft.Text(
                                value="Página ambientada para armazenamento das viagens.",
                                font_family="Poppins-Regular",
                                size=14,
                            ),
                        ]
                    ),
                ),
            ]
        )
        super().__init__(
            expand=True,
            controls=[self.pagina_inicial],
            animate_opacity=ft.animation.Animation(200, "EASE-IN"),
        )

    def update_content(self, content):
        self.controls = [content]
        self.update()


class CardsViagem(ft.Container):
    def __init__(self,cidade_nome:str,cidade_img:str,periodo_viagem:str):
        super().__init__(
            height=240,
            width=200,
            border_radius=ft.border_radius.all(15),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=5,
                color=ft.colors.BLACK12,
                offset=ft.Offset(0, 10),
                blur_style=ft.ShadowBlurStyle.OUTER,
            ),
        )
        self.content = ft.Column(
            spacing=0,
            controls=[
                ft.Container(
                    height=148,
                    content=ft.Image(
                        src=cidade_img,
                        fit="cover",
                    ),
                ),
                ft.Container(
                    height=92,
                    margin=ft.margin.only(11, 8, 0, 0),
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        expand=True,
                        controls=[
                            ft.Text(
                                value=cidade_nome,
                                font_family="Poppins-Regular",
                                size=20,
                            ),
                            ft.Container(
                                padding=ft.padding.all(11),
                                alignment=ft.alignment.center_right,
                                content=
                                    ft.Text(
                                        value=periodo_viagem,
                                        font_family="Poppins-Regular",
                                        color="#929292",
                                        size=13,
                                    )
                            ),
                        ],
                    ),
                ),
            ],
        )
