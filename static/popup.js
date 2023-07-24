document.getElementById("post-button").addEventListener("click", function() {
  document.getElementById("popup-overlay").style.display = "block";
});

document.getElementById("submit-button").addEventListener("click", function() {
  var content = document.getElementById("post-content").value;
  var currentUsername = document.getElementById("current-user").dataset.username;

  fetch('/create_post', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        content: content,
        currentUsername: currentUsername
    })
  })
  .then(response => response.json())
  .then(data => {
    console.log(data);

    // Criar o elemento HTML do novo post e adicionar ao feed
    var postElement = document.createElement('article');
    postElement.className = 'publi';

    var user_info = document.createElement('div');
    user_info.className = 'user-info';
    user_info.innerHTML = `
      <img class="profile" src="../static/img/user-prof.png" alt="Profile">
      <p class="name">${current_user.username}</p>
      <p class="divisor">·</p>
      <p class="data">${data.created_at}</p>
    `;
    postElement.appendChild(user_info);

    var contentElement = document.createElement('p');
    contentElement.className = 'conteudo';
    contentElement.textContent = data.content;
    postElement.appendChild(contentElement);

    // Adicionar o novo post no início do feed
    var feed = document.querySelector('.posts');
    feed.insertBefore(postElement, feed.firstChild);

    closeModal();
  })
  .catch(error => {
    console.error('Error:', error);
  });

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
