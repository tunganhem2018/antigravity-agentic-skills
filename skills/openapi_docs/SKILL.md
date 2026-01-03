---
name: openapi_docs
router_kit: FullStackKit
description: Proje geneli OpenAPI (Swagger) spesifikasyonu yazımı ve yönetimi.
metadata:
  skillport:
    category: documentation
    tags: [architecture, automation, best practices, clean code, coding, collaboration, compliance, debugging, design patterns, development, documentation, efficiency, git, openapi docs, optimization, productivity, programming, project management, quality assurance, refactoring, software engineering, standards, testing, utilities, version control, workflow]      - api-specs
---

# 📜 OpenAPI Documentation

> Standartlara uygun, interaktif API dökümantasyonu tasarımı.

---

*Openapi Docs v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [OpenAPI 3.1 Specification](https://spec.openapis.org/oas/v3.1.0) & [Stoplight Elements](https://stoplight.io/open-source/elements)

### Aşama 1: Specification Design (Spec-First)
- [ ] **OAS 3.0/3.1**: Doğru versiyonu seç ve ana dosyayı (`openapi.yaml`) oluştur.
- [ ] **Servers**: Geliştirme, Test ve Üretim sunucusu URL'lerini tanımla.
- [ ] **Tags**: Endpointleri mantıksal gruplara ayır.

### Aşama 2: Components & Schemas
- [ ] **Schemas**: Veri modellerini (User, Error, Response) `components/schemas` altında tanımla (DRY).
- [ ] **Parameters**: Header, Query ve Path parametrelerini standardize et.
- [ ] **Security**: Global auth (JWT, API Key) şemalarını belirt.

### Aşama 3: Rendering & Tools
- [ ] **Swagger UI**: Kod veya statik dosya üzerinden Swagger UI yayını yap.
- [ ] **Validation**: `spectral` vb. araçlarla spec dosyasının standartlara uygunluğunu denetle.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Request/Response örnekleri (Examples) güncel mi? |
| 2 | Tüm "Error States" (401, 403, 404, 500) belgelendi mi? |
| 3 | Doküman üzerinden "Try it out" yapılabiliyor mu? |
