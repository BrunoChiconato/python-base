#!/usr/bin/env python3
"""Hello World Multi Linguas.

Dependendo da língua configurada no ambiente o programa exibe a mensagem 
correspondente.

Como usar:

Tenha a variável LANG devidamente configurada ex:

    export LANG=pt_BR

Execução:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.1.5"
__author__ = "Bruno Chiconato"
__license__ = "Unlicense"

import logging
import os
import sys
from logging import handlers

log_level = os.getenv("LOG_LEVEL", "WARNING")
logger = logging.Logger("bruno", level=log_level)
# ch = logging.StreamHandler()
# ch.setLevel(log_level)
fh = handlers.RotatingFileHandler("meulog.log", maxBytes=10**6, backupCount=10)
fh.setLevel(log_level)
fmt = logging.Formatter(
    "%(asctime)s | %(name)s | %(levelname)s |"
    " line:%(lineno)d | file:%(filename)s:\n%(message)s"
)
# ch.setFormatter(fmt)
fh.setFormatter(fmt)
logger.addHandler(fh)

arguments = {"lang": None, "count": 1}

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "es_SP": "Hola, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "fr_FR": "Bonjour, Monde!",
}

for arg in sys.argv[1:]:
    try:
        key, value = arg.split("=")
    except ValueError:
        logger.error("You need to use '=' after '--lang'")
        sys.exit(1)

    key = key.lstrip("-").strip()
    value = value.strip()

    if key not in arguments:
        print(f"Invalid option: '{key}'")
        sys.exit()

    arguments[key] = value

current_language = arguments.get("lang", None)

if current_language is None or current_language not in msg:
    current_language = os.getenv("LANG", "en_US")[:5]

print(msg[current_language] * int(arguments.get("count", 1)))
