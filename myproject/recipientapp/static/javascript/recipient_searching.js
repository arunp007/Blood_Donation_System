function search(){
    var blood = document.getElementById('bloodgroup')
    var location = document.getElementById('location')

    if(blood.value == 'A+' && location.value == 'Karuvarakundu'){
        window.open("https://blooddonationsystem1.herokuapp.com/recipientapp/donors_details")
    }

    if(blood.value == 'A-' && location.value == 'Karuvarakundu'){
        window.open("https://blooddonationsystem1.herokuapp.com/recipientapp/donors_details")
    }

    if(blood.value == 'B+' && location.value == 'Karuvarakundu'){
        window.open("https://blooddonationsystem1.herokuapp.com/recipientapp/donors_details")
    }

    if(blood.value == 'B-' && location.value == 'Karuvarakundu'){
        window.open("https://blooddonationsystem1.herokuapp.com/recipientapp/donors_details")
    }

    if(blood.value == 'O+' && location.value == 'Karuvarakundu'){
        window.open("https://blooddonationsystem1.herokuapp.com/recipientapp/donors_details")
    }

    if(blood.value == 'O-' && location.value == 'Karuvarakundu'){
        window.open("https://blooddonationsystem1.herokuapp.com/recipientapp/donors_details")
    }

    if(blood.value == 'AB+' && location.value == 'Karuvarakundu'){
        window.open("https://blooddonationsystem1.herokuapp.com/recipientapp/donors_details")
    }
    
}