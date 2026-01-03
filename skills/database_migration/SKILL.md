---
name: database_migration
router_kit: FullStackKit
description: Database schema migrasyonları, rollback stratejileri ve zero-downtime yaklaşımları.
metadata:
  skillport:
    category: development
    tags: [accessibility, api integration, backend, browser apis, client-side, components, css3, database migration, debugging, deployment, frameworks, frontend, fullstack, html5, javascript, libraries, node.js, npm, performance optimization, responsive design, seo, state management, testing, typescript, ui/ux, web development]      - database-design
---

# 🚀 Database Migration

> Veritabanı şema ve veri migrasyonu rehberi.

---

## 📋 Migration Patterns

### 1. Schema Migration (DDL)
- **Tooling**: Prisma Migrate, Drizzle Kit, Liquibase, Flyway.
- **Goal**: Version-controlled DB structure.

### 2. Data Migration (DML)
- **Tooling**: Custom scripts, dbt.
- **Goal**: Transform data from old schema to new.

---

## 🛡️ Best Practices

- **Atomic Migrations**: Her migrasyon bağımsız ve geri alınabilir (Rollbackable) olmalı.
- **Pre-deployment Testing**: Proda çıkmadan önce staging ortamında mutlaka test et.
- **Idempotency**: Migrasyon scriptleri birden fazla kez çalıştırıldığında aynı sonucu vermeli.

---

## ⏪ Rollback Strategy Example

```javascript
export const up = async (db) => {
  await db.schema.alterTable('users', (t) => {
    t.addColumn('phone', 'varchar(20)');
  });
};

export const down = async (db) => {
  await db.schema.alterTable('users', (t) => {
    t.dropColumn('phone');
  });
};
```

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

---
*Database Migration v1.5 - With Workflow*
