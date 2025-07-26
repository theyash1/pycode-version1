document.getElementById('checkStrength').addEventListener('click', function() {
    const password = document.getElementById('password').value;
    const resultDiv = document.getElementById('result');
    
    
    resultDiv.innerHTML = '';

    
    if (!password) {
        resultDiv.innerHTML = 'Please enter a password.';
        return;
    }

    
    fetch('/check-password', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ password: password })
    })
    .then(response => response.json())
    .then(data => {
        if (data.isValid) {
            resultDiv.innerHTML = 'Password is strong and meets all criteria!';
        } else {
            resultDiv.innerHTML = 'Password doesn't meet the following criteria:<br>';
            resultDiv.innerHTML += data.missingCriteria.join('<br>');
        }
    })
    .catch(error => {
        resultDiv.innerHTML = 'Error validating password: ' + error.message;
    });
});

document.getElementById('generatePassword').addEventListener('click', function() {
    fetch('/generate-password')
        .then(response => response.json())
        .then(data => {
            const generatedPassword = data.password;
            document.getElementById('generatedPassword').innerHTML = 'Generated Password: ' + generatedPassword;
        })
        .catch(error => {
            document.getElementById('generatedPassword').innerHTML = 'Error generating password: ' + error.message;
        });
});
