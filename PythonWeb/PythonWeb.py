import reflex as rx
from PythonWeb.styles.styles import *
from PythonWeb.constants import *


import PythonWeb.pages.index
import PythonWeb.pages.english

from PythonWeb.api.api import repo, live 

app = rx.App(
    style=BASE_STYLE,
    stylesheets=STYLES_AND_FONTS,
    head_components=[
        rx.script(src=f"https://www.googletagmanager.com/gtag/js?id={GTAG}"),
        rx.script(
            """
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());
            gtag('config', 'G-QFHWGRCS3T');
            """),
    ],
)



