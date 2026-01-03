---
name: api_design
router_kit: FullStackKit
description: API tasarımı, GraphQL schema, OpenAPI spec, versioning. ⚠️ Tasarım aşaması için kullan. Uygulama/security için → backend-api.
metadata:
  skillport:
    category: development
    tags: [accessibility, api design, api integration, backend, browser apis, client-side, components, css3, debugging, deployment, frameworks, frontend, fullstack, html5, javascript, libraries, node.js, npm, performance optimization, responsive design, seo, state management, testing, typescript, ui/ux, web development]      - openapi
---

# 🔌 API Design

> RESTful ve GraphQL API tasarımı rehberi.

---

*API Design v2.0 - Compact*

## 🔄 Workflow

> **Kaynak:** [Best Practices for API-First Development](https://timebusinesses.com/best-practices-for-api-first-development/)

### Aşama 1: Design Phase (Spec-First)
- [ ] **Define Resources**: Identify nouns (Users, Orders) and relationships.
- [ ] **Draft OpenAPI/Schema**: Write `openapi.yaml` or `schema.graphql` BEFORE coding.
- [ ] **Mocking**: Use tools like Prism/Stoplight to generate mock servers from spec.
- [ ] **Review**: Get stakeholder feedback on the mock API.

### Aşama 2: Implementation
- [ ] **Codegen**: Generate TypeScript types/interfaces from the spec.
- [ ] **Business Logic**: Implement controllers/resolvers connecting to services.
- [ ] **Validation**: Ensure Zod/Joi schemas match the OpenAPI spec.

### Aşama 3: Testing & Security
- [ ] **Contract Testing**: Verify implementation matches spec (e.g., using Dredd/Pact).
- [ ] **Security Audit**: Check Rate Limiting, AuthN/AuthZ scopes.
- [ ] **Error Handling**: Verify standard error responses (RFC 7807).

### Aşama 4: Documentation (Auto)
- [ ] **Publish**: Deploy Swagger UI / Redoc.
- [ ] **Changelog**: Document breaking changes if any (versioning strategy).

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | OpenAPI spec onaylandı (lint geçerli) |
| 2 | Kod ve Spec tipleri senkronize (codegen) |
| 3 | Contract testleri geçiyor |
| 4 | Dokümantasyon canlı ve güncel |
