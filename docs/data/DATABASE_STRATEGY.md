# Estratégia de Banco de Dados do Cosmos

## Decisão de produto

O Cosmos terá banco de dados relacional com SQL. A direção padrão é **PostgreSQL como banco central de referência** para dados persistentes e relacionais. Supabase é uma opção de hospedagem/serviços sobre PostgreSQL, não uma justificativa para reutilizar automaticamente o projeto, as tabelas ou as políticas do Baluarte.

SQLite pode ser adotado para um modo local/offline, cache persistente ou protótipo desktop, desde que tenha fronteira explícita e sincronização definida. Ele não deve criar uma segunda fonte de verdade silenciosa.

## Por que SQL

- Relações explícitas entre entidades, com chaves primárias e estrangeiras.
- Constraints para integridade, UNIQUE, NOT NULL e validação no banco.
- Transações para operações que precisam ser atômicas.
- Consultas e relatórios auditáveis.
- Migrações versionadas e testes de schema.
- Base adequada para identidade, projetos, sessões, preferências e histórico estruturado.

JSON pode continuar sendo usado para payloads, configurações e snapshots limitados; não substituirá relações centrais por grandes blobs sem uma justificativa documentada.

## Arquitetura de acesso

    TypeScript UI
        ↓ contratos tipados / HTTP API
    API e serviços Cosmos (TypeScript ou Rust, conforme ADR)
        ↓ camada de repositórios / queries parametrizadas
    PostgreSQL
        ├── constraints / índices / transações
        ├── migrações versionadas
        └── auditoria e políticas de acesso
    Python AI / agentes ── API/contrato autorizado ──┘
    Runtime Rust local ─── API/contrato autorizado ──┘

A interface do navegador não recebe credenciais privilegiadas nem conecta diretamente ao banco com segredo de serviço. Python e Rust também não devem contornar autenticação, autorização ou regras de domínio: os acessos devem passar por contratos explícitos.

## Domínios candidatos ao modelo relacional

| Domínio | Dados candidatos | Regra |
|---|---|---|
| Identidade e preferências | referências do usuário, preferências, configurações | Não armazenar senhas em texto; identidade pode delegar autenticação a um provedor. |
| Projetos e repositórios | projetos registrados, links, metadados, execuções de diagnóstico | Não guardar tokens de acesso em linhas comuns nem em logs. |
| J.A.R.V.I.S. | sessões, mensagens, metadados de memória, execuções de ferramentas | Definir retenção, exclusão e limites de tamanho antes de ativar persistência. |
| Skills e automações | definição versionada, permissões, execução, resultado e auditoria | Nunca executar conteúdo não confiável apenas porque foi gravado no banco. |
| Datasets | catálogo, schema, origem, versão, checksum, licença e consumidor | O binário grande permanece em object storage quando apropriado; SQL mantém metadados. |
| Assets | manifesto, hash, licença, URI, tamanho e consumidores | Evitar guardar arquivos pesados como blobs sem requisito explícito. |
| Operação | eventos de auditoria, jobs, estado de migração | Retenção e acesso devem ser definidos por tipo de evento. |

Esta lista é um modelo conceitual, não autorização para criar todas as tabelas de uma vez. Cada domínio precisa de consumidor confirmado, contrato, classificação de sensibilidade e testes.

## Migrações SQL

- Manter migrações em database/migrations/, numeradas e imutáveis após aplicação compartilhada.
- Cada migração deve ter objetivo, pré-condições, efeito, plano de recuperação e teste.
- Nunca editar uma migração já aplicada em ambiente compartilhado; criar uma nova migração corretiva.
- Testar desde um banco vazio e também a atualização de um schema anterior suportado.
- Não executar migrações destrutivas automaticamente em produção.
- Usar dados sintéticos em fixtures; nunca exportar dados pessoais, credenciais ou tokens reais.
- Seeds devem ser determinísticos, idempotentes quando possível e separados dos dados do usuário.

## Segurança obrigatória

- Queries parametrizadas; nunca concatenar input do usuário em SQL.
- Privilégio mínimo para cada usuário/serviço de banco.
- Autenticação e autorização no servidor, com isolamento por usuário/tenant quando aplicável.
- Se Supabase for escolhido, revisar RLS por tabela, operações e funções expostas; RLS habilitado sozinho não prova política correta.
- Segredos em variáveis de ambiente/secret manager, fora do Git e fora do frontend.
- Logs sem senhas, tokens, conteúdo privado desnecessário ou strings SQL contendo dados sensíveis.
- Backups criptografados, política de retenção, teste de restauração e métricas RPO/RTO antes de declarar recuperação estável.

## Critérios para marcar a camada de dados como estável

- [ ] Provedor e ambientes registrados num ADR.
- [ ] Modelo e relações aprovados por domínio.
- [ ] Migrações reproduzíveis do zero.
- [ ] Testes de constraints, transações, autorização e isolamento.
- [ ] Testes de query parametrizada e tratamento de falhas.
- [ ] Backup e restauração testados.
- [ ] Política de exclusão, retenção e exportação documentada.
- [ ] Nenhuma credencial privilegiada enviada ao cliente.

## Relação com o Baluarte

O Baluarte é referência para requisitos, comportamentos e possíveis entidades. Não copiar automaticamente tabelas, credenciais, sessões, policies ou dados. Qualquer esquema legado encontrado deve ser reconciliado com consumidores e contratos do Cosmos antes de propor migração.
