# Storage Analysis

## Evidência

A auditoria local do checkout do Baluarte encontrou **3.706,57 MiB**. O Git reportou um pack de aproximadamente **4,18 GiB**. O maior consumidor é `scripts/arma3`, com **3.300,61 MiB**. Por extensão, `.p3d` ocupa **3.096,53 MiB**, `.webp` ocupa **232,66 MiB** e `.json` ocupa **232,52 MiB**.

Os maiores grupos são modelos `.p3d`, exports JSON gerados e imagens do Arma 3. Portanto, a alegação de armazenamento deve separar checkout, histórico Git, build, deploy, storage externo, cache, logs e backup.

## Classificação

| Classe | Política Cosmos |
|---|---|
| Código-fonte | Git, com revisão e limites de tamanho. |
| Documentação | Git, em `docs/`, com links e decisões. |
| Dados pequenos e estáveis | Git, se houver consumidor e schema. |
| Datasets grandes | Storage externo ou download sob demanda. |
| Modelos `.p3d` e exports gerados | Fora do Git; archive/storage externo. |
| Assets selecionados | Git apenas quando pequenos; caso contrário CDN/object storage. |
| Cache, logs e builds | Nunca versionar no repositório principal. |
| Backups | Storage separado, com retenção e teste de restauração. |

## Estratégia

O Git do Cosmos deve conter código, contratos, documentação, schemas e pequenos fixtures de teste. Datasets grandes devem ser versionados por manifesto, checksum, origem, versão e URL de storage. O build deve baixar apenas o conjunto necessário para a funcionalidade construída. O cache deve ser descartável e separado de dados de fonte.

## Controle de duplicidade

Antes de adicionar assets, calcular hash SHA-256 e comparar nome, conteúdo e dimensões. Assets duplicados devem ter um único registro canônico. Assets obsoletos permanecem em archive ou são descartados somente com justificativa.

## Backup e recuperação

Backups devem existir fora do Git, possuir checksum, data, origem e política de retenção. A recuperação deve ser testada periodicamente. O Cosmos não deve depender de um checkout histórico de 4 GiB para recuperar dados essenciais.

## Ferramenta

A auditoria reproduzível está em `scripts/audit_baluarte.py`. A saída bruta está em `docs/infrastructure/STORAGE_AUDIT_RAW.txt`.
