# Migration Matrix — Baluarte → Cosmos

Status válidos: `DISCOVERY`, `DOCUMENTED`, `PLANNED`, `APPROVED`, `IN_PROGRESS`, `BLOCKED`, `TESTING`, `STABLE`, `DEPRECATED`.

| ID | Baluarte | Tipo | Cosmos | Método | Status | Motivo e observação |
|---|---|---|---|---|---|---|
| MIG-001 | `src/main.js`, `src/core`, `src/layout` | arquitetura web | shell/runtime Cosmos | REBUILD | DOCUMENTED | O código antigo não deve comandar a arquitetura nova. |
| MIG-002 | `project V2/Modelar objeto 3D/jarvis-nucleo-v7.*` | visual/artefato | `public/jarvis-v7` | ADAPT | IN_PROGRESS | Artefato já transferido; integração de rota ainda pendente. |
| MIG-003 | `src/utils/jarvis-v7-visual.ts` | adaptador visual | módulo visual Cosmos | ADAPT | PLANNED | Importa helpers e contratos do Baluarte. |
| MIG-004 | `src/data/cerebro.json`, `src/data/dossie.json` | dados | data/JARVIS | COPY | DOCUMENTED | Dados pequenos; consumidor Cosmos ainda precisa ser definido. |
| MIG-005 | `src/data/arsenal.js` | dataset editorial | módulo Arsenal | ADAPT | PLANNED | Formato útil, mas precisa de schema e namespace Cosmos. |
| MIG-006 | `src/pages/arsenal.ts` | UI | módulo Arsenal | REBUILD | PLANNED | Recriar com lifecycle, contratos e estilos próprios. |
| MIG-007 | `src/styles/arsenal.css` | estilo | design system Arsenal | ADAPT | PLANNED | Extrair regras e mapear tokens. |
| MIG-008 | `public/arma3/armas-db.json` | dataset técnico | data/arma3/weapons | ADAPT | PLANNED | Migrar só com consumidor técnico aprovado. |
| MIG-009 | `scripts/arma3/out/*.p3d` | modelo gerado | storage externo | ARCHIVE | DOCUMENTED | 3.096,53 MiB de `.p3d`; não cabe no Git do Cosmos. |
| MIG-010 | `scripts/arma3/out/*.json` | export gerado | pipeline/data externo | REFERENCE | DOCUMENTED | Validar origem e consumidor antes de transportar. |
| MIG-011 | `public/arma3/**/*.webp` | imagens/assets | CDN/storage por módulo | ADAPT | DOCUMENTED | 232,66 MiB; selecionar por consumidor e registrar origem. |
| MIG-012 | `src/pages/*` | páginas | catálogo de módulos | REFERENCE | DOCUMENTED | Inventariadas; implementar apenas após priorização. |
| MIG-013 | `src/data/*.json` | datasets | catálogo de dados | REFERENCE | DOCUMENTED | Nenhum JSON deve entrar sem finalidade definida. |
| MIG-014 | `.env`, tokens e secrets | configuração | nenhum | DISCARD | STABLE | Nunca migrar segredos. |
| MIG-015 | `.github`, Vercel e deploy antigo | infraestrutura | contratos de infraestrutura | REFERENCE | DISCOVERY | Reavaliar depois da decisão tecnológica. |
| MIG-016 | `supabase/migrations`, backend e APIs | backend/banco | API e banco Cosmos | REBUILD | DISCOVERY | Schema novo; não reproduzir automaticamente o banco antigo. |
| MIG-017 | `docs`, histórico e relatórios | documentação | docs/source-history | ARCHIVE | DOCUMENTED | Preservar rastreabilidade sem tornar runtime dependente. |
| MIG-018 | `desktop`, `android`, `backend-java` | plataformas | future/platforms | REFERENCE | PLANNED | Avaliar somente após estabilizar o núcleo web. |

Nenhuma implementação em massa deve começar antes de cada item ter um destino e método aprovados.
