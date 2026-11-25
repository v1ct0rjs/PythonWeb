# Constantes de la aplicación: proyectos, enlaces, certificaciones y textos (ES/EN).

APP_VERSION = "V3.0"

# ---------------------------------------------------------------------------
# Proyectos
# Cada proyecto tiene la descripción en ambos idiomas, una categoría (para las
# pestañas), etiquetas de tecnología y un indicador de proyecto destacado.
# ---------------------------------------------------------------------------

CATEGORIES = ["ia", "devops", "iot", "web", "scripts"]

PROJECTS = [
    {"title": "Yolo Alarm", "url": "https://github.com/v1ct0rjs/yoloAlarm", "icon": "camera",
     "category": "ia", "featured": True, "tags": ["Python", "YOLO", "Visión artificial"],
     "desc": {"es": "Sistema de detección de movimiento e identificación de objetos.",
              "en": "Motion detection and object identification system."}},

    {"title": "OCR Document Search System", "url": "https://github.com/v1ct0rjs/ocr-search-system",
     "icon": "file-search", "category": "ia", "featured": True, "tags": ["Python", "OCR"],
     "desc": {"es": "Sistema de indexación y búsqueda de documentos con OCR.",
              "en": "Document indexing and search system using OCR."}},

    {"title": "LoRaIM", "url": "https://github.com/v1ct0rjs/LoRaIM", "icon": "radio",
     "icon_path": "/loraim.svg", "category": "iot", "featured": True, "tags": ["LoRa", "IoT"],
     "desc": {"es": "Plataforma de mensajería instantánea que utiliza LoRa.",
              "en": "Instant messaging platform using LoRa."}},

    {"title": "Grafana Octopus", "url": "https://github.com/v1ct0rjs/grafana_octopus", "icon": "chart-line",
     "icon_path": "/grafana.svg", "category": "devops", "featured": True,
     "tags": ["Grafana", "InfluxDB", "Telegraf"],
     "desc": {"es": "Stack de monitorización con Grafana, InfluxDB 2 y Telegraf.",
              "en": "Monitoring stack with Grafana, InfluxDB 2 and Telegraf."}},

    {"title": "Jenkins Deployment", "url": "https://github.com/v1ct0rjs/jenkins_deployment", "icon": "server",
     "icon_path": "/jenkins.svg", "category": "devops", "tags": ["Jenkins", "Docker", "CI/CD"],
     "desc": {"es": "Automatización CI/CD hacia Docker Hub utilizando Jenkins.",
              "en": "CI/CD automation towards Docker Hub using Jenkins."}},

    {"title": "Integración SonarQube",
     "url": "https://github.com/v1ct0rjs/jenkins_deployment/tree/main/SonarQube", "icon": "shield-check",
     "icon_path": "/sonarqube.svg", "category": "devops", "tags": ["SonarQube", "Ngrok"],
     "desc": {"es": "Instancia pública de SonarQube utilizando un túnel Ngrok.",
              "en": "Public SonarQube instance using an Ngrok tunnel."}},

    {"title": "Oracle Autonomous Database", "url": "https://github.com/v1ct0rjs/oci-autonomousdb",
     "icon": "database", "icon_path": "/database.svg", "category": "devops", "tags": ["OCI", "Cloud"],
     "desc": {"es": "Base de datos autónoma en Oracle Cloud Infrastructure.",
              "en": "Autonomous database in Oracle Cloud Infrastructure."}},

    {"title": "Pulsera detector de actividad", "url": "https://github.com/v1ct0rjs/m5_move-detector",
     "icon": "watch", "category": "iot", "tags": ["MicroPython", "M5Stack"],
     "desc": {"es": "Programa en MicroPython para competir en los TELECO GAMES.",
              "en": "MicroPython program to compete in the TELECO GAMES."}},

    {"title": "10Tacle WebApp", "url": "https://10tacle.org", "icon": "app-window",
     "category": "web", "tags": ["Web"],
     "desc": {"es": "Web de 10Tacle, DJ y productor de música electrónica.",
              "en": "Web app for 10Tacle, DJ and electronic music producer."}},

    {"title": "El Campito WebApp", "url": "https://elcampitoo.net/", "icon": "app-window",
     "category": "web", "tags": ["Web"],
     "desc": {"es": "Página web para el apartamento rural El Campito.",
              "en": "Website for El Campito rural apartment."}},

    {"title": "Python Web App", "url": "https://github.com/v1ct0rjs/PythonWeb", "icon": "app-window",
     "category": "web", "tags": ["Python", "Reflex"],
     "desc": {"es": "Código de esta web, programada con Reflex.",
              "en": "Source code of this web app, built with Reflex."}},

    {"title": "Auto Fastfetch", "url": "https://github.com/v1ct0rjs/auto_fastfetch", "icon": "terminal",
     "category": "scripts", "tags": ["Python", "Linux"],
     "desc": {"es": "Script en Python que descarga y ejecuta Fastfetch automáticamente.",
              "en": "Python script that automatically downloads and runs Fastfetch."}},

    {"title": "Pyter", "url": "https://github.com/v1ct0rjs/pyther", "icon": "message-square-text",
     "category": "scripts", "tags": ["Python", "gRPC"],
     "desc": {"es": "Mensajería cliente-servidor que utiliza gRPC.",
              "en": "Client-server messaging program using gRPC."}},

    {"title": "PyAgenda", "url": "https://github.com/v1ct0rjs/PyAgenda", "icon": "calendar-plus",
     "category": "scripts", "tags": ["Python", "CLI"],
     "desc": {"es": "Gestor de tareas por línea de comandos.",
              "en": "Command-line task manager."}},

    {"title": "Pyng", "url": "https://github.com/v1ct0rjs/Pyng", "icon": "network",
     "category": "scripts", "tags": ["Python", "Redes"],
     "desc": {"es": "Script detector de equipos en la LAN.",
              "en": "Script for detecting devices on the LAN."}},

    {"title": "Shell Script Usuarios-Grupos", "url": "https://github.com/v1ct0rjs/iso_shell_scripts",
     "icon": "file-terminal", "category": "scripts", "tags": ["Bash", "Linux"],
     "desc": {"es": "Script Bash para gestionar usuarios y grupos.",
              "en": "Bash script for managing users and groups."}},

    {"title": "Conversor DBOH", "url": "https://github.com/v1ct0rjs/DBOH", "icon": "calculator",
     "category": "scripts", "tags": ["Utilidad"],
     "desc": {"es": "Conversor decimal, binario, hexadecimal y octal.",
              "en": "Decimal, binary, hexadecimal and octal converter."}},

    {"title": "Ruleta de la fortuna", "url": "https://github.com/v1ct0rjs/RuletaDeLaFortuna/", "icon": "dices",
     "category": "scripts", "tags": ["Juego"],
     "desc": {"es": "Juego de la ruleta de la fortuna.", "en": "Wheel of Fortune game."}},

    {"title": "Ahorcado", "url": "https://github.com/v1ct0rjs/ahorcado/", "icon": "signpost-big",
     "category": "scripts", "tags": ["Juego"],
     "desc": {"es": "Juego de adivinar palabras.", "en": "Word guessing game (hangman)."}},
]

