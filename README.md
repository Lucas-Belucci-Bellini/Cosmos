# Cosmos

O Cosmos é a continuação seletiva do Projeto Baluarte. Em vez de copiar tudo de uma vez, cada funcionalidade é analisada, adaptada ou refeita antes de entrar no novo projeto.

## Primeira migração

A primeira fatia traz o **J.A.R.V.I.S. Núcleo V7**, seu artefato standalone, a fonte TypeScript, documentação técnica e um conjunto inicial de JSONs para dados e Arsenal.

- [Plano e inventário da migração seletiva](docs/MIGRACAO_SELETIVA.md)
- [Abrir o Núcleo V7](public/jarvis-v7/index.html)
- [Documentação transferida do V7](docs/baluarte-v7/)

O V7 ainda é uma superfície standalone. A integração com o shell, a rota principal, o fallback e o chat do Cosmos serão implementados separadamente.

## Regra de evolução

O código do Baluarte é uma base de referência. O Cosmos deve puxar o que for útil, manter a atribuição de origem e refazer as partes que precisarem de uma arquitetura melhor. Nenhuma integração externa ou credencial é copiada automaticamente.

## Origem

- [Projeto-Baluarte](https://github.com/Lucas-Belucci-Bellini/Projeto-Baluarte)
- [Cosmos](https://github.com/Lucas-Belucci-Bellini/Cosmos)
