# Plano inicial do modelo relacional SQL

## Objetivo

Definir uma primeira fatia pequena e verificável para o banco do Cosmos. Este documento não é uma migração executável e não cria tabelas em nenhum ambiente.

## Princípios de modelagem

- Identificadores estáveis; timestamps UTC; constraints e índices guiados por consultas reais.
- Chaves estrangeiras para relações de propriedade e integridade.
- Separar dados de autenticação do perfil e das preferências da aplicação.
- Não confiar em um user_id enviado pelo cliente: derivar identidade da sessão validada no servidor.
- Planejar isolamento por usuário e possível tenant/workspace sem afirmar que multi-tenancy já está implementado.
- Dados privados devem ter políticas de leitura, alteração, exportação e exclusão.
- Conteúdo JSON só é aceitável quando flexibilidade/snapshot é intencional e há validação de schema.
- Tabelas de auditoria não devem ser editáveis por usuários comuns.

## Domínios e relações candidatas

    identity provider
        └── app_users
              ├── user_preferences
              ├── projects
              │     └── repository_scans
              ├── jarvis_sessions
              │     └── jarvis_messages
              ├── skills
              │     └── skill_runs
              └── audit_events

    datasets
        └── dataset_versions
              └── provenance / checksums

O diagrama é conceitual. A estrutura final deve ser normalizada a partir dos casos de uso e dos contratos de módulo.

## Ordem recomendada de implementação

### Fase DB-0 — Escolha operacional
- Confirmar PostgreSQL local em desenvolvimento/teste e destino gerenciado.
- Escolher driver/migração e definir comandos reproduzíveis.
- Definir ambientes, secrets, pool/limites de conexão e estratégia de backup.
- Registrar decisão de provedor e compatibilidade com deploy.

### Fase DB-1 — Fundação mínima
- Migração inicial de schema e mecanismo de migração.
- Health check sem revelar credenciais.
- Teste de conexão e rollback de transação.
- CI executando testes com banco efêmero.

### Fase DB-2 — Identidade e preferências
- Perfil da aplicação referenciado por identidade validada.
- Preferências tipadas, timestamps e controle de versão.
- Testes de autorização cruzada: um usuário não lê nem altera dados de outro.

### Fase DB-3 — Projetos e diagnóstico
- Projetos registrados pelo usuário.
- Metadados de repositório sem tokens privados.
- Execuções de diagnóstico com status, timestamps e resumo redigido de segredos.

### Fase DB-4 — J.A.R.V.I.S.
- Sessões e mensagens com ordenação determinística.
- Política de retenção, exclusão e exportação.
- Memória derivada separada da conversa original, com proveniência e opção de remoção.
- Limites de tamanho e testes para concorrência.

### Fase DB-5 — Catálogos e proveniência
- Catálogo de datasets, versões, checksums, fontes, licença e consumidores.
- Não armazenar grandes assets binários no banco por padrão.
- Validar origem e checksum antes de publicar uma versão de dataset.

### Fase DB-6 — Skills, jobs e auditoria
- Definição/versionamento de skills, permissões concedidas e execuções.
- Auditoria de ações sensíveis com campos mínimos e retenção definida.
- Execuções não confiáveis ficam em sandbox; persistir metadados não autoriza execução.

## Migrações

Local proposto: database/migrations/. Nome sugerido: 0001_create_initial_metadata.sql, mas o arquivo só deve ser criado após o provedor e as tabelas da primeira fatia serem aprovados.

Cada migração deve conter apenas mudanças coesas. Para alterações de alto risco, preferir expandir → migrar dados → validar → contrair em versões separadas.

## Testes mínimos

- Criar schema vazio e aplicar todas as migrações.
- Verificar chaves estrangeiras, unicidade e campos obrigatórios.
- Confirmar rollback em erro de transação.
- Confirmar queries parametrizadas com inputs contendo aspas e caracteres especiais.
- Testar acesso negado entre usuários e papéis.
- Confirmar exportação/remoção de dados pessoais.
- Testar backup e restauração em ambiente isolado.
- Verificar que falha de banco não expõe query, token ou dados privados na resposta.

## Gate para iniciar código

A primeira migração SQL só deve ser criada quando DB-0 e o escopo de DB-1 estiverem definidos. Não aplicar alterações em bancos legados nem em produção como parte desta fase documental.
