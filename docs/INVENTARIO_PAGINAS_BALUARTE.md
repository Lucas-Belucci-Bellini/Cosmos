# Inventário de páginas do Projeto Baluarte

## Finalidade

Este inventário registra as superfícies encontradas em `src/pages` e as rotas registradas em `src/main.js` do Projeto Baluarte. Ele serve como catálogo de migração para o Cosmos. A existência de uma página neste documento não significa que ela deva ser copiada imediatamente.

A regra é migrar por **fatias verticais**. Uma fatia vertical inclui a rota, o componente de página, os dados que ela consome, os estilos necessários, os assets usados e os testes mínimos. Código sem consumidor identificado deve permanecer no Baluarte até uma decisão explícita.

## Estados de migração

| Estado | Uso |
|---|---|
| `catalogado` | Página identificada, sem implementação no Cosmos. |
| `selecionado` | Página escolhida para a próxima fase. |
| `migrado` | Arquivos mínimos copiados para o Cosmos. |
| `adaptando` | Dependências e identidade estão sendo ajustadas. |
| `validado` | Rota e testes básicos confirmados. |
| `refeito` | A experiência foi reconstruída sem copiar a implementação original. |
| `adiado` | Não há consumidor, dependência ou prioridade imediata. |

No momento, o **J.A.R.V.I.S. Núcleo V7** está migrado como artefato standalone. O shell e as páginas de aplicação do Cosmos ainda estão em planejamento. O Arsenal abaixo é o próximo candidato de implementação.

## Páginas por domínio

### Entrada, sistema e conta

| Rota ou página | Arquivo de origem | Estado recomendado |
|---|---|---|
| `/home` | `src/pages/home.ts` | Refazer no shell Cosmos |
| `/sobre` | `src/pages/sobre.ts` | Adiado |
| `/roadmap` | `src/pages/roadmap.ts` | Adiado |
| `/baixar` | `src/pages/baixar.ts` | Adiado |
| `/login` | `src/pages/login.ts` | Adiado; depende de auth |
| `/perfil` | `src/pages/perfil.ts` | Adiado; depende de auth |
| `/diagnostico` | `src/pages/diagnostico.ts` | Adiado; superfície operacional |
| `/projetos` | `src/pages/projetos.ts` | Adiado |
| `/mural` | `src/pages/mural.ts` | Adiado; depende de persistência |

### Ferramentas de desenvolvimento e dados

| Rota ou página | Arquivo de origem | Estado recomendado |
|---|---|---|
| `/ferramentas` | `src/pages/ferramentas.ts` | Adiado |
| `/editor` | `src/pages/editor.ts` | Adiado |
| `/json-studio` | `src/pages/json-studio.ts` | Adiado |
| `/qr-studio` | `src/pages/qr-studio.ts` | Adiado |
| `/git-helper` | `src/pages/git-helper.ts` | Adiado |
| `/terminal` | `src/pages/terminal.ts` | Adiado; exige sandbox virtual |
| `/terminal-ia` | `src/pages/terminal-ia.ts` / Núcleo | Adiado |
| `/codigo` | `src/pages/codigo.ts` | Adiado |
| `/gerar-codigo` | `src/pages/gerar-codigo.ts` | Adiado; superfície do Núcleo |
| `/apis` | `src/pages/apis.ts` / Núcleo | Adiado |
| `/regex` | `src/pages/regex.ts` | Adiado |
| `/ocr` | `src/pages/ocr.ts` | Adiado |
| `/llm-lab` | `src/pages/llm-lab.ts` / Núcleo | Adiado |
| `/banco` | `src/pages/banco.ts` | Adiado |

### Cálculo, lógica e criptografia

