---
name: graphql_architect
router_kit: FullStackKit
description: GraphQL schema design, Apollo Server, resolvers ve n+1 query optimizasyonu.
metadata:
  skillport:
    category: development
    tags: [accessibility, api integration, backend, browser apis, client-side, components, css3, debugging, deployment, frameworks, frontend, fullstack, graphql architect, html5, javascript, libraries, node.js, npm, performance optimization, responsive design, seo, state management, testing, typescript, ui/ux, web development]      - query-language
---

# 🕸️ GraphQL Architect

> Performanslı ve ölçeklenebilir GraphQL API mimarisi.

---

*GraphQL Architect v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [GraphQL Best Practices](https://graphql.org/learn/best-practices/) & [Apollo Client/Server Guide](https://www.apollographql.com/docs/)

### Aşama 1: Schema Design (SDL)
- [ ] **Types**: Veri modellerini (Query, Mutation, Subscription) tanımla.
- [ ] **Directives**: Özel kurallar (Auth vb.) için directive'leri belirle.

### Aşama 2: Implementation (Resolvers)
- [ ] **Execution**: Alan bazlı (Field-level) resolver fonksiyonlarını yaz.
- [ ] **Batching**: N+1 problemini çözmek için `DataLoader` kullan.

### Aşama 3: Performance & Security
- [ ] **Complexity**: Çok derin sorguları (Deep nesting) engellemk için depth limit koy.
- [ ] **Caching**: Response veya Persisted query caching stratejisini kur.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Şema dökümantasyonu ototmatik üretiliyor mu? |
| 2 | Veritabanı sorguları (DB Queries) optimize edildi mi? |
| 3 | Hassas veriler resolver seviyesinde yetki kontolüne tabi mi? |
