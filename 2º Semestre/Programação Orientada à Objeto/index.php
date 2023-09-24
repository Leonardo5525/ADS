<?php

echo 'Hello World! <br>';
echo 'Unimar - ADS 2023 <br>';

$idade = 20;

if ($idade >= 18){
    echo 'maior de idade <br>';
} else{
    echo 'menor de idade <br>';
}

$altura = 1.90;

if ($altura >= 2){
    echo 'muito alto <br>';
}   elseif ($altura >= 1.90){
    echo 'alto <br>';
}   elseif($altura >= 1.70){
    echo 'padrao <br>';
}   else{
    echo 'baixo';
}

$limite = 10;
$i = 0;

while ($i <= 10){
    echo "{$i} <br>";
    $i++;
}