| Rota ou página | Arquivo de origem | Estado recomendado |
|---|---|---|
| `/calc-cientifica` | `src/pages/calc-cientifica.ts` | Adiado |
| `/calc-numerica` | `src/pages/calc-numerica.ts` | Adiado |
| `/calculadoras` | `src/pages/calculadoras/index.ts` | Adiado |
| `/tabela-verdade` | `src/pages/tabela-verdade.ts` | Adiado |
| `/logic-sim` | `src/pages/logic-sim.ts` | Adiado |
| `/cripto` | `src/pages/cripto/index.ts` | Adiado |
| `/esteganografia` | `src/pages/esteganografia.ts` | Adiado |
| `/graficos` | `src/pages/graficos.ts` | Adiado |
| `/tabela-periodica` | `src/pages/tabela-periodica.ts` | Adiado |
| `/morse` | `src/pages/morse.ts` | Adiado |
| `/portas` | `src/pages/portas.ts` | Adiado |
| `/simbolos` | `src/pages/simbolos.ts` | Adiado |
| `/color-studio` | `src/pages/color-studio.ts` | Adiado |

### Conhecimento, biblioteca e narrativa

| Rota ou página | Arquivo de origem | Estado recomendado |
|---|---|---|
| `/biblioteca` | `src/pages/biblioteca.ts` | Selecionar depois do shell |
| `/academia` | `src/pages/academia.ts` | Adiado |
| `/aprendizado` | `src/pages/aprendizado.ts` | Adiado |
| `/universo` | `src/pages/universo.ts` | Adiado |
| `/cerebro` | `src/pages/cerebro.ts` | Selecionar com memória J.A.R.V.I.S. |
| `/dossie` | `src/pages/dossie.ts` | Adiado; JSON já selecionado |
| `/memoria` | `src/pages/memoria.ts` | Selecionar depois do contrato de storage |
| `/memes` | `src/pages/memes.ts` | Adiado |
| `/filmes` | `src/pages/filmes.ts` | Adiado |
| `/tv` | `src/pages/tv.ts` | Adiado |
| `/videos` | `src/pages/videos.ts` | Adiado |
| `/jogos` | `src/pages/jogos.ts` | Adiado |
| `/modpack` | `src/pages/modpack.ts` | Adiado |
| `/zomboid` | `src/pages/zomboid.ts` | Adiado |
| `/zomboid-admin` | `src/pages/zomboid-admin.ts` | Adiado; exige servidor |
| `/projetos` | `src/pages/projetos.ts` | Adiado |

### J.A.R.V.I.S., núcleo e mídia

| Rota ou página | Arquivo de origem | Estado recomendado |
|---|---|---|
| `/jarvis` | `src/pages/jarvis-nucleo.ts` na web; `src/pages/jarvis.ts` no app | V7 migrado; shell pendente |
| `/jarvis-dashboard` | `src/pages/jarvis-dashboard.ts` / Núcleo | Adiado |
| `/jarvis-vision` | `src/pages/jarvis-vision.ts` | Adiado |
| `/ia-proprietaria` | `src/pages/git-nexus-gate.ts` | Adiado |
| `/cerebro` | `src/pages/cerebro.ts` | Adiado |
| `/memoria` | `src/pages/memoria.ts` | Adiado |
| `/media` | `src/pages/media.ts` | Adiado |
| `/fft` | `src/pages/fft.ts` | Adiado |
| `/radio` | `src/pages/radio.ts` | Adiado |
| `/musicas` | `src/pages/musicas.ts` | Adiado |
| `/mapa` | `src/pages/mapa.ts` | Adiado |
| `/radar` | `src/pages/radar.ts` | Adiado |
| `/geo` | `src/pages/geopulse.ts` | Adiado |
| `/triangulacao` | `src/pages/triangulacao.ts` | Adiado |
| `/find` | `src/pages/find.ts` | Adiado |
| `/visao` | `src/pages/visao.ts` | Adiado |

### Arsenal, Arma 3 e militar

