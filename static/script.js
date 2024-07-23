function submitQuery() {
    const query = document.getElementById('query').value;
    fetch('/query', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ query: query })
    })
        .then(response => response.json())
        .then(data => {
            document.getElementById('response').innerText = data.output;
            if (data.plot_url) {
                document.getElementById('plot').src = data.plot_url;
            } else {
                document.getElementById('plot').src = '';
            }
        })
        .catch(error => console.error('Error submitting query:', error));
}
