# Migration Matrix — Baluarte → Cosmos

Status válidos: `DISCOVERY`, `DOCUMENTED`, `PLANNED`, `APPROVED`, `IN_PROGRESS`, `BLOCKED`, `TESTING`, `STABLE`, `DEPRECATED`.

Métodos: `COPY` (dados/artefatos aprovados sem lógica acoplada), `ADAPT` (transformar para contrato Cosmos), `REBUILD` (reimplementar), `REFERENCE` (consultar origem sem trazer para runtime), `ARCHIVE` (preservar fora do caminho ativo), `DISCARD` (não migrar, com motivo).

| ID | Baluarte / origem | Capacidade | Destino Cosmos | Método | Status | Motivo/ação necessária |
|---|---|---|---|---|---|---|
| MIG-001 | `src/main.js`, `src/core`, `src/layout`, `src/core/router.ts` (canônico; `router.js` é wrapper) | shell, router hash-based e lifecycle | shell/runtime Cosmos | REBUILD | DOCUMENTED | Inspeção estática confirmou registro/validação de rotas, parâmetros/query, eventos `route:*` e tratamento de handlers assíncronos; criar testes Cosmos equivalentes, sem portar o shell V1. |
| MIG-002 | `project V2/Modelar objeto 3D/jarvis-nucleo-v7.*` | núcleo visual V7 | `public/jarvis-v7` | ADAPT | IN_PROGRESS | Artefato transferido; integração de rota e testes ainda pendentes. |
| MIG-003 | `src/utils/jarvis-v7-visual.ts` | adaptador visual | módulo visual Cosmos | ADAPT | PLANNED | Eliminar dependência de helpers internos da origem. |
| MIG-004 | `src/data/cerebro.json`, `src/data/dossie.json` | dados de conhecimento | data/JARVIS | COPY | DOCUMENTED | Definir schema, consumidor, versão e política de privacidade. |
| MIG-005 | `src/pages/jarvis.ts`, `src/utils/jarvis-context.ts`, `jarvis-recall.js`, `jarvis-tools.js` e demais `jarvis-*` | chat, providers/modos, contexto, memória, voz, skills e ferramentas de agente | módulos JARVIS | REBUILD | DISCOVERY | Inspeção estática confirmou orçamento de contexto, recall TF-IDF/cosseno com cache limitado, schemas de ferramentas e integração com guard/permissões; mapear o caminho de envio e validar os limites antes de migrar. |
| MIG-006 | `src/pages/arsenal*`, `src/data/arsenal*` | catálogo editorial | módulo Arsenal | REBUILD/ADAPT | PLANNED | Validar dataset e schema antes da importação. |
| MIG-007 | `src/pages/arma3*`, `src/data/arma3-*` | catálogo técnico Arma 3 | módulos técnicos sob demanda | ADAPT | PLANNED | Importar datasets por consumidor, não como lote único. |
| MIG-008 | `public/arma3/**/*.webp` | imagens de catálogo | storage/CDN por módulo | ADAPT | DOCUMENTED | Selecionar assets e verificar origem/licença/hash. |
| MIG-009 | `scripts/arma3/out/**/*.p3d` | modelos/exportações geradas | archive/object storage | ARCHIVE | DOCUMENTED | Cerca de 3.096,53 MiB; fora do Git do Cosmos. |
| MIG-010 | `scripts/arma3/out/**/*.json` | exportações geradas | pipeline de dados | REFERENCE | DOCUMENTED | Validar proveniência e consumidor antes de transportar. |
| MIG-011 | `src/pages/biblioteca.ts`, `src/pages/dossie.ts`, `src/data/dossie.json` | biblioteca e dossiês | módulo Knowledge | ADAPT/REBUILD | DISCOVERY | Indexação, links, permissões e fontes precisam de contrato. |
| MIG-012 | `src/pages/editor.ts`, `json-studio.ts`, `codigo.ts` | editores | módulo IDE/Tools | REBUILD | DISCOVERY | Criar modelo de workspace e validação segura. |
| MIG-013 | `src/pages/terminal.ts`, `src/utils/terminal-engine*` | terminal e comandos | serviço local Rust/adapter | REBUILD | DISCOVERY | Exigir allowlist, consentimento, cancelamento e auditoria. |
| MIG-014 | `src/pages/git-*`, `src/utils/git-nexus-*` | ferramentas Git e análise | módulo Developer Tools | ADAPT/REBUILD | DISCOVERY | Separar leitura do repo de operações mutáveis; testar permissões. |
| MIG-015 | `src/pages/calc-*`, `src/utils/calc-engine*` | calculadoras | módulo Calculations | REBUILD/ADAPT | DISCOVERY | Definir precisão, unidades e testes de referência. |
| MIG-016 | `src/pages/tabela-verdade.ts`, `logic-sim.ts`, `src/data/logic-*` | lógica e simulação | módulo Logic | REBUILD | DISCOVERY | Testar resultados e documentar regras formais. |
| MIG-017 | `src/pages/musicas.ts`, `radio.ts`, `fft.ts`, `src/utils/*audio*` | mídia e áudio | módulo Media | REBUILD/REFERENCE | DISCOVERY | APIs, direitos, consentimento e compatibilidade externa. |
| MIG-018 | `src/pages/ocr.ts`, `visao.ts`, `jarvis-python/` | OCR/visão e pipelines IA | serviço Python isolado | REBUILD | DISCOVERY | Contratos de entrada/saída, privacidade e limites de recursos. |
| MIG-019 | `src/pages/mapa.ts`, `radar.ts`, `geopulse.ts`, `triangulacao.ts` | mapas e geodados | módulo Geospatial | REBUILD/REFERENCE | DISCOVERY | Avaliar fonte, permissões de localização e necessidade real. |
| MIG-020 | `src/pages/login.ts`, `perfil.ts`, `src/core/auth-session.ts` | conta e preferências | identidade Cosmos | REBUILD | DISCOVERY | Schema e modelo de ameaça próprios; sem migrar tokens. |
| MIG-021 | `desktop/src` | desktop, IPC, arquivos, música, Nexus e Hermes | runtime local Cosmos | REBUILD/REFERENCE | PLANNED | Extrair requisitos; não reutilizar IPC sem auditoria. |
| MIG-022 | `android/`, `capacitor.config.json` | aplicativo Android | futura plataforma móvel | REFERENCE | PLANNED | Adiar até núcleo e contratos estabilizados. |
| MIG-023 | `src/pages/zomboid*`, `modpack.ts`, `src/data/zomboid-*` | jogos, modpacks e administração | módulo Game Knowledge | REFERENCE/REBUILD | DISCOVERY | Versionar dados e validar compatibilidade. |
| MIG-024 | `src/pages/jogos.ts`, `videos.ts`, `src/data/cronicas.js`, `universos.js` | mídia e universo narrativo | módulos de conteúdo | REFERENCE/ADAPT | DISCOVERY | Confirmar licenças, origem e escopo antes de importar. |
| MIG-025 | `src/pages/apis.ts`, `economia.ts`, `dolar.ts`, helpers de API | integrações externas | adapters de serviço | REBUILD | DISCOVERY | Segredos fora do Git, timeout, cache e fallback. |
| MIG-026 | `src/core/backup.js`, `src/core/storage*`, `src/core/politica.js`, `scripts/v2-backup-restore-drill.mjs` | backup, restore, storage e sync | camada Data/Storage | REBUILD | DISCOVERY | O backup exclui `auth:session`, valida envelope versionado e restaura apenas chaves conhecidas; o drill local deixa RPO/RTO como não aprovados. Criar formato Cosmos próprio e medir recuperação. |
| MIG-027 | `src/pages/aprendizado.ts`, tutoriais e guia de PC | aprendizagem e documentação interativa | módulo Learning | ADAPT/REBUILD | DISCOVERY | Separar conteúdo estático de lógica executável. |
| MIG-028 | `src/pages/robotica.ts`, `tecnologia-militar.ts` e páginas técnicas | conteúdo técnico | módulo Technical Knowledge | REFERENCE/REBUILD | DISCOVERY | Curadoria, fontes e manutenção antes da migração. |
| MIG-029 | `supabase/migrations`, `backend/`, `backend-java/`, `api/` | APIs, auth, banco e realtime | serviços Cosmos | REBUILD | DISCOVERY | Desenhar schema e contratos novos; não reproduzir automaticamente o backend. |
| MIG-030 | `src/pages/*`, wrappers `.js` e implementações `.ts` | inventário de páginas | catálogo de módulos | REFERENCE | DOCUMENTED | Confirmar pares canônicos e evitar duplicar wrappers de compatibilidade. |
| MIG-031 | `src/data/*`, JSONs técnicos e exports | datasets | catálogo de dados versionado | REFERENCE | DOCUMENTED | Nada entra no runtime sem consumidor, schema e proveniência. |
| MIG-032 | `.env`, tokens e segredos reais | configuração sensível | nenhum | DISCARD | STABLE | Nunca migrar segredos; recriar placeholders e rotacionar quando necessário. |
| MIG-033 | `.github`, Vercel, Render e workflows antigos | CI/CD e deploy | infraestrutura Cosmos | REFERENCE | DISCOVERY | Reavaliar com a stack e os ambientes novos. |
| MIG-034 | `docs/`, relatórios, histórico e notas | conhecimento histórico | `docs/source-history` | ARCHIVE/REFERENCE | DOCUMENTED | Preservar rastreabilidade; evitar dependência de runtime. |
| MIG-035 | `public/modelos-3d`, áudio, PDFs, PNGs e outros assets | assets diversos | storage por módulo | ADAPT/ARCHIVE | DISCOVERY | Catalogar tamanho, checksum, licença, finalidade e consumidor. |
| MIG-036 | `.claude/skills`, `AGENTS.md`, `CLAUDE.md`, scripts de automação | instruções e ferramentas de agentes | automação Cosmos revisada | REFERENCE/ADAPT | DISCOVERY | Auditar comandos e caminhos; nenhuma instrução antiga é confiável por padrão. |
| MIG-037 | `.obsidian`, canvases e notas pessoais/projeto | base de conhecimento | docs/knowledge opcional | REFERENCE/ARCHIVE | DISCOVERY | Filtrar duplicatas e conteúdo não destinado ao produto. |
| MIG-038 | `test/`, `scripts/v2-integracao.mjs`, `scripts/v2-backup-restore-drill.mjs` | testes, harness de integração e evidências de recuperação | testes de regressão Cosmos | REFERENCE/ADAPT | DOCUMENTED | Foram inspecionados scripts, não executados nesta auditoria. Adaptar testes comportamentais e manter resultados/ambiente registrados; teste antigo não prova o Cosmos. |

