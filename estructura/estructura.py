import reflex as rx
from estructura.contacto import contac_form



def index() -> rx.Component:
    return rx.vstack(
        contac_form(),
        padding_top="2rem",
        padding="2rem",
    )

app = rx.App()
app.add_page(index)
