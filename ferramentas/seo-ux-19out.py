# Melhorias de SEO e UX (19 out 2026). Uso: python3 seo-ux-19out.py ficheiro.html [...]
import sys, re
META = {
 "pt": ("Grape to Know · Prova o que sabes",
        "Perguntas rápidas e situações reais de sala, das castas às regiões de Portugal. Para quem trabalha com vinho, estuda ou simplesmente gosta. Prova o que sabes."),
 "en": ("Grape to Know · Taste what you know",
        "Quick questions and real service situations, from grape varieties to the regions of Portugal. For people who work with wine, study it or simply love it. Taste what you know."),
 "es": ("Grape to Know · Demuestra lo que sabes",
        "Preguntas rápidas y situaciones reales de sala, de las castas a las regiones de Portugal. Para quien trabaja con vino, lo estudia o simplemente lo disfruta. Demuestra lo que sabes."),
}
U = "https://grapetoknow.com/"
HEAD = f'''<title>{META["pt"][0]}</title>
<link rel="canonical" href="{U}">
<meta name="theme-color" content="#1D131B">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Grape to Know">
<meta property="og:url" content="{U}">
<meta property="og:title" content="{META["pt"][0]}">
<meta property="og:description" content="{META["pt"][1]}">
<meta property="og:image" content="{U}og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="pt_PT">
<meta property="og:locale:alternate" content="en_GB">
<meta property="og:locale:alternate" content="es_ES">
<meta name="twitter:card" content="summary_large_image">
<script type="application/ld+json">{{"@context":"https://schema.org","@graph":[{{"@type":"WebSite","name":"Grape to Know","url":"{U}","inLanguage":["pt-PT","en","es"]}},{{"@type":"Organization","name":"Grape to Know","url":"{U}","email":"grapehits@gmail.com","slogan":"Prova o que sabes.","founder":{{"@type":"Person","name":"Priscila Lopes"}}}}]}}</script>'''
CSS = '''  .ctas .btn{flex:1 1 100%}
  .niveis{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}
  .niveis > span{grid-column:1/-1}
  .nivel{padding:10px 12px}
  .lang button{min-height:40px;min-width:40px}
  .pe a{padding-block:7px;line-height:1.45}
  }'''
TROCAS = [
 (re.compile(r'<meta name="description" content="[^"]*">'), f'<meta name="description" content="{META["pt"][1]}">'),
 (re.compile(r'<title>Grape to Know</title>'), HEAD),
 (re.compile(r'(  \.fone-a\{left:0\}\.fone-b\{right:0\}\n)  \}'), r'\1' + CSS),
 (re.compile(r'let L = "pt", modo = 0, escolha = null;\ntry\{'),
  'let L = "pt", modo = 0, escolha = null;\nconst LQ = new URLSearchParams(location.search).get("lang");\nif(T[LQ]) L = LQ; else try{'),
 (re.compile(r'(  document\.documentElement\.lang = L==="pt" \? "pt-PT" : L;\n)'),
  r'\1  document.title = T[L]["meta-title"];\n  document.querySelector("meta[name=description]").content = T[L]["meta-desc"];\n'),
 (re.compile(r'href="#" data-jogo target="_blank" rel="noopener"'), 'href="#form-t" data-jogo'),
 (re.compile(r'"acesso-p":"As primeiras mesas abrem em breve, por convite\.[^"]*"'), '"acesso-p":"As primeiras mesas abrem em breve, por convite."'),
 (re.compile(r'"acesso-p":"The first tables open soon, by invitation\.[^"]*"'), '"acesso-p":"The first tables open soon, by invitation."'),
 (re.compile(r'"acesso-p":"Las primeras mesas abren pronto, por invitación\.[^"]*"'), '"acesso-p":"Las primeras mesas abren pronto, por invitación."'),
]
for l in ("pt","en","es"):
    t, d = META[l]
    TROCAS.append((re.compile(r'\n %s:\{\n' % l), '\n %s:{\n  "meta-title":"%s", "meta-desc":"%s",\n' % (l, t, d)))
for f in sys.argv[1:]:
    s = open(f, encoding="utf-8").read()
    if '"meta-title"' in s: print(f, "já aplicado"); continue
    for rx, novo in TROCAS:
        s, n = rx.subn(lambda m: m.expand(novo) if "\\1" in novo else novo, s, count=0)
        if n == 0: print(f, "FALHOU:", rx.pattern[:60])
    open(f, "w", encoding="utf-8").write(s)
    print(f, "ok")
