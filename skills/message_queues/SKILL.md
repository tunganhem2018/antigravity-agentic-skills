---
name: message_queues
router_kit: FullStackKit
description: RabbitMQ, Redis Pub/Sub ve Kafka ile asenkron message processing ve event-driven mimariler.
metadata:
  skillport:
    category: architectural-pattern
    tags: [architecture, asynchronous, automation, backend, best practices, cloud computing, debugging, decoupling, design patterns, development, distributed systems, documentation, efficiency, event-driven, git, kakfa, message queues, optimization, productivity, quality assurance, rabbitmq, redis, refactoring, scalability, software engineering, standards, testing, utilities, workflow]      - event-driven
---

# 📨 Message Queues

> RabbitMQ, Redis ve Kafka ile asenkron mesaj kuyruğu yönetimi.

---

## 🏗️ Core Concepts

### 1. Producer
Mesajı kuyruğa gönderen servis.

### 2. Queue (Broker)
Mesajın işlenene kadar tutulduğu geçici depo (RabbitMQ, Redis vb.).

### 3. Consumer
Kuyruktaki mesajı çekip işleyen (worker) servis.

---

## 🛠️ Comparison

| Özellik | Redis Pub/Sub | RabbitMQ | Kafka |
|---------|---------------|----------|-------|
| **Kalıcılık** | Yok (Hafızada) | Var | Çok Yüksek |
| **Hız** | Çok Hızlı | Hızlı | Orta/Hızlı |
| **Kayıp Riski** | Var | Düşük | Çok Düşük |
| **Kullanım** | Basit sinyaller | Task queue | Büyük veri/Log |

---

## 🛡️ Reliability Patterns

- **Ack (Acknowledgement)**: Mesajın başarıyla işlendiğinin onaylanması.
- **DLQ (Dead Letter Queue)**: İşlenemeyen hatalı mesajların toplandığı ayrı kuyruk.
- **Retry Logic**: Hata anında belirli aralıklarla (exponential backoff) tekrar deneme.

---

*Message Queues v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [RabbitMQ Tutorials](https://www.rabbitmq.com/getstarted.html) & [CloudAMQP Best Practices](https://www.cloudamqp.com/blog/part1-rabbitmq-best-practice.html)

### Aşama 1: Message Design
- [ ] **Payload**: Mesaj içeriğini (JSON) minimal tut, büyük veri yerine ID gönder.
- [ ] **Idempotency**: Aynı mesaj iki kere işlendiğinde sistem bozulmamalı (Unique ID kontrolü).
- [ ] **TTL**: Mesajın kuyrukta ne kadar kalacağını (Time To Live) belirle.

### Aşama 2: Infrastructure Setup
- [ ] **Connection**: Broker bağlantısını (connection pool) yönet, her mesajda yeni bağlantı açma.
- [ ] **Exchanges**: (RabbitMQ için) Mesajı doğru kuyruğa yönlendirmek için `direct`, `topic` veya `fanout` seç.
- [ ] **Prefetch**: Bir worker'ın aynı anda kaç mesaj alacağını (`prefetch_count`) belirle.

### Aşama 3: Monitoring & Ops
- [ ] **Metric**: Kuyruk derinliğini (Queue length) ve worker cpu kullanımını izle.
- [ ] **Alarms**: Kuyruk dolduğunda veya workerlar çöktüğünde alarm kur.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Worker çöktüğünde kuyruktaki mesajlar kayboluyor mu? (Ack kontrolü) |
| 2 | Mesaj sırası (Ordering) kritik mi? (Kritikse partitioning ayarları yapıldı mı?) |
| 3 | DLQ'ya düşen mesajlar için bir bildirim mekanizması var mı? |
