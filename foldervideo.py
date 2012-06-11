#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Autor: @dodilei
# DATA: 10 de Junho de 2012
# Folder-Video lê arquivos de video em sua pasta e gera uma interface em html5 para acessá-lo via browser.

import os
import sys
import subprocess

cmd = os.getcwd()
folder = cmd.split('/')
n = len(folder)
pasta_atual = folder[n-1]
local_storage = pasta_atual.replace(' ', '')

pasta_origem = os.listdir("./")
pasta_origem.sort()
arquivo_destino = "index.html"
formatos_aceitos = ["mp4","ogv","webm"]
arquivos_local = "./foldervideo"
escreve = open(arquivo_destino, 'w')

jquery = "https://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"
videojs = "http://vjs.zencdn.net/c/video.js"
videojscss = "http://vjs.zencdn.net/c/video-js.css"

parametro = ""
if len(sys.argv) > 1:
    parametro = sys.argv[1]

if not os.path.exists(arquivos_local):
    subprocess.call(["mkdir %s" % arquivos_local], shell=True)
    if parametro and parametro == "--local":
        subprocess.call(["cd %s && wget %s" % (arquivos_local, jquery)], shell=True)
        subprocess.call(["cd %s && wget %s" % (arquivos_local, videojs)], shell=True)
        subprocess.call(["cd %s && wget %s" % (arquivos_local, videojscss)], shell=True)
        subprocess.call(["cd %s && wget https://github.com/zencoder/video-js/blob/master/design/video-js.png?raw=true && mv video-js.png?raw=true video-js.png" % arquivos_local], shell=True)
        jquery = "jquery.min.js"
        videojs = "video.js"
        videojscss = "video-js.css"

quantidade = 0
lista_videos = []
for arquivos in pasta_origem:
    try:
        ehvideo = arquivos.rsplit('.', 1)[1] in formatos_aceitos
        if ehvideo:
            quantidade += 1
            lista_videos.append(arquivos)
            print "escrevendo o arquivo %s " % arquivos
        else:
            print "o arquivo %s nao eh video" % arquivos
    except:
        print "*** erro ao escrever"
        
print "--- %d arquivos tratados" % quantidade
quantidade += 1

html="""
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="utf-8">
    <title>Folder-Video</title>
"""
escreve.write(html)

bibliotecas='<script src="%s"></script>\n<script src="%s">\n</script><link href="%s" rel="stylesheet">\n' % (jquery,videojs,videojscss)
escreve.write(bibliotecas)

html="""
<style type="text/css" media="screen">
div#lista_videos {
padding: 15px;
border: 1px solid black;
-moz-column-count: 8;
-webkit-column-count: 8;

-moz-column-width: 40px; 
-webkit-column-width: 40px; 

-moz-column-gap: 40px;
-webkit-column-gap: 40px;
}

#video {
margin: auto;
box-shadow: 0 0 30px #000;
max-width: 100%;
max-height: 100%;
}

/* estiliza os botoes */
button:active {
    position: relative;
    top: 2px;
}
button.play {
}  
button.pause {
}
    </style>
</head>
<body>
    <video id="video" class="video-js vjs-default-skin"  
      controls preload="auto" width="640" height="360" 
      data-setup='{"example_option":true}'>
"""
escreve.write(html)

formatovideo = lista_videos[0].rsplit('.', 1)[1]
escreve.write('<source src="../%s" type="video/%s"/>' % (lista_videos[0],formatovideo))

html="""
    </video>
    <hgroup>
    <h1>Marque seus videos e saiba aonde parou!</h1>
    <h3></h3>
    </hgroup>
    <div id="lista_videos">
"""
escreve.write(html)

for x in range(1,quantidade):
    #print x+'\n'
    escreve.write('<p><input type="checkbox" value="%s"  name="checks"> <span>%s</span> <button class="play" value="%s">></button><button class="pause">II</button></p>\n' % (x,x,x))

html="""
    </div>
<script type="text/javascript">
// Coloca no localStorage o que foi marcado no checkbox
var checks = [];
if (localStorage['%s'] == null) {
    localStorage.clear();
    localStorage['%s']=JSON.stringify(checks);
} else {
    //localStorage['%s']=JSON.stringify(checks);
    checks = JSON.parse(localStorage['%s']);
}

$('input:checkbox[name=checks]').each(function () {
    //init the checkbox
    $(this).prop("checked", checks[this.value]?true:false);
    $(this).change(function () {
        $('input:checkbox[name=checks]').each(function () {
            checks[this.value] = this.checked;
        });
        localStorage['%s']=JSON.stringify(checks);
    });
});

// Adicionq lista de videos contidos na pasta em questao
""" % (local_storage.lower(),local_storage.lower(),local_storage.lower(),local_storage.lower(),local_storage.lower(),)
escreve.write(html)

escreve.write('var videoList = %s;' % lista_videos)

html="""

allVideos  = JSON.parse(localStorage['%s'])
allVideos.shift()

var marcados = []
for(var i=0;i<allVideos.length;i++){ 
    if(allVideos[i]==true)
        marcados.push(i)
}

if(marcados.length >0) {
    console.log("foi marcado")
    console.log(marcados.length)
    ultimoMarcado = marcados.length-1
    onload = function () {
        document.getElementsByTagName('video')[0].src = "../" + videoList[marcados[ultimoMarcado]];
    }
}

function searchVideo(video) {
    var buttonValueInt = parseInt(video),
        videoNumber = buttonValueInt -1;

    document.getElementsByTagName('video')[0].src = "../" + videoList[videoNumber];
    document.getElementsByTagName('h3')[0].innerHTML = "Você está assistindo o VÍDEO " + buttonValueInt + ": " + videoList[videoNumber];
}

var videoAteFinal = function(){
    var myPlayer = this;
    foiateofim = JSON.parse(localStorage['videoateofim']);
    $('input:checkbox[value='+foiateofim+']').attr('checked', true);
    $('input:checkbox[name=checks]').each(function () {
            checks[this.value] = this.checked;
        });
    localStorage['%s']=JSON.stringify(checks);
};

// PLAY e PAUSE do video
$(".play").click(function() {
    // chama a lista de videos dinamicamente
    searchVideo(this.value);
    var numeroVideo = [];
    numeroVideo = this.value;
    localStorage['videoateofim']=JSON.stringify(numeroVideo);
    
  _V_("video").ready(function(){

      var myPlayer = this;
      myPlayer.play();
      myPlayer.addEvent("ended", videoAteFinal);
    });
});

$(".pause").click(function() {
  _V_("video").ready(function(){

      var myPlayer = this;
      myPlayer.pause();

    });
});
</script>
</body>
</html>
""" % (local_storage.lower(), local_storage.lower())
escreve.write(html)
escreve.close()

subprocess.call(["mv index.html %s" % arquivos_local], shell=True)