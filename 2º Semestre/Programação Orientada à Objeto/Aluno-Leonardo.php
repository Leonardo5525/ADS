<?php
class Aluno {
    public string $nome;
    public bool $estaPresente;

    public function __construct(string $nome, bool $estaPresente = false) {
        $this->nome = $nome;
        $this->estaPresente = $estaPresente;
    }
}

$alunos = [
    new Aluno("Leonardo", true),
    new Aluno("Vitória", false),
    new Aluno("Vitor", false),
    new Aluno("Lucas", true),
    new Aluno("William", true),
];

$totalPresentes = count(array_filter($alunos, fn($aluno) => $aluno->estaPresente));
$totalFaltantes = count($alunos) - $totalPresentes;

foreach ($alunos as $aluno) {
    $status = $aluno->estaPresente ? "Presente" : "Faltou";
    echo "{$aluno->nome}: {$status}<br>";
}

echo "Total de alunos presentes: {$totalPresentes}<br>";
echo "Total de alunos que faltaram: {$totalFaltantes}";
