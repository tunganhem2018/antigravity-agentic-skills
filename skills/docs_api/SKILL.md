---
name: docs_api
router_kit: FullStackKit
description: OpenAPI (Swagger) ve GraphQL dokümantasyonu oluşturma ve yönetimi.
metadata:
  skillport:
    category: documentation
    tags: [accessibility, api integration, backend, browser apis, client-side, components, css3, debugging, deployment, docs api, frameworks, frontend, fullstack, html5, javascript, libraries, node.js, npm, performance optimization, responsive design, seo, state management, testing, typescript, ui/ux, web development]      - openapi
---

# 📚 API Documentation

> Etkileşimli ve standartlara uygun API dokümantasyonu.

---

*API Documentation v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [OpenAPI Specification](https://swagger.io/specification/)

### Aşama 1: Spec Design
- [ ] **OpenAPI**: `swagger.yaml` veya `openapi.json` dosyasını oluştur.
- [ ] **Endpoints**: Tüm rotaları, parametreleri ve response tiplerini tanımla.
- [ ] **Security**: Auth yöntemlerini (Bearer, OAuth) belgele.

### Aşama 2: Generation & UI
- [ ] **Auto-gen**: Koddan doküman üretmek için (Örn: `swagger-jsdoc`, `tsoa`) araçları kur.
- [ ] **UI**: `Swagger UI` veya `Redoc` ile dokümanı görselleştir.
- [ ] **Examples**: Her endpoint için gerçekçi request/response örnekleri ekle.

### Aşama 3: Publishing
- [ ] **Host**: `/docs` veya `/api-docs` rotasında dokümanı yayına al.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Tüm endpointler listelenmiş mi? |
| 2 | Hata kodları (4xx, 5xx) açıkça tanımlanmış mı? |
| 3 | Doküman kodla güncel (Sync) mi? |
