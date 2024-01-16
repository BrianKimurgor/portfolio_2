// about.js
fetch('/api/about_data')
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        document.getElementById('about-text').innerText = data.about_text;

        // Display personal information
        const personalInfoList = document.getElementById('personal-info-list');
        for (const [key, value] of Object.entries(data.personal_info)) {
            const li = document.createElement('li');
            li.innerHTML = `<i class="bi bi-chevron-right"></i> <strong>${key}:</strong> <span>${value}</span>`;
            personalInfoList.appendChild(li);
        }

        // Display additional information
        document.getElementById('additional-info').innerText = data.additional_info;
    })
    .catch(error => console.error('Error:', error));
