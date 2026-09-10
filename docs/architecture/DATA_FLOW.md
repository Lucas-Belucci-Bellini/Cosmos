# Data Flow

Dados entram por fonte documentada, passam por normalização e validação, recebem versão e checksum e só então são expostos por um loader de módulo. A UI consome contratos, não arquivos brutos.

```text
Source → Ingestion/Adapter → Validation → Versioned Dataset → Module Loader → UI
                              ↘ checksum / provenance / tests
```

Datasets grandes devem ser carregados sob demanda. Dados pessoais e estado de usuário devem seguir um fluxo separado, com autenticação, autorização, retenção e auditoria.
