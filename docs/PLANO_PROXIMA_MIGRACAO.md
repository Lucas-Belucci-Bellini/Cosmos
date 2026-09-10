# Plano da próxima migração Baluarte → Cosmos

## 1. Regra geral

O Cosmos não deve receber o Baluarte inteiro de uma vez. Cada módulo deve passar por uma ficha de migração, ter seus consumidores identificados e entrar com o menor conjunto possível de código, dados, assets e testes.

Estados recomendados:

| Estado | Significado |
|---|---|
| `catalogado` | Existe no Baluarte e foi descrito, mas ainda não foi copiado. |
| `selecionado` | O Cosmos precisa dele e seus limites foram definidos. |
| `migrado` | Código e dados mínimos foram copiados. |
| `adaptando` | O código está sendo ajustado para contratos e identidade Cosmos. |
| `validado` | Build, testes e comportamento básico foram confirmados. |
| `refeito` | A ideia foi preservada, mas a implementação foi reconstruída. |
| `adiado` | Não é necessário agora ou depende de outra base. |

## 2. Ficha de cada módulo

Cada módulo faltante deve ter um arquivo em `docs/modules/<nome>.md` com estes campos:

1. **Identificação:** nome, origem, versão e responsável pela migração.
2. **Propósito:** qual problema o módulo resolve no Cosmos.
3. **Superfície:** rota, página, comando ou API que o usuário utiliza.
4. **Arquivos de origem:** caminhos exatos no Baluarte.
5. **Dependências:** imports, estilos, assets, bibliotecas, APIs externas e variáveis de ambiente.
6. **Dados:** JSONs consumidos, schema mínimo, tamanho, origem e política de atualização.
7. **O que será copiado:** partes estáveis que serão preservadas.
8. **O que será adaptado:** nomes, rotas, mensagens, storage, permissões e identidade visual.
9. **O que será refeito:** partes frágeis, acopladas ao Baluarte ou difíceis de testar.
10. **Segurança e privacidade:** credenciais, iframe, `postMessage`, permissões de microfone/captura e dados locais.
11. **Testes de aceitação:** comportamento mínimo que precisa funcionar no Cosmos.
12. **Atribuição:** autoria, contribuição de terceiros, licenças e links de origem.
13. **Decisão:** migrar agora, migrar depois, refazer ou não migrar.
14. **Histórico:** commits do Cosmos que implementaram a decisão.

Além da ficha, manter `docs/modules/INDEX.md` com uma linha por módulo e `docs/modules/manifest.json` com estado, rota, dependências de dados e cobertura de testes. O manifesto deve ser pequeno e legível; ele não deve duplicar os JSONs de conteúdo.

## 3. Módulos que faltam, por ordem recomendada

| Ordem | Módulo | Decisão inicial | Motivo |
|---:|---|---|---|
| 1 | Shell e roteamento Cosmos | Refazer | O repositório destino ainda não tem aplicação, layout ou router. |
| 2 | J.A.R.V.I.S. Núcleo V7 | Migrado; integrar | O artefato já está em `public/jarvis-v7`; falta a rota e o fallback do shell. |
| 3 | Presença musical do Núcleo | Adaptar depois | Depende de um contrato Cosmos para estado de playback; não é necessária para abrir o V7. |
| 4 | J.A.R.V.I.S. chat/memória | Selecionar após o shell | É maior e depende de storage, provedor, permissões e possivelmente backend. |
| 5 | Arsenal mínimo | Selecionar | Começar por uma página e uma base de dados, não pelo catálogo inteiro. |
| 6 | Biblioteca/crônicas | Selecionar | Pode entrar depois que o shell tiver busca, leitura e navegação. |
| 7 | Ferramentas técnicas | Migrar/refazer por unidade | Calculadoras, editor, terminal e criptografia têm contratos e riscos diferentes. |
| 8 | Desktop/mobile/backend | Adiar | Só fazem sentido depois que a experiência web Cosmos estiver estável. |

## 4. JSONs necessários agora

### Para criar o shell e integrar o V7

**Nenhum JSON adicional é necessário.** O V7 standalone usa Three.js e fontes externas e recebe comandos por interação local. Os arquivos já migrados em `data/baluarte/` podem permanecer como dados de referência, mas não devem ser acoplados à primeira rota.

### Para o próximo módulo, escolher um único vertical slice

A opção mais segura é um **Arsenal inicial**. Nesse caso, migrar somente:

