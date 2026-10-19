# Grape to Know · site

Site publicado em https://grapetoknow.com (Netlify).
`index.html` é o ficheiro único gerado a partir de `site/index.html` no projeto.

## O jogo dentro do site
O jogo é sempre editado em `/mnt/project-files/jogo/grape-to-know.html` (fonte única) e copiado para o site com
`python3 ferramentas/atualizar-jogo.py`. Até abrir ao público fica em `/jogo-previa-7481774e/`, sem ligação nos menus,
com noindex (meta e `_headers`). Não pôr o endereço no robots.txt: ficaria público. No dia da abertura: mudar `PASTA` para `jogo`,
atualizar `_headers` e apontar `JOGO_URL` em index.html para `/jogo/`.
