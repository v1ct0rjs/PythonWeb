import reflex as rx
from PythonWeb.styles.styles import *
from PythonWeb.constants import *

# Importar los módulos de las páginas para que Reflex las descubra
import PythonWeb.pages.index
import PythonWeb.pages.english

from PythonWeb.api.api import repo, live # Asumiendo que estas son rutas API

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

# No necesitas app.add_page(index) o app.add_page(eng) explícitamente
# si los decoradores @rx.page se usan sin argumentos de app,
# ya que se registran con la instancia de app predeterminada.
# Si has pasado app=app al decorador, entonces esta forma es correcta.
# Si no, Reflex las encontrará porque los módulos han sido importados.

# app.api.add_api_route("/repo", repo)
# app.api.add_api_route("/live/{user}", live)

