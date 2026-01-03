---
name: event_driven
router_kit: FullStackKit
description: Event-driven mimari, Pub/Sub, Redis Streams ve Kafka kullanımı. ⚠️ Ölçeklenebilir sistemler için kullan. Basit iletişim için → webhooks.
metadata:
  skillport:
    category: architecture
    tags: [architecture, automation, best practices, clean code, coding, collaboration, compliance, debugging, design patterns, development, documentation, efficiency, event driven, git, optimization, productivity, programming, project management, quality assurance, refactoring, software engineering, standards, testing, utilities, version control, workflow]      - pub-sub
---

# ⚡ Event-Driven Architecture

> Asenkron ve gevşek bağlı (loosely coupled) sistem tasarımı.

---

*Event Driven v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [Enterprise Integration Patterns](https://www.enterpriseintegrationpatterns.com/) & [AWS Event-Driven Guide](https://aws.amazon.com/event-driven-architecture/)

### Aşama 1: Event Design
- [ ] **Schema**: Event payload'unu (JSON) tanımla ve versiyonla (`v1`).
- [ ] **Granularity**: "OrderCreated" (Fat) vs "OrderReference" (Thin) kararını ver.
- [ ] **Idempotency**: Her event'e unique `event_id` ekle.

### Aşama 2: Architecture Setup
- [ ] **Producer**: Event fırlatma noktasını belirle (Transaction sonrası?).
- [ ] **Broker**: Kafka/RabbitMQ/SQS seçimini load/latency ihtiyacına göre yap.
- [ ] **Consumer**: Hata durumunda (DLQ) retry stratejisini kur.

### Aşama 3: Monitoring
- [ ] **Tracing**: OpenTelemetry ile request zincirini (Producer -> Broker -> Consumer) izle.
- [ ] **Lag**: Consumer lag süresini monitör et (Alarm kur).

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Event schema değişikliği geriye dönük uyumlu mu? |
| 2 | Aynı event iki kere gelirse sistem bozuluyor mu? |
| 3 | Sistem çöküp kalktığında kayıp mesaj var mı? |
