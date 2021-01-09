const form = document.getElementById("form")
const first_name = document.getElementById("first_name")
const last_name = document.getElementById("last_name")
const email = document.getElementById("email")
const username = document.getElementById("username")
const cur_user = username.value
const number1 = document.getElementById("number1")
form.addEventListener('submit', (e)=>{    
    if (first_name.value == "" || first_name == null){
        e.preventDefault()
        first_name.classList.add('border-danger')
    }
    if (last_name.value == "" || last_name == null){
        e.preventDefault()
        last_name.classList.add('border-danger')
    }
    if (email.value == "" || email == null){
        e.preventDefault()
        email.classList.add('border-danger')
    }
    if (username.value == "" || username == null){
        e.preventDefault()
        username.classList.add('border-danger')
    }
    if (number1.value == "" || number1 == null){
        e.preventDefault()
        number1.classList.add('border-danger')
    }
})

function username_valid() {
    var illegalChars = /\W/;
    var illegalVar = /\[A-Z]/;
    console.log(illegalVar.test(username.value))   
    if(illegalChars.test(username.value)){
        return false
    }
    else{
        return true
    }
}

username.onkeyup = function(){            
    if (username_valid()) {
        $.get("/user/api/check-user/",{username : $('#username').val(), csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()},    
        function(data){
            show(data);
        });
    }
    else{
        username.classList.remove('border-success')
        username.classList.add('border-danger')
        var sub = document.getElementById("username_sub")
        sub.classList.remove('d-none')
        sub.style.color = 'red'
        sub.innerHTML='Invaild username. Please use "[a-z]/[0-9]/_/."'
    }
}

function show(data) {
    if (data['available']==false && username.value != cur_user){
        username.classList.remove('border-success')
        username.classList.add('border-danger')
        var sub = document.getElementById("username_sub")
        sub.classList.remove('d-none')
        sub.style.color = 'red'
        sub.innerHTML='This username is not available'
    }
    else if (username.value == cur_user || username.value == ''){        
        username.classList.remove('border-danger')
        username.classList.remove('border-success')
        var sub = document.getElementById("username_sub")
        sub.classList.add('d-none')
    }
    else{
        username.classList.remove('border-danger')        
        username.classList.add('border-success')
        var sub = document.getElementById("username_sub")
        sub.classList.remove('d-none')
        sub.style.color = 'green'
        sub.innerHTML = 'This username is available'
    }
}