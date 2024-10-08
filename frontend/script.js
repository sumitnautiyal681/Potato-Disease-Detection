document.getElementById('uploadForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    
    const formData = new FormData();
    const imageFile = document.getElementById('image').files[0];
    formData.append('image', imageFile);
    
    try {
        const response = await fetch('http://127.0.0.1:5000/predict', {
            method: 'POST',
            body: formData
        });
        
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        
        const result = await response.json();  // Parse JSON response
        console.log(result.class);  // Access the 'class' field in the JSON response

        document.getElementById('result').innerHTML = `
            <p>Class: ${result.class}</p>
        `;
    } catch (error) {
        document.getElementById('result').innerHTML = `
            <p>Error: ${error.message}</p>
        `;
    }
});