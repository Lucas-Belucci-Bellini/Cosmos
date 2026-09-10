# API Architecture

Nenhuma API do Baluarte é automaticamente preservada. Cada endpoint futuro deve registrar método, autenticação, headers, request, response, erros, rate limit, dependências, fonte, status e versão.

A API do Cosmos deve separar endpoints públicos, autenticados, administrativos e jobs. Schemas formais devem validar entrada e saída. Adapters externos não devem vazar formatos de terceiros para a UI.

## Estado

`DISCOVERY`. Os endpoints observados no Baluarte serão catalogados antes da escolha de backend.
