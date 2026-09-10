# Política de referência do Projeto-Baluarte

## Princípio

O Projeto-Baluarte é fonte histórica, de requisitos, conhecimento, dados, assets, URLs, APIs, contratos, comportamento e referência visual. Ele não é arquitetura-base, implementação definitiva, conjunto obrigatório de dependências, credenciais ou serviços.

## Métodos permitidos

| Método | Definição |
|---|---|
| `COPY` | Transferência praticamente sem alteração, apenas quando o formato e a licença permitirem. |
| `ADAPT` | Transferência com alteração explícita de contrato, nomes, dependências ou formato. |
| `REBUILD` | Reconstrução funcional com arquitetura própria do Cosmos. |
| `REFERENCE` | Uso apenas para entender comportamento, requisitos ou aparência. |
| `ARCHIVE` | Permanência no histórico, sem entrar no runtime do Cosmos. |
| `DISCARD` | Não migrar por obsolescência, duplicidade, risco ou ausência de finalidade. |

## Regras

Toda migração deve registrar origem, caminho, método, motivo, destino, proprietário do dado, testes e commit. Nenhum segredo, token, `.env` real ou credencial pode ser migrado. O código novo deve depender dos contratos do Cosmos, não de imports acidentais do Baluarte.

## Decisão inicial

O Núcleo V7 já migrado é um artefato temporário de referência/integrável. O shell, o router, a storage e os módulos de aplicação serão `REBUILD`. Datasets pequenos e compatíveis podem ser `COPY` após validação. Datasets grandes, gerados ou acoplados a pipelines antigos serão `REFERENCE`, `ARCHIVE` ou `ADAPT`.
