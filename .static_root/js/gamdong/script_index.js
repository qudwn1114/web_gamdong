const btn_submit = document.getElementById("submitButton");
const input_name = document.getElementById('name');
const input_email = document.getElementById('email');
const input_phone = document.getElementById('phone');
const input_message = document.getElementById('message');
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;


btn_submit.addEventListener("click", async() => {
    if(validation() == false){
        return false;
    }
    const data =new FormData(document.getElementById("contactForm"));
    input_name.disabled = true;
    input_email.disabled = true;
    input_phone.disabled = true;
    input_message.disabled = true;
    btn_submit.disabled = true;
    btn_submit.innerHTML='<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Loading...';

    const response = await fetch('/contact',{
        method: 'POST',
        headers: {'X-CSRFToken': csrftoken},
        body: data
    })
    try{
        const result = await response.json()
        if (!response.ok) {
            throw new Error(`${result.message}`);
        }
        alert(result.message);
        window.location.reload();
    }
    catch(error){
        alert(error);
        input_name.disabled = false;
        input_email.disabled = false;
        input_phone.disabled = false;
        input_message.disabled = false;
        btn_submit.disabled = false;
        btn_submit.innerHTML='Send Message';
        return false;
    }
});

function validation(){
    let reg_email = /^([0-9a-zA-Z_\.-]+)@([0-9a-zA-Z_-]+)(\.[0-9a-zA-Z_-]+){1,2}$/;

    if(input_name.value==''){
        input_name.focus();
        return false;
    }
    if(input_email.value==''){
        input_email.focus();
        return false;
    }
    if(!reg_email.test(input_email.value)){
        input_email.focus();
        alert('잘못된 이메일 형식 입니다.');
        return false;
    }         
    if(input_phone.value==''){
        input_phone.focus();
        return false;
    }
    if(input_message.value==''){
        input_message.focus();
        return false;
    }
    return true;
}