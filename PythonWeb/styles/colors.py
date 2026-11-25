from enum import Enum


class Colors(Enum):
    PRIMARY = '#1dd3b0'        # Verde agua (acento)
    SECONDARY = '#b2ff9e'      # Verde claro
    BACKGROUND = '#000000'     # Fondo de página
    SURFACE = '#0b1113'        # Fondo de tarjetas
    SURFACE_HOVER = '#0f191b'  # Tarjeta al pasar el ratón
    BORDER = '#1c2a2d'         # Bordes sutiles
    CONTENT = '#086375'        # Azul petróleo (solo decorativo, no para texto)
    BLACK = '#000000'
    WHITE = '#FFFFFF'


class TextColor(Enum):
    PRIMARY = '#1dd3b0'
    SECONDARY = '#b2ff9e'
    BODY = '#e6edf0'           # Texto principal
    MUTED = '#9aa8ab'          # Texto secundario (contraste > 7:1 sobre el fondo)
    BLACK = '#000000'
    WHITE = '#FFFFFF'


class Fonts(Enum):
    JETBRAINS_MONO = 'JetBrains Mono'   # Títulos y detalles "terminal"
    INTER = 'Inter'                     # Texto corrido
