# Escreve no HTML o texto PT do dicionário T, para motores de busca e pré-visualizações
# verem a página sem correr JavaScript. O JS continua a trocar de língua como antes.
# Correr depois de mudar textos: python3 ferramentas/prerender.py index.html
import sys, re, json, subprocess, html
for f in sys.argv[1:]:
    s = open(f, encoding="utf-8").read()
    a = s.index("const T = {"); b = s.index("\n};", a) + 3
    T = json.loads(subprocess.run(["node", "-e", s[a:b] + "\nconsole.log(JSON.stringify(T.pt))"],
                                  capture_output=True, text=True, check=True).stdout)
    corpo_ini = s.index("</style>")
    head, corpo = s[:corpo_ini], s[corpo_ini:]
    js = corpo.index("<script>")
    marc, resto = corpo[:js], corpo[js:]
    n = [0]
    def txt(m):
        v = T.get(m.group(3))
        if v is None: return m.group(0)
        n[0] += 1
        return m.group(1) + html.escape(v, quote=False) + "</" + m.group(2) + ">"
    marc = re.sub(r'(<(\w+)\b[^>]*\bdata-t="([^"]+)"[^>]*>)[^<]*</\2>', txt, marc)
    marc = re.sub(r'data-ta="([^"]+)" alt="[^"]*"', lambda m: f'data-ta="{m.group(1)}" alt="{html.escape(T.get(m.group(1), ""))}"', marc)
    marc = re.sub(r'data-ta-label="([^"]+)" aria-label="[^"]*"', lambda m: f'data-ta-label="{m.group(1)}" aria-label="{html.escape(T.get(m.group(1), ""))}"', marc)
    open(f, "w", encoding="utf-8").write(head + marc + resto)
    print(f, n[0], "textos")
