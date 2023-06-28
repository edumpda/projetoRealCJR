document.getElementById("post-button").addEventListener("click", function() {
    document.getElementById("popup-overlay").style.display = "block";
});

document.getElementById("submit-button").addEventListener("click", function() {
    document.getElementById("popup-overlay").style.display = "none";
});
document.getElementById("cancel-button").addEventListener("click", function() {
    document.getElementById("popup-overlay").style.display = "none";
  });