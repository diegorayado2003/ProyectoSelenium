function searchGames() {
    var searchTerm = document.getElementById("searchInput").value;
    // Aquí deberías realizar una llamada a una base de datos o API para obtener los resultados de búsqueda.
    // En este ejemplo, simplemente simularemos algunos resultados.
    var results = [
        { name: "The Legend of Zelda", description: "Un juego de aventuras y acción de Nintendo." },
        { name: "Super Mario Bros", description: "Un clásico de plataformas de Nintendo." },
        { name: "Final Fantasy VII", description: "Un juego de rol épico de Square Enix." }
    ];

    var searchResultsDiv = document.getElementById("searchResults");
    searchResultsDiv.innerHTML = ""; // Limpiar resultados anteriores

    results.forEach(function(game) {
        var gameLink = document.createElement("a");
        gameLink.href = "#"; // Enlace temporal, debería llevar a la descripción del juego
        gameLink.innerText = game.name;
        gameLink.onclick = function() {
            showGameDescription(game);
            return false;
        };
        searchResultsDiv.appendChild(gameLink);
        searchResultsDiv.appendChild(document.createElement("br"));
    });
}

function showGameDescription(game) {
    alert("Descripción de " + game.name + ":\n" + game.description);
}
