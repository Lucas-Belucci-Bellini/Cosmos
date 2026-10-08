# Feature Catalog — Projeto-Baluarte → Cosmos

Este catálogo agrupa as capacidades identificadas no repositório de origem. É um inventário de descoberta, não uma promessa de reconstrução integral. A implementação só é considerada migrada quando existe no Cosmos, tem contrato próprio e passou por testes.

| ID | Domínio | Funcionalidade/capacidade | Origem indicativa no Baluarte | Dependências/risco | Prioridade inicial | Decisão inicial |
|---|---|---|---|---|---|---|
| FTR-001 | J.A.R.V.I.S. | Núcleo visual V7 | `project V2/Modelar objeto 3D`, `src/pages/jarvis*` | WebGL, áudio, iframe, lifecycle | P0 | ADAPT/REBUILD |
| FTR-002 | J.A.R.V.I.S. | Chat, contexto e memória | `src/pages/jarvis*`, `src/utils/jarvis-*`, `src/data/cerebro.json` | IA, privacidade, storage | P1 | REBUILD |
| FTR-003 | J.A.R.V.I.S. | Voz, escuta e síntese | `src/utils/jarvis-voice*`, `jarvis-python/` | Permissão de microfone, runtime | P2 | ADAPT/REBUILD |
| FTR-004 | J.A.R.V.I.S. | Skills, ferramentas e agentes | `src/utils/jarvis-tools*`, `src/utils/jarvis-skills*` | Permissões, chamadas de ferramentas | P1 | REBUILD |
| FTR-005 | Arsenal | Catálogo editorial | `src/pages/arsenal*`, `src/data/arsenal*` | Dataset, pesquisa e filtros | P1 | REBUILD/ADAPT |
| FTR-006 | Arma 3 | Catálogo de armas e balística | `src/pages/arma3*`, `src/data/arma3-*`, `public/arma3` | Dataset grande, assets/licenças | P2 | ADAPT |
| FTR-007 | Arma 3 | Veículos, unidades, mapas e equipamentos | `src/data/arma3-*`, `public/arma3` | JSONs grandes, procedência | P3 | ADAPT/REFERENCE |
| FTR-008 | Knowledge | Biblioteca, dossiês e busca | `src/pages/biblioteca.ts`, `src/pages/dossie.ts`, `src/data/dossie.json` | Documentos, indexação | P1 | REBUILD/ADAPT |
| FTR-009 | Conhecimento militar | Enciclopédia, história e conflitos | `src/pages/enciclopedia-militar.ts`, `src/pages/historia-militar.ts` | Conteúdo editorial, fontes | P3 | REBUILD/REFERENCE |
| FTR-010 | IDE/Tools | Editor de código e snippets | `src/pages/editor.ts`, `src/utils/editor-*`, `src/data/editor-*` | Workspace, sandbox, linguagem | P1 | REBUILD |
| FTR-011 | IDE/Tools | Editor e validador JSON | `src/pages/json-studio.ts`, `src/pages/codigo.ts` | Validação, arquivos, limites | P1 | REBUILD |
| FTR-012 | IDE/Tools | Terminal e execução de comandos | `src/pages/terminal.ts`, `src/utils/terminal-engine*`, `desktop/src` | RISCO ALTO: execução local | P2 | REBUILD COM PERMISSÕES |
| FTR-013 | Developer Tools | Git Helper e Git Nexus | `src/pages/git-helper.ts`, `src/pages/git-nexus*`, `src/utils/git-nexus-*` | Git, filesystem, análise de repositório | P1 | REBUILD/ADAPT |
| FTR-014 | Data/Calculators | Calculadoras científica, numérica e especializada | `src/pages/calc-*`, `src/pages/calculadoras/`, `src/utils/calc-engine*` | Precisão e testes matemáticos | P2 | REBUILD/ADAPT |
| FTR-015 | Logic/Education | Tabela-verdade, lógica e circuitos | `src/pages/tabela-verdade.ts`, `src/pages/logic-sim.ts`, `src/data/logic-*` | Correção de regras, acessibilidade | P2 | REBUILD |
| FTR-016 | Media | Música, rádio e reprodução | `src/pages/musicas.ts`, `src/pages/radio.ts`, `src/utils/jarvis-spotify*` | APIs externas, direitos, credenciais | P3 | REBUILD/REFERENCE |
| FTR-017 | Media | FFT, visualização e análise de áudio | `src/pages/fft.ts`, `src/utils/fft-engine*` | Performance, Web Audio | P3 | ADAPT/REBUILD |
| FTR-018 | Vision/Maps | OCR e visão computacional | `src/pages/ocr.ts`, `src/pages/visao.ts`, `jarvis-python/` | IA, privacidade, CPU/GPU | P3 | REBUILD |
| FTR-019 | Vision/Maps | Mapas, radar, geopulse e triangulação | `src/pages/mapa.ts`, `src/pages/radar.ts`, `src/pages/geopulse.ts` | Geolocalização e APIs | P4 | REBUILD/REFERENCE |
| FTR-020 | Account | Login, perfil e preferências | `src/pages/login.ts`, `src/pages/perfil.ts`, `src/core/auth-session.ts` | Auth, segurança, banco | P2 | REBUILD |
| FTR-021 | Platform | Desktop e IPC | `desktop/src` | Processo local, permissões, empacotamento | P3 | REBUILD/REFERENCE |
| FTR-022 | Platform | Android/Capacitor | `android/`, `capacitor.config.json` | Permissões móveis e release | P5 | DEFER |
| FTR-023 | Content | Zomboid, modpacks e administração | `src/pages/zomboid*`, `src/pages/modpack.ts`, `src/data/zomboid-*` | Dados de jogos, versões e compatibilidade | P4 | REFERENCE/REBUILD |
| FTR-024 | Content | Jogos, vídeos, filmes e universo narrativo | `src/pages/jogos.ts`, `src/pages/videos.ts`, `src/data/universos.js`, `src/data/cronicas.js` | Direitos, conteúdo e metadados | P4 | REFERENCE/REBUILD |
| FTR-025 | Integrations | APIs, economia, câmbio e fontes externas | `src/pages/apis.ts`, `src/pages/economia.ts`, `src/pages/dolar.ts`, `src/utils/*api*` | Limites, disponibilidade e segredos | P3 | REBUILD |
| FTR-026 | Platform | Backup, storage, sincronização e offline | `src/core/backup*`, `src/core/storage*`, `src/core/media-sync*` | Integridade, privacidade e recuperação | P1 | REBUILD |
| FTR-027 | Learning | Aprendizado, tutoriais e guia de PC | `src/pages/aprendizado.ts`, `src/pages/arma3-tutorial.ts`, `src/pages/guia-pc.ts` | Conteúdo versionado | P3 | REBUILD/ADAPT |
| FTR-028 | Robotics/Tech | Robótica, tecnologia e guias técnicos | `src/pages/robotica.ts`, `src/pages/tecnologia-militar.ts` | Conteúdo, fontes e manutenção | P4 | REFERENCE/REBUILD |

