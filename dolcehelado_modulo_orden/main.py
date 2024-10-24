import flet as ft

# Variable global para llevar el total acumulado
total_price = 0

# Función para actualizar el total en el botón "REVISAR ORDEN"
def update_total(button, amount):
    global total_price
    total_price += amount
    button.content.controls[0].value = f"TOTAL ${total_price}"
    button.update()

# Función que muestra la ventana emergente para seleccionar la cantidad
def show_quantity_dialog(page, total_button):
    # Ref para almacenar la cantidad seleccionada
    quantity = ft.Ref[ft.Text]()

    # Función para actualizar la cantidad en la pantalla
    def update_quantity(delta):
        current_value = int(quantity.current.value.split(": ")[1])  # Obtener la cantidad actual
        new_value = max(0, current_value + delta)  # No permitir cantidades negativas
        quantity.current.value = f"Cantidad: {new_value}"
        quantity.current.update()

    # Crear la ventana emergente (Dialog)
    dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Selecciona la cantidad"),
        content=ft.Column(
            [
                ft.Text("Cantidad: 0", ref=quantity, size=20),  # Texto inicial con Ref
                ft.Row(
                    [
                        ft.ElevatedButton(
                            text="-",
                            on_click=lambda e: update_quantity(-1),
                        ),
                        ft.ElevatedButton(
                            text="+",
                            on_click=lambda e: update_quantity(1),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
            tight=True,
        ),
        actions=[
            ft.TextButton(
                "Cancelar",
                on_click=lambda e: close_dialog(page),  # Cerrar el diálogo
            ),
            ft.TextButton(
                "Confirmar",
                on_click=lambda e: confirm_quantity(page, total_button, quantity),
            ),
        ],
    )

    # Mostrar la ventana emergente
    page.dialog = dialog
    dialog.open = True
    page.update()

# Función para cerrar el diálogo
def close_dialog(page):
    page.dialog.open = False
    page.update()

# Función que se llama al confirmar la cantidad
def confirm_quantity(page, total_button, quantity_ref):
    quantity = int(quantity_ref.current.value.split(": ")[1])  # Obtener la cantidad
    if quantity > 0:
        update_total(total_button, quantity * 50)  # Cada producto cuesta $50
    close_dialog(page)  # Cerrar el diálogo

# Definición del botón de comida (MealButton) con evento on_tap
def meal_button(page, total_button):
    return ft.Container(
        content=ft.GestureDetector(
            on_tap=lambda e: show_quantity_dialog(page, total_button),  # Mostrar ventana emergente
            content=ft.Container(
                padding=10,
                border=ft.border.all(3, "#DFAB9F"),
                border_radius=50,
                content=ft.Column(
                    [
                        ft.CircleAvatar(
                            radius=50,
                            bgcolor="#C4634B",
                        ),
                        ft.Text("$50", size=14, color="black"),  # Precio
                        ft.Text("Frape Moka", size=14, color="black"),  # Nombre del producto
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            ),
        ),
    )

# Pantalla principal
def order_screen(page: ft.Page):
    page.bgcolor = "#FFFFFF"  # Fondo de la página

    # Botón para revisar orden (se actualizará su contenido)
    total_button = ft.ElevatedButton(
        width=200,
        height=50,
        on_click=lambda e: print("Revisar Orden"),
        style=ft.ButtonStyle(
            bgcolor="#DDA965",
            color="white",
        ),
        content=ft.Column(
            [
                ft.Text("TOTAL $0", color="white", size=15),  # Texto inicial
                ft.Text("REVISAR ORDEN", color="white", size=15),
            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )

    page.add(
        ft.Container(
            padding=15,
            content=ft.Column(
                [
                                        ft.Container(height=20),  # Espacio vertical
                    # Fila superior (Regresar y Avatar)
                    ft.Row(
                        [
                            ft.GestureDetector(
                                on_tap=lambda e: print("Regresar"),
                                content=ft.Row(
                                    [
                                        ft.Icon(ft.icons.ARROW_BACK_IOS, size=25, color="black"),
                                        ft.Text("REGRESAR", size=14, color="black"),
                                    ]
                                ),
                            ),
                            ft.CircleAvatar(
                                radius=25,
                                background_image_url="https://scontent.fcjs3-2.fna.fbcdn.net/v/t39.30808-6/339337613_1482630939209668_1392032162257633573_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=6ee11a&_nc_ohc=uUw-kHajVEcQ7kNvgGL9por&_nc_ht=scontent.fcjs3-2.fna&_nc_gid=A3u4OynPOH-N0J7MPfSunu2&oh=00_AYBhcxz6ke6nuH7vWffnetMb1QJw5xOxHPkAV87aPZBh-Q&oe=671B9D6B"
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    ft.Container(height=60),  # Espacio vertical
                    

                    # Fila de botones (Bebidas, Comida, Postres)
                    ft.Row(
                        [

                            ft.ElevatedButton(                                
                                width=100,
                                height=30,
                                on_click=lambda e: print("Bebidas"),
                                style=ft.ButtonStyle(
                                    bgcolor="#C4634B",
                                    padding=ft.Padding(8, 0, 8, 0),  # Relleno alrededor del contenido
                                ),
                                content=ft.Row(
                                    [
                                        ft.Icon(ft.icons.LOCAL_DRINK, color="white", size=14),  # Ícono
                                        ft.Text("BEBIDAS", color="white", size=14),  # Texto sin saltos
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,  # Alineación horizontal
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,  # Alineación vertical
                                ),
                            ),
                            ft.ElevatedButton(
                                width=100,
                                height=30,
                                on_click=lambda e: print("Comida"),
                                style=ft.ButtonStyle(
                                    bgcolor="#C4634B",  # Color de fondo del botón
                                    padding=ft.Padding(8, 0, 8, 0),  # Relleno alrededor del contenido
                                ),
                                content=ft.Row(
                                    [
                                        ft.Icon(ft.icons.LUNCH_DINING, color="white", size=14),  # Ícono
                                        ft.Text("COMIDA", color="white", size=14),  # Texto sin saltos
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,  # Alineación horizontal
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,  # Alineación vertical
                                ),
                            ),
                            ft.ElevatedButton(                                
                                width=100,
                                height=30,
                                on_click=lambda e: print("Postres"),
                                style=ft.ButtonStyle(
                                    bgcolor="#C4634B",
                                    padding=ft.Padding(8, 0, 8, 0),  # Relleno alrededor del contenido
                                ),
                                content=ft.Row(
                                    [
                                        ft.Icon(ft.icons.ICECREAM, color="white", size=14),  # Ícono
                                        ft.Text("POSTRES", color="white", size=14),  # Texto sin saltos
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,  # Alineación horizontal
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,  # Alineación vertical
                                ),
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    ft.Container(height=40),  # Espacio vertical
                    # Fila de botones MealButton con eventos
                    ft.Row(
                        [meal_button(page, total_button), meal_button(page, total_button)],
                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                    ),
                    ft.Container(height=40),  # Espacio vertical
                    ft.Row(
                        [meal_button(page, total_button), meal_button(page, total_button)],
                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                    ),
                    ft.Container(height=40),  # Espacio vertical

                    # Botón para revisar orden
                    total_button,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        ),
    )

# Ejecutar la aplicación
if __name__ == "__main__":
    ft.app(target=order_screen)
