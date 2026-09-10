# Technology Decision

## Estado

`DISCOVERY`. Esta é uma comparação inicial, não uma decisão final. A reconstrução não deve escolher tecnologia apenas porque o Baluarte usa JavaScript/TypeScript.

## Requisitos

O Cosmos precisa suportar uma UI modular, rotas e lifecycle, validação de dados, APIs, storage externo, testes de navegador e integração futura com IA, automação, desktop/mobile e processamento local. O deploy deve ser compatível com Vercel ou infraestrutura equivalente, sem impedir workers ou backend separado.

## Alternativas

| Área | Alternativas | Avaliação inicial |
|---|---|---|
| Web UI | TypeScript + Vite, React, Svelte | TypeScript é familiar; React/Svelte precisam justificar complexidade e lifecycle. |
| API | TypeScript runtime, Rust, Python | TypeScript acelera produto; Rust é candidato para kernels; Python para dados/IA. |
| Core pesado | TypeScript, Rust, Python | Rust deve ser avaliado por segurança/performance, sem forçar todo o produto a ele. |
| Schemas | JSON Schema, Zod, OpenAPI | Usar contratos formais e geração quando possível. |
| Banco | Postgres/Supabase, SQLite local, object storage | Separar estado transacional de datasets e assets. |
| Deploy | Vercel + serviços, container/PaaS, VM | Decidir conforme API, workers e storage. |

## Proposta provisória

Usar uma arquitetura web TypeScript modular para a superfície inicial, contratos formais de dados e adapters para serviços. Avaliar Rust apenas para processamento pesado ou core determinístico após benchmark. Usar Python apenas quando houver vantagem clara em IA, análise ou pipeline. Essa proposta preserva produtividade sem transformar a linguagem em decisão estética.

## Critérios antes da aprovação

Medir performance, segurança, manutenção, testes, deploy, custo, disponibilidade de bibliotecas, integração com APIs, processamento local, desktop/mobile e banco. A aprovação deve gerar ADR e registrar consequências.
