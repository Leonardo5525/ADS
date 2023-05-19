let dados = {};
(async () => {
    dados = await fetch('produtos.json').then(response => {
        return response.json();
    }).catch(err => {
        const app = document.querySelector('#lista-produtos');
        app.innerHTML +=
        `<div class="">
            <p>Infelizmente não foi possível mostrar os produtos!</p>
        </div>`
    });
    produtos = dados.produtos.filter(p => p.ativo == true);
    let listaProdutos = document.getElementById("lista-produtos");
    for(let p of produtos){
        listaProdutos.innerHTML += `<div class="col-4">
                                        <div class="card">
                                        <img src="${p.img}" class="card-img-top" alt="...">
                                        <div class="card-body">
                                            <h5 class="card-title">${p.nome}</h5>
                                            <p class="card-text">R$${p.preco}</p>
                                            <a href="${p.link}" target="_blank" class="btn btn-primary">Detalhes</a>
                                        </div>
                                        </div>
                                    </div>`;
    }
})();