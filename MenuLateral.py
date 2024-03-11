import flet as ft
from menu_list import lista


        #botão do menu lateral...
class BotaoMenu(ft.Container):
    def __init__(self, text, icon_deactive, icon_active):
        super().__init__(
            border=ft.border.all(0.5, "#838383"),
            border_radius=9,
            margin=ft.margin.only(left=44, right=25,bottom=8),
            bgcolor="white",
            padding=ft.padding.only(20, 8, 20, 8),
            animate=ft.animation.Animation(duration=200,curve="EASE_OUT"),
        )

        #atributos dos botões...
        self.text = text
        self.icon_deactive = icon_deactive
        self.icon_active =icon_active
        
        self.content = ft.Row(
            spacing=18,
            controls=[
                ft.Image(src=self.icon_deactive, width=18, height=17.8, fit=ft.ImageFit.FILL),
                ft.Text(
                    value=self.text,
                    font_family="Poppins-Regular",
                ),
            ],
        )       

        #menu lateral...
class MenuLateral(ft.Container):
    def __init__(self):
        super().__init__(
            width=250,
            height=936,
            border_radius=ft.BorderRadius(0, 133, 0, 0),
            border=ft.Border(right=ft.BorderSide(1, "#F5F5F5")),
        )

        #declarando lista de objeto dos botões
        self.lista_obj_menu = []
        
        #incrementando a lista de objeto dos botões
        for list in lista:
            self.lista_obj_menu.append(BotaoMenu(list['name'],list['icon_deactive'],list['icon_active']))        
        
        
        self.content = ft.Container(
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Container(
                                margin=ft.margin.only(left=45, top=82),
                                content=ft.Row(
                                    spacing=17,
                                    controls=
                                    [
                                        ft.Image(
                                            src="imgs/menu_icon.png",
                                            width=20,
                                            height=18.75,
                                        ),
                                        ft.Text(
                                            value="MENU",
                                            size=28,
                                            font_family="Poppins-Bold",
                                            color="#515151",
                                        ),
                                    ]
                                ),
                            ),
                        ],
                    ),
                    ft.Divider(height=65,color="transparent"),
                    ft.Column(
                        controls=self.lista_obj_menu
                    )
                ]
            )
        )
        
        ## configurando 
        for btn in self.lista_obj_menu:
            btn.on_hover = lambda e: self.on_hover_btn(e)
            btn.on_click= lambda e: self.on_click_btn(e)
    
    def redefinir_btns(self, e):
        for btn in self.lista_obj_menu:
            btn.active = False
            btn.content.controls[0].src = btn.icon_deactive
            btn.content.controls[0].color = "#000000"
            btn.content.controls[1].color = "#000000"
            btn.bgcolor = "white"
            btn.update()
    
    def on_click_btn(self, e):
        self.redefinir_btns(e)
        e.control.content.controls[0].src = e.control.icon_active
        e.control.content.controls[0].color = "white"
        e.control.content.controls[1].color = "white"
        e.control.bgcolor = "#252525"
        e.control.update()
    
    def on_hover_btn(self, e):                
        if e.control.bgcolor == "white":
            e.control.bgcolor = "#F9F9F9"
        elif e.control.bgcolor == "#F9F9F9":
            e.control.bgcolor = "white"
        e.control.update()