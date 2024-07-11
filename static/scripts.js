document.getElementById("scrape-button").addEventListener("click", function() {
    const url = document.getElementById("url-input").value;
    window.location.href = `/scrape?url=${encodeURIComponent(url)}`;
});
