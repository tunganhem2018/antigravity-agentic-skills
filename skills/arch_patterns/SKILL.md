---
name: arch_patterns
router_kit: FullStackKit
description: Modern yazılım mimarisi desenleri (Microservices, Hexagonal, Clean Architecture) uygulama.
metadata:
  skillport:
    category: architecture
    tags: [architecture, patterns, clean-architecture, hexagonal, ddd]
---

# 🏗️ Architecture Patterns

Yazılımın temel iskeletini oluşturan yapısal desenler ve organizasyon.

---

## 🔄 Workflow

> **Kaynak:** [Refactoring.Guru - Design Patterns](https://refactoring.guru/design-patterns) & [Clean Architecture by Robert C. Martin](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)

### Aşama 1: İhtiyaç Analizi (Needs Analysis)
- [ ] **Karmaşıklık Değerlendirmesi:** Projenin boyutuna göre Monolith mi yoksa Microservices mi gerektiğini analiz et.
- [ ] **Domain Discovery (DDD):** İş mantığının sınırlarını (Bounded Contexts) ve ana aktörleri belirle.
- [ ] **Non-Functional Requirements:** Scalability, Reliability ve Maintainability önceliklerini sırala.

### Aşama 2: Pattern Seçimi ve Implementasyon (Pattern Selection)
- [ ] **Layers:** Katmanlı mimari (UI, Business, Data) veya Clean Architecture (Entities, Use Cases, Web) yapısını kur.
- [ ] **Dependency Rule:** Bağımlılıkların her zaman iç halkalara (İş mantığına) doğru olmasını sağla.
- [ ] **Separation of Concerns:** Veritabanı kodunu iş mantığından, UI kodunu veriden tamamen izole et (Hexagonal/Ports & Adapters).

### Aşama 3: Doğrulama ve Refactor (Validation & Refactor)
- [ ] **Coupling Check:** Bileşenler arası sıkı bağ (Tight Coupling) var mı kontrol et.
- [ ] **Unit Testing:** İş mantığının (Core Logic) dış dünyadan (DB, Web) bağımsız test edilebilirliğini doğrula.
- [ ] **Code Review:** Mimari kuralların ihlal edilip edilmediğini (ArchUnit gibi araçlarla) denetle.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1     | Veritabanı değiştiğinde (Örn: MySQL -> MongoDB) iş mantığı kodunda değişiklik gerekiyor mu? |
| 2     | Yeni bir özellik eklendiğinde mimari buna esneklik sağlıyor mu? |
| 3     | Proje klasör yapısı seçilen mimari deseni yansıtıyor mu? |

---
*Arch Patterns v1.3 - Evidence-Based Update*
