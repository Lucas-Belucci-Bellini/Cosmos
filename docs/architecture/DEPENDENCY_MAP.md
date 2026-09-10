# Dependency Map

| Camada | Pode depender de | Não deve depender de |
|---|---|---|
| UI | contratos de módulo, design system | secrets, arquivos brutos gigantes, banco direto |
| Modules | core, data contracts, adapters | páginas de outros módulos |
| Core | bibliotecas estáveis e contratos | detalhes de uma página específica |
| Data | schemas, loaders, manifests | DOM e APIs visuais |
| Adapters | SDK/API externa | estado visual global |
| Workers | jobs, data, storage | lifecycle do browser |
| Infrastructure | build, deploy, observability | lógica editorial de módulos |

O grafo real deve ser gerado quando a fundação existir. Durante a Fase 0, esta matriz impede copiar o grafo de dependências do Baluarte sem análise.