| MIG-039 | `src/main.js`, `src/core`, `src/layout`, `src/pages/home.ts` | shell, router, navegação e lifecycle | shell Cosmos | REBUILD | PLANNED | Criar contrato de módulo e testes de rota; não importar o shell antigo. |
| MIG-040 | `src/pages/git-nexus*`, `src/utils/git-nexus-*`, `src/data/codemap.json` | inteligência de repositórios | Developer Tools | REBUILD/ADAPT | DISCOVERY | Confirmar fontes, atualidade do índice, exclusões e limites de processamento. |
| MIG-041 | `src/pages/regex.ts`, `src/pages/simbolos.ts`, `src/pages/utilidades.ts` | regex e utilitários de texto | Utilities | REBUILD/ADAPT | DISCOVERY | Validar Unicode, entradas inválidas e padrões que possam bloquear a UI. |
| MIG-042 | `src/pages/tabela-periodica.ts` | tabela periódica | Science/Learning | ADAPT/REBUILD | DISCOVERY | Identificar fonte, licença, unidades e valores de referência. |
| MIG-043 | `src/pages/mural.ts`, `src/pages/comms.ts`, `src/pages/conselho.ts`, `src/core/events*` | mural, eventos e notificações | Communication opcional | REBUILD/REFERENCE | DISCOVERY | Definir consumidor real, identidade, autorização e retenção antes de construir. |
| MIG-044 | `src/pages/projetos.ts`, `roadmap.ts`, `sobre.ts`, `baixar.ts`, `perfil.ts` | projetos, roadmap, perfil e downloads | Product/Projects | ADAPT/REBUILD | DISCOVERY | Separar conteúdo público de dados privados e validar origem dos downloads. |
| MIG-045 | `src/pages/modelos-3d.ts`, `src/data/modelos-3d.json`, `public/modelos-3d/` | galeria e visualizador 3D | Visual/Assets | ADAPT/REBUILD | DISCOVERY | Selecionar assets por consumidor, licença, checksum e orçamento de tamanho. |
| MIG-046 | `src/pages/diagnostico.ts`, `src/pages/seguranca.ts`, `src/pages/ciberseg.ts` | diagnóstico e segurança defensiva | Security/Operations | REBUILD/ADAPT | DISCOVERY | Distinguir evidência de hipótese e impedir ações fora do escopo autorizado. |
| MIG-047 | `src/pages/media.ts`, `filmes.ts`, `tv.ts`, `videos.ts`, `musicas.ts`, `radio.ts` | catálogo e players audiovisuais | Media adapters | ADAPT/REFERENCE | DISCOVERY | Confirmar providers, licenças, links e fallback. |
| MIG-048 | `src/pages/mapa.ts`, `radar.ts`, `geopulse.ts`, `triangulacao.ts`, `find.ts`, `visao.ts` | mapas, geodados e localização | Geospatial | REBUILD/REFERENCE | DISCOVERY | Validar fontes, permissões e precisão declarada. |
| MIG-049 | `src/pages/cripto/`, `src/pages/esteganografia.ts` | ferramentas criptográficas educacionais | Learning/Security | REBUILD/REFERENCE | DISCOVERY | Distinguir demonstração de segurança de produção; testar formatos e limites. |
| MIG-050 | `src/pages/jogos.ts`, `modpack.ts`, `zomboid.ts`, `zomboid-admin.ts`, `src/data/zomboid-*` | jogos, modpacks e administração de servidor | Game Knowledge | ADAPT/REBUILD | DISCOVERY | Separar catálogo de ações administrativas e exigir autorização. |
| MIG-051 | `src/pages/login.ts`, `perfil.ts`, `src/core/auth-session.ts` | identidade, sessão e preferências | Identity/Data Layer | REBUILD | DISCOVERY | Definir fluxo, modelo de ameaça, retenção e testes de autorização. |
| MIG-052 | `backend/`, `backend-java/`, `api/`, `supabase/` | serviços, endpoints e banco | API/Services | REBUILD/REFERENCE | DISCOVERY | Mapear consumidores, schemas e secrets; não portar credenciais. |
| MIG-053 | `src/pages/robotica.ts`, `src/pages/tecnologia-militar.ts` e páginas técnicas | conteúdo técnico especializado | Technical Knowledge | ADAPT/REFERENCE | DISCOVERY | Curar fontes e separar artigos de simuladores verificáveis. |
| MIG-054 | `src/pages/economia.ts`, `src/pages/dolar.ts` e helpers de API | câmbio e indicadores externos | Data Integrations | REBUILD/ADAPT | DISCOVERY | Mostrar fonte, unidade, timestamp, atraso e política de falha. |
| MIG-055 | `src/pages/forcas-especiais.ts`, `organizacao-militar.ts`, `enciclopedia-militar.ts`, `historia-militar.ts`, `armas-por-pais.ts`, `guerras-conflitos.ts`, `batalhas-historicas.ts`, `orcamentos-militares.ts`, `poder-militar.ts`, `taticas-estrategias.ts` | enciclopédia, história e indicadores militares | Technical Knowledge | ADAPT/REFERENCE | DISCOVERY | Confirmar fontes, data, metodologia e duplicatas; conteúdo deve ser educativo e verificável. |
| MIG-056 | `src/pages/utilidades.ts`, `shadow.ts`, `batalha-naval.ts` | utilidades restantes, Shadow e jogo Batalha Naval | Utilities/Games | REBUILD/ADAPT | DISCOVERY | Confirmar comportamento no código; não inferir função pelo nome da rota. |
| MIG-057 | schema e serviços SQL do Cosmos; legado Baluarte `backend/`, `api/`, `supabase/` apenas como referência | persistência relacional, migrações, relações e transações | PostgreSQL central; provedor gerenciado pendente | REBUILD/REFERENCE | DOCUMENTED | ADR-0002 aprova SQL-first/PostgreSQL como alvo central; não reutilizar schema/credenciais legadas sem reconciliação. Criar tabelas somente após confirmar consumidores, acesso e testes. |

## Regras de migração

- Nunca copiar todo o checkout, `node_modules`, builds, caches, artefatos gerados ou secrets.
- A origem deve ser identificada por caminho e, quando possível, commit SHA.
- Todo item aprovado tem destino, responsável, critérios de aceite e evidência de teste.
- `DOCUMENTED` significa inventariado; não significa implementado.
- O Cosmos deve compilar, testar e executar sem depender de um checkout do Baluarte.
- Migrar em fatias verticais: contrato → dados → implementação → testes → documentação.
