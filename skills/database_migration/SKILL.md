---
name: database_migration
router_kit: FullStackKit
description: Veritabanı şema değişimi, veri taşıma ve rollback stratejileri.
metadata:
  skillport:
    category: database
    tags: [big data, cleaning, csv, data analysis, data engineering, data science, database, database migration, etl pipelines, export, import, json, machine learning basics, migration, nosql, numpy, pandas, python data stack, query optimization, reporting, schema design, sql, statistics, transformation, visualization]      - schema-change
---

# 🚚 Database Migration

> Şema değişimi ve veri taşıma yönetimi.

---

*Database Migration v1.5 - With Workflow*

## 🔄 Workflow

> **Kaynak:** [Prisma Migration Guide - Zero Downtime](https://www.prisma.io/dataguide/postgresql/database-migrations) & [Liquibase Best Practices](https://docs.liquibase.com/concepts/best-practices.html)

### Aşama 1: Planning & Backup (Safety First)
- [ ] **Backup**: Migrasyon öncesi tam veritabanı yedeği al veya Point-in-Time Recovery (PITR) ayarlarını kontrol et.
- [ ] **Impact Analysis**: Tablo büyüklüğüne göre migrasyonun ne kadar süreceğini ve kilitlenme (Lock) riskini hesapla.
- [ ] **Rollback Script**: Her `up` betiği için mutlaka çalışan bir `down` betiği hazırla.

### Aşama 2: Expand-Contract Strategy (Zero Downtime)
- [ ] **Expand**: Yeni alanları ekle (Backward compatible). Eski kod hala çalışabilir olmalı.
- [ ] **Backfill**: Verileri eski alandan yeni alana (varsa) arka planda küçük paketler halinde kopyala.
- [ ] **Contract**: Tüm kod yeni alanı kullanmaya başladığında eski alanı veya tabloyu kaldır.

### Aşama 3: Validation & Drift Detection
- [ ] **Verification**: Migrasyon sonrası şema bütünlüğünü doğrula.
- [ ] **Schema Drift**: Dosya bazlı şema ile veritabanındaki gerçek şema arasındaki farkları (Drift) kontrol et.
- [ ] **Automation**: Migrasyonu CI/CD sürecine (Github Actions/Gitlab CI) entegre et.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Migrasyon sırasında veritabanı kilitlendi mi? (Lock Analysis) |
| 2 | Rollback testi yapıldı mı ve başarılı oldu mu? |
| 3 | Migrasyon logları merkezi sistemde saklanıyor mu? |
