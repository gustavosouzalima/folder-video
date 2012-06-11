folder-video
=================

Folder-Video é um programa em Python que lê os arquivos de video de uma pasta local de sua escolha e gera uma interface em html5 via browser para acessar e organizar sua visualização.

---------------------------------------

Dependências
----------

Para rodar o Folder-Video você precisará de:

- Python
- Firefox 4+, Chrome 6+
- Vídeos no formato: mp4, webm, ogg para Chrome
- Vídeos no formato: webm, ogg para Firefox


**Adendos:**

- Você pode querer converter seus vídeos para um dos formatos acima. Eu recomendo a extension para Firefox FireFogg para formatos webm ou ogg http://firefogg.org/

---------------------------------------

Como usar
-----------
Copie o arquivo "foldervideo.py" para uma pasta que contenha seus vídeos.

Dê permissão de execução:
$ chmod +x foldervideo.py

Agora basta executar o programa:
$ python foldervideo.py


**Opcional:**
Se você quiser ter todos os arquivos necessários (jquery, videojs e etc) baixados no seu computador e não diretamente da internet:
$ python foldervideo.py --local

---------------------------------------

Changelog
-----------

**v 1.0**:

- Exibe os videos da pasta em que foi executado o "foldervideo.py" em uma página index.html
- Vídeo pode ser marcado como visto e mesmo que feche o navegador não é desmarcado
- Exibe os videos em fullscreen
- Página é aberta no ultimo vídeo marcado
- Vídeo é automaticamente marcado quando visto até o fim

TO DO:

- Melhorar a UI, inicialmente está feio e sem grandes estilizações :(
- Fallback para vídeos em outros formatos.
- Abrir automaticamente pagina após executado script "foldervideo.py".

---------------------------------------

Desenvolvido por:
-------

**@dodilei**

+ [http://tech4noobs.agenciax4.com.br](http://tech4noobs.agenciax4.com.br/ "Tech4Noobs")
+ [@dodilei](http://twitter.com/dodilei "Twitter - @dodilei")

---------------------------------------
