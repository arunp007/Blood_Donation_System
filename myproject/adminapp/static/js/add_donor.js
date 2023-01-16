function validation(){
    var status = 1
    var name = document.getElementById('name')
    var blood = document.getElementById('blood-group')
    var location = document.getElementById('location')
    var phone = document.getElementById('phone')

    if(name.value == ""){
        document.getElementById('name').style.borderColor="red"
        document.getElementById('name_error').innerHTML="** Please Enter Your Name **"
        document.getElementById('name_error').style.color="red"
        document.getElementById('name_error').style.display="block"
        var status = 0
    }

    else{
        document.getElementById('name').style.borderColor="black"
        document.getElementById('name_error').style.display="none"
        var status = 1
    }

    if(blood.value == ""){
        document.getElementById('blood-group').style.borderColor="red"
        document.getElementById('blood_error').innerHTML="** Please Enter Your Blood Group **"
        document.getElementById('blood_error').style.color="red"
        document.getElementById('blood_error').style.display="block"
        var status = 0
    }

    else{
        document.getElementById('blood-group').style.borderColor="black"
        document.getElementById('blood_error').style.display="none"
        var status = 1
    }

    if(location.value == ""){
        document.getElementById('location').style.borderColor="red"
        document.getElementById('location_error').innerHTML="** Please Enter Your Location **"
        document.getElementById('location_error').style.color="red"
        document.getElementById('location_error').style.display="block"
        var status = 0
    }

    else{
        document.getElementById('location').style.borderColor="black"
        document.getElementById('location_error').style.display="none"
        var status = 1
    }

    if(phone.value == ""){
        document.getElementById('phone').style.borderColor="red"
        document.getElementById('phone_error').innerHTML="** Please Enter Your Phone Number **"
        document.getElementById('phone_error').style.color="red"
        document.getElementById('phone_error').style.display="block"
        var status = 0
    }

    else{
        document.getElementById('phone').style.borderColor="black"
        document.getElementById('phone_error').style.display="none"
        var status = 1
    }


    if(status == 0){
        return false
    }

    if(status = 1){
        return true
    }
}

function name_valid(){
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

function phone_valid(){
    var phone = document.getElementById('phone').value

    if(isNaN(phone)){
        document.getElementById('phone').style.borderColor="red"
        document.getElementById('phone_error').innerHTML="** Please Enter A Valid Phone Number **"
        document.getElementById('phone_error').style.color="red"
        document.getElementById('phone_error').style.display="block"
    }

    else{
        document.getElementById('phone').style.borderColor="black"
        document.getElementById('phone_error').style.display="none"
    }

    if(phone.length<= 3){
        document.getElementById('phone').style.borderColor="red"
        document.getElementById('phone_error').innerHTML="** Please Enter A Valid Phone Number **"
        document.getElementById('phone_error').style.color="red"
        document.getElementById('phone_error').style.display="block"
    }

    if(phone.length == 10){
        document.getElementById('phone').style.borderColor="green"
        document.getElementById('phone_error').innerHTML="** You Entered A Perfect Phone Number **"
        document.getElementById('phone_error').style.color="green"
        document.getElementById('phone_error').style.display="block"
    }

    if(phone.length > 10){
        document.getElementById('phone').style.borderColor="red"
        document.getElementById('phone_error').innerHTML="** Please Enter A Valid Phone Number **"
        document.getElementById('phone_error').style.color="red"
        document.getElementById('phone_error').style.display="block"
    }
}