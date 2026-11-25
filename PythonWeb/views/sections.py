import reflex as rx
from PythonWeb.components.title import title
from PythonWeb.components.cards import project_card, info_card
from PythonWeb.styles.styles import section_style, subheading_style, MONO
from PythonWeb.constants import PROJECTS, CATEGORIES, CERTS, SOCIALS

_GRID_2 = rx.breakpoints(initial="1", sm="2")
_GRID_3 = rx.breakpoints(initial="1", sm="2", lg="3")
_GRID_4 = rx.breakpoints(initial="1", xs="2", md="4")


def _grid(items: list, columns) -> rx.Component:
    return rx.grid(*items, columns=columns, gap="1em", width="100%")


def projects_section(t: dict, lang: str) -> rx.Component:
    featured = [p for p in PROJECTS if p.get("featured")]
    others = [p for p in PROJECTS if not p.get("featured")]
    categories = [c for c in CATEGORIES if any(p["category"] == c for p in others)]

    tab_style = {"font_family": MONO, "font_size": "0.85em"}
    return rx.vstack(
        title(t["projects"]),
        rx.text(t["featured"], style=subheading_style),
        _grid([project_card(p, lang) for p in featured], _GRID_2),
        rx.text(t["more"], style=subheading_style, padding_top="1.5em"),
        rx.tabs.root(
            rx.tabs.list(
                rx.tabs.trigger(t["all"], value="all", style=tab_style),
                *[rx.tabs.trigger(t["cat"][c], value=c, style=tab_style) for c in categories],
                style={"flex_wrap": "wrap"},
            ),
            rx.tabs.content(
                _grid([project_card(p, lang) for p in others], _GRID_3),
                value="all", padding_top="1em",
            ),
            *[
                rx.tabs.content(
                    _grid([project_card(p, lang) for p in others if p["category"] == c], _GRID_3),
                    value=c, padding_top="1em",
                )
                for c in categories
            ],
            default_value="all",
            width="100%",
        ),
        id="proyectos",
        style=section_style,
    )


def certs_section(t: dict, lang: str) -> rx.Component:
    return rx.vstack(
        title(t["certs"]),
        _grid([info_card(c, lang) for c in CERTS], _GRID_2),
        id="certificaciones",
        style=section_style,
    )


def socials_section(t: dict, lang: str) -> rx.Component:
    return rx.vstack(
        title(t["socials"]),
        _grid([info_card(s, lang) for s in SOCIALS], _GRID_4),
        id="contacto",
        style=section_style,
    )
