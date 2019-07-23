console.log('Jogo-Senha JS')
var socket;
socket = io.connect('http://' + document.domain + ':' + location.port + '/');

var jogoForm = document.getElementById("jogoForm");

function onSignIn(googleUser) {
    var profile = googleUser.getBasicProfile();
    var user = {
        "token": googleUser.getAuthResponse().id_token,
        "nome": profile.getName(),
        "email": profile.getEmail()
    }
    $.post('http://localhost:5000/authroute', user);
}

socket.on('retorna jogada', function(dados) {
        numero = $('#tabela-chutes tr').length-1;
        linha = "<tr> \
            <td>" + numero + "</td> \
            <td>" + dados.chute + "</td> \
            <td>" + 'dados.qualidade[0]' + "</td> \
            <td>" + 'dados.qualidade[1]' + "</td> \
            <td>" + 'dados.qualidade[2]' + "</td> \
        </tr>"        
        $('#tabela-chutes tbody').prepend(linha);
    }
);

jogoForm.addEventListener("submit", function(ev){
    ev.preventDefault();
    dados = document.querySelectorAll('input');
    elementos = []
    dados.forEach(element => {
        elementos.push(element.value);
    });
    socket.emit('jogada', {'chute': elementos});
    console.log('Se chegou aqui... ', elementos);
});