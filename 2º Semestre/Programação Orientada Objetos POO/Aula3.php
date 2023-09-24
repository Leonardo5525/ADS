<?php

function total_Computers($f, $c){
    return $f * $c;
}

function valor_total($fileiras, $colunas){
    $valor = 3000;
    return Total_Computers($fileiras, $colunas) * $valor;
}


$fileiras = 7;
$colunas = 5;


$custo = valor_total($fileiras, $colunas);

echo "O preço total da sala é de R$ {$custo}";