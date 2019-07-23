console.log('Jogo-Senha JS')
var jogoForm = document.getElementById("jogoForm");
var socket;
socket = io.connect('http://' + document.domain + ':' + location.port + '/');

socket.on('retorna jogada', function(dados) {
    console.log('Dados recebidos', dados)
    numero = $('#tabela-chutes tr').length-1;
    linha = "<tr> \
    <td>" + numero + "</td> \
    <td>" + dados.chute.toString().replace(/\,/g,'') + "</td> \
    <td>" + dados.qualidade[0] + "</td> \
    <td>" + dados.qualidade[1] + "</td> \
    <td>" + dados.qualidade[2] + "</td> \
    </tr>"        
    $('#tabela-chutes tbody').prepend(linha);
});

$("#criajogo").on("click", function(ev){
    socket.emit('novo jogo');
});

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


function onSignIn(googleUser) {
    var profile = googleUser.getBasicProfile();
    var user = {
        "token": googleUser.getAuthResponse().id_token,
        "nome": profile.getName(),
        "email": profile.getEmail()
    }
    $.post('http://localhost:5000/authroute', user);
}
