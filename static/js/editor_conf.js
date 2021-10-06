// referencia a codemirror: https://codemirror.net/doc/manual.html
var alto = 700;
var editor = CodeMirror.fromTextArea(document.getElementById("entrada"),{
    lineNumbers : true,
    theme : "twilight",
    mode : "julia",
    autoRefresh:true
});

editor.setSize(null, alto);
editor.refresh();

var editors = CodeMirror.fromTextArea(document.getElementById("salida"),{
    lineNumbers : true,
    theme : "twilight",
    autoRefresh:true,
    mode : "go"
    //readOnly:true
    
});

editors.setSize(null, alto);
editors.refresh();

var editorg = CodeMirror.fromTextArea(document.getElementById("grafica"),{
    lineNumbers : true,
    theme : "twilight",
    autoRefresh:true,
    mode : "ebnf",
    readOnly:true
    
});

editorg.setSize(null, alto);
editorg.refresh();