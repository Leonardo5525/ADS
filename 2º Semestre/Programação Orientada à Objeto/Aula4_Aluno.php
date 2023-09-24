<?php

// Alun0

class Aluno{
    public string $genero;
    public int $idade;
    public  string $cor;

    public function __construct(string $genero, int $idade, string $cor){
      $this -> genero = $genero;
      $this -> idade = $idade;
      $this -> cor = $cor;
    }
    public function pedalar(): string {
      return "Oi eu sou do genêro {$this -> genero} da {$this -> idade} e da cor {$this -> cor}";
    }
}

// Objeto da minha classe

$aluno1 = new Aluno ('masculino', '26', 'amarelo');
$aluno2 = new Aluno ('feminino', '25', 'branca');

