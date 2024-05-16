import reflex as rx


class State(rx.State):
    pass


def index() -> rx.Component:
    return rx.hstack(rx.box(rx.heading("Víctor Jiménez", color="black"),
        rx.text("Soy un desarrollador de software, me gusta la programación y la tecnología en general.", color="black"),
        background_color="yellow",
        border_radius="8px",
        width="50%",
        margin="8px",
        padding="8px"), aling="center", margin="8px")


app = rx.App()
app.add_page(index)
app._compile()
