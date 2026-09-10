# Database Overview

O Cosmos ainda não possui banco próprio aprovado. O banco antigo do Baluarte não será reproduzido automaticamente.

O modelo futuro deve separar identidade, preferências, estado de módulos, conteúdo editorial, telemetria e jobs. Datasets grandes e assets não devem ser tratados como linhas transacionais quando object storage for mais adequado.

## Estado

`DISCOVERY`. Antes da implementação, documentar schema, relacionamentos, índices, constraints, tenancy, permissões, RLS, auditoria, retenção e migrations.
