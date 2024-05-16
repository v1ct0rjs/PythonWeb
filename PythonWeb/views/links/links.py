import reflex as rx
from PythonWeb.components.link_button import link_button


def links() -> rx.Component:
    return rx.vstack(
        link_button("GitHub", "https://github.com/v1ct0rjs"),
        link_button("LinkedIn", "https://www.linkedin.com/in/v1ct0rjs/"),
        link_button("Twitter", "https://twitter.com/v1ct0rjs"),
        link_button("Instagram", "https://www.instagram.com/v1ct0rjs/"),
        align="center"
    )
