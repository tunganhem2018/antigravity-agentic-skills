---
name: error_handling
router_kit: FullStackKit
description: Global hata yönetimi, custom error sınıfları ve frontend/backend hata yakalama stratejileri.
metadata:
  skillport:
    category: quality
    tags: [architecture, automation, best practices, clean code, coding, collaboration, compliance, debugging, design patterns, development, documentation, efficiency, error handling, git, optimization, productivity, programming, project management, quality assurance, refactoring, software engineering, standards, testing, utilities, version control, workflow]      - resilience
---

# ⚠️ Error Handling

> Dayanıklı ve hata toleranslı sistemler için stratejiler.

---

*Error Handling v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [Ultimate Guide to Error Handling in Node.js](https://github.com/goldbergyoni/nodebestpractices#-2-error-handling-practices)

### Aşama 1: Classification & Design
- [ ] **Types**: Operasyonel hatalar (Input validation) vs Programcı hataları (Crash) ayrımı yap.
- [ ] **Custom Errors**: HTTP durum kodlarını içeren özel hata sınıfları (`BaseError`, `NotFoundError`) oluştur.

### Aşama 2: Backend Implementation
- [ ] **Try/Catch**: Async işlemler için merkezi `ErrorHandler` middleware'i kur.
- [ ] **Logging**: Hataları bağlamıyla (Context) birlikte logla.

### Aşama 3: Frontend Implementation
- [ ] **Boundary**: React `ErrorBoundary` ile UI çökmelerini engelle.
- [ ] **User Feedback**: Kullanıcıya teknik olmayan, aksiyon alınabilir hata mesajları göster.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Tüm catch blokları loglamaya sahip mi? |
| 2 | Hassas veriler hata mesajıyla dışarı sızıyor mu? |
| 3 | Sistem kritik bir hatada kendini restart edebiliyor mu? |
