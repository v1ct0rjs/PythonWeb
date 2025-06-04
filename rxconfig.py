# rxconfig.py  (root of project)
import os, reflex as rx

BACKEND = "http://localhost:8000"            # ↔ running `reflex run --backend-only`
# BACKEND = "https://api.v1ct0r.dev"        # ← use this in prod

config = rx.Config(
    app_name="PythonWeb",
    api_url=BACKEND,                         # <── ❶ MUST NOT be empty
    cors_allowed_origins=[
        "https://www.v1ct0r.dev",
        "https://victorjs-web.vercel.app",
        "http://localhost:3000",
    ],
    frontend_port=3000,
    frontend_packages=[                      # <── ❷ lock rc-util forever
        "rc-util@5.40.1",
    ],
)

# ❸ silence Tailwind deprecation
config.plugins = [rx.plugins.TailwindV3Plugin()]
#  # or, if you don’t use it:
# config.tailwind = None




