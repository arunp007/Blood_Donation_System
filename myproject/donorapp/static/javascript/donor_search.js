function validation(){
    var status = 1
    var blood = document.getElementById('bloodgroup')
    var location = document.getElementById('location')

    if(blood.value == ""){
      document.getElementById('bloodgroup').style.borderColor="red"
      document.getElementById('blood_error').innerHTML="** Please Select Your Blood Group **"
      document.getElementById('blood_error').style.color="red"
      document.getElementById('blood_error').style.display="block"
      var status = 0
    }

    else{
      document.getElementById('bloodgroup').style.borderColor="black"
      document.getElementById('blood_error').style.display="none"
      var status = 1
    }

    if(location.value == ""){
      document.getElementById('location').style.borderColor="red"
      document.getElementById('location_error').innerHTML="** Please Select Your Location **"
      document.getElementById('location_error').style.color="red"
      document.getElementById('location_error').style.display="block"
      var status = 0
    }

    else{
      document.getElementById('location').style.borderColor="black"
      document.getElementById('location_error').style.display="none"
      var status = 1
    }

    if(status == 1){
      return true
    }
    
    if(status == 0){
      return false
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