---
name: backend_api
router_kit: FullStackKit
description: Sağlam, hızlı ve dökümante edilmiş backend API'leri geliştirme süreçleri.
metadata:
  skillport:
    category: backend
    tags: [backend, api, nodejs, express, fastify]
---

# 🏗️ Backend API

Verimli veri işleme ve sunum sağlayan backend servisleri.

---

## 🔄 Workflow

> **Kaynak:** [Express.js Best Practices](https://expressjs.com/en/advanced/best-practice-performance.html) & [NestJS Standards](https://docs.nestjs.com/)

### Aşama 1: İskelet ve Middleware (Setup & Middleware)
- [ ] **Router Yapısı:** Modüler route yönetimini kur (Örn: `routes/user.js`).
- [ ] **Global Middleware:** CORS, Helmet (Güvenlik), Compression (Bant genişliği) ve JSON parsers ekle.
- [ ] **Error Handler:** Tüm uygulama genelinde hataları yakalayan merkezi bir middleware yaz.

### Aşama 2: Business Logic ve DTO (Logic & Validation)
- [ ] **Request Validation:** Zod veya Joi kullanarak gelen verileri (Body, Params, Query) doğrula.
- [ ] **Service Layer:** Veritabanı işlemlerini controller'dan ayırarak servis sınıflarına taşı.
- [ ] **Business Rules:** İş mantığını saf fonksiyonlar ile (Pure Functions) izole et.

### Aşama 3: Performance ve Test (Optimization & Test)
- [ ] **Caching:** Sık sorgulanan verileri Redis veya bellek içi cache ile hızlandır.
- [ ] **Unit/Integration Tests:** API uç noktalarını (Endpoints) Supertest veya benzeri araçlarla test et.
- [ ] **Documentation:** OpenAPI (Swagger) dökümantasyonunu otomatik olarak üret.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1     | Controller'lar "Thin" (ince), servisler "Thick" (kalın) mı? |
| 2     | Hatalar 4xx/5xx standartlarına uygun dönüyor mu? |
| 3     | Veritabanı sorguları (Queries) N+1 problemi içeriyor mu? |

---
*Backend API v1.3 - Evidence-Based Update*
