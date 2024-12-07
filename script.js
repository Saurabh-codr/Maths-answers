document.getElementById('submit-btn').addEventListener('click', () => {
    const password = document.getElementById('password').value;
    const resultDiv = document.getElementById('result');
    const successImg = document.getElementById('success-img');

    // Set your desired password
    const correctPassword = 'cristianoronaldodossantosaveiro';

    if (password === correctPassword) {
        resultDiv.textContent = 'Correct Password! Image Unlocked.';
        resultDiv.className = 'text-success fw-bold mt-3';
        successImg.style.display = 'block';
    } else {
        resultDiv.textContent = 'Incorrect Password. Try Again.';
        resultDiv.className = 'text-danger fw-bold mt-3';
        successImg.style.display = 'none';
    }
});