| FTR-029 | Core/Shell | Home, router, navegação, lifecycle e estados de erro | `src/main.js`, `src/core`, `src/layout`, `src/pages/home.ts` | Contrato de módulo, roteamento, acessibilidade | P0 | REBUILD |
| FTR-030 | Developer Tools | Git Nexus, mapa de símbolos e inteligência de repositórios | `src/pages/git-nexus*`, `src/utils/git-nexus-*`, `src/data/codemap.json` | Tamanho do repo, stale indexes, operações Git | P1 | REBUILD/ADAPT |
| FTR-031 | Developer Tools | Regex, texto, símbolos e utilitários de conversão | `src/pages/regex.ts`, `src/pages/simbolos.ts`, `src/pages/utilidades.ts` | Entradas adversariais, Unicode, performance | P2 | REBUILD/ADAPT |
| FTR-032 | Science/Education | Tabela periódica e propriedades científicas | `src/pages/tabela-periodica.ts` | Proveniência, unidades, precisão | P3 | ADAPT/REBUILD |
| FTR-033 | Communication | Mural, Conselho, eventos e notificações | `src/pages/mural.ts`, `src/pages/comms.ts`, `src/pages/conselho.ts`, `src/core/events*` | Auth, persistência, spam, privacidade | P4 | REBUILD/DEFER |
| FTR-034 | Product/Projects | Projetos, roadmap, perfil público, sobre e downloads | `src/pages/projetos.ts`, `roadmap.ts`, `sobre.ts`, `baixar.ts`, `perfil.ts` | Conteúdo canônico, links, dados privados | P2 | REBUILD/ADAPT |
| FTR-035 | Visual | Galeria 3D, preview, seleção e carregamento de modelos | `src/pages/modelos-3d.ts`, `src/data/modelos-3d.json`, `public/modelos-3d/` | WebGL, licença, tamanho dos assets | P3 | ADAPT/REBUILD |
| FTR-036 | Security/Operations | Diagnóstico, segurança defensiva e privacidade | `src/pages/diagnostico.ts`, `src/pages/seguranca.ts`, `src/pages/ciberseg.ts` | Escopo autorizado, falsos positivos, dados sensíveis | P1 | REBUILD/ADAPT |
| FTR-037 | Media | Catálogo audiovisual, players, rádio e música | `src/pages/media.ts`, `filmes.ts`, `tv.ts`, `videos.ts`, `musicas.ts`, `radio.ts` | Providers, licença, links externos | P3 | ADAPT/REFERENCE |
| FTR-038 | Geospatial | Mapas, Geopulse, radar, find e triangulação | `src/pages/mapa.ts`, `radar.ts`, `geopulse.ts`, `triangulacao.ts`, `find.ts` | Localização, precisão, permissões | P3 | REBUILD/REFERENCE |
| FTR-039 | Security/Learning | Criptografia educacional e esteganografia | `src/pages/cripto/`, `src/pages/esteganografia.ts` | Limites, formatos e alegações de segurança | P3 | REBUILD/REFERENCE |
| FTR-040 | Games | Jogos, modpacks e administração Project Zomboid | `src/pages/jogos.ts`, `modpack.ts`, `zomboid.ts`, `zomboid-admin.ts` | Compatibilidade, credenciais, efeitos remotos | P3 | ADAPT/REBUILD |
| FTR-041 | Identity | Login, sessão, perfil e preferências | `src/pages/login.ts`, `perfil.ts`, `src/core/auth-session.ts` | Autorização, sessão, dados sensíveis | P1 | REBUILD |
| FTR-042 | Backend/API | Endpoints, serviços, migrations e integrações legadas | `backend/`, `backend-java/`, `api/`, `supabase/` | Consumers, secrets, contratos | P1 | REBUILD/REFERENCE |
| FTR-043 | Technical Knowledge | Robótica e páginas técnicas especializadas | `src/pages/robotica.ts`, `tecnologia-militar.ts` | Fontes, atualização, precisão | P4 | ADAPT/REFERENCE |
| FTR-044 | External Data | Câmbio, economia e indicadores | `src/pages/economia.ts`, `src/pages/dolar.ts` | Fonte, timestamp, unidades e quotas | P2 | ADAPT/REBUILD |
| FTR-045 | Technical Knowledge | Enciclopédia militar, história, conflitos e indicadores por país | páginas históricas e de dados em `src/pages/` | Proveniência, atualização, metodologia | P4 | ADAPT/REFERENCE |
| FTR-046 | Utilities/Games | Utilidades restantes, Shadow e Batalha Naval | `src/pages/utilidades.ts`, `shadow.ts`, `batalha-naval.ts` | Função real, duplicatas, consumidores | P3 | REBUILD/ADAPT |
| FTR-047 | SQL Data Layer | Persistência relacional, migrações, constraints, transações e proveniência | `docs/data/DATABASE_STRATEGY.md`, `docs/data/SQL_DATA_MODEL_PLAN.md` | Acesso, policies, migrations, backup e isolamento | P1 | REBUILD |

