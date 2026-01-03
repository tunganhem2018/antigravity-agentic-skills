---
name: data_transform
router_kit: FullStackKit
description: ETL süreçleri, veri temizleme ve JSON/CSV/SQL arası dönüşümler.
metadata:
  skillport:
    category: data
    tags: [big data, cleaning, csv, data analysis, data engineering, data science, data transform, database, etl pipelines, export, import, json, machine learning basics, migration, nosql, numpy, pandas, python data stack, query optimization, reporting, schema design, sql, statistics, transformation, visualization]      - etl
---

# 🔄 Data Transform

> Veri dönüştürme ve temizleme (ETL).

---

*Data Transform v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [ETL Best Practices (Informatica)](https://www.informatica.com/resources/articles/what-is-etl.html)

### Aşama 1: Extraction (Kaynaktan Alma)
- [ ] **Source**: Verinin kaynağını (API, DB, File) belirle.
- [ ] **Format**: Ham verinin formatını (JSON, CSV, XML) doğrula.

### Aşama 2: Transformation (Dönüştürme)
- [ ] **Cleaning**: Hatalı veya eksik verileri temizle/doldur.
- [ ] **Mapping**: Kaynak alanları hedef şemaya eşle.
- [ ] **Encoding**: Karakter seti (UTF-8) uyumluluğunu sağla.

### Aşama 3: Loading (Yükleme)
- [ ] **Validation**: Yükleme öncesi son şema kontrolü yap.
- [ ] **Load**: Hedef sisteme veriyi aktar.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Veri kaybı yaşandı mı? |
| 2 | Dönüşüm kuralları tutarlı mı? |
| 3 | Performans (Batch size) optimize mi? |
