function validation(){
    var status = 1
    var user = document.getElementById('username')
    var password = document.getElementById('password')

    if(user.value == ""){
      document.getElementById('username').style.borderColor="red"
      document.getElementById('user_error').innerHTML="** Please Enter Your Username **"
      document.getElementById('user_error').style.color="red"
      document.getElementById('user_error').style.display="block"
      var status = 0
    }

    else{
      document.getElementById('username').style.borderColor="black"
      document.getElementById('user_error').style.display="none"
      var status = 1
    }

    if(password.value == ""){
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
    
    if(status == 0){
      return false
    }

    if(status == 1){
      return true
    }

}

function uservalid(){
   var user = document.getElementById('username').value

   if(isNaN(user)){
      document.getElementById('username').style.borderColor="black"
      document.getElementById('user_error').style.display="none" 
   }
   
   else{
      document.getElementById('username').style.borderColor="red"
      document.getElementById('user_error').innerHTML="** Please Enter A Valid Username **"
      document.getElementById('user_error').style.color="red"
      document.getElementById('user_error').style.display="block"
   }

}

function passvalid(){
   var password = document.getElementById('password').value
   if(password.length <= 8){
     document.getElementById('password').style.borderColor="red"
     document.getElementById('password_error').innerHTML="** Password Must Contain 8 Characters **"
     document.getElementById('password_error').style.color="red"
     document.getElementById('password_error').style.display="block"
   }

   if(password.length == 8){
     document.getElementById('password').style.borderColor="green"
     document.getElementById('password_error').innerHTML="** You Entered Perfect Password **"
     document.getElementById('password_error').style.color="green"
     document.getElementById('password_error').style.display="block"
   }

   if(password.length == 9){
        document.getElementById('password').style.borderColor="red"
        document.getElementById('password_error').innerHTML="** Password Must Have 8 characters **"
        document.getElementById('password_error').style.color="red"
        document.getElementById('password_error').style.display="block" 
    }

}