function validation(){
    var status = 1
    var hname = document.getElementById('hospital')
    var address = document.getElementById('address')
    var place = document.getElementById('location')
    var file = document.getElementById('file')
    var state = document.getElementById('state')
    var district = document.getElementById('district')     
    var pin =  document.getElementById('pincode')
    var phone = document.getElementById('phone')
    var email = document.getElementById('emailid')
    var pass = document.getElementById('password')
    var cpass = document.getElementById('cpassword')
    var auth = document.getElementById('auth')


    if(hname.value == ""){
        document.getElementById('hospital').style.borderColor="red"
        document.getElementById('hospital_error').innerHTML="** Please Enter Hospital Name **"
        document.getElementById('hospital_error').style.color="red"
        document.getElementById('hospital_error').style.display="block"
        var status = 0
    }

    else{
        document.getElementById('hospital').style.borderColor="black"
        document.getElementById('hospital_error').style.display="none"
        var status = 1
    }

    if(address.value == ""){
        document.getElementById('address').style.borderColor="red"
        document.getElementById('address_error').innerHTML="** Please Enter Your Permanent Address **"
        document.getElementById('address_error').style.color="red"
        document.getElementById('address_error').style.display="block"
        var status = 0
    }

    else{
        document.getElementById('address').style.borderColor="black"
        document.getElementById('address_error').style.display="none"
        var status = 1
    }

    if(place.value == ""){
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

    if(file.value == ""){
        document.getElementById('file').style.borderColor="red"
        document.getElementById('file_error').innerHTML="** Please Upload File **"
        document.getElementById('file_error').style.color="red"
        document.getElementById('file_error').style.display="block"
        var status = 0
    }

    else{
        document.getElementById('file').style.borderColor="black"
        document.getElementById('file_error').style.display="none"
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

    if(auth.value == ""){
        document.getElementById('auth').style.borderColor="red"
        document.getElementById('auth_error').innerHTML="** Please Enter Your Authenticaton **"
        document.getElementById('auth_error').style.color="red"
        document.getElementById('auth_error').style.display="block"
        var status = 0
    }

    if(auth.checked){
        document.getElementById('auth').style.borderColor="black"
        document.getElementById('auth_error').style.display="none"
        var status = 0
    }


    if(status == 0){
        return false
    }

    if(status == 1){
        return true
    }
}

function hospitalvalid(){
        var hospital = document.getElementById('hospital').value

    if(isNaN(hospital)){
      document.getElementById('hospital').style.borderColor="black"
      document.getElementById('hospital_error').style.display="none" 
    }
   
   else{
      document.getElementById('hospital').style.borderColor="red"
      document.getElementById('hospital_error').innerHTML="** Please Enter A Valid Hospital Name **"
      document.getElementById('hospital_error').style.color="red"
      document.getElementById('hospital_error').style.display="block"
    }

            
}

function locationvalid(){
    var location = document.getElementById('location').value
    if(isNaN(location)){
      document.getElementById('location').style.borderColor="black"
      document.getElementById('location_error').style.display="none" 
    }
   
   else{
      document.getElementById('location').style.borderColor="red"
      document.getElementById('location_error').innerHTML="** Please Enter A Valid Location **"
      document.getElementById('location_error').style.color="red"
      document.getElementById('location_error').style.display="block"
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
    var phone = document.getElementById('phone').value
    if(isNaN(phone)){
        document.getElementById('phone').style.borderColor="red"
        document.getElementById('phone_error').innerHTML="** Please Enter A Valid Mobile Number **"
        document.getElementById('phone_error').style.color="red"
        document.getElementById('phone_error').style.display="block"
    }

    if(phone.length <= 0){
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