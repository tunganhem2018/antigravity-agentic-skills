---
name: backend_database
router_kit: FullStackKit
description: Veritabanı şeması tasarımı, sorgu optimizasyonu ve veri yönetimi stratejileri.
metadata:
  skillport:
    category: backend
    tags: [database, sql, nosql, optimization, modeling]
---

# 🗄️ Backend Database

Veri saklama, modelleme ve hızlı erişim teknikleri.

---

## 🔄 Workflow

> **Kaynak:** [PostgreSQL Performance Tuning Guide](https://wiki.postgresql.org/wiki/Performance_Optimization) & [MongoDB Data Modeling Best Practices](https://www.mongodb.com/developer/products/mongodb/data-modeling-best-practices/)

### Aşama 1: Modelleme ve Şema (Modeling & Schema)
- [ ] **Normalizasyon:** Gereksiz veri tekrarını önlemek için DB normalizasyon seviyelerini (1NF, 2NF, 3NF) uygula.
- [ ] **Index Strategy:** Sık sorgulanan kolonlar için uygun index tiplerini (B-Tree, GIN, Hash) belirle.
- [ ] **Constraints:** Veri bütünlüğü için `Foreign Key`, `Unique` ve `Check` kısıtlarını tanımla.

### Aşama 2: Sorgu Optimizasyonu (Query Optimization)
- [ ] **Explain Analyze:** Yavaş sorguları `EXPLAIN` ile analiz et ve "Sequential Scan"leri engelle.
- [ ] **Connection Pooling:** Veritabanı bağlantılarını verimli kullanmak için pooler (Örn: Prisma Accelerate, PgBouncer) kur.
- [ ] **Denormalization:** Çok yüksek performans gerektiren durumlarda veri tekrarına (Read-optimization) kontrollü izin ver.

### Aşama 3: Yönetim ve Güvenlik (Admin & Security)
- [ ] **Migration Policy:** Şema değişikliklerini sürüm kontrollü araçlarla (Prisma Migrate, Liquibase) yönet.
- [ ] **Backup & Recovery:** Düzenli yedekleme ve felaket anında geri yükleme testlerini planla.
- [ ] **Encryption:** Hassas verileri "At-rest" ve "In-transit" olarak şifrele.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1     | Sorgular büyük veri setlerinde (Big Data) hala hızla çalışıyor mu? |
| 2     | Ölçeklenme için Okuma/Yazma ayrımı (Read Replicas) düşünüldü mü? |
| 3     | SQL Injection saldırılarına karşı hazırlıklı (Prepared Statements) mısın? |

---
*Backend Database v1.4 - Evidence-Based Update*
