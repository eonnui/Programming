const loginForm = document.getElementById('login-form');
const registerForm = document.getElementById('register-form');
const showLogin = document.getElementById('show-login');
const showRegister = document.getElementById('show-register');

showRegister.addEventListener('click', () => {
    loginForm.classList.add('hidden');
    registerForm.classList.remove('hidden');
});

showLogin.addEventListener('click', () => {
    registerForm.classList.add('hidden');
    loginForm.classList.remove('hidden');
})


async function handleFormSubmit(form, endpoint) {
    const formData = new FormData(form);
    const response = await fetch(endpoint, {
        method: 'POST',
        body: formData,
    });
    
    const result = await response.json();
    alert(result.message);

    if (result.success) {
        if (endpoint === '/register') showLogin.click();
        else window.location.href = '/dashboard';
    }
}

registerForm.onsubmit = (e) => {
    e.preventDefault();
    handleFormSubmit(registerForm, '/register');   
};

loginForm.onsubmit = (e) => {
    e.preventDefault();
    handleFormSubmit(loginForm, '/login');
};