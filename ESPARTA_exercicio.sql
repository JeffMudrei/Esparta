-- Buscar os nomes de todos os alunos que frequentam alguma turma do professor 'JOAO PEDRO'.
SELECT aluno.nome 
FROM TURMA 
INNER JOIN aluno ON aluno.id = turma.aluno_id 
INNER JOIN professor on professor.id = turma.professor_id
where professor.nome = 'JOAO PEDRO'

-- Buscar os dias da semana que tenham aulas da disciplina 'MATEMATICA'.
select turma.dia_da_semana
from turma 
inner join disciplina on disciplina.id = turma.disciplina_id
where disciplina.nome = 'MATEMATICA'

-- Buscar todos os alunos que frequentem aulas de 'MATEMATICA' e também 'FISICA'.
select aluno.nome from turma 
inner join disciplina on disciplina.id = turma.disciplina_id
inner join aluno on aluno.id = turma.aluno_id
where disciplina.nome = 'FISICA' OR disciplina.nome = 'MATEMATICA'

-- Buscar as disciplinas que não tenham nenhuma turma.
SELECT disciplina.nome from disciplina
left join turma on disciplina.id = turma.disciplina_id
where turma.disciplina_id is null

-- Buscar os alunos que frequentem aulas de 'MATEMATICA' exceto os que frequentem 'QUIMICA'.
select aluno.nome from turma 
inner join disciplina on disciplina.id = turma.disciplina_id
inner join aluno on aluno.id = turma.aluno_id
where disciplina.nome = 'MATEMATICA' AND disciplina.nome <> 'QUIMICA'