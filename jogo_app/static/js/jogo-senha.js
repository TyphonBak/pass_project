console.log('Jogo-Senha JS')
function onSignIn(googleUser) {
    var profile = googleUser.getBasicProfile();
    var user = {
        "token": googleUser.getAuthResponse().id_token,
        "nome": profile.getName(),
        "email": profile.getEmail()
    }
    $.post('http://localhost:5000/authroute', data=JSON.stringify({'usuario': user}));
}
