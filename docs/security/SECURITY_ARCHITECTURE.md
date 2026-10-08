# Security Architecture

A segurança começa pela separação de código, dados e credenciais. Nenhum `.env` real, token, chave ou sessão do Baluarte entra no Cosmos. O browser recebe somente dados públicos e capacidades explicitamente permitidas.

A futura arquitetura deve definir autenticação, autorização, RBAC, sessões, validação, sanitização, rate limiting, logging, auditoria, isolamento de workers, supply chain, backup e recuperação. Iframes devem validar `origin` e `source`; datasets não devem ser inseridos como HTML arbitrário.

A reconstrução deve usar schema próprio para usuários e permissões. O banco antigo não é uma autoridade automática. Cada integração externa deve possuir threat model, política de falha e segredo armazenado fora do Git.

## Defesa em profundidade e múltiplas linguagens

Consulte [Modelo de segurança multicamada e contratos entre linguagens](MULTI_LANGUAGE_SECURITY_MODEL.md). A quantidade de linguagens não é um controle de segurança por si só. Cada camada deve ter responsabilidade explícita, contrato validado, privilégio mínimo, observabilidade e testes de falha.

A autorização deve ser aplicada no servidor em cada operação protegida e, quando aplicável, reforçada por constraints e políticas do banco. Falhas, timeouts, respostas malformadas ou políticas indisponíveis devem negar a operação protegida, nunca conceder acesso por fallback. A validação no frontend é apenas uma ajuda de UX, não uma fronteira de segurança.

C#/.NET só deve ser adicionado se uma avaliação demonstrar benefício operacional ou técnico concreto. C++ não deve ser adicionado apenas para dificultar ataques; uma camada nativa aumenta o custo de segurança e manutenção sem corrigir automaticamente falhas de autorização, lógica ou configuração.

Nenhum controle isolado garante segurança. Antes de produção, testar autorização por recurso, isolamento entre tenants, falhas de serviços, exposição de segredos, dependências e configuração de deployment.
