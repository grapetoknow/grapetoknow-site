#!/usr/bin/env python3
"""Copia o jogo (fonte única: /mnt/project-files/jogo/grape-to-know.html) para dentro do site.
Enquanto o jogo não abre ao público, fica num endereço de pré-visualização, fora dos menus e com noindex.
Uso: python3 ferramentas/atualizar-jogo.py [fonte]"""
import os, sys
FONTE = sys.argv[1] if len(sys.argv) > 1 else "/mnt/project-files/jogo/grape-to-know.html"
PASTA = "jogo-previa-7481774e"  # trocar por "jogo" no dia em que o jogo abrir
AQUI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
jogo = open(FONTE, encoding="utf-8").read()
CABECA = """<!doctype html><html lang="pt-PT"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="robots" content="noindex,nofollow">
<style>:root{box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>
</head><body>
"""
os.makedirs(os.path.join(AQUI, PASTA), exist_ok=True)
open(os.path.join(AQUI, PASTA, "index.html"), "w", encoding="utf-8").write(CABECA + jogo + "\n</body></html>\n")
print("jogo copiado para /" + PASTA + "/")
