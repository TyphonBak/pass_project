console.log('Jogo-Senha JS')
var criaAlerta = function(texto) {
    return `<div class="alert alert-danger alert-dismissible fade show" role="alert"> \
        <strong>Eita!</strong> ${texto} \
        <button type="button" class="close" data-dismiss="alert" aria-label="Close"> \
            <span aria-hidden="true">&times;</span> \
        </button> \
    </div>`
};

var criaModal = function(dados) {
    let cabecalho;
    let corpo;
    if (dados.titulo) {
        cabecalho = `
        <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">Well Done!</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
            </button>
        </div>`
    }
    if (dados.texto) {
        corpo = `
        <div class="modal-body">
            
        </div>`
    }
    modal = `
    <div class="modal fade" id="${dados.nome}" tabindex="-1" role="dialog" aria-labelledby="${dados.nome}Label" aria-hidden="true">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
                ${cabecalho}
                ${corpo}
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-primary">Save changes</button>
                </div>
            </div>
        </div>
    </div>`;
    return modal
};

var jogoForm = document.getElementById("jogoForm");
var socket;
socket = io.connect('http://' + document.domain + ':' + location.port + '/');

socket.on('retorna jogada', function(dados) {
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
});

socket.on('fim de jogo', function(dados) {
    console.log(dados);
    modal = `
    <div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLabel">Well Done!</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body">
                    ...
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-primary">Save changes</button>
                </div>
            </div>
        </div>
    </div>`;
    $('body').append(modal);
    $('#exampleModal').modal();
    console.log('Acabou o LOL !!!');
});

socket.on('emite alerta', function(dados) {
    $(criaAlerta(dados.msg)).appendTo("#entradaForm").hide().slideToggle(400, function(){
        setTimeout(function(){
            $('.alert').slideToggle().alert('close');
        }, 5000);
    });
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
