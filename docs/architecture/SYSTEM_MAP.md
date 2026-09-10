# System Map

## Domínios descobertos

| Domínio | Responsabilidade | Estado |
|---|---|---|
| Shell/UI | Navegação, layout, lifecycle e acessibilidade | REBUILD / PLANNED |
| Core | Contratos, eventos, configuração e erros | REBUILD / PLANNED |
| Data | Schemas, loaders, validação e versionamento | REBUILD / DOCUMENTED |
| J.A.R.V.I.S. | Visual V7, contexto, memória e possíveis agentes | V7 migrado; restante DISCOVERY |
| Knowledge | Biblioteca, dossiê, wiki e narrativa | DOCUMENTED |
| Arsenal/Militar | Catálogos, Arma 3, modelos e ferramentas | DOCUMENTED |
| Media | Áudio, vídeo, rádio, FFT e presença | DISCOVERY |
| Integrations | Wikipedia, Spotify, Supabase, CDNs e APIs | DISCOVERY |
| Storage | Git, object storage, cache, backup e manifests | DOCUMENTED |
| Backend/API | Serviços, auth, jobs e contratos | DISCOVERY |
| Infrastructure | Build, deploy, observabilidade e segurança operacional | PLANNED |
| Platforms | Desktop, Android e processamento local | DEFERRED |

## Fronteiras

A UI não deve importar diretamente datasets gigantes nem secrets. A camada Data valida e fornece contratos. Integrações externas ficam atrás de adapters. O storage de objetos não é tratado como filesystem do Git. Workers e IA não devem ser necessários para a primeira renderização do shell.

## Fluxo de alto nível

```text
UI/Shell → Module Contract → Core/Data → Adapter → External Service or Storage
                         ↘ Tests / Observability / Error Boundary
```

O Baluarte é uma fonte externa de conhecimento durante a migração, não uma dependência de runtime.
