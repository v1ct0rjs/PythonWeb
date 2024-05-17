import reflex as rx
from PythonWeb.components.link_button import link_button
from PythonWeb.components.title import title

def links() -> rx.Component:
    return rx.vstack(
        title("Redes Sociales"),
        link_button("GitHub", "Repositorios","https://github.com/v1ct0rjs"),
        link_button("LinkedIn",
                    "Perfil De LinkedIn",
                    "https://www.linkedin.com/in/v1ct0rjs/"),
        link_button("Twitter",
                    "Perfil de X",
                    "https://twitter.com/v1ct0rjs"),
        link_button("Instagram",
                    "Perfil De Instagram",
                    "https://www.instagram.com/v1ct0rjs/"),
        title("Redes Sociales"),
        link_button("GitHub", "Repositorios", "https://github.com/v1ct0rjs"),
        link_button("LinkedIn",
                    "Perfil De LinkedIn",
                    "https://www.linkedin.com/in/v1ct0rjs/"),
        link_button("Twitter",
                    "Perfil de X",
                    "https://twitter.com/v1ct0rjs"),
        link_button("Instagram",
                    "Perfil De Instagram",
                    "https://www.instagram.com/v1ct0rjs/"),
        align = "center", width = "100%"
    )
