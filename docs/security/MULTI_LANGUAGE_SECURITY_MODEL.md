# Modelo de segurança multicamada e contratos entre linguagens

## Estado

**PROPOSTA PARA REVISÃO — NÃO IMPLEMENTADA.** Usar mais linguagens não torna automaticamente um sistema mais difícil de quebrar. Linguagens diferentes podem ajudar a isolar responsabilidades, mas também aumentam dependências, interfaces, configurações, pontos de falha e o custo de revisão.

## Decisão recomendada para o Cosmos

Não adicionar C++ apenas para “proteger o site”. A stack-alvo já prevê TypeScript, Rust e Python; adicionar C# ou C++ exige um requisito concreto, um protótipo, uma comparação de custo/risco e testes que provem benefício.

- **TypeScript:** interface e, se aprovado, endpoints de aplicação; nunca confiar em validação feita apenas no navegador.
- **Rust:** runtime local e operações de sistema operacional com permissões mínimas. Não é uma barreira mágica contra ataques.
- **Python:** tarefas de IA/pipelines isoladas, com limites de recursos e contratos validados.
- **PostgreSQL:** constraints, transações e políticas de acesso no banco quando aplicáveis; credenciais privilegiadas nunca no cliente.
- **C#/.NET:** alternativa válida para um backend dedicado se houver requisito operacional claro (hosting, bibliotecas, deployment ou manutenção), não uma camada extra por obscuridade.
- **C++:** reservar para componentes nativos que realmente precisem dele e tenham justificativa de desempenho/compatibilidade. Não recomendá-lo como gateway web genérico: aumenta a responsabilidade de segurança de memória e não elimina falhas de autorização ou lógica.

## O que significa “uma linguagem pergunta para outra”

A ideia pode ser implementada como **verificação independente de políticas por contratos**, não como confiança cega entre serviços:

1. A API recebe a solicitação e autentica a identidade no servidor.
2. A API valida schema, tamanho, formato e limites do pedido.
3. O serviço de autorização verifica identidade, ação, recurso, tenant e contexto usando uma política versionada.
4. A operação só continua quando a decisão é explicitamente allow; timeout, resposta inválida, erro ou indisponibilidade resultam em negação para operações protegidas.
5. O serviço de dados também aplica as suas próprias restrições relevantes. Não se deve confiar que a camada anterior já verificou tudo.
6. A decisão e o resultado são auditados sem gravar tokens, segredos ou dados sensíveis desnecessários.

Um segundo serviço não deve receber autoridade irrestrita nem aceitar um simples isAdmin: true enviado pelo cliente. Deve receber um contrato mínimo, validar emissor/audiência/expiração quando houver credenciais assinadas, limitar a rede e ter credenciais próprias com privilégio mínimo.

## Contrato mínimo de decisão

Exemplo conceitual, não é código de produção:

```json
{
  "contractVersion": 1,
  "subject": "user-id",
  "action": "project.read",
  "resource": "project-id",
  "tenant": "tenant-id",
  "requestId": "correlation-id"
}
```

Resposta conceitual:

```json
{
  "contractVersion": 1,
  "decision": "deny",
  "reasonCode": "POLICY_NOT_SATISFIED",
  "requestId": "correlation-id"
}
```

O serviço deve validar o schema e os limites; a API deve rejeitar respostas desconhecidas ou malformadas. Não devolver detalhes internos da política ao usuário final. Os exemplos não contêm tokens ou segredos e não devem ser interpretados como autenticação.

## Controles obrigatórios antes de produção

- Autenticação no servidor e autorização em cada operação protegida.
- Negação por padrão e menor privilégio; isolamento entre tenants.
- Validação no servidor, queries parametrizadas e prevenção de injeção.
- Proteção contra CSRF quando aplicável, CORS restrito e cookies de sessão seguros.
- Rate limiting, limites de payload/tempo/conexões e tratamento de abuso.
- Gestão de segredos fora do Git, rotação e nenhuma chave privilegiada no bundle do browser.
- Logs de auditoria com redaction; nunca registar passwords, tokens ou conteúdo sensível desnecessário.
- Atualização de dependências, análise estática, testes negativos e revisão de configuração de deploy.
- Testes de falha: serviço de política indisponível, timeout, JSON inválido, identidade expirada, tenant divergente, permissão ausente e tentativa de acesso direto ao banco/API.
- Revisão de threat model e testes de segurança antes de declarar qualquer camada “segura”.

## Critérios para escolher C# ou C++

Antes de introduzir outra linguagem, comparar pelo menos: ameaça mitigada, ganho demonstrável, novas fronteiras de confiança, dependências, latência, deployment, observabilidade, testes, manutenção e capacidade de atualização. Se não houver ganho medido e responsável pela manutenção, manter a stack menor.

## Critérios de aceite

1. Diagrama de fronteiras de confiança e fluxos de identidade aprovado.
2. Contratos versionados com schema e política de compatibilidade.
3. Testes demonstram que erros e timeouts nunca viram autorização.
4. Testes demonstram que chamadas diretas sem autorização são recusadas.
5. Segredos privilegiados ausentes do frontend e dos repositórios.
6. Testes de isolamento de tenant e autorização por recurso.
7. Análise de dependências e revisão de segurança registradas.
8. Só então decidir, por ADR, se um serviço adicional em C# ou outra linguagem se justifica.

## Referências

- OWASP, [Security Principles](https://devguide.owasp.org/en/02-foundations/03-security-principles/): defesa em profundidade, mediação completa e simplicidade.
- OWASP, [Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html): não depender de um único framework/controle para autorização.
- OWASP, [Top 10 Proactive Controls — Secure Architecture](https://top10proactive.owasp.org/the-top-10/c4-secure-architecture/): reduzir superfície de ataque e projetar para falha de uma camada.
- OWASP, [C-Based Toolchain Hardening](https://cheatsheetseries.owasp.org/cheatsheets/C-Based_Toolchain_Hardening_Cheat_Sheet.html): endurecimento de toolchain C/C++; isto complementa, não substitui, desenho e testes de segurança.

## Limitação desta etapa

A documentação não representa uma implementação. O package.json não foi encontrado na raiz atual do Cosmos durante esta inspeção; portanto, não há base confirmada para adicionar código executável, dependências ou afirmar que testes passaram. A próxima etapa deve inspecionar a estrutura real do branch padrão e implementar uma fatia pequena com testes, se existir uma base executável.
