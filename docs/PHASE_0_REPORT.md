# Phase 0 Report — Cosmos

## Estado atual

O Cosmos possui uma primeira migração do J.A.R.V.I.S. Núcleo V7 e agora possui a estrutura documental necessária para reconstrução modular. O Projeto-Baluarte não foi alterado e continua sendo a fonte histórica.

## Principais descobertas

A auditoria do checkout do Baluarte encontrou aproximadamente 3.706,57 MiB. O pack Git possui aproximadamente 4,18 GiB. `scripts/arma3` representa cerca de 3.300,61 MiB. A extensão dominante é `.p3d`, com aproximadamente 3.096,53 MiB. Imagens `.webp` representam aproximadamente 232,66 MiB. JSONs representam aproximadamente 232,52 MiB.

O consumo é dominado por modelos e exports gerados do Arma 3. Isso confirma que o Cosmos não deve receber o checkout completo, nem tratar todo o conteúdo histórico como código de runtime.

## Documentação criada

A Fase 0 agora contém Master Plan, índice documental, matriz de migração, política de referência do Baluarte, catálogo funcional, mapa de sistemas, arquitetura inicial, fronteiras, fluxo de dados, mapa de dependências, decisão tecnológica inicial, análise de storage, catálogo de dados, catálogo de assets, recursos externos, segurança, testes, roadmap, ADR de reconstrução e inventário de páginas.

## Reutilizável

O Núcleo V7, pequenos datasets com finalidade definida, documentação técnica, contratos de comportamento e referências visuais podem ser aproveitados após adaptação e validação. Cada item está sujeito à matriz de migração.

## Deve ser refeito

O shell, router, lifecycle de módulos, storage, loaders, contratos de API, banco, autenticação, observabilidade e design system devem ser próprios do Cosmos. O código do Baluarte não deve comandar essas decisões.

## Deve permanecer fora do Git do Cosmos

Modelos `.p3d`, exports gigantes, caches, builds, logs, backups e datasets sem consumidor devem permanecer em archive ou storage externo, registrados por manifest, checksum, origem e versão.

## Próxima fase

A próxima fase deve aprovar a tecnologia e construir a fundação mínima. Depois disso, criar o shell/router, integrar o V7 por contrato próprio e só então reconstruir o Arsenal mínimo.

## Issues fundamentais

As Issues 3 a 10 do repositório Cosmos foram criadas para arquitetura, inventário, storage, fundação, segurança, dados, testes e integração do V7.

## Critério de saída da Fase 0

A Fase 0 pode ser considerada documentada, mas não encerrada como aprovada, até que a decisão tecnológica, as fronteiras de segurança e a política operacional de storage sejam revisadas. A implementação em massa continua bloqueada por decisão.

## Referências

[1]: https://github.com/Lucas-Belucci-Bellini/Projeto-Baluarte "Projeto Baluarte — fonte histórica"
[2]: https://github.com/Lucas-Belucci-Bellini/NEXORA "NEXORA — referência documental"
[3]: https://github.com/Lucas-Belucci-Bellini/Cosmos/issues "Issues fundamentais do Cosmos"
