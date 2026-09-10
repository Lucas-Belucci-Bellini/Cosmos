# Security Architecture

A segurança começa pela separação de código, dados e credenciais. Nenhum `.env` real, token, chave ou sessão do Baluarte entra no Cosmos. O browser recebe somente dados públicos e capacidades explicitamente permitidas.

A futura arquitetura deve definir autenticação, autorização, RBAC, sessões, validação, sanitização, rate limiting, logging, auditoria, isolamento de workers, supply chain, backup e recuperação. Iframes devem validar `origin` e `source`; datasets não devem ser inseridos como HTML arbitrário.

A reconstrução deve usar schema próprio para usuários e permissões. O banco antigo não é uma autoridade automática. Cada integração externa deve possuir threat model, política de falha e segredo armazenado fora do Git.
