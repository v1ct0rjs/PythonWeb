import reflex as rx

def link_button(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag="activity"
                ),
                rx.vstack(
                    rx.text(text),
                    rx.text("Click me", color="white", font_size="12px"),
                ),
            )
        ),
        href=url,
        is_external=True,
        width="100%",
    )