| FTR-048 | Data Layer / Identity | Storage versionado, fallback offline, projeção de sessão e adaptadores remotos seguros | `src/core/storage.ts`, `src/core/auth-session.ts`, `src/core/supabase.js`, `src/core/permissions.ts` | Privacidade, autorização server-side, migrações e falhas de rede | P1 | REBUILD/ADAPT |

| FTR-049 | Data/Platform | Mural, métricas públicas e conteúdo com fallback local | `src/pages/mural.ts`, `src/utils/visit-counter.ts`, `src/utils/page-views.ts` | Consistência, abuso de RPC, fonte de verdade e RLS | P2 | REBUILD/REFERENCE |

| FTR-050 | J.A.R.V.I.S. / Memory | Seleção de contexto e recuperação lexical entre sessões | `src/utils/jarvis-context.ts`, `src/utils/jarvis-recall.js` | Privacidade, custo de contexto, cache e isolamento por usuário | P1 | REBUILD/ADAPT |

| FTR-051 | Security/Authorization | Política central, permissões explícitas, negação por padrão, revogação e auditoria | `src/core/permissions.ts`, `src/core/politica.js`, testes de permissão e política | Autorização server-side, isolamento de recursos/tenants, falhas de política | P1 | REBUILD |\n\n## Regras de priorização

1. P0/P1 primeiro: shell, integração do V7, ferramentas de desenvolvimento seguras, dados básicos e conhecimento essencial.
2. P2 após contratos e quality gates: catálogos técnicos, cálculos, login e ferramentas locais controladas.
3. P3/P4/P5 dependem de prioridade real, fontes, licenças, custo operacional e consumidores confirmados.
4. Itens semelhantes devem ser consolidados em módulos quando compartilham contratos e domínio; não criar páginas só para reproduzir o menu antigo.
5. Cada módulo aprovado deve ter ficha em `docs/modules/` com propósito, limites, contrato, modelo de dados, permissões, migração, testes e critérios de aceite.

## Estados

Use os estados definidos na matriz de migração. `DOCUMENTED` significa inventariado; não significa implementado. Nenhum estado pode ser elevado sem evidência verificável.
