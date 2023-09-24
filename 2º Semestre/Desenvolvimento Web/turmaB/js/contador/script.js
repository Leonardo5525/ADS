document.addEventListener("DOMContentLoaded",()=>{
    let cont=document.querySelector("#lblcontador");
    let botaoInc=document.querySelector("#btnInc");
    botaoInc.addEventListener("click",()=>{
        cont.innerHTML++;
    });

   let botaoDec=document.querySelector("#btnDec");
   botaoDec.addEventListener("click",()=>{
        cont.innerHTML--;
        if(cont.innerHTML<0){
            cont.innerHTML=0;
        }
   });
});