# ADR-0001 — Reconstruir em vez de copiar

## Contexto

O Projeto-Baluarte reúne código, dados, assets, artefatos gerados, integrações e histórico em uma estrutura extensa. A auditoria encontrou aproximadamente 3,7 GiB no checkout e 4,18 GiB no pack Git.

## Problema

Copiar a estrutura inteira transferiria acoplamentos, dependências, artefatos e custos antes de definir os requisitos do Cosmos.

## Alternativas

1. Copiar tudo e organizar depois.
2. Copiar páginas por ordem de aparência.
3. Documentar, classificar e reconstruir por módulos.

## Decisão

Escolher a alternativa 3. O Baluarte será fonte histórica e de requisitos. Cada item recebe `COPY`, `ADAPT`, `REBUILD`, `REFERENCE`, `ARCHIVE` ou `DISCARD`.

## Consequências

O início é mais lento, mas o Cosmos ganha fronteiras, rastreabilidade, storage controlado, testes e liberdade tecnológica. O Núcleo V7 já transferido deve ser tratado como exceção provisória e integrado por contrato, não como arquitetura-base.

## Status

`APPROVED` para a Fase 0; implementação da fundação ainda requer decisão tecnológica posterior.