# ---------------------------------------------------------------------------
# Redes sociales y certificaciones
# ---------------------------------------------------------------------------

SOCIALS = [
    {"title": "GitHub", "url": "https://github.com/v1ct0rjs", "icon_path": "/github.svg",
     "desc": {"es": "Repositorios", "en": "Repositories"}},
    {"title": "LinkedIn", "url": "https://www.linkedin.com/in/v1ct0rdev/", "icon_path": "/linkedin.svg",
     "desc": {"es": "Perfil profesional", "en": "Professional profile"}},
    {"title": "X", "url": "https://x.com/vmjimsan", "icon_path": "/x-twitter.svg",
     "desc": {"es": "@vmjimsan", "en": "@vmjimsan"}},
    {"title": "Mastodon", "url": "https://mastodon.social/@v1ct0rjs", "icon_path": "/mastodon.svg",
     "desc": {"es": "@v1ct0rjs", "en": "@v1ct0rjs"}},
]

CERTS = [
    {"title": "AWS Academy Graduate", "icon_path": "/aws_cloud.png",
     "desc": {"es": "Cloud Foundations", "en": "Cloud Foundations"}},
    {"title": "Cisco Cybersecurity", "icon_path": "/cybersecurity-essentials.png",
     "desc": {"es": "Cybersecurity Essentials", "en": "Cybersecurity Essentials"}},
]

