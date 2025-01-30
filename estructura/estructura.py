import reflex as rx
from estructura.contacto import contac_form
from estructura.add_users import add_customer_button, show_user, State


        
    

def index() -> rx.Component:
    return rx.vstack(
            add_customer_button(),
            rx.table.root(
                rx.table.header(
                    rx.table.row(
                        rx.table.column_header_cell("Nombre"),
                        rx.table.column_header_cell("Email"),
                        rx.table.column_header_cell("Sexo"),
                    ),
                ),
                rx.table.body(
                    rx.foreach(State.users, show_user),
                ),
                variant="surface",
                size="3",
            ),
            
            contac_form(),
            padding_top="2rem",
            padding="2rem",
    )

app = rx.App()
app.add_page(index)
