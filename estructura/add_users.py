import reflex as rx

class User(rx.Base):
    nombre: str
    email: str
    sexo: str
    

class State(rx.State):
    users: list [User] = [
        User(
           nombre="Mariano Epherra",
           email="mariano@example.com", 
           sexo="Masculino", 
        ),
        User(
           nombre="Marisa Lagardo",
           email="marisa@example.com", 
           sexo="Femenino", 
        ),
    ]
    
    def add_user(self, form_data: dict):
        self.users.append(User(**form_data))
        
    
def show_user(user:User):
    return rx.table.row(
        rx.table.cell(user.nombre),
        rx.table.cell(user.email),
        rx.table.cell(user.sexo),
    )
    
def add_customer_button() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.icon("plus", size=26),
                rx.text("Agregar Usuario", size="4"),
            ),
        ),
        rx.dialog.content(
            rx.dialog.title(
                "Agregar Nuevo Usuario",
            ),
            rx.dialog.description(
               "Rellenar el formulario con la informacion del usuario",
        ),
        rx.form(
            rx.flex(    
                rx.input(
                    placeholder="Nombre Usuario",
                    name="Nombre",
                    required=True,
                ),
                rx.input(
                    placeholder="example@example.com",
                    name="email",
                    required=True,
                ),
                rx.select(
                    ["Masculino", "Femenino"],
                    placeholder="Femenino",
                    name="Sexo",
                    required=True, 
                ),
                rx.flex(
                    rx.dialog.close(
                        rx.button(
                            "Cancelar",
                            variant="soft",
                            color_scheme="gray",
                        ),
                    ),
                    rx.dialog.close(
                        rx.button(
                            "Agregar", type="Agregar"
                        ),
                    ),
                    spacing="3",
                    justify="end",
                ),
                direction="column",
                spacing="4",            
            ),
            on_submit=State.add_user,
            reset_on_submit=False,
        ),
        max_width="450px",
    ),
)
    

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
)