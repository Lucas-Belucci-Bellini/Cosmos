# Migração seletiva Baluarte → Cosmos

## Primeira fatia: J.A.R.V.I.S. Núcleo V7

Esta etapa não copia o Projeto Baluarte inteiro. Ela traz para o Cosmos apenas a primeira base selecionada:

- `public/jarvis-v7/index.html`: superfície standalone do Núcleo V7;
- `public/jarvis-v7/jarvis-nucleo-v7.js`: artefato compilado que roda no navegador;
- `src/jarvis-v7/jarvis-nucleo-v7.ts`: fonte TypeScript canônica para futuras alterações;
- `src/jarvis-v7/jarvis-v7-visual.ts`: referência do adaptador de iframe, fallback e mensagens entre o Núcleo e a aplicação;
- `docs/baluarte-v7/`: contratos, observações, release report e testes documentais do V7.

O V7 oferece visualização 3D com Three.js, temas ouro/rubi/jade, animação, partículas, bloom, interação por mouse, captura de arquivo de áudio, microfone, captura do som do sistema/aba, analisador FFT, música generativa, pulso, varredura, vistas, rotação e captura de imagem. A página continua standalone e usa Three.js via CDN; a integração com o shell do Cosmos será feita em etapa posterior.

## JSONs trazidos nesta etapa

Foram selecionados dados pequenos e diretamente úteis para a próxima integração:

- `data/baluarte/cerebro.json`;
- `data/baluarte/dossie.json`;
- `data/baluarte/modelos-3d.json`;
- `data/baluarte/arsenal-expandido.json`;
- `data/baluarte/armas-db.json`;
- `data/baluarte/equipamento-db.json`;
- `data/baluarte/terrenos-db.json`;
- `data/baluarte/arma3-grupos.json`.

As bases grandes restantes do Arsenal não foram trazidas agora. Elas devem ser escolhidas conforme os módulos que forem realmente reconstruídos no Cosmos, evitando aumentar o repositório sem necessidade.

## O que ainda não foi integrado

O adaptador `jarvis-v7-visual.ts` é uma referência de integração e ainda depende de helpers e estilos do shell original. Ele não foi conectado automaticamente à aplicação Cosmos porque o Cosmos remoto ainda não possui uma arquitetura web definida. A próxima implementação deve criar o shell, a rota e o fallback do Cosmos, depois adaptar o import de `h()` e o CSS sem copiar o restante do Baluarte.

Também não foram migrados nesta etapa o chat completo, memória, Spotify, autenticação, backend, desktop, mobile, workflows ou o Core V2. Esses componentes serão avaliados separadamente e puxados somente quando houver uma superfície Cosmos para recebê-los.

## Origem e atribuição

Os arquivos foram selecionados do `main` de [Projeto-Baluarte](https://github.com/Lucas-Belucci-Bellini/Projeto-Baluarte) e estão sendo reorganizados no [Cosmos](https://github.com/Lucas-Belucci-Bellini/Cosmos). O histórico original e os documentos de origem permanecem no repositório Baluarte. Alterações futuras devem registrar se cada componente foi **copiado**, **adaptado** ou **refeito**.

## Critério das próximas migrações

Uma funcionalidade só deve ser puxada quando houver uma resposta clara para estas perguntas:

1. Qual experiência do Cosmos ela atende?
2. Quais arquivos são o mínimo necessário para executá-la?
3. Quais JSONs ou assets ela realmente consome?
4. Quais partes serão refeitas em vez de copiadas?
5. Como será testada sem depender de serviços ou credenciais do Baluarte?

Esse critério permite aproveitar o trabalho existente sem transformar o Cosmos em uma cópia difícil de manter.
