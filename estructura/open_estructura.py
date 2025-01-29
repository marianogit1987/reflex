import reflex as rx

def index() -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Nombre"),
                rx.table.column_header_cell("Email"),
                rx.table.column_header_cell("Sexo"),
            ),
        ),
        
        rx.table.body(
            rx.table.row(
                rx.table.cell("Mariano Epherra"),
                rx.table.cell("mariano@example.com"),
                rx.table.cell("Masculino"),
            ),
            rx.table.row(
                rx.table.cell("Marisa Lagardo"),
                rx.table.cell("marisa@example.com"),
                rx.table.cell("Femenino"),
            ),
        ),
    )


app = rx.App()
app.add_page(index)