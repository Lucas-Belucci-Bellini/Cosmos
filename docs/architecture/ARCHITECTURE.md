# Architecture

O Cosmos será dividido em módulos com contratos explícitos. O shell conhece lifecycle e navegação. Módulos conhecem suas próprias telas e dados. A camada de dados valida schemas. Adapters isolam serviços externos. Storage diferencia Git, banco, object storage, cache e backup.

A arquitetura será orientada por dependências unidirecionais: UI → contratos de módulo → core/data → adapters. Um módulo não deve importar páginas, helpers ou estado privado de outro módulo.

A implementação inicial está bloqueada até a Fase 0 produzir decisões tecnológicas e de segurança aprovadas. O Núcleo V7 existente é material migrado de referência e não define a arquitetura definitiva.
