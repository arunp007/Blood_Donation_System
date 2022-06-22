function validation(){
    var status = 1
    var name = document.getElementById('name')
    var email = document.getElementById('emailid')
    var message = document.getElementById('message')

    if(name.value == ""){
        document.getElementById('name').style.borderColor="red"
        document.getElementById('name_error').innerHTML="** Please Enter Your Name **"
        document.getElementById('name_error').style.color="red"
        document.getElementById('name_error').style.display="block"
        status = 0
    }

    else{
        document.getElementById('name').style.borderColor="black"
        document.getElementById('name_error').style.display="none"
        status = 1
    }

    if(email.value == ""){
        document.getElementById('emailid').style.borderColor="red"
        document.getElementById('email_error').innerHTML="** Please Enter Your Email Id **"
        document.getElementById('email_error').style.color="red"
        document.getElementById('email_error').style.display="block"
        status = 0
    }

    else{
        document.getElementById('emailid').style.borderColor="black"
        document.getElementById('email_error').style.display="none"
        status = 1
    }

    if(message.value == ""){
        document.getElementById('message').style.borderColor="red"
        document.getElementById('message_error').innerHTML="** Please Enter Your Message **"
        document.getElementById('message_error').style.color="red"
        document.getElementById('message_error').style.display="block"
        status = 0
    }

    else{
        document.getElementById('message').style.borderColor="black"
        document.getElementById('message_error').style.display="none"
        status = 1
    }

    if(status == 1){
        return true
    }

    if(status == 0){
        return false
    }

}

function namevalid(){
    var name = document.getElementById('name').value

    if(isNaN(name)){
        document.getElementById('name').style.borderColor="black"
        document.getElementById('name_error').style.display="none"
    }

    else{
       
        document.getElementById('name').style.borderColor="red"
        document.getElementById('name_error').innerHTML="** Please Enter A Valid Name **"
        document.getElementById('name_error').style.color="red"
        document.getElementById('name_error').style.display="block"
    }
}

function emailvalid(){
    var email = document.getElementById('emailid').value

    if(isNaN(email)){
        document.getElementById('emailid').style.borderColor="black"
        document.getElementById('email_error').style.display="none"
    }

    else{
        document.getElementById('emailid').style.borderColor="red"
        document.getElementById('email_error').innerHTML="** Please Enter A Valid Email Id **"
        document.getElementById('email_error').style.color="red"
        document.getElementById('email_error').style.display="block"  
    }
}

function messagevalid(){
    var message = document.getElementById('message').value

    if(isNaN(message)){
        document.getElementById('message').style.borderColor="black"
        document.getElementById('message_error').style.display="none"
    }

    else{
        document.getElementById('message').style.borderColor="red"
        document.getElementById('message_error').innerHTML="** Please Enter A Valid Message **"
        document.getElementById('message_error').style.color="red"
        document.getElementById('message_error').style.display="block"
    }
}