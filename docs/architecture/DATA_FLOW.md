# Data Flow

Dados entram por fonte documentada, passam por normalização e validação, recebem versão e checksum e só então são expostos por um loader de módulo. A UI consome contratos, não arquivos brutos.

```text
Source → Ingestion/Adapter → Validation → Versioned Dataset → Module Loader → UI
                              ↘ checksum / provenance / tests
```

Datasets grandes devem ser carregados sob demanda. Dados pessoais e estado de usuário devem seguir um fluxo separado, com autenticação, autorização, retenção e auditoria.


## Persistência relacional

Dados de aplicação que exigem relações, integridade ou transações são persistidos via API/serviços autorizados no PostgreSQL central. A UI não recebe credenciais privilegiadas e não conecta diretamente ao banco. Cada alteração de schema passa por migração versionada e testes de integração. Metadados de datasets/assets podem ficar no SQL; binários grandes permanecem em object storage/CDN quando apropriado.

    TypeScript UI → API/contrato → repositório → PostgreSQL
                                  ↑
                       Rust/Python via interfaces autorizadas

Ver [Database Strategy](../data/DATABASE_STRATEGY.md), [SQL Data Model Plan](../data/SQL_DATA_MODEL_PLAN.md) e [ADR-0002](../decisions/ADR/ADR-0002-sql-first-data-layer.md).
