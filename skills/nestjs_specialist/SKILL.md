---
name: nestjs_specialist
router_kit: FullStackKit
description: NestJS kurumsal mimari, Dependency Injection ve microservices gelişimi.
metadata:
  skillport:
    category: development
    tags: [accessibility, api integration, backend, browser apis, client-side, components, css3, debugging, deployment, frameworks, frontend, fullstack, html5, javascript, libraries, nestjs specialist, node.js, npm, performance optimization, responsive design, seo, state management, testing, typescript, ui/ux, web development]      - enterprise
---

# 🦁 NestJS Specialist

> Kurumsal düzeyde Node.js uygulamaları mimarisi ve geliştirme.

---

*NestJS Specialist v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [NestJS Official Documentation](https://docs.nestjs.com/)

### Aşama 1: Module & DI Setup
- [ ] **Modules**: Uygulamayı mantıksal parçalara (UserModule, OrderModule) böl.
- [ ] **Providers**: İş mantığını `Services` ve `Repositories` içine alıp Dependency Injection ile yönet.

### Aşama 2: Middleware & Pipes
- [ ] **Validation**: Gelen veriyi (DTO) `ValidationPipe` ve `class-validator` ile doğrula.
- [ ] **Guards**: Yetkilendirme (RBAC/Auth) katmanlarını `Guards` ile koru.
- [ ] **Interceptors**: Response formatını standartlaştırmak için interceptor kullan.

### Aşama 3: Infrastructure & Integration
- [ ] **DB**: TypeORM veya Prisma entegrasyonunu yap.
- [ ] **OpenAPI**: Swagger/OpenAPI entegrasyonu ile döküman üret.
- [ ] **Microservices**: Gerekirse Redis/SQS/NATS transport katmanlarını kur.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Kod "Circular Dependency" hatası veriyor mu? |
| 2 | Hatalar `ExceptionFilters` ile merkezi yönetiliyor mu? |
| 3 | Gereksiz yere `any` tipi kullanıldı mı? |
