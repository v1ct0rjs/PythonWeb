import reflex as rx

def header () -> rx.Component:
    return rx.vstack(
        rx.avatar(name="Víctor Jiménez", fallback='VJ', color_scheme="cyan", variant="solid", high_contrast=True, size="6"),
        rx.text("@vmjimsan"),
        rx.text("Hola, soy Víctor Jiménez, un desarrollador web", font_size="20px", color="black"), align="center"
    )