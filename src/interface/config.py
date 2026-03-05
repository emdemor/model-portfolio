import os
from importlib import resources

import interface

TITLE = "CSV Explorer"

LOGO_FILEPATH = str(resources.files("interface.assets").joinpath("logo.png"))

STYLE_FILEPATH = str(resources.files("interface.assets").joinpath("style.css"))

PLT_STYLE = str(resources.files("interface.assets").joinpath("plots.mplstyle"))

INSTRUCTIONS_PATH = str(resources.files("interface.assets").joinpath("instructions.md"))

if os.environ.get("ENV", "local") == "local":
    LOGS_PATH = "logs"
else:
    LOGS_PATH = os.path.join(
        os.sep.join(os.path.abspath(interface.__file__).split(os.sep)[:-1]),
        "logs",
    )

if not os.path.exists(LOGS_PATH):
    os.makedirs(LOGS_PATH) 

ICON_ALERT = "🚨"
ICON_HIGH_TEMPERATURE = "🌡️"
ICON_ERROR = "❌"
ICON_SUCCESS = "✅"