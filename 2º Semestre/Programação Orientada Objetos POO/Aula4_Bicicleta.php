<?php

// Bicicleta

class Bicicleta{
    public string $marca;
    public string $modelo;
    public  string $cor;

    public function __construct(string $marca, string $modelo, string $cor){
      $this -> marca = $marca;
      $this -> modelo = $modelo;
      $this -> cor = $cor;
    }
    public function pedalar(): string {
      return "Pedalando bicicleta {$this -> marca} {$this -> modelo} {$this -> cor} está pedalando </br>";
    }
}

// Objeto da minha classe

$caloi01 = new Bicicleta ('caloi01', 'mk120', 'azul');
$steel = new Bicicleta ('SteelLegend', 'VL420', 'preto');
echo $caloi01 -> pedalar();
echo $steel -> pedalar();

