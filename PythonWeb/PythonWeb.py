import reflex as rx
from PythonWeb.styles.styles import *
from PythonWeb.constants import *
from PythonWeb.pages.index import index
from PythonWeb.pages.english import eng
from PythonWeb.api.api import repo, live

app = rx.App(
    style=BASE_STYLE,
    stylesheets=GFONTS,
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

app.api.add_api_route("/repo", repo)
app.api.add_api_route("/live/{user}", live)