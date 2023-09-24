<?php

// Bicicleta

class Bike{
    public $marca;
    public $modelo;
    public $cor;

    public function pedalar(){
        echo "Bicicleta {$this -> marca} {$this -> modelo} {$this -> cor} está pedalando </br>";
    }
}

// Objeto da minha classe

$caloi01 = new Bike();
$caloi01 -> marca = 'caloi';
$caloi01 -> modelo = 'mk120';
$caloi01 -> cor = 'azul';
$caloi01 -> pedalar();

$steelLegend = new Bike();
$steelLegend -> marca = 'steel';
$steelLegend -> modelo = 'VL420';
$steelLegend -> cor = 'preto';
$steelLegend -> pedalar();

