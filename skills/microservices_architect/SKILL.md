---
name: microservices_architect
router_kit: FullStackKit
description: Microservices mimarisi, servis ayrıştırma ve dağıtık sistemler tasarımı. ⚠️ Büyük projeler için kullan. Modüler yapı için → monolithic-modularity.
metadata:
  skillport:
    category: architecture
    tags: [architecture, automation, best practices, clean code, coding, collaboration, compliance, debugging, design patterns, development, documentation, efficiency, git, microservices architect, optimization, productivity, programming, project management, quality assurance, refactoring, software engineering, standards, testing, utilities, version control, workflow]      - distributed-systems
---

# 🏛️ Microservices Architect

> Bağımsız ve ölçeklenebilir mikroservis ekosistemleri tasarımı.

---

*Microservices Architect v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [Microservices Patterns (Chris Richardson)](https://microservices.io/)

### Aşama 1: Decomposition (Servis Dağıtımı)
- [ ] **Bounded Context**: Domain driven design (DDD) prensiplerine göre servis sınırlarını çiz.
- [ ] **Database**: Her servisin kendi veritabanına sahip olmasını sağla (Database-per-service).

### Aşama 2: Communication & Discovery
- [ ] **Protocols**: Sync (REST/gRPC) ve Async (Pub-Sub) iletişim yollarını belirle.
- [ ] **Discovery**: Servislerin birbirini bulabilmesi için "Service Registry" kur.
- [ ] **Gateways**: Tek noktadan erişim için "API Gateway" yapılandır.

### Aşama 3: Observability & Resilience
- [ ] **Tracing**: Servisler arası isteği takip etmek için `Distributed Tracing` ekle.
- [ ] **Patterns**: Cascade hataları önlemek için `Circuit Breaker` uygula.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Servisler birbirinden bağımsız deploy edilebiliyor mu? |
| 2 | Servisler arası "Chatty API" (çok fazla çağrı) problemi var mı? |
| 3 | Bir servis çöktüğünde tüm sistem duruyor mu? |
