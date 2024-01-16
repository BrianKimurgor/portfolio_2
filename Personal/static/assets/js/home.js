// home.js
fetch('/api/home_data')
    .then(response => response.json())
    .then(data => {
        document.getElementById('intro').innerText = data.intro;
        // Add more updates as needed
    })
    .catch(error => console.error('Error:', error));
