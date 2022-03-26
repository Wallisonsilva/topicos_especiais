function numeros1A10() {
    limparTela();
    for (let i = 0; i <= 10; i ++) {
        let para = document.createElement('p');
        para.textContent = i;
        document.body.appendChild(para);
    }
}
    
function mostrarInfosSonarJenkins() {
    return "infos.html";
}

function botaoVoltar() {
    return "index.html";
}


function mostrarTextoDebitoTecnico() {
    limparTela();
    let para = document.createElement('p');
    para.textContent = "O débito técnico no desenvolvimento de produtos acontece quando tomamos decisões priorizando\
                        a velocidade da implementação em detrimento de escolhas arquiteturais que resolvam o problema\
                        por completo. Geralmente é resultado da implementação de correções rápidas e momentâneas, sem\
                        considerar uma solução mais adequada para o longo prazo. O débito técnico possui dois fatores\
                        que impactam diretamente o negócio: custo e risco.";
    document.body.appendChild(para)
}

function limparTela() {
    const pTag = document.querySelectorAll('p');
    pTag.forEach(function(p) {
      p.innerHTML = "";
    }); 
}
