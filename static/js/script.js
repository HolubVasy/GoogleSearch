document.addEventListener('DOMContentLoaded', function() {
    const searchForm = document.getElementById('search-form');
    const searchInput = document.getElementById('search-input');
    const searchButton = document.getElementById('search-button');
    const luckyButton = document.getElementById('lucky-button');

    searchForm.addEventListener('submit', function(event) {
        if (searchInput.value.trim() === '') {
            event.preventDefault();
            alert('Please enter a search query.');
        } else if (searchInput.value.trim().length < 3) {
            event.preventDefault();
            alert('Search query must be at least 3 characters long.');
        }
    });

    luckyButton.addEventListener('click', function(event) {
        event.preventDefault();
        if (searchInput.value.trim() === '') {
            alert('Please enter a search query.');
        } else if (searchInput.value.trim().length < 3) {
            alert('Search query must be at least 3 characters long.');
        } else {
            window.location.href = '/lucky?q=' + encodeURIComponent(searchInput.value.trim());
        }
    });
});