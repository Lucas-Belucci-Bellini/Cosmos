# External Resources

| ID | Recurso | Classe | Uso observado | Cosmos | Estado |
|---|---|---|---|---|---|
| EXT-001 | Three.js CDN | THIRD_PARTY | Núcleo V7 | manter provisoriamente; avaliar pin/local | DOCUMENTED |
| EXT-002 | Google Fonts | THIRD_PARTY | tipografia V7 | opcional; fallback local | DOCUMENTED |
| EXT-003 | Wikipedia REST API | OPTIONAL | imagens do Arsenal | não bloquear primeira versão | PLANNED |
| EXT-004 | Spotify | OPTIONAL | presença/música J.A.R.V.I.S. | adapter futuro | DISCOVERY |
| EXT-005 | Supabase | THIRD_PARTY | auth/database/realtime observados | schema e políticas próprios | DISCOVERY |
| EXT-006 | Vercel | OFFICIAL/INFRA | deploy antigo | reavaliar depois da arquitetura | DISCOVERY |
| EXT-007 | APIs de mapas/visão/OCR | UNKNOWN/OPTIONAL | módulos diversos | catalogar por endpoint | DISCOVERY |

Credenciais, tokens e secrets não são migrados. Cada recurso aprovado deve ter contrato, autenticação, rate limit, erros, custo, fallback e responsável documentados.
