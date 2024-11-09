import flet as ft

def pagina_estatisticas(page:ft.Page):
    dp_tipo_jogo=ft.Dropdown(
        label='Modo de Jogo',
        options=[
            ft.dropdown.Option("Lotofacil"),
            ft.dropdown.Option("Mega-Sena"),
            ft.dropdown.Option("Lotomania")],
        value='Lotofacil',
    )
    def buscar_arquivo(e: ft.FilePickerResultEvent):
        #função que identifica o arquivo selecionado
        if e.files:
            status_arquivo.value = e.files[0].name
            btn_atualizar.disabled=False
            global caminho
            caminho = e.files[0].path
            page.update()

    # Componente para exibir o nome do arquivo selecionado
    status_arquivo = ft.Text("Nenhum arquivo selecionado", col=2)

    # FilePicker para selecionar arquivos
    file_picker = ft.FilePicker(on_result=buscar_arquivo)

    # Botão para abrir o FilePicker
    btn_selecionar_arquivo = ft.ElevatedButton(
        "Selecionar arquivo",
        on_click=lambda _: file_picker.pick_files(allow_multiple=False),
        col=3,
    )
    resprow_btns=ft.ResponsiveRow(
        columns=6,
        spacing=5,
        controls=[
            ft.Column(
                col=2,
                controls=[
                    btn_selecionar_arquivo,
                    status_arquivo,
                ]
            ),
            ft.Column(
                col=2,
                controls=[
                    btn_atualizar :=ft.ElevatedButton('Atualizar_estátistica', disabled=True )
                ]
            )   
        ]
    )

    # Adicionando os componentes à página
    layout_estatistica=ft.Column(
        expand=True,
        controls=[
        dp_tipo_jogo,
        resprow_btns        
        ]
    )

    # Necessário adicionar o FilePicker na página
    page.overlay.append(file_picker)
    page.update()
    return layout_estatistica
  