---
name: postgres_pro
router_kit: FullStackKit
description: Advanced PostgreSQL - window functions, CTEs, indexing stratejileri ve performance tuning.
metadata:
  skillport:
    category: database
    tags: [advanced queries, architecture, automation, backend, backup and recovery, best practices, database, database design, indexing, optimization, performance tuning, postgres_pro_1, postgresql, query optimization, replication, scalability, schema design, software engineering, sql, testing, transactions, workflow]      - sql-mastery
---

# 🐘 Postgres Pro (Advanced)

> PostgreSQL derinlemesine sorgu optimizasyonu ve mimari rehberi.

---

## 🚀 Advanced Querying

### Window Functions
```sql
SELECT 
    name, 
    salary, 
    department,
    AVG(salary) OVER(PARTITION BY department) as dept_avg
FROM employees;
```

### Recursive CTEs
```sql
WITH RECURSIVE category_tree AS (
    SELECT id, name, parent_id FROM categories WHERE parent_id IS NULL
  UNION ALL
    SELECT c.id, c.name, c.parent_id 
    FROM categories c 
    JOIN category_tree ct ON c.parent_id = ct.id
)
SELECT * FROM category_tree;
```

---

## ⚡ Indexing & Performance

### Index Tipleri
- **B-Tree**: Genel amaçlı.
- **GIN**: JSONB ve Full-text search için.
- **BRIN**: Çok büyük, zaman damgalı veriler için.
- **Partial Index**: `WHERE active = true` gibi şartlı indexler.

### Analiz Komutları
```sql
EXPLAIN ANALYZE 
SELECT * FROM orders WHERE status = 'shipped';
```

---

## 🔧 Workflow

> **Kaynak:** [PostgreSQL Official Documentation](https://www.postgresql.org/docs/) & [Use The Index, Luke](https://use-the-index-luke.com/)

### Aşama 1: Schema Design & Normalization
- [ ] **Data Types**: Doğru veri tipini seç (`UUID` vs `Serial`, `JSONB` vs `Structured Fields`).
- [ ] **Constraints**: Veri bütünlüğünü veritabanı seviyesinde (`Check`, `Unique`, `Foreign Key`) koru.
- [ ] **Partitioning**: Çok büyük tabloları (`Declarative Partitioning`) zaman veya ID bazlı parçala.

### Aşama 2: Query Optimization
- [ ] **Execution Plans**: Yavaş sorguları `EXPLAIN (ANALYZE, BUFFERS)` ile incele, "Sequential Scan" olan yerleri bul.
- [ ] **Index Hygiene**: Kullanılmayan index'leri temizle, sıkışan (Bloated) index'leri `REINDEX` et.
- [ ] **Connection Pooling**: Uygulama tarafında `PgBouncer` gibi bir pooler kullan.

### Aşama 3: Maintenance & Reliability
- [ ] **VACUUM**: Autovacuum ayarlarını tablo büyüklüğüne göre optimize et.
- [ ] **Backup**: `WAL` (Write Ahead Logging) loglarını ve `pg_dump` yedeklerini düzenli kontrol et.
- [ ] **Monitoring**: `pg_stat_statements` kullanarak en çok yük getiren sorguları takip et.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | `JSONB` kolonları GIN index ile destekleniyor mu? |
| 2 | "N+1" sorgu problemi uygulama tarafında çözüldü mü? |
| 3 | Transaction isolation level (Read Committed vb.) ihtiyaca uygun mu? |

---

*Postgres Pro v1.1 - Enhanced*
