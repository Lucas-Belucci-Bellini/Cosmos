# System Boundaries

O browser renderiza UI e executa somente dados necessários à tela. APIs validam entrada e saída. Workers executam tarefas demoradas. Object storage mantém datasets e assets grandes. Git mantém código, docs, schemas e fixtures pequenos.

Credenciais não pertencem ao browser nem ao Git. Integrações externas não são importadas diretamente por componentes visuais. O Baluarte não é uma dependência de runtime.
