# Cosmos Master Plan

## Visão

O Cosmos será uma reconstrução modular, documentada e testável das capacidades relevantes descobertas no Projeto-Baluarte. O Cosmos não será uma cópia menor do Baluarte. O Baluarte permanece como arquivo histórico, fonte de requisitos, dados, assets e conhecimento.

## Regra de trabalho

> **Entender → Documentar → Classificar → Planejar → Decidir → Reconstruir → Testar.**

Nenhum módulo importante deve ser implementado antes de possuir objetivo, fronteiras, dependências, dados, riscos, método de migração e critérios de aceitação documentados.

## Escopo inicial

A Fase 0 cobre descoberta, inventário, classificação de migração, arquitetura proposta, análise de storage, catálogo funcional, dados, assets, integrações, segurança e testes. A implementação do shell, Arsenal ou outros módulos permanece bloqueada até a aprovação da fundação documental.

## Não-escopo

Não fazem parte da Fase 0 a cópia integral do Baluarte, a migração de credenciais, a migração de todo o `scripts/arma3`, a reprodução obrigatória do banco antigo, a importação indiscriminada de assets e a implementação de funcionalidades aleatórias.

## Descobertas atuais

O checkout do Baluarte possui aproximadamente **3.706,57 MiB**. O Git pack possui aproximadamente **4,18 GiB**. `scripts/arma3` consome cerca de **3.300,61 MiB**, principalmente modelos `.p3d`. O checkout contém aproximadamente 3.096,53 MiB em `.p3d`, 232,66 MiB em `.webp` e 232,52 MiB em JSON. Isso confirma que o problema não é apenas código-fonte.

## Arquitetura proposta

A proposta é separar Web/UI, API, Core, Data, Workers, AI, Storage e Infrastructure. A decisão final depende da comparação em `docs/architecture/TECHNOLOGY_DECISION.md`. O código de origem do Baluarte não define a arquitetura do Cosmos.

## Critérios de aceitação de módulos

Um módulo só entra no Cosmos quando possuir documentação própria, contrato de montagem, dados classificados, origem registrada, método de migração, testes, limites de dependência, comportamento de erro e decisão de storage.

## Roadmap

- **Phase 0 — Discovery:** inventário e decisões.
- **Phase 1 — Foundation:** tecnologia, estrutura, CI, testes e observabilidade.
- **Phase 2 — Core:** contratos, storage e runtime modular.
- **Phase 3 — Application:** shell, J.A.R.V.I.S. V7 e módulos selecionados.
- **Phase 4 — Integrations:** APIs e serviços externos aprovados.
- **Phase 5 — Optimization:** performance, cache e datasets sob demanda.
- **Phase 6 — Production:** deploy, backup, segurança operacional e suporte.
- **Phase 7 — Future:** módulos adiados e novas capacidades.

## Referências

[1]: https://github.com/Lucas-Belucci-Bellini/Projeto-Baluarte "Projeto Baluarte — fonte histórica"
[2]: https://github.com/Lucas-Belucci-Bellini/NEXORA "NEXORA — referência de planejamento e arquitetura"
[3]: https://github.com/Lucas-Belucci-Bellini/Cosmos "Cosmos — reconstrução modular"
