import reflex as rx
from PythonWeb.components.no_link_button import no_link_button
from PythonWeb.components.title import title

def info_button(titulo: str, enlaces: list) -> rx.Component:
    componentes = [title(titulo)]
    for enlace in enlaces:
        componentes.append(no_link_button(enlace['title'], enlace['subtitle']))
    return rx.vstack(*componentes, align="start", width="100%")