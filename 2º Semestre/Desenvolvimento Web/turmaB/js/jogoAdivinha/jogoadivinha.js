document.addEventListener("DOMContentLoaded",()=>{

    function sorteio(){
        let max=10;
        let s=Math.floor(Math.random()*max)+1;
        return s;
    }

    let n=sorteio();
    let btnTentar=document.querySelector("#btnTentar");
    let tentativas=document.querySelector("#lbltentativas");
    btnTentar.addEventListener("click",()=>{
        let palpite=document.querySelector("#num").value;
        res="";
        if(n==palpite){
            res="Você acertou!";
        }
        else if(palpite>n){
            res="Chutou alto!";
            tentativas.innerHTML--;
            if(tentativas.innerHTML<=0){
                btnTentar.disabled=true;
            }
        }
        else{
            res="Chutou baixo!";
            tentativas.innerHTML--;
            if(tentativas.innerHTML<=0){
                btnTentar.disabled=true;
            }
        }
        let resultado=document.querySelector("#resultado");
        resultado.innerHTML=res;
        
    });
    let btnReiniciar=document.querySelector("#btnReiniciar");
    btnReiniciar.addEventListener("click",()=>{
        tentativas.innerHTML=3;
        n=sorteio();
        btnTentar.disabled=false;
        resultado.innerHTML="";
    })

});