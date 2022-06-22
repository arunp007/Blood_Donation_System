function validation(){
    var status = 1
    var organization = document.getElementById('organization')
    var datetime = document.getElementById('datetime')
    var address = document.getElementById('address')
    var state = document.getElementById('state')
    var district = document.getElementById('district')
    var name = document.getElementById('name')
    var phone = document.getElementById('phone')
    var email = document.getElementById('emailid')

    if(organization.value == ""){
        document.getElementById('organization').style.borderColor="red"
        document.getElementById('organization_error').innerHTML="** Please Enter Your Organization Name **"
        document.getElementById('organization_error').style.color="red"
        document.getElementById('organization_error').style.display="block"
        var status = 0
    }

    else{
        document.getElementById('organization').style.borderColor="black"
        document.getElementById('organization_error').style.display="none"
        var status = 1
    }

    if(datetime.value == ""){
        document.getElementById('datetime').style.borderColor="red"
        document.getElementById('datetime_error').innerHTML="** Please Enter Date And Time **"
        document.getElementById('datetime_error').style.color="red"
        document.getElementById('datetime_error').style.display="block"
        var status = 0
    }

    else{
        document.getElementById('datetime').style.borderColor="black"
        document.getElementById('datetime_error').style.display="none"
        var status = 1
    }

    if(address.value == ""){
        document.getElementById('address').style.borderColor="red"
        document.getElementById('address_error').innerHTML="** Please Enter Permanent Address **"
        document.getElementById('address_error').style.color="red"
        document.getElementById('address_error').style.display="block"
        var status = 0
    }

    else{
        document.getElementById('address').style.borderColor="black"
        document.getElementById('address_error').style.display="none"
        var status = 1
    }

    if(state.value == ""){
        document.getElementById('state').style.borderColor="red"
        document.getElementById('state_error').innerHTML="** Please Enter Your State **"
        document.getElementById('state_error').style.color="red"
        document.getElementById('state_error').style.display="block"
        var status = 0
    }

    else{
        document.getElementById('state').style.borderColor="black"
        document.getElementById('state_error').style.display="none"
        var status = 1
    }

    if(district.value == ""){
        document.getElementById('district').style.borderColor="red"
        document.getElementById('district_error').innerHTML="** Please Enter Your District **"
        document.getElementById('district_error').style.color="red"
        document.getElementById('district_error').style.display="block"
        var status = 0
    }

    else{
        document.getElementById('district').style.borderColor="black"
        document.getElementById('district_error').style.display="none"
        var status = 1
    }

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

    if(email.value == ""){
        document.getElementById('emailid').style.borderColor="red"
        document.getElementById('email_error').innerHTML="** Please Enter Your Email Id **"
        document.getElementById('email_error').style.color="red"
        document.getElementById('email_error').style.display="block"
        var status = 0
    }

    else{
        document.getElementById('emailid').style.borderColor="black"
        document.getElementById('email_error').style.display="none"
        var status = 1
    }

    if(status == 0){
        return false
    }

    if(status == 1){
        return true
    }
    
}

function campvalid(){
    var camp = document.getElementById('organization').value
    if(isNaN(camp)){
        document.getElementById('organization').style.borderColor="black"
        document.getElementById('organization_error').style.display="none"
    }

    else{
        document.getElementById('organization').style.borderColor="red"
        document.getElementById('organization_error').innerHTML="** Please Enter A Valid Camp Name **"
        document.getElementById('organization_error').style.color="red"
        document.getElementById('organization_error').style.display="block"
    }
}

function addressvalid(){
    var address = document.getElementById('address').value
    if(isNaN(address)){
        document.getElementById('address').style.borderColor="black"
        document.getElementById('address_error').style.display="none"
    }

    else{
        document.getElementById('address').style.borderColor="red"
        document.getElementById('address_error').innerHTML="** Please Enter A Valid Address **"
        document.getElementById('address_error').style.color="red"
        document.getElementById('address_error').style.display="block"
    }
}

function statevalid(){
    var state = document.getElementById('state').value
    if(isNaN(state)){
        document.getElementById('state').style.borderColor="black"
        document.getElementById('state_error').style.display="none"
    }

    else{
        document.getElementById('state').style.borderColor="red"
        document.getElementById('state_error').innerHTML="** Please Enter A Valid State **"
        document.getElementById('state_error').style.color="red"
        document.getElementById('state_error').style.display="block"
    }
}

function districtvalid(){
    var district = document.getElementById('district').value
    if(isNaN(district)){
        document.getElementById('district').style.borderColor="black"
        document.getElementById('district_error').style.display="none"
    }

    else{
        document.getElementById('district').style.borderColor="red"
        document.getElementById('district_error').innerHTML="** Please Enter A Valid District **"
        document.getElementById('district_error').style.color="red"
        document.getElementById('district_error').style.display="block"
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

function phonevalid(){
    var phone = document.getElementById('phone').value
    if(isNaN(phone)){
        document.getElementById('phone').style.borderColor="red"
        document.getElementById('phone_error').innerHTML="** Please Enter A Valid Mobile Number **"
        document.getElementById('phone_error').style.color="red"
        document.getElementById('phone_error').style.display="block"
    }

    if(phone.length<=0){
        document.getElementById('phone').style.borderColor="red"
        document.getElementById('phone_error').innerHTML="** Mobile Number Must Have 10 Digits **"
        document.getElementById('phone_error').style.color="red"
        document.getElementById('phone_error').style.display="block"
    }

    if(phone.length == 10){
        document.getElementById('phone').style.borderColor="green"
        document.getElementById('phone_error').innerHTML="** You Entered A Perfect Mobile Number **"
        document.getElementById('phone_error').style.color="green"
        document.getElementById('phone_error').style.display="block"
    }

    if(phone.length == 11){
        document.getElementById('phone').style.borderColor="red"
        document.getElementById('phone_error').innerHTML="** Mobile Number Must Have 10 Digits **"
        document.getElementById('phone_error').style.color="red"
        document.getElementById('phone_error').style.display="block"
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