- `public/arma3/armas-db.json` — catálogo principal de armas;
- `public/arma3/acessorios-db.json` — somente se a tela de arma mostrar acessórios;
- `public/arma3/equipamento-db.json` — somente se a tela incluir equipamento;
- `src/data/arma3-armas.js` e seus tipos — adaptador e metadados;
- `src/data/arma3-acessorios.js` ou `src/data/arma3-equipamento.js` — apenas quando usados pela tela;
- imagens referenciadas pela primeira tela, não a pasta inteira de assets.

`veiculos-db.json`, `soldados-db.json`, `terrenos-db.json`, `municao` e os índices de extração devem ficar adiados até existir uma rota que os consuma. Copiar esses arquivos antes cria peso sem entregar comportamento.

### Para J.A.R.V.I.S. com contexto local

Os arquivos já trazidos `cerebro.json` e `dossie.json` são suficientes como dados iniciais. Antes de trazer `fanfic.json`, `codemap.json`, `codemap-symbols.json` ou históricos, confirmar qual tela Cosmos os lerá e se o formato será mantido ou transformado.

### Para Biblioteca e narrativa

O candidato inicial é `projetos.json` mais o dataset específico da tela escolhida. `fanfic.json` e grandes documentos narrativos só devem entrar junto com uma rota de leitura, busca ou índice; não devem ser copiados apenas por disponibilidade.

## 5. Shell Cosmos para o V7

A primeira versão deve ser pequena e sem framework obrigatório:

```text
index.html
package.json
src/
  main.ts
  core/
    dom.ts
    router.ts
  layout/
    shell.ts
  pages/
    home.ts
    jarvis-v7.ts
  styles/
    shell.css
    jarvis-v7.css
public/
  jarvis-v7/
    index.html
    jarvis-nucleo-v7.js
```

### Contratos mínimos

- `router.ts` deve aceitar as rotas `/` e `/jarvis-v7`, fazer fallback para Home e permitir desmontagem da página anterior.
- `shell.ts` deve renderizar cabeçalho, navegação, área de conteúdo e uma mensagem de estado sem expor stack trace.
- `jarvis-v7.ts` deve criar um iframe same-origin para `/jarvis-v7/index.html`, com `sandbox="allow-scripts allow-same-origin"`, `allow="microphone; display-capture"` e um fallback textual.
- A página deve remover listeners e zerar o iframe ao sair da rota.
- O `postMessage` deve aceitar somente mensagens cujo `origin` seja o mesmo do Cosmos e cuja origem seja a janela do iframe.
- A primeira versão não deve integrar chat, Spotify ou autenticação. Ela só abre o visual e informa `loading`, `ready` ou `fallback`.

### Adaptação necessária no adaptador V7

O arquivo atual `src/jarvis-v7/jarvis-v7-visual.ts` veio do Baluarte e importa `./helpers.js`, que ainda não existe no Cosmos. Ao integrar:

1. criar um `h()` mínimo em `src/core/dom.ts` ou substituir o import por criação DOM explícita;
2. mover estilos do switcher para `src/styles/jarvis-v7.css`;
3. manter temporariamente os nomes de mensagens `baluarte-*` por compatibilidade e registrar essa decisão;
4. criar uma versão futura `cosmos-*` somente quando houver testes de contrato para os dois lados;
5. trocar o texto e a identidade visual do iframe sem alterar o comportamento de áudio até existir teste de regressão;
6. adicionar teste de rota, teste de fallback e teste de isolamento de `postMessage`.

### Critérios de aceite da primeira rota

- `/jarvis-v7` abre o Núcleo V7 no navegador;
- o iframe é same-origin e carrega o artefato JavaScript local;
- o shell continua funcionando se WebGL, Three.js ou áudio falharem;
- sair e voltar à rota não duplica listeners nem iframes;
- mensagens de origem externa são ignoradas;
- a Home continua disponível;
- `npm run build` e os testes de contrato passam.

## 6. Decisão prática

A próxima implementação deve ser o **shell mínimo + rota `/jarvis-v7`**, sem migrar novos JSONs. Depois de validar essa fatia, escolher entre Arsenal mínimo, memória do J.A.R.V.I.S. ou Biblioteca. Essa ordem evita transportar dados que ainda não possuem consumidor e permite que cada módulo seja documentado, testado e eventualmente refeito sem comprometer o restante do Cosmos.
