document.getElementById("post-button").addEventListener("click", function() {
    document.getElementById("popup-overlay").style.display = "block";
});

document.getElementById("submit-button").addEventListener("click", function() {
    document.getElementById("popup-overlay").style.display = "none";
});
document.getElementById("cancel-button").addEventListener("click", function() {
    document.getElementById("popup-overlay").style.display = "none";
  });

function bold(event) {
    event.preventDefault();
    var textarea = document.getElementById("post-content");
    var selectedText = textarea.value.substring(textarea.selectionStart, textarea.selectionEnd);
    var newText = '<b>' + selectedText + '</b>';
    textarea.value = textarea.value.substring(0, textarea.selectionStart) + newText + textarea.value.substring(textarea.selectionEnd);
}

function italic(event) {
    event.preventDefault();
    var textarea = document.getElementById("post-content");
    var selectedText = textarea.value.substring(textarea.selectionStart, textarea.selectionEnd);
    var newText = '<i>' + selectedText + '</i>';
    textarea.value = textarea.value.substring(0, textarea.selectionStart) + newText + textarea.value.substring(textarea.selectionEnd);
}

function header(event) {
    event.preventDefault();
    var textarea = document.getElementById("post-content");
    var selectedText = textarea.value.substring(textarea.selectionStart, textarea.selectionEnd);
    var newText = '<h1>' + selectedText + '</h1>';
    textarea.value = textarea.value.substring(0, textarea.selectionStart) + newText + textarea.value.substring(textarea.selectionEnd);
}

function link(event) {
    event.preventDefault();
    var url = prompt("Insira o URL do link:");
    if (url) {
        var textarea = document.getElementById("post-content");
        var selectedText = textarea.value.substring(textarea.selectionStart, textarea.selectionEnd);
        var newText = '<a href="' + url + '">' + selectedText + '</a>';
        textarea.value = textarea.value.substring(0, textarea.selectionStart) + newText + textarea.value.substring(textarea.selectionEnd);
    }
}

function image(event) {
    event.preventDefault();
    var url = prompt("Insira o URL da imagem:");
    if (url) {
        var textarea = document.getElementById("post-content");
        var newText = '<img src="' + url + '">';
        textarea.value += newText;
    }
}

function help(event) {
    event.preventDefault();
    // Lógica para abrir a central de ajuda
    alert("Central de Ajuda");
}