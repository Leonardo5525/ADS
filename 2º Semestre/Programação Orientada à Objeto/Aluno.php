<?php

class Aluno {
    public string $nome;
    public string $curso;
    public string $disciplina;
    public bool $presente;
    
    public function __construct(string $nome, string $disciplina, string $curso, bool $presente = false) {
        $this->nome = $nome;
        $this->disciplina = $disciplina;
        $this->curso = $curso;
        $this->presente = $presente;
    }
}

$alunos = array(
    new Aluno("Ronaldo", "poo", "ads", true),
    new Aluno("Fernando", "poo", "ads", false),
    new Aluno("Silva", "poo", "ads", true),
    new Aluno("Lucas", "poo", "ads", true),
    new Aluno("Reginaldo", "poo", "ads", false),
);

$totalPresentes = 0;
$totalFaltantes = 0;


foreach ($alunos as $value) {
    if ($value->presente) {
        $totalPresentes += 1;
        echo "{$value->nome}: Presente</br>";
    }else{
        $totalFaltantes += 1;
        echo "{$value->nome}: Faltou</br>";
    }
}

echo "Total de alunos presente: {$totalPresentes}</br>";
echo "Total de alunos que faltaram: {$totalFaltantes}";