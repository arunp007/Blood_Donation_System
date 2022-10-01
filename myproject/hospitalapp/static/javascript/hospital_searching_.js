function search(){
    var blood = document.getElementById('bloodgroup')
    var location = document.getElementById('location')

    if(blood.value == 'A+' && location.value == 'Karuvarakundu'){
        window.open("https://blooddonationsystem1.herokuapp.com/hospitalapp/kvk_aplus")
    }

    if(blood.value == 'A-' && location.value == 'Karuvarakundu'){
        window.open("https://blooddonationsystem1.herokuapp.com/hospitalapp/kvk_aminus")
    }

    if(blood.value == 'B+' && location.value == 'Karuvarakundu'){
        window.open("https://blooddonationsystem1.herokuapp.com/hospitalapp/kvk_bplus")
    }

    if(blood.value == 'B-' && location.value == 'Karuvarakundu'){
        window.open("https://blooddonationsystem1.herokuapp.com/hospitalapp/kvk_bminus")
    }

    if(blood.value == 'O+' && location.value == 'Karuvarakundu'){
        window.open("https://blooddonationsystem1.herokuapp.com/hospitalapp/kvk_oplus")
    }

    if(blood.value == 'O-' && location.value == 'Karuvarakundu'){
        window.open("https://blooddonationsystem1.herokuapp.com/hospitalapp/kvk_ominus")
    }

    if(blood.value == 'AB+' && location.value == 'Karuvarakundu'){
        window.open("https://blooddonationsystem1.herokuapp.com/hospitalapp/kvk_abplus")
    }

    if(blood.value == 'AB-' && location.value == 'Karuvarakundu'){
        document.getElementById('table_error').innerHTML="No Data Founded"
        return false
    }

    if(blood.value == 'A+' && location.value == 'Manjeri'){
        window.open("https://blooddonationsystem1.herokuapp.com/hospitalapp/manjeri_aplus")
    }

    if(blood.value == 'A-' && location.value == 'Manjeri'){
        window.open("https://blooddonationsystem1.herokuapp.com/hospitalapp/manjeri_aminus")
    }

    if(blood.value == 'B+' && location.value == 'Manjeri'){
        window.open("https://blooddonationsystem1.herokuapp.com/hospitalapp/manjeri_bplus")
    }

    if(blood.value == 'B-' && location.value == 'Manjeri'){
        window.open("https://blooddonationsystem1.herokuapp.com/hospitalapp/manjeri_bminus")
    }

    if(blood.value == 'O+' && location.value == 'Manjeri'){
        window.open("https://blooddonationsystem1.herokuapp.com/hospitalapp/manjeri_oplus")
    }

    if(blood.value == 'O-' && location.value == 'Manjeri'){
        window.open("https://blooddonationsystem1.herokuapp.com/hospitalapp/manjeri_ominus")
    }

    if(blood.value == 'AB+' && location.value == 'Manjeri'){
        window.open("https://blooddonationsystem1.herokuapp.com/hospitalapp/manjeri_abplus")
    }

    if(blood.value == 'AB-' && location.value == 'Manjeri'){
        window.open("https://blooddonationsystem1.herokuapp.com/hospitalapp/manjeri_abminus")
    }
    
}