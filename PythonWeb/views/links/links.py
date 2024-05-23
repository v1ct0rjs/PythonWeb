import reflex as rx
from PythonWeb.components.link_button import link_button
from PythonWeb.components.title import title

# def links(titulo: str) -> rx.Component:
#     return rx.vstack(
#         title(titulo),
#         link_button("GitHub", "Repositorios","https://github.com/v1ct0rjs"),
#         link_button("LinkedIn",
#                     "Perfil De LinkedIn",
#                     "https://www.linkedin.com/in/v1ct0rjs/"),
#         link_button("Twitter",
#                     "Perfil de X",
#                     "https://twitter.com/v1ct0rjs"),
#         link_button("Instagram",
#                     "Perfil De Instagram",
#                     "https://www.instagram.com/v1ct0rjs/"),
#         align = "start", width = "100%",
#     )


def links(titulo: str, enlaces: list) -> rx.Component:
    componentes = [title(titulo)]
    for enlace in enlaces:
        componentes.append(link_button(enlace['title'], enlace['subtitle'], enlace['url'], enlace['icon'], enlace.get('icon_path')))
    return rx.vstack(*componentes, align="start", width="100%")



