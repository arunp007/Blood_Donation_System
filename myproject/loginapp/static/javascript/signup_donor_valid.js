function validation(){
    var status = 1
    var fname = document.getElementById('firstname')
    var lname = document.getElementById('lastname')
    var blood = document.getElementById('bloodgroup')
    var aadhaar = document.getElementById('aadhaar')
    var day = document.getElementById('day')
    var month = document.getElementById('month')
    var year = document.getElementById('year')
    var gender = document.getElementById('gender')
    var address = document.getElementById('permanentaddress')
    var state = document.getElementById('state')
    var district = document.getElementById('district')
    var pin = document.getElementById('pincode')
    var phone = document.getElementById('phonenumber')
    var email = document.getElementById('emailid')
    var pass = document.getElementById('password')
    var cpass = document.getElementById('cpassword')

    if(fname.value == ""){
        document.getElementById('firstname').style.borderColor="red"
        document.getElementById('first_error').innerHTML="** Please Enter Your First Name **"
        document.getElementById('first_error').style.color="red"
        document.getElementById('first_error').style.display="block"
        var status = 0
    }

    else{
        document.getElementById('firstname').style.borderColor="black"
        document.getElementById('first_error').style.display="none"
        var status = 1
  
    }

    if(lname.value == ""){
        document.getElementById('lastname').style.borderColor="red"
        document.getElementById('last_error').innerHTML="** Please Enter Your Last Name **"
        document.getElementById('last_error').style.color="red"
        document.getElementById('last_error').style.display="block"
        var status = 0
    }

    else{
        document.getElementById('lastname').style.borderColor="black"
        document.getElementById('last_error').style.display="none"
        var status = 1
    }

    if(blood.value == ""){
        document.getElementById('bloodgroup').style.borderColor="red"
        document.getElementById('blood_error').innerHTML="** Please Enter Your Blood Group **"
        document.getElementById('blood_error').style.color="red"
        document.getElementById('blood_error').style.display="block"
        var status = 0
    }

    else{
        document.getElementById('bloodgroup').style.borderColor="black"
        document.getElementById('blood_error').style.display="none"
        var status = 1
    }

    if(aadhaar.value == ""){
        document.getElementById('aadhaar').style.borderColor="red"
        document.getElementById('aadhaar_error').innerHTML="** Please Enter Your Aadhaar Number **"
        document.getElementById('aadhaar_error').style.color="red"
        document.getElementById('aadhaar_error').style.display="block"
        var status = 0
    }

    else{
        document.getElementById('aadhaar').style.borderColor="black"
        document.getElementById('aadhaar_error').style.display="none"
        var status = 1
    }


    if(day.value == ""){
        document.getElementById('day').style.borderColor="red"
        document.getElementById('dob_error1').innerHTML="** Please Enter Your Day **"
        document.getElementById('dob_error1').style.color="red"
        document.getElementById('dob_error1').style.display="block"
        var status = 0
    }

    else{
        document.getElementById('day').style.borderColor="black"
        document.getElementById('dob_error1').style.display="none"
        var status = 1
    }

    if(month.value == ""){
        document.getElementById('month').style.borderColor="red"
        document.getElementById('dob_error2').innerHTML="** Please Enter Your Month **"
        document.getElementById('dob_error2').style.color="red"
        document.getElementById('dob_error2').style.display="block"
        var status = 0
    }

    else{
        document.getElementById('month').style.borderColor="black"
        document.getElementById('dob_error2').style.display="none"
        var status = 1
    }

    if(year.value == ""){
        document.getElementById('year').style.borderColor="red"
        document.getElementById('dob_error3').innerHTML="** Please Enter Your Year **"
        document.getElementById('dob_error3').style.color="red"
        document.getElementById('dob_error3').style.display="block"
        var status = 0
    }

    else{
        document.getElementById('year').style.borderColor="black"
        document.getElementById('dob_error3').style.display="none"
        var status = 1
    }

    if(gender.value == ""){
        document.getElementById('gender').style.borderColor="red"
        document.getElementById('gender_error').innerHTML="** Please Enter Your Gender **"
        document.getElementById('gender_error').style.color="red"
        document.getElementById('gender_error').style.display="block"
        var status = 0
    }

    else{
        document.getElementById('gender').style.borderColor="black"
        document.getElementById('gender_error').style.display="none"
        var status = 1
    }

    if(address.value == ""){
        document.getElementById('permanentaddress').style.borderColor="red"
        document.getElementById('address_error').innerHTML="** Please Enter Your Permanent Address **"
        document.getElementById('address_error').style.color="red"
        document.getElementById('address_error').style.display="block"
        var status = 0
    }

    else{
        document.getElementById('permanentaddress').style.borderColor="black"
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
        document.getElementById('district_error').innerHTML="** Please Enter Your State **"
        document.getElementById('district_error').style.color="red"
        document.getElementById('district_error').style.display="block"
        var status = 0
    }

    else{
        document.getElementById('district').style.borderColor="black"
        document.getElementById('district_error').style.display="none"
        var status = 1
    }

    if(pin.value == ""){
        document.getElementById('pincode').style.borderColor="red"
        document.getElementById('pincode_error').innerHTML="** Please Enter Your Pincode **"
        document.getElementById('pincode_error').style.color="red"
        document.getElementById('pincode_error').style.display="block"
        var status = 0
    }

    else{
        document.getElementById('pincode').style.borderColor="black"
        document.getElementById('pincode_error').style.display="none"
        var status = 1
    }

    if(phone.value == ""){
        document.getElementById('phonenumber').style.borderColor="red"
        document.getElementById('phone_error').innerHTML="** Please Enter Your Mobile Number **"
        document.getElementById('phone_error').style.color="red"
        document.getElementById('phone_error').style.display="block"
        var status = 0
    }

    else{
        document.getElementById('phonenumber').style.borderColor="black"
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

    if(pass.value == ""){
        document.getElementById('password').style.borderColor="red"
        document.getElementById('password_error').innerHTML="** Please Enter Your Password **"
        document.getElementById('password_error').style.color="red"
        document.getElementById('password_error').style.display="block"
        var status = 0
    }

    else{
        document.getElementById('password').style.borderColor="black"
        document.getElementById('password_error').style.display="none"
        var status = 1
    }

    if(cpass.value == ""){
        document.getElementById('cpassword').style.borderColor="red"
        document.getElementById('cpassword_error').innerHTML="** Please Enter Your Confirm Password **"
        document.getElementById('cpassword_error').style.color="red"
        document.getElementById('cpassword_error').style.display="block"
        var status = 0
    }

    else{
        document.getElementById('cpassword').style.borderColor="black"
        document.getElementById('cpassword_error').style.display="none"
        var status = 1
    }

    if(status == 0){
        return false
    }

    if(status == 1){
        return true
    }

}

function firstnamevalid(){
    var fname = document.getElementById('firstname').value

    if(isNaN(fname)){
        document.getElementById('firstname').style.borderColor="black"
        document.getElementById('first_error').style.display="none" 
    }

    else{
        document.getElementById('firstname').style.borderColor="red"
        document.getElementById('first_error').innerHTML="** Please Enter A Valid Email Id **"
        document.getElementById('first_error').style.color="red"
        document.getElementById('first_error').style.display="block"
    }

        
}

function lastnamevalid(){
    var lname = document.getElementById('lastname').value
    if(isNaN(lname)){
        document.getElementById('lastname').style.borderColor="black"
        document.getElementById('last_error').style.display="none" 
    }

    else{
        document.getElementById('lastname').style.borderColor="red"
        document.getElementById('last_error').innerHTML="** Please Enter A Valid Email Id **"
        document.getElementById('last_error').style.color="red"
        document.getElementById('last_error').style.display="block"
    }
}

function aadhaarvalid(){
    var aadhaar = document.getElementById('aadhaar').value
    if(isNaN(aadhaar)){
        document.getElementById('aadhaar').style.borderColor="red"
        document.getElementById('aadhaar_error').innerHTML="** Please Enter A Valid Aadhaar Number **"
        document.getElementById('aadhaar_error').style.color="red"
        document.getElementById('aadhaar_error').style.display="block" 
    }

    if(aadhaar.length<=0){
        document.getElementById('aadhaar').style.borderColor="red"
        document.getElementById('aadhaar_error').innerHTML="** Aadhaar Number Must Have 12 Digits **"
        document.getElementById('aadhaar_error').style.color="red"
        document.getElementById('aadhaar_error').style.display="block"  
    }

    if(aadhaar.length == 12){
        document.getElementById('aadhaar').style.borderColor="green"
        document.getElementById('aadhaar_error').innerHTML="** You Entered A Perfect Aadhaar Number **"
        document.getElementById('aadhaar_error').style.color="green"
        document.getElementById('aadhaar_error').style.display="block"
    }

    if(aadhaar.length == 13){
        document.getElementById('aadhaar').style.borderColor="red"
        document.getElementById('aadhaar_error').innerHTML="** Aadhaar Number Must Have 12 Digits **"
        document.getElementById('aadhaar_error').style.color="red"
        document.getElementById('aadhaar_error').style.display="block"
    }

}

function addressvalid(){
    var address = document.getElementById('permanentaddress').value
    if(isNaN(address)){
        document.getElementById('permanentaddress').style.borderColor="black"
        document.getElementById('address_error').style.display="none" 
    }

    else{
        document.getElementById('permanentaddress').style.borderColor="red"
        document.getElementById('address_error').innerHTML="** Please Enter A Valid Permanent Address **"
        document.getElementById('address_error').style.color="red"
        document.getElementById('address_error').style.display="block"
    }
}

function pincodevalid(){
    var pin = document.getElementById('pincode').value
    if(isNaN(pin)){
        document.getElementById('pincode').style.borderColor="red"
        document.getElementById('pincode_error').innerHTML="** Please Enter A Valid Pincode **"
        document.getElementById('pincode_error').style.color="red"
        document.getElementById('pincode_error').style.display="block"
    }

    if(pin.length <= 0){
        document.getElementById('pincode').style.borderColor="red"
        document.getElementById('pincode_error').innerHTML="** Pincode Must Have 6 Digits **"
        document.getElementById('pincode_error').style.color="red"
        document.getElementById('pincode_error').style.display="block"
    }

    if(pin.length == 6){
        document.getElementById('pincode').style.borderColor="green"
        document.getElementById('pincode_error').innerHTML="** You Entered A Perfect Pincode **"
        document.getElementById('pincode_error').style.color="green"
        document.getElementById('pincode_error').style.display="block" 
    }

    if(pin.length == 7){
        document.getElementById('pincode').style.borderColor="red"
        document.getElementById('pincode_error').innerHTML="** Pincode Must Have 6 Digits **"
        document.getElementById('pincode_error').style.color="red"
        document.getElementById('pincode_error').style.display="block"
    }

}

function phonevalid(){
    var phone = document.getElementById('phonenumber').value
    if(isNaN(phone)){
        document.getElementById('phonenumber').style.borderColor="red"
        document.getElementById('phone_error').innerHTML="** Please Enter A Valid Mobile Number **"
        document.getElementById('phone_error').style.color="red"
        document.getElementById('phone_error').style.display="block"
    }

    if(phone.length <= 0){
        document.getElementById('phonenumber').style.borderColor="red"
        document.getElementById('phone_error').innerHTML="** Mobile Number Must Have 10 Digits **"
        document.getElementById('phone_error').style.color="red"
        document.getElementById('phone_error').style.display="block"
    }

    if(phone.length == 10){
        document.getElementById('phonenumber').style.borderColor="green"
        document.getElementById('phone_error').innerHTML="** You Entered A Perfect Mobile Number **"
        document.getElementById('phone_error').style.color="green"
        document.getElementById('phone_error').style.display="block" 
    }

    if(phone.length == 11){
        document.getElementById('phonenumber').style.borderColor="red"
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

function passwordvalid(){
    var pass = document.getElementById('password').value
    if(pass.length <= 8){
        document.getElementById('password').style.borderColor="red"
        document.getElementById('password_error').innerHTML="** Password Must Have 8 Characters **"
        document.getElementById('password_error').style.color="red"
        document.getElementById('password_error').style.display="block" 
    }

    if(pass.length == 8){
        document.getElementById('password').style.borderColor="green"
        document.getElementById('password_error').innerHTML="** You Entered A Perfect Password **"
        document.getElementById('password_error').style.color="green"
        document.getElementById('password_error').style.display="block"
    }

    if(pass.length == 9){
        document.getElementById('password').style.borderColor="red"
        document.getElementById('password_error').innerHTML="** Password Must Have 8 Characters **"
        document.getElementById('password_error').style.color="red"
        document.getElementById('password_error').style.display="block" 
    }

}

function confirmpassvalid(){
    var pass = document.getElementById('password').value
    var cpass = document.getElementById('cpassword').value
    if(cpass.length <= 8){
        document.getElementById('cpassword').style.borderColor="red"
        document.getElementById('cpassword_error').innerHTML="** Confirm Password Must Have 8 Characters **"
        document.getElementById('cpassword_error').style.color="red"
        document.getElementById('cpassword_error').style.display="block" 
    }

    if(cpass.length == 8){
        document.getElementById('cpassword').style.borderColor="green"
        document.getElementById('cpassword_error').innerHTML="** You Entered A Perfect Confirm Password **"
        document.getElementById('cpassword_error').style.color="green"
        document.getElementById('cpassword_error').style.display="block"
    }

    if(cpass.length == 9){
        document.getElementById('cpassword').style.borderColor="red"
        document.getElementById('cpassword_error').innerHTML="** Confirm Password Must Have 8 Characters **"
        document.getElementById('cpassword_error').style.color="red"
        document.getElementById('cpassword_error').style.display="block" 
    }   

    if(pass != cpass){
        document.getElementById('cpassword').style.borderColor="red"
        document.getElementById('cpassword_error').innerHTML="** Password And Confirm Password Must Be Same **"
        document.getElementById('cpassword_error').style.color="red"
        document.getElementById('cpassword_error').style.display="block"   
    }

}

