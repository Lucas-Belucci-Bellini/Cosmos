# Feature Catalog

O catálogo descreve capacidades observadas no Baluarte e decisões iniciais para o Cosmos. O estado do Baluarte não implica compromisso de reconstrução.

| ID | Domínio | Funcionalidade | Entradas/saídas | Dependências | Cosmos | Prioridade | Decisão |
|---|---|---|---|---|---|---|---|
| FTR-001 | J.A.R.V.I.S. | Núcleo visual V7 | interação, áudio → visual 3D | WebGL, áudio, iframe | DOCUMENTED | P0 | REBUILD/ADAPT |
| FTR-002 | J.A.R.V.I.S. | Chat e memória | texto/contexto → resposta/estado | auth, storage, IA | DISCOVERY | P2 | avaliar depois do core |
| FTR-003 | Arsenal | catálogo editorial | filtros → itens/detalhes | dataset local | PLANNED | P1 | REBUILD |
| FTR-004 | Arsenal | catálogo técnico Arma 3 | arma/filtro → dados balísticos | JSONs grandes | PLANNED | P2 | ADAPT |
| FTR-005 | Militar | enciclopédia e história | busca → artigos | conteúdo editorial | DISCOVERY | P3 | avaliar |
| FTR-006 | Knowledge | biblioteca/dossiê | navegação → leitura | JSON/documentos | DISCOVERY | P2 | avaliar |
| FTR-007 | Tools | editor/JSON/terminal | arquivo/comando → resultado | sandbox/segurança | DISCOVERY | P3 | reconstruir isoladamente |
| FTR-008 | Media | música/rádio/FFT | mídia → reprodução/análise | APIs/permissões | DISCOVERY | P3 | avaliar |
| FTR-009 | Vision | visão/OCR/mapa/radar | imagem/localização → análise | APIs/device | DISCOVERY | P4 | avaliar |
| FTR-010 | Account | login/perfil | credenciais → sessão | auth/database | DISCOVERY | P4 | schema próprio |
| FTR-011 | Platform | desktop/mobile | comandos → runtime | wrappers nativos | DEFERRED | P5 | não iniciar agora |
| FTR-012 | Content | jogos/Zomboid/modpack | configuração → conteúdo | dados/assets | DISCOVERY | P4 | avaliar |

Cada funcionalidade aprovada deverá receber uma ficha em `docs/modules/` com contrato, dados, integração, testes e método de migração.
