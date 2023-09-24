<?php

function total_Computers($f, $c){
    return $f * $c;
}

function valor_total($valor, $quantidade){
    return $valor * $quantidade;
}

$fileiras = 7;
$colunas = 5;
$valor = 3000;


$total =  total_Computers($fileiras, $colunas);
$custo = valor_total($valor, $total);

echo "O total de computadores na sala é de {$total} com um custo total de R$ ($custo)";