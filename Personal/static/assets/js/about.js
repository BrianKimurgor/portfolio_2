// about.js
fetch('/about')
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

        // Update the counts using PureCounter library
        const counters = document.querySelectorAll('.purecounter');
        counters.forEach(counter => {
            counter.setAttribute('data-purecounter-end', data.counts_data[counter.id]);
        });

        // Initialize PureCounter
        new PureCounter('.purecounter', {
            duration: 1,
        });
    })
    .catch(error => console.error('Error:', error));
