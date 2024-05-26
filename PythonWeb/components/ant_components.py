import reflex as rx
from reflex.components import Component
from PythonWeb.routes import Route

class FloatButton(Component):
    library = 'antd'
    tag = 'FloatButton'
    icon = rx.image(src="/languages.svg")
    href = Route.ENG.value

float_button = FloatButton.create
