# ADR-0002 — Camada de dados SQL-first

## Status

**ACEITO para a direção SQL-first.** PostgreSQL é a escolha padrão para o banco relacional central. A hospedagem/provedor gerenciado (incluindo a possibilidade de Supabase) e a adoção de SQLite local ainda precisam de protótipo e decisão operacional própria.

## Contexto

O Cosmos precisa persistir dados estruturados de vários módulos, com relações, integridade, transações, histórico e consultas auditáveis. O Baluarte contém integrações e modelos de dados que não devem ser adotados sem reconciliação.

## Decisão

1. O Cosmos terá banco de dados relacional com SQL.
2. PostgreSQL será o alvo canônico do modelo central e das migrações SQL.
3. A UI não conectará ao PostgreSQL com credenciais privilegiadas; o acesso ocorrerá por API/serviços autorizados.
4. Rust e Python usarão os mesmos contratos de domínio e limites de acesso, sem duplicar regras de autorização.
5. SQLite só será introduzido para um requisito local/offline concreto, com estratégia explícita de sincronização e sem fonte de verdade concorrente.
6. Dados estruturados ficam no banco; arquivos grandes, modelos e mídia ficam em object storage/CDN quando apropriado, com metadados e checksums no SQL.
7. O esquema evolui por migrações versionadas e testes, não por alterações manuais invisíveis.

## Alternativas consideradas

- **Guardar tudo em JSON/localStorage:** rejeitado como persistência principal; não oferece a integridade relacional e as transações necessárias ao produto.
- **Banco NoSQL como única fonte de verdade:** não escolhido como padrão, porque as relações e invariantes centrais se beneficiam do modelo relacional.
- **PostgreSQL gerenciado (por exemplo, Supabase):** candidato forte para serviço gerenciado, mas a seleção final exige avaliar autenticação, RLS, custo, backups, ambientes e portabilidade.
- **PostgreSQL + SQLite para offline:** possível evolução, não requisito para a primeira fundação.
- **Reutilizar diretamente o banco do Baluarte:** rejeitado sem inventário, reconciliação, autorização explícita e plano de migração.

## Consequências

- A fundação deverá incluir camada de repositórios, migrações SQL, fixtures e testes de integração.
- Identidade, tenants/workspaces, sessões do J.A.R.V.I.S., projetos, skills, proveniência de datasets e auditoria precisam de modelagem por domínio.
- Não criar dezenas de tabelas especulativas antes de confirmar consumidores e fluxos.
- Um eventual banco local deve ter sincronização, resolução de conflitos e proteção de dados documentadas.
- A camada SQL não substitui validação na API, autorização, backups nem testes de segurança.

## Condições antes da produção

- Definir ambientes local/teste/staging/produção e gestão de segredos.
- Validar migrações num banco vazio e em atualização.
- Testar permissões, isolamento de dados, constraints, transações e falhas de conexão.
- Se Supabase for adotado, revisar RLS e funções expostas tabela por tabela.
- Realizar exercício de backup/restauração e registrar RPO/RTO medidos.

## Referências

- [Estratégia de Banco de Dados](../../data/DATABASE_STRATEGY.md)
- [Technology Decision](../../architecture/TECHNOLOGY_DECISION.md)
- [Security Architecture](../../security/SECURITY_ARCHITECTURE.md)
- [Data Flow](../../architecture/DATA_FLOW.md)
