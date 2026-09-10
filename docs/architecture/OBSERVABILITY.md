# Observability

O Cosmos deve registrar erros de módulo, falhas de carregamento de dados, duração de tarefas e estado de integrações sem registrar segredos ou conteúdo privado desnecessário. Eventos devem possuir versão, módulo, ambiente e correlation id quando houver backend.

# Performance

A primeira renderização não deve depender de datasets grandes ou workers pesados. Módulos devem ser carregados sob demanda. O orçamento de bundle, tempo de boot, memória e tamanho de dataset deve ser definido na Phase 1 e verificado em CI.

## Estado

`PLANNED`. O Baluarte contém sinais e telemetria própria, mas eles serão tratados como referência, não copiados automaticamente.
