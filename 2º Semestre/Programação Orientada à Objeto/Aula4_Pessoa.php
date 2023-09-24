<?php


class Pessoa{
    public string $nome;
    public int $peso;


    public function __construct(string $nome, int $peso){
      $this -> $nome = $nome;
      $this -> peso = $peso;
    }
    public function pedalar(): string {
      return "Oi eu sou o {$this -> nome} e peso {$this -> peso} kilos";
    }
}

$pessoa1 = new Pessoa ('Leo', '100');
$pessoa2 = new Pessoa ('Vi', '60');
