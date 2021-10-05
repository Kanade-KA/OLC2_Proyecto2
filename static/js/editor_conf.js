// referencia a codemirror: https://codemirror.net/doc/manual.html
var ancho = 650;
var alto = 605
var editor = CodeMirror.fromTextArea(document.getElementById("entrada"),{
    lineNumbers : true,
    theme : "twilight",
    mode : "julia",
    autoRefresh:true
});

editor.setSize(ancho, alto);
editor.refresh();

var editors = CodeMirror.fromTextArea(document.getElementById("salida"),{
    lineNumbers : true,
    theme : "twilight",
    autoRefresh:true,
    mode : "go"
    //readOnly:true
    
});

editors.setSize(ancho, alto);
editors.refresh();