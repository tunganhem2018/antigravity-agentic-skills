---
name: database_design
router_kit: FullStackKit
description: Veritabanı şeması, normalizasyon ve ER diyagramı tasarımı.
metadata:
  skillport:
    category: database
    tags: [big data, cleaning, csv, data analysis, data engineering, data science, database, database design, etl pipelines, export, import, json, machine learning basics, migration, nosql, numpy, pandas, python data stack, query optimization, reporting, schema design, sql, statistics, transformation, visualization]      - modeling
---

# 🏛️ Database Design

> Veritabanı şeması ve veri modelleme.

---

*Database Design v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [Database Design Guide (Agile Data)](http://www.agiledata.org/essays/databaseDesign.html)

### Aşama 1: Requirements Analysis
- [ ] **Entities**: Nesneleri (User, Order, Product) belirle.
- [ ] **Attributes**: Her nesnenin özelliklerini tanımla.

### Aşama 2: Logical Design (ERD)
- [ ] **Relationships**: One-to-one, One-to-many, Many-to-many bağlarını kur.
- [ ] **Normalization**: 1NF, 2NF, 3NF kurallarına göre şemayı optimize et.

### Aşama 3: Physical Design
- [ ] **Data Types**: En uygun veri tiplerini (`INT`, `VARCHAR`, `JSONB`) seç.
- [ ] **Keys**: PK (Primary Key) ve FK (Foreign Key) alanlarını belirle.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Veri tekrarı (Redundancy) minimize edildi mi? |
| 2 | Referans bütünlüğü (Referential Integrity) sağlandı mı? |
| 3 | Gelecekteki büyüme (Scaling) için şema esnek mi? |
