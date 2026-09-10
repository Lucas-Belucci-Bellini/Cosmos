# Data Catalog — Baluarte → Cosmos

Todo dataset precisa de consumidor, schema, origem, atualização, sensibilidade e método antes de entrar no Cosmos.

| ID | Dataset | Origem | Formato/tamanho aproximado | Consumidor candidato | Método | Status |
|---|---|---|---|---|---|---|
| DAT-001 | `cerebro.json` | `src/data/cerebro.json` | JSON, 5 KiB | J.A.R.V.I.S./memória | COPY | DOCUMENTED |
| DAT-002 | `dossie.json` | `src/data/dossie.json` | JSON, 128 KiB | J.A.R.V.I.S./dossiê | COPY | DOCUMENTED |
| DAT-003 | `modelos-3d.json` | `src/data/modelos-3d.json` | JSON, 204 KiB | galeria 3D | ADAPT | DOCUMENTED |
| DAT-004 | `arsenal-expandido.json` | `src/data/arsenal-expandido.json` | JSON, 468 KiB | catálogo editorial | REFERENCE | DOCUMENTED |
| DAT-005 | `armas-db.json` | `public/arma3/armas-db.json` | JSON, 1,8 MiB | Arsenal técnico | ADAPT | PLANNED |
| DAT-006 | `equipamento-db.json` | `public/arma3/equipamento-db.json` | JSON, 0,6 MiB | equipamento técnico | ADAPT | PLANNED |
| DAT-007 | `acessorios-db.json` | `public/arma3/acessorios-db.json` | JSON, 2,2 MiB | acessórios técnicos | ADAPT | PLANNED |
| DAT-008 | `veiculos-db.json` | `public/arma3/veiculos-db.json` | JSON, 2,7 MiB | veículos | REFERENCE | DISCOVERY |
| DAT-009 | `soldados-db.json` | `public/arma3/soldados-db.json` | JSON, 14,4 MiB | unidades | REFERENCE | DISCOVERY |
| DAT-010 | `terrenos-db.json` | `public/arma3/terrenos-db.json` | JSON, 0,5 MiB | terrenos/mapas | REFERENCE | DISCOVERY |
| DAT-011 | `scripts/arma3/out/*.json` | exports gerados | até dezenas de MiB | pipeline Arma 3 | ARCHIVE | DOCUMENTED |
| DAT-012 | `fanfic.json` | `src/data/fanfic.json` | JSON, 5,8 MiB | narrativa | REFERENCE | DISCOVERY |
| DAT-013 | `codemap.json` e símbolos | `src/data/` | JSON, até 0,5 MiB | Git Nexus | REFERENCE | DISCOVERY |

Nenhum dataset com status `REFERENCE`, `ARCHIVE` ou `DISCOVERY` deve ser copiado para runtime. Campos de sensibilidade e licença precisam ser preenchidos antes de aprovação.
