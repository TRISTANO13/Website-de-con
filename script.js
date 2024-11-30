// script.js

// Fonction pour rediriger selon la recherche
function handleSearch() {
    const searchInput = document.getElementById('search-input').value.trim();
    if (searchInput.toLowerCase() === 'chaewon') {
        window.location.href = 'chaewon.html';
    } else if (searchInput.toLowerCase() === 'idol') {
        window.location.href = 'idol.html';
    } else if (searchInput.toLowerCase() === 'netflix' || searchInput.toLowerCase() === 'jellyfin' || searchInput.toLowerCase() === 'stream') {
        window.location.href = 'http://tristanhost.ddns.net:8096';
    } else {
        window.location.href = 'results.html';
    }
}

document.addEventListener("DOMContentLoaded", function() {
    const searchInput = document.getElementById("search-input");
    searchInput.addEventListener("keypress", function(event) {
        if (event.key === "Enter") {
            event.preventDefault();
            handleSearch();
        }
    });
});
