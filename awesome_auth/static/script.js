function validateForm(data){
    var name = data.user_name.value;
    var password = data.password.value;
    var confirm_password = data.confirm_password.value;

    if(password == confirm_password && name.length != 0){
        return true
    }
    else{
        alert("Invalid Input")
        return false
    }
   
}

function validateSignIn(data){
    var name = data.user_name.value;
    var password = data.password.value;

    if(password.length != 0 && name.length != 0){
        return true
    }
    else{
        alert("Invalid Input")
        return false
    }
}