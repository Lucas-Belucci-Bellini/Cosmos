# Cosmos

O **Cosmos** é uma reconstrução modular e planejada do Projeto-Baluarte. O Baluarte permanece como fonte histórica, de requisitos, conhecimento, dados e assets. Ele não define automaticamente a arquitetura, as dependências ou a implementação do Cosmos.

## Regra principal

> **Entender → Documentar → Classificar → Planejar → Decidir → Reconstruir → Testar.**

O Cosmos não deve virar uma cópia menor do Baluarte. Cada funcionalidade precisa de um destino, um método de migração, uma origem rastreável, um contrato, testes e uma estratégia de armazenamento.

## Documentação da Fase 0

Comece pelo [índice da documentação](docs/INDEX.md) e pelo [Cosmos Master Plan](docs/COSMOS_MASTER_PLAN.md).

Os documentos centrais são:

- [Matriz de migração Baluarte → Cosmos](docs/migration/MIGRATION_MATRIX.md);
- [Política de referência do Baluarte](docs/migration/BALUARTE_REFERENCE_POLICY.md);
- [Catálogo de funcionalidades](docs/product/FEATURE_CATALOG.md);
- [Mapa de sistemas](docs/architecture/SYSTEM_MAP.md);
- [Análise de armazenamento](docs/infrastructure/STORAGE_ANALYSIS.md);
- [Catálogo de dados](docs/data/DATA_CATALOG.md);
- [Catálogo de assets](docs/assets/ASSET_CATALOG.md);
- [Estratégia de testes](docs/testing/TEST_STRATEGY.md).

## Material já migrado

O Núcleo V7 do J.A.R.V.I.S. está preservado como artefato standalone em [`public/jarvis-v7`](public/jarvis-v7/). Ele será integrado depois por um contrato próprio do Cosmos. Sua existência não transforma a arquitetura do Baluarte em arquitetura do Cosmos.

## Auditoria de tamanho

A auditoria atual encontrou aproximadamente **3.706,57 MiB** no checkout do Baluarte e um pack Git de aproximadamente **4,18 GiB**. `scripts/arma3` representa cerca de **3.300,61 MiB**, principalmente modelos `.p3d`. Por isso, datasets grandes, builds, caches, backups e assets pesados não devem entrar automaticamente no Git do Cosmos.

A auditoria pode ser reproduzida com:

```bash
python3 scripts/audit_baluarte.py /home/ubuntu/Projeto-Baluarte
```

## Origem

- [Projeto-Baluarte](https://github.com/Lucas-Belucci-Bellini/Projeto-Baluarte)
- [NEXORA](https://github.com/Lucas-Belucci-Bellini/NEXORA)
- [Cosmos](https://github.com/Lucas-Belucci-Bellini/Cosmos)
