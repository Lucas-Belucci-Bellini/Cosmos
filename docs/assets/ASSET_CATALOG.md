# Asset Catalog — Baluarte → Cosmos

## Política

Assets devem ser registrados por origem, licença conhecida, finalidade, hash, tamanho, duplicidade e destino. Um asset grande só entra no Cosmos com estratégia de storage explícita.

| ID | Grupo | Origem | Evidência de tamanho | Destino inicial | Método | Status |
|---|---|---|---:|---|---|---|
| AST-001 | modelos Arma 3 `.p3d` | `scripts/arma3/out/modelos` | parte dos 3.096,53 MiB em `.p3d` | archive/object storage | ARCHIVE | DOCUMENTED |
| AST-002 | imagens Arma 3 `.webp` | `public/arma3` | 232,66 MiB em `.webp` | storage por módulo | ADAPT | DOCUMENTED |
| AST-003 | modelos web `.glb` | `public/modelos-3d` | 22,60 MiB em `.glb` | selecionar por rota | ADAPT | DISCOVERY |
| AST-004 | fontes e estilos | `src/styles`, configurações | pequeno | design system Cosmos | REBUILD | PLANNED |
| AST-005 | áudio `.mp3` | diretórios de mídia | 5,36 MiB | avaliar licença/uso | REFERENCE | DISCOVERY |
| AST-006 | PDFs e documentos | raiz/docs | 28,48 MiB em PDF | archive/document storage | ARCHIVE | DOCUMENTED |
| AST-007 | screenshots e PNGs | raiz/public/docs | 13,55 MiB em PNG | catálogo por finalidade | REFERENCE | DISCOVERY |

## Próximos campos obrigatórios

Para cada asset selecionado, adicionar checksum, dimensões, licença ou origem conhecida, consumidor, transformação permitida, política de cache e destino final. Não copiar a pasta `public/arma3` inteira.