# ---------------------------------------------------------------------------
# URLs
# ---------------------------------------------------------------------------

URL_GITHUB = "https://github.com/v1ct0rjs"
URL_LINKEDIN = "https://www.linkedin.com/in/v1ct0rdev/"
URL_EMAIL = "mailto:vmjimenezs02@educarex.es"
URL_TELEGRAM = "https://t.me/p3sc4"
URL_TWITCH = "https://www.twitch.tv/dj_10tacle"

# ---------------------------------------------------------------------------
# Textos de la página
# ---------------------------------------------------------------------------

TEXT_TAB_TITLE = "V1cT0r's Portfolio"

TEXTO_HEADER = ("Desarrollador de Inteligencia Artificial y Big Data, con perfil de SysAdmin y experiencia "
                "en Python, Deep Learning, MLOps, Linux y arquitecturas Cloud.")
TEXT_ENG_HEADER = ("Artificial Intelligence and Big Data Developer with a SysAdmin background and experience "
                   "in Python, Deep Learning, MLOps, Linux and Cloud architectures.")

TEXTS = {
    "es": {
        "nav_brand": "['D3v_1A', 'B1g_D4t4', 'SysAdm1n', 'l1nuX3r0', 'PyTh0n1sta']",
        "nav_projects": "Proyectos",
        "nav_certs": "Certificaciones",
        "nav_contact": "Contacto",
        "lang_label": "EN",
        "lang_title": "English version",
        "lang_href": "https://www.v1ct0r.dev/eng/",
        "role": "Desarrollador IA & Big Data, SysAdmin y Linuxero",
        "bio": TEXTO_HEADER,
        "location": "Zafra, Badajoz · España",
        "cta_projects": "Ver proyectos",
        "cta_contact": "Contactar",
        "projects": "proyectos",
        "featured": "Destacados",
        "more": "Más proyectos",
        "all": "Todos",
        "cat": {"ia": "IA & Datos", "devops": "DevOps & Cloud", "iot": "IoT & Electrónica",
                "web": "Web", "scripts": "Scripts & Otros"},
        "certs": "certificaciones",
        "socials": "contacto",
        "live": "en directo",
    },
    "en": {
        "nav_brand": "['AI_D3v', 'B1g_D4t4', 'SysAdm1n', 'l1nuX3r', 'PyTh0n1st']",
        "nav_projects": "Projects",
        "nav_certs": "Certifications",
        "nav_contact": "Contact",
        "lang_label": "ES",
        "lang_title": "Versión en español",
        "lang_href": "https://www.v1ct0r.dev/",
        "role": "AI & Big Data Developer, SysAdmin and Linuxer",
        "bio": TEXT_ENG_HEADER,
        "location": "Zafra, Badajoz · Spain",
        "cta_projects": "See projects",
        "cta_contact": "Get in touch",
        "projects": "projects",
        "featured": "Featured",
        "more": "More projects",
        "all": "All",
        "cat": {"ia": "AI & Data", "devops": "DevOps & Cloud", "iot": "IoT & Electronics",
                "web": "Web", "scripts": "Scripts & Misc"},
        "certs": "certifications",
        "socials": "contact",
        "live": "live",
    },
}

# ---------------------------------------------------------------------------
# Fuentes y analítica
# ---------------------------------------------------------------------------

STYLES_AND_FONTS = [
    "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;600;700&display=swap",
    "/css/styles.css",
]

GTAG = "G-QFHWGRCS3T"
