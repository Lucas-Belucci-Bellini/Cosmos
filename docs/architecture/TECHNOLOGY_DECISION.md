# Technology Decision

## Estado

DISCOVERY. Este documento registra a direção desejada para o Cosmos e as decisões que ainda precisam de validação. A stack é escolhida por responsabilidade, contratos e medições — não para forçar todas as partes a usar a mesma linguagem.

## Objetivo arquitetural

Reconstruir no Cosmos as funcionalidades úteis do Projeto-Baluarte, preservando seus comportamentos e dados necessários, mas criando uma implementação modular, testável e com acesso local controlado ao computador. O Baluarte continua como referência histórica; o Cosmos é o produto novo.

## Stack-alvo proposta

| Camada | Tecnologia candidata | Responsabilidade |
|---|---|---|
| Frontend e experiência da IDE | TypeScript + framework web escolhido por ADR | Interface, navegação, editor visual, painel de módulos e estado da aplicação. |
| Ferramentas de frontend | Vite e ferramentas de build/teste compatíveis | Desenvolvimento, build, lint, typecheck e testes de navegador. |
| Runtime local e integração com o sistema operacional | Rust | Operações locais que precisem de desempenho, controle de recursos, segurança de memória e APIs nativas do sistema. |
| IA, agentes e pipelines | Python | Orquestração de IA, avaliação, preparação de dados e integração com bibliotecas de ML. |
| API e serviços | TypeScript ou Rust, por caso de uso | Endpoints e serviços de aplicação; a escolha depende de deployment, carga e limites de segurança. |
| Contratos entre linguagens | JSON Schema/OpenAPI e mensagens versionadas | Tipos, validação, erros, compatibilidade e evolução entre UI, runtime e serviços de IA. |
| Dados transacionais | PostgreSQL/Supabase ou SQLite local, conforme o modo | Estado de conta, configurações e dados estruturados. |
| Assets e datasets grandes | Object storage/CDN com manifestos e checksums | Evitar que o Git carregue arquivos gerados, caches ou grandes coleções de mídia. |

## Integração local com o PC e ferramentas de programação

O acesso ao sistema operacional deve ficar numa camada Rust explícita, com permissões mínimas e operações auditáveis. A interface TypeScript não deve executar comandos locais arbitrários nem acessar arquivos sem uma API autorizada. A camada de IA Python deve pedir operações por contratos definidos, e não obter acesso irrestrito ao computador.

Antes de implementar recursos de IDE, definir limites para leitura/escrita de arquivos, projetos permitidos, execução de processos, cancelamento, logs, permissões, tratamento de erros e proteção contra caminhos fora do workspace. Não executar código de projeto automaticamente sem ação e contexto explícitos do usuário.

## Regras de fronteira

- UI TypeScript → contratos de módulo/API → Core/serviços → adaptadores Rust, Python, banco ou serviços externos.
- Rust não deve absorver tarefas de IA que sejam mais bem atendidas pelo ecossistema Python.
- Python não deve ser necessário para a primeira renderização da interface.
- A UI não importa diretamente arquivos internos de outro módulo nem datasets grandes.
- Comunicação entre processos deve ser versionada, validada e limitada; não depender de detalhes internos de implementação.
- Segredos, tokens e arquivos .env reais nunca são migrados do Baluarte.
- O código do Baluarte não define automaticamente dependências, permissões ou arquitetura do Cosmos.

## Estratégia de seleção do framework frontend

Avaliar React, Vue e Svelte com TypeScript a partir de critérios concretos: acessibilidade, lifecycle de módulos, roteamento, ecossistema, testes, complexidade, compatibilidade com a interface desejada e manutenção. A decisão final deve ser registrada num ADR antes da fundação de produção. Vite é ferramenta de build/desenvolvimento, não framework de interface.

## Critérios antes de aprovar a stack

1. Benchmark pequeno e reproduzível para as operações locais que realmente precisem de Rust.
2. Protótipo de contrato entre TypeScript e o runtime local.
3. Protótipo controlado de chamada da camada de IA Python.
4. Testes de segurança de permissões, validação, cancelamento e falhas.
5. Comparação de frameworks frontend e estratégia de testes.
6. Avaliação de empacotamento, atualização, logs, deploy, custo e suporte a Windows.
7. ADR que registra decisão, alternativas rejeitadas, consequências e plano de migração.

## Estado da decisão

A direção TypeScript + Rust + Python está registrada como alvo de projeto. Framework frontend, transporte entre processos, empacotamento desktop e divisão final dos serviços permanecem pendentes de protótipos e ADR. Não declarar a stack final aprovada até os critérios acima serem verificados.
