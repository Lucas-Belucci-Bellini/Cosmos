# Test Strategy

## Princípios

Todo módulo importante deve definir como será testado antes da implementação. Testes de origem não substituem testes do Cosmos.

| Camada | Objetivo |
|---|---|
| Unit | funções puras, filtros, normalização e validação |
| Integration | contratos entre módulo, core, data e adapters |
| API | request, response, auth, erros e rate limit |
| Database | schema, constraints, migrations e permissões |
| Browser | rotas, lifecycle, acessibilidade e fallback |
| Security | origem de mensagens, sanitização, secrets e autorização |
| Regression | comportamento já validado do V7 e módulos reconstruídos |
| Performance | bundle, tempo de boot, memória e datasets |
| Smoke | deploy mínimo e rotas críticas |

## Critério

Uma funcionalidade não é `STABLE` sem testes de caminho feliz, falha, cleanup e regressão. Fixtures devem ser pequenas e não carregar datasets completos apenas para testar filtros.
