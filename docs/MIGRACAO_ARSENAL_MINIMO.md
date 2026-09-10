# Migração do Arsenal mínimo para o Cosmos

## Decisão de escopo

O primeiro Arsenal do Cosmos deve ser um catálogo local de equipamentos com busca, filtros, seleção e detalhes. Ele deve reutilizar a experiência comprovada do Baluarte, mas não deve trazer toda a wiki Arma 3, todos os modelos, todos os parsers ou as bases de dezenas de megabytes.

Há duas superfícies diferentes no Baluarte:

| Superfície | Conteúdo | Escolha |
|---|---|---|
| `/arsenal` | Catálogo editorial de armas, veículos, doutrinas, tiers e equipes | **Migrar agora** |
| `/wiki-arma3` e `/arsenal-expandido` | Dados técnicos e grandes bases do Arma 3 | Migrar depois, em fatias separadas |

## Arquivos exatos para a primeira fatia

### Arquivos obrigatórios do Baluarte

| Origem no Baluarte | Destino recomendado no Cosmos | Motivo |
|---|---|---|
| `src/pages/arsenal.ts` | `src/modules/arsenal/pages/arsenal.ts` | Componente da página e interação |
| `src/data/arsenal.js` | `src/modules/arsenal/data/arsenal.js` | Dataset editorial, categorias, equipes e doutrinas |
| `src/styles/arsenal.css` | `src/modules/arsenal/arsenal.css` | Estilos específicos da lista e detalhes |
| `src/styles/biblioteca.css` | Extrair apenas regras usadas ou adaptar | Dependência atual da página; evitar copiar a folha inteira |
| `src/styles/variables.css` | Mapear tokens para o design system Cosmos | Variáveis de cor, espaço e tipografia |
| `src/styles/base.css` | Adaptar seletivamente | Reset e elementos básicos necessários |
| `src/styles/components.css` | Extrair classes usadas | Badges, botões, cards e inputs |
| `src/utils/helpers.js` | Reimplementar somente `h`, `cx`, `debounce`, `empty`, `normalize` | Reduzir acoplamento ao Core antigo |
| `src/core/storage.js` | Criar `src/core/storage.ts` mínimo no Cosmos | Persistir filtros e item selecionado com namespace Cosmos |
| `src/utils/toast.js` ou equivalente | Criar `src/core/feedback.ts` | Feedback sem transportar o sistema inteiro de toast |
| `src/utils/immersive.js` | Reimplementar ou adiar | O hero imersivo não é necessário para a primeira entrega |

### Arquivos que não devem entrar nesta primeira fatia

Não copiar agora:

- `src/data/arma3-armas.js`;
- `src/data/arma3-acessorios.js`;
- `src/data/arma3-equipamento.js`;
- `public/arma3/acessorios-db.json`;
- `public/arma3/veiculos-db.json`;
- `public/arma3/soldados-db.json`;
- `public/arma3/terrenos-db.json`;
- `scripts/arma3/out/arma3-config.json`;
- `scripts/arma3/out/arma3-itens.json`;
- `scripts/arma3/out/arma3-veiculos.json`;
- parsers Python, dumps `.rpt`, modelos `.p3d` e a pasta completa de imagens.

Esses arquivos pertencem ao Arsenal técnico do Arma 3 e só devem ser migrados quando uma rota específica tiver sido escolhida.

## JSONs do segundo estágio Arma 3

Quando o Cosmos implementar uma tela técnica de armas, a ordem mínima deve ser:

| Ordem | Arquivo | Tamanho aproximado no Baluarte | Dependência |
|---:|---|---:|---|
| 1 | `public/arma3/armas-db.json` | 1,8 MB | Tela de armas técnicas |
| 2 | `public/arma3/acessorios-db.json` | 2,2 MB | Detalhes de acessórios |
| 3 | `public/arma3/equipamento-db.json` | 0,6 MB | Tela de equipamentos |
| 4 | `public/arma3/terrenos-db.json` | 0,5 MB | Tela de mapas/terrenos |
| 5 | `public/arma3/veiculos-db.json` | 2,7 MB | Tela de veículos |
| 6 | `public/arma3/soldados-db.json` | 14,4 MB | Tela de unidades |

O primeiro vertical slice técnico deve trazer apenas `armas-db.json`. Os demais arquivos só entram quando a interface possuir uma busca, filtro ou detalhe que os consuma.

## Contrato mínimo de dados editoriais

O dataset `src/data/arsenal.js` deve ser normalizado para um contrato Cosmos semelhante a:

