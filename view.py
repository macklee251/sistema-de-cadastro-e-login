from controller import *
import flet as ft

def main(page: ft.Page):
    page.title = "Keyboard Pro"
    page.spacing = 30 
    page.theme_mode="light"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    
    def cadastrar(e):
        print(ControllerCadastro.cadastrar(nome.value, email.value, senha.value))
    
    def validate(e):
        if all([nome.value, email.value, senha.value]):
            button_submit.disabled=False
        else:
            button_submit.disabled=True
        page.update()

    nome = ft.TextField(label="nome", text_align=ft.TextAlign.LEFT, width=400)
    email = ft.TextField(label="email", text_align=ft.TextAlign.LEFT, width=400)
    senha = ft.TextField(label="senha", text_align=ft.TextAlign.LEFT, width=400, password=True)
    button_submit = ft.ElevatedButton(text='Sign up', width=200, disabled=True, on_click=cadastrar)
    
    nome.on_change=validate
    email.on_change=validate
    senha.on_change=validate
    
    layout = ft.Row(
        controls=[
            ft.Column(
                [
                    nome,
                    email,
                    senha,
                ]
            )
        ],
        alignment=ft.MainAxisAlignment.SPACE_AROUND
    )
    
    page.add(layout, button_submit)
    
ft.app(target=main)