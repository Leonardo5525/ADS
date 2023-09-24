<?php

class Aluno {
    public string $nome;
    public string $disciplina;
    public string $curso;
    public bool $estaPresente;
    
    public function __construct(string $nome, string $disciplina, string $curso, bool $estaPresente = false) {
        $this->nome = $nome;
        $this->disciplina = $disciplina;
        $this->curso = $curso;
        $this->estaPresente = $estaPresente;
    }
}

$aluno1 = new Aluno("Ronaldo", "Programação Orientada a Objetos", "Análise e Desenvolvimento de Sistemas", true);
$aluno2 = new Aluno("Fernando", "Programação Orientada a Objetos", "Análise e Desenvolvimento de Sistemas", false);
$aluno3 = new Aluno("Silva", "Programação Orientada a Objetos", "Análise e Desenvolvimento de Sistemas", false);
$aluno4 = new Aluno("Lucas", "Programação Orientada a Objetos", "Análise e Desenvolvimento de Sistemas", true);
$aluno5 = new Aluno("Reginaldo", "Programação Orientada a Objetos", "Análise e Desenvolvimento de Sistemas", true);

$alunos = array($aluno1, $aluno2, $aluno3, $aluno4, $aluno5);

$totalPresentes = 0;
$totalFaltantes = 0;
$numeroAlunos = count($alunos);

for ($i = 0; $i < $numeroAlunos; $i++) {
    $aluno = $alunos[$i];
    
    if ($aluno->estaPresente) {
        $totalPresentes += 1;
        echo "{$aluno->nome}: Presente</br>";
    } else {
        $totalFaltantes += 1;
        echo "{$aluno->nome}: Faltou</br>";
    }
}

echo "Total de alunos presentes: {$totalPresentes}<br>";
echo "Total de alunos que faltaram: {$totalFaltantes}";
?>
 