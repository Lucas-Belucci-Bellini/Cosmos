# Subinventário funcional — Projeto Baluarte → Cosmos

## Propósito e limite

Este documento aprofunda as páginas catalogadas e transforma áreas que poderiam ficar esquecidas em uma lista verificável de funções candidatas. Os nomes abaixo são **pistas de auditoria derivadas do inventário atual**, não garantia de que cada função já exista ou funcione. A confirmação exige leitura do arquivo de origem, dependências, dados, rotas e testes.

Regra: cada item precisa terminar com uma decisão explícita: `ADAPT`, `REBUILD`, `REFERENCE`, `ARCHIVE` ou `DISCARD`, com motivo. Não copiar uma página inteira só porque ela tem uma rota.

## 1. Núcleo da aplicação

| Área | Funções a verificar | Destino candidato | Issue |
|---|---|---|---|
| Shell/Home | inicialização, layout, rotas, navegação, loading, erro, not-found | shell modular Cosmos | [#28](https://github.com/Lucas-Belucci-Bellini/Cosmos/issues/28) |
| Módulos | registro, metadados, permissões, ciclo de vida, lazy loading | Module Registry | #28 |
| Sobre/Roadmap | conteúdo institucional, versões, links | docs e páginas institucionais | [#33](https://github.com/Lucas-Belucci-Bellini/Cosmos/issues/33) |
| Downloads | versão, origem, integridade, instruções | catálogo de releases | #33 |
| Diagnóstico | checks, status, evidências, exportação de relatório | diagnóstico defensivo | [#35](https://github.com/Lucas-Belucci-Bellini/Cosmos/issues/35) |

## 2. J.A.R.V.I.S. e IA

| Subárea | Funções a verificar | Destino candidato | Issue |
|---|---|---|---|
| Núcleo visual V7 | canvas/WebGL, animação, estados, resize, cleanup | adapter visual | #10 / #11 |
| Chat | mensagens, contexto, histórico, cancelamento, erros | chat provider-agnostic | [#12](https://github.com/Lucas-Belucci-Bellini/Cosmos/issues/12) |
| Memória | gravação, recuperação, busca, exclusão, exportação | memory service | #12 |
| Voz | permissões, entrada/saída, seleção de dispositivo, indisponibilidade | voice adapter | #12 |
| Skills | catálogo, schemas, roteamento, resultados, timeout | tool registry | #12 / #22 |
| Python IA | pipeline, modelos, dependências, limites CPU/GPU | serviço Python isolado | #12 / #20 |
| LLM Lab / geração de código | providers, prompts, resposta estruturada, validação | AI adapters; execução sempre separada | #12 / #13 |

## 3. Ferramentas de programação

| Subárea | Funções a verificar | Destino candidato | Issue |
|---|---|---|---|
| Editor | abas, edição, snippets, realce, salvar/abrir | editor web/local | [#13](https://github.com/Lucas-Belucci-Bellini/Cosmos/issues/13) |
| JSON Studio | parse, format, schema, diff, validação | ferramenta de dados | #13 |
| Terminal | comandos, saída, cancelamento, timeout, histórico | runtime local restrito | #13 |
| Git Helper | status, diff, branch, commits, operações mutáveis | adapter Git | #29 |
| Git Nexus | símbolos, mapa de código, relações, relatórios | indexador de repositórios | [#29](https://github.com/Lucas-Belucci-Bellini/Cosmos/issues/29) |
| Regex | testar padrão, flags, grupos, substituição, exemplos | utilitários de texto | [#30](https://github.com/Lucas-Belucci-Bellini/Cosmos/issues/30) |
| QR Studio | gerar/ler QR, exportar imagem, validar payload | utilitário local | [#23](https://github.com/Lucas-Belucci-Bellini/Cosmos/issues/23) |
| APIs | catálogo, exemplos, status, documentação de endpoints | API explorer seguro | [#20](https://github.com/Lucas-Belucci-Bellini/Cosmos/issues/20) |
| Banco | explorar schema, exemplos e conectores, se existentes | ferramenta de dados com permissões | #20 / #19 |

## 4. Cálculo, lógica e ciência

| Subárea | Funções a verificar | Destino candidato | Issue |
|---|---|---|---|
| Calculadora científica | operações, precedência, parênteses, funções | engine matemático testado | [#16](https://github.com/Lucas-Belucci-Bellini/Cosmos/issues/16) |
| Cálculo numérico | métodos, iterações, tolerância, convergência | engine com testes de referência | #16 |
| Calculadoras especializadas | fórmulas, unidades, validação e pressupostos | submódulos por domínio | #16 |
| Tabela-verdade | operadores, precedência, avaliação de expressões | engine lógico | #16 |
| Simulador lógico/portas | circuitos, entradas, saídas e visualização | simulador de lógica | #16 |
| Tabela periódica | propriedades, unidades, busca e filtros | catálogo científico | [#31](https://github.com/Lucas-Belucci-Bellini/Cosmos/issues/31) |
| Gráficos | datasets, séries, eixos, exportação e acessibilidade | visualização reutilizável | [#24](https://github.com/Lucas-Belucci-Bellini/Cosmos/issues/24) |
| Morse/símbolos | conversão, tabela de referência, Unicode | utilitários de texto | #23 / #30 |
| Criptografia educacional | encoding, hashing e demonstrações didáticas | ferramentas com limitações explícitas | #23 |

## 5. Conteúdo e conhecimento

| Subárea | Funções a verificar | Destino candidato | Issue |
|---|---|---|---|
| Biblioteca | lista, filtros, pesquisa, links e metadados | Knowledge | [#14](https://github.com/Lucas-Belucci-Bellini/Cosmos/issues/14) |
| Dossiês/Cérebro | registros, relações, fontes, revisão e pesquisa | conhecimento estruturado | #14 / #12 |
| Aprendizado/Academia | módulos didáticos, progresso e referências | Learning | #16 |
| Enciclopédia/história | artigos, datas, fontes e referências cruzadas | conteúdo editorial versionado | #14 |
| Jogos/modpacks | jogo, versão, loader, dependências, compatibilidade | Game Knowledge | [#26](https://github.com/Lucas-Belucci-Bellini/Cosmos/issues/26) |
| Crônicas/universos | obra, capítulo, personagem, cronologia e links | biblioteca narrativa | [#27](https://github.com/Lucas-Belucci-Bellini/Cosmos/issues/27) |
| Projetos | descrição, estado, links, prioridades e histórico | painel de projetos | #33 |
| Mural/Conselho | posts, eventos, persistência e autorização, se realmente necessários | módulo social opcional | [#32](https://github.com/Lucas-Belucci-Bellini/Cosmos/issues/32) |

## 6. Media, visão e visualização

| Subárea | Funções a verificar | Destino candidato | Issue |
|---|---|---|---|
| Música/Rádio/TV/Vídeos | catálogo, links, player, provider, erros e permissões | adapters de mídia | [#17](https://github.com/Lucas-Belucci-Bellini/Cosmos/issues/17) |
| FFT | entrada de sinal, janela, amostragem, gráfico e exportação | engine de áudio | #17 |
| OCR | upload local, extração, idioma, confiança e revisão | serviço Python com privacidade | [#18](https://github.com/Lucas-Belucci-Bellini/Cosmos/issues/18) |
| Visão computacional | entradas, inferência, limites e indicação de confiança | serviço de visão opcional | #18 |
| Mapas/Geopulse/Radar | fonte, filtros, atualização e permissões de localização | módulo geoespacial | #18 |
| Galeria 3D | catálogo, preview, carregamento, fallback e metadados | viewer com lazy loading | [#34](https://github.com/Lucas-Belucci-Bellini/Cosmos/issues/34) |
| Color Studio/Temas | tokens, paletas, contraste, preferências e persistência | design system Cosmos | #24 |

## 7. Plataforma, dados e integrações

| Subárea | Funções a verificar | Destino candidato | Issue |
|---|---|---|---|
| Login/Perfil | sessão, perfil, preferências, recuperação e logout | identidade Cosmos | [#19](https://github.com/Lucas-Belucci-Bellini/Cosmos/issues/19) |
| Storage/Backup | exportação, integridade, restore, retenção e sync | Data Layer | #19 |
| Desktop/IPC | filesystem, processos, eventos, logs e empacotamento | runtime local Rust candidato | [#21](https://github.com/Lucas-Belucci-Bellini/Cosmos/issues/21) |
| Android/Capacitor | capacidades, permissões, builds e estado atual | avaliar após core estável | #21 |
| APIs externas | autenticação, quotas, cache, timeout e fallback | adapters isolados | [#20](https://github.com/Lucas-Belucci-Bellini/Cosmos/issues/20) |
| Economia/Câmbio | fontes, unidade, timestamp e atualização | dados com proveniência | [#25](https://github.com/Lucas-Belucci-Bellini/Cosmos/issues/25) |
| Comms/WebSocket | eventos, autenticação, reconexão e ordenação | camada de eventos | #32 |
| Segurança/Privacidade | checklist, evidência, escopo, logs e retenção | módulo defensivo | [#35](https://github.com/Lucas-Belucci-Bellini/Cosmos/issues/35) |
| CI/CD | workflows, build, testes, releases e rollback | pipelines Cosmos próprios | #11 / #20 |

## 8. Procedimento obrigatório para cada função

1. Abrir o arquivo de origem e confirmar que a função existe.
2. Encontrar quem a chama, quais dados lê e quais efeitos colaterais produz.
3. Registrar dependências, permissões, APIs, assets, segredos e limitações.
4. Identificar duplicatas e wrappers JS/TS antes de escolher a implementação canônica.
5. Atribuir decisão, prioridade e destino.
6. Definir contrato, testes e critério de aceite.
7. Implementar uma fatia vertical pequena.
8. Rodar testes e registrar evidência no relatório de migração.
9. Só então marcar como `STABLE`.

## 9. Relatórios de auditoria

Cada rodada deve criar um novo relatório, sem sobrescrever o anterior, em `docs/reports/migration/`. Nome sugerido: `AUDIT-YYYY-MM-DD-NNN.md`. Cada relatório precisa registrar commit de origem, commit do Cosmos, arquivos analisados, itens confirmados, itens descartados com motivo, riscos, testes executados e próximos passos.

## Aviso de estado

Este documento amplia o mapa de investigação. Não afirma que todas as funções listadas já foram inspecionadas, migradas ou testadas. As conclusões só mudam após evidência do código e dos testes.
