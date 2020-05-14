function gritar(){
    alert("BÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃÃO!");
}

function perguntar(){
    var nome;
    nome = prompt("Qual é o seu nome?");
    alert("Olá "+nome);
}

function mudar_texto(){
    var h1 = document.getElementsByTagName("h1");
    if(h1[0].innerText == "Opa, bão? Maravilha."){
        h1[0].innerText = "Evolua seu lado BÃO!"
    } else {
        h1[0].innerText = "Opa, bão? Maravilha."
    }
    
}

function incrementar(){
    var num = document.getElementById("p1");
    num.innerText = parseInt(num.innerText) + 1;
}