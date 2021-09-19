const login = document.getElementById('login');
console.log(login)
login.addEventListener('click', () => {
    //alert('aaa')
    const email=document.getElementById('email1').value;
    console.log(email)
    localStorage.setItem('user',email);
})