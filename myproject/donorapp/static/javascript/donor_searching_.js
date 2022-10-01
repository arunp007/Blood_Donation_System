function search(){
    var blood = document.getElementById('bloodgroup')
    var location = document.getElementById('location')

    if(blood.value == 'A+' && location.value == 'Karuvarakundu'){
        window.open("https://blooddonationsystem1.herokuapp.com/donorapp/kvk_aplus")
    }

    if(blood.value == 'A-' && location.value == 'Karuvarakundu'){
        window.open("https://blooddonationsystem1.herokuapp.com/donorapp/kvk_aminus")
    }

    if(blood.value == 'B+' && location.value == 'Karuvarakundu'){
        window.open("https://blooddonationsystem1.herokuapp.com/donorapp/kvk_bplus")
    }

    if(blood.value == 'B-' && location.value == 'Karuvarakundu'){
        window.open("https://blooddonationsystem1.herokuapp.com/donorapp/kvk_bminus")
    }

    if(blood.value == 'O+' && location.value == 'Karuvarakundu'){
        window.open("https://blooddonationsystem1.herokuapp.com/donorapp/kvk_oplus")
    }

    if(blood.value == 'O-' && location.value == 'Karuvarakundu'){
        window.open("https://blooddonationsystem1.herokuapp.com/donorapp/kvk_ominus")
    }

    if(blood.value == 'AB+' && location.value == 'Karuvarakundu'){
        window.open("https://blooddonationsystem1.herokuapp.com/donorapp/kvk_abplus")
    }

    if(blood.value == 'AB-' && location.value == 'Karuvarakundu'){
        document.getElementById('table_error').innerHTML="No Data Founded"
        return false
    }

    if(blood.value == 'A+' && location.value == 'Manjeri'){
        window.open("https://blooddonationsystem1.herokuapp.com/donorapp/manjeri_aplus")
    }

    if(blood.value == 'A-' && location.value == 'Manjeri'){
        window.open("https://blooddonationsystem1.herokuapp.com/donorapp/manjeri_aminus")
    }

    if(blood.value == 'B+' && location.value == 'Manjeri'){
        window.open("https://blooddonationsystem1.herokuapp.com/donorapp/manjeri_bplus")
    }

    if(blood.value == 'B-' && location.value == 'Manjeri'){
        window.open("https://blooddonationsystem1.herokuapp.com/donorapp/manjeri_bminus")
    }

    if(blood.value == 'O+' && location.value == 'Manjeri'){
        window.open("https://blooddonationsystem1.herokuapp.com/donorapp/manjeri_oplus")
    }

    if(blood.value == 'O-' && location.value == 'Manjeri'){
        window.open("https://blooddonationsystem1.herokuapp.com/donorapp/manjeri_ominus")
    }

    if(blood.value == 'AB+' && location.value == 'Manjeri'){
        window.open("https://blooddonationsystem1.herokuapp.com/donorapp/manjeri_abplus")
    }

    if(blood.value == 'AB-' && location.value == 'Manjeri'){
        window.open("https://blooddonationsystem1.herokuapp.com/donorapp/manjeri_abminus")
    }
    
}