```ts
export interface ArsenalItem {
  id: string;
  name: string;
  category: string;
  subcat?: string;
  origin: string;
  year?: number;
  caliber?: string;
  rangeM?: number;
  weightKg?: number;
  equipe?: string;
  notes?: string;
  tier: 'S' | 'A' | 'B' | 'C';
  specs?: Array<{ label: string; value: string }>;
}
```

O Cosmos deve validar a entrada ao carregar o dataset. Campos opcionais ausentes devem ser exibidos como `—`, e não convertidos silenciosamente em zero.

## Implementação passo a passo

### Etapa 1 — criar a estrutura do módulo

Criar:

```text
src/modules/arsenal/
  data/arsenal.js
  pages/arsenal.ts
  arsenal.css
  types.ts
  index.ts
```

Copiar inicialmente apenas os três arquivos de comportamento e dados: `arsenal.ts`, `arsenal.js` e `arsenal.css`. As folhas globais devem ser adaptadas manualmente.

### Etapa 2 — definir o contrato do shell

A página deve receber um elemento de montagem e não depender diretamente de `document.body`, de IDs globais ou de um router específico do Baluarte.

```ts
export interface ArsenalPageOptions {
  mount: HTMLElement;
  onNavigate?: (path: string) => void;
  onError?: (error: unknown) => void;
}

export function mountArsenal(options: ArsenalPageOptions): () => void;
```

A função deve devolver um cleanup. O cleanup remove listeners, cancela debounce, interrompe requisições de imagem e remove o conteúdo montado.

### Etapa 3 — adaptar o estado

Trocar a chave antiga `arsenal:state` por uma chave com namespace do Cosmos, por exemplo:

```text
cosmos:arsenal:state:v1
```

O estado deve conter somente filtros e seleção. Nenhum dado do catálogo deve ser salvo no `localStorage`.

### Etapa 4 — implementar a primeira tela

A primeira tela deve conter:

1. título e descrição curta;
2. chips de categorias;
3. filtro de equipe;
4. filtro de tier;
5. busca textual com debounce;
6. lista de itens;
7. painel de detalhes;
8. estado vazio;
9. estado de erro;
10. layout responsivo.

A busca de imagens na Wikipedia deve ser adiada ou isolada atrás de uma opção. A primeira entrega deve funcionar sem rede externa e sem chave de API.

### Etapa 5 — integrar a rota

Registrar `/arsenal` no router do shell Cosmos. A rota deve carregar o módulo sob demanda e desmontá-lo quando a navegação mudar.

O shell não deve conhecer o dataset interno do Arsenal. Ele apenas monta a página e exibe seus estados de carregamento e erro.

### Etapa 6 — validar

Testes mínimos:

| Teste | Verificação |
|---|---|
| carregamento | A rota monta com dataset não vazio |
| filtros | Categoria, equipe e tier reduzem a lista corretamente |
| busca | Nome, origem, calibre, nota e equipe são pesquisáveis |
| detalhes | Selecionar item atualiza o painel |
| persistência | Filtros são restaurados pela chave Cosmos |
| vazio | Busca sem resultado não quebra a página |
| cleanup | Desmontar remove listeners e timers |
| offline | A tela funciona sem Wikipedia |
| segurança | Dados não executam HTML arbitrário como markup |
| responsividade | Lista e painel funcionam em viewport estreita |

## Passo a passo do próximo módulo do Baluarte

1. Escolher uma página do inventário.
2. Registrar a decisão em `docs/modules/<nome>.md`.
3. Listar os imports diretos e os assets usados.
4. Separar código obrigatório de código opcional.
5. Migrar o menor dataset que a página consome.
6. Criar o contrato Cosmos de montagem e cleanup.
7. Adaptar estilos para tokens Cosmos.
8. Integrar a rota sob demanda.
9. Escrever testes de comportamento e de falha.
10. Executar build e testes.
11. Registrar limitações e atribuição.
12. Só então escolher a página seguinte.

## Critério de conclusão

O Arsenal mínimo estará concluído quando `/arsenal` funcionar no Cosmos sem depender do router, storage, helpers, CSS global ou API externa do Baluarte. O Baluarte será a fonte documentada, mas o módulo deverá ser executável e testável dentro do Cosmos.

## Referências

[1]: https://github.com/Lucas-Belucci-Bellini/Projeto-Baluarte/blob/main/src/pages/arsenal.ts "Página Arsenal do Projeto Baluarte"
[2]: https://github.com/Lucas-Belucci-Bellini/Projeto-Baluarte/blob/main/src/data/arsenal.js "Dataset editorial do Arsenal"
[3]: https://github.com/Lucas-Belucci-Bellini/Projeto-Baluarte/blob/main/src/main.js "Registro de rotas do Projeto Baluarte"
[4]: https://github.com/Lucas-Belucci-Bellini/Cosmos "Repositório Cosmos"
