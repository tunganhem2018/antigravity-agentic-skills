---
name: microservices_patterns
router_kit: FullStackKit
description: Microservices uygulama desenleri, Saga, CQRS ve API Composition.
metadata:
  skillport:
    category: architecture
    tags: [architecture, automation, best practices, clean code, coding, collaboration, compliance, debugging, design patterns, development, documentation, efficiency, git, microservices patterns, optimization, productivity, programming, project management, quality assurance, refactoring, software engineering, standards, testing, utilities, version control, workflow]      - design-patterns
---

# 🧩 Microservices Patterns

> Dağıtık sistemlerin problemlerini çözen spesifik desenler.

---

*Microservices Patterns v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [Microservices.io Patterns](https://microservices.io/patterns/index.html)

### Aşama 1: Pattern Selection
- [ ] **Data Consistency**: Güçlü tutarlılık gerekiyorsa **2PC** (nadiren), nihai tutarlılık için **Saga** seç.
- [ ] **Querying**: Karmaşık joinler gerekiyorsa **CQRS** veya **API Graph Composition** uygula.
- [ ] **Resilience**: Dış bağımlılıklar için **Circuit Breaker** ve **Bulkhead** tanımla.

### Aşama 2: Implementation
- [ ] **Idempotency**: Tüm "Retry" edilebilir operasyonlar için idempotency key mekanizmasını kur.
- [ ] **Outbox Pattern**: Veritabanı write ve event publish atomic olmalı (Transaction Log Tailing veya Polling).
- [ ] **Sidecar**: Cross-cutting concern'leri (logging, auth, tracing) sidecar proxy'ye devret.

### Aşama 3: Validation
- [ ] **Chaos Testing**: Bağımlılıkları kapatarak resilience pattern'lerin çalıştığını test et.
- [ ] **Contract Testing**: Pact benzeri araçlarla servis kontratlarını doğrula.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Saga pattern'de "Compensating Transaction"lar (rollback) tanımlı mı? |
| 2 | Circuit Breaker açıldığında (Open State) fallback mekanizması çalışıyor mu? |
| 3 | Event şeması evrimi (Schema Registry) geriye dönük uyumlu mu? |
