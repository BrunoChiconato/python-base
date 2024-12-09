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
__version__ = "0.1.3"
__author__ = "Bruno Chiconato"
__license__ = "Unlicense"

import os
import sys

arguments = {
    "lang": None,
    "count": 1
}

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "es_SP": "Hola, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "fr_FR": "Bonjour, Monde!"
}

for arg in sys.argv[1:]:
    # TODO: Tratar ValueError

    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()

    if key not in arguments:
        print(f"Invalid option: '{key}'")
        sys.exit()

    arguments[key] = value

current_language = arguments.get("lang", None)

if current_language is None or current_language not in msg:
    current_language = os.getenv("LANG","en_US")[:5]

print(msg[current_language] * int(arguments.get("count", 1)))