| Rota ou página | Arquivo de origem | Estado recomendado |
|---|---|---|
| `/arsenal` | `src/pages/arsenal.ts` | **Próximo vertical slice** |
| `/arsenal-expandido` | `src/pages/arsenal-expandido.ts` | Adiado; base maior |
| `/militar` | `src/pages/militar.ts` | Adiado; hub |
| `/wiki-arma3` | `src/pages/wiki-arma3.ts` | Depois do Arsenal mínimo |
| `/arma3-tutorial` | `src/pages/arma3-tutorial.ts` | Adiado |
| `/arma3-extracao-painel` | `src/pages/arma3-extracao-painel.ts` | Adiado; exige pipeline |
| `/modelos-3d` | `src/pages/modelos-3d.ts` | Adiado; assets pesados |
| `/vanguard` | `src/pages/vanguard.ts` | Adiado; balística e mapas |
| `/forcas-armadas` | `src/pages/forcas-armadas.ts` | Adiado |
| `/forcas-especiais` | `src/pages/forcas-especiais.ts` | Adiado |
| `/organizacao-militar` | `src/pages/organizacao-militar.ts` | Adiado |
| `/enciclopedia-militar` | `src/pages/enciclopedia-militar.ts` | Adiado |
| `/historia-militar` | `src/pages/historia-militar.ts` | Adiado |
| `/armas-por-pais` | `src/pages/armas-por-pais.ts` | Adiado |
| `/guerras-conflitos` | `src/pages/guerras-conflitos.ts` | Adiado |
| `/batalhas-historicas` | `src/pages/batalhas-historicas.ts` | Adiado |
| `/orcamentos-militares` | `src/pages/orcamentos-militares.ts` | Adiado; dados externos |
| `/poder-militar` | `src/pages/poder-militar.ts` | Adiado |
| `/tecnologia-militar` | `src/pages/tecnologia-militar.ts` | Adiado |
| `/taticas-estrategias` | `src/pages/taticas-estrategias.ts` | Adiado |
| `/historia-militar` | `src/pages/historia-militar.ts` | Adiado |
| `/batalhas-historicas` | `src/pages/batalhas-historicas.ts` | Adiado |

### Economia, comunicação e utilidades

| Rota ou página | Arquivo de origem | Estado recomendado |
|---|---|---|
| `/economia` | `src/pages/economia.ts` | Adiado |
| `/dolar` | `src/pages/dolar.ts` | Adiado; workflow externo |
| `/comms` | `src/pages/comms.ts` | Adiado; persistência/realtime |
| `/utilidades` | `src/pages/utilidades.ts` | Adiado |
| `/seguranca` | `src/pages/seguranca.ts` / Núcleo | Adiado |
| `/shadow` | `src/pages/shadow.ts` | Adiado |
| `/batalha-naval` | `src/pages/batalha-naval.ts` | Adiado |

## Arquivos duplicados JavaScript/TypeScript

Muitas páginas possuem `.ts`, `.js` e `.d.ts`. Para uma migração nova, o Cosmos deve preferir a fonte `.ts` quando ela for a implementação canônica e copiar o `.js` apenas quando o navegador precisar de um artefato standalone. Os arquivos `.d.ts` entram somente quando o novo build TypeScript os referenciar.

## Próximas páginas a migrar

A sequência recomendada é:

1. **Shell Cosmos e Home.** Sem isso, não há ciclo de vida de rotas.
2. **`/jarvis-v7` ou `/jarvis`.** O visual V7 já está no Cosmos como artefato standalone.
3. **`/arsenal`.** É o menor módulo militar útil e usa um dataset local relativamente pequeno.
4. **`/wiki-arma3`.** Só depois de estabilizar o padrão de catálogo e detalhes.
5. **`/cerebro` e `/memoria`.** Só depois do contrato de storage e privacidade.

## Referências

[1]: https://github.com/Lucas-Belucci-Bellini/Projeto-Baluarte "Projeto Baluarte — repositório de origem"
[2]: https://github.com/Lucas-Belucci-Bellini/Cosmos "Cosmos — repositório de destino"
