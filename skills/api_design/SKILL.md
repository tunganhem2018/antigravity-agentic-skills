---
name: api_design
router_kit: FullStackKit
description: RESTful, GraphQL ve modern API mimarileri tasarımı, dökümantasyonu ve standartları.
metadata:
  skillport:
    category: backend
    tags: [api, rest, graphql, openapi, design-patterns]
---

# 🔌 API Design

Sürdürülebilir, ölçeklenebilir ve kullanıcı dostu arayüz tasarımı.

---

## 🔄 Workflow

> **Kaynak:** [Microsoft API Design Guidelines](https://github.com/microsoft/api-guidelines) & [Google API Design Guide](https://cloud.google.com/apis/design)

### Aşama 1: Sözleşme ve Modelleme (Contract & Modeling)
- [ ] **Resource Modeling:** Kaynakları (Users, Posts, Orders) ve aralarındaki ilişkileri belirle.
- [ ] **Protocol Selection:** İhtiyaca göre REST, GraphQL veya gRPC seçimini yap.
- [ ] **Spec First:** Kod yazmadan önce OpenAPI (Swagger) veya GraphQL Schema dökümanını oluştur.

### Aşama 2: Standartlar ve Güvenlik (Standards & Security)
- [ ] **Naming Conventions:** Kebab-case, camelCase veya snake_case standartlarından birini seç ve tutarlı kal.
- [ ] **Status Codes:** Doğru HTTP statü kodlarını (200, 201, 400, 401, 403, 404, 500) eşleştir.
- [ ] **Security Layer:** Authentication (OAuth2, JWT) ve Rate Limiting politikalarını belirle.

### Aşama 3: Sürümleme ve Dökümantasyon (Versioning & Docs)
- [ ] **Versioning Path:** API sürümünü (v1, v2) URL veya Header üzerinden yönetme stratejisini kur.
- [ ] **Developer Experience:** Örnek istekler (Curl) ve hata mesajı formatlarını netleştir.
- [ ] **Breaking Changes Strategy:** Geriye dönük uyumluluk ve "Deprecation" planını hazırla.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1     | API uç noktaları (Endpoints) "Noun-based" mi? (Örn: `/users` yerine `getUsers` değil) |
| 2     | Hata mesajları son kullanıcıyı bilgilendirirken sistem sırlarını ifşa ediyor mu? |
| 3     | Dökümantasyon canlı (Swagger/Redoc) ve güncel mi? |

---
*API Design v1.4 - Evidence-Based Update*
