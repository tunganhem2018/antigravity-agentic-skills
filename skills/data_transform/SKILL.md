---
name: data_transform
description: Tasarım ve verimlilik odaklı veri dönüşümü (ETL/ELT) süreçleri, dbt ve Polars optimizasyonu.
metadata:
  skillport:
    category: data
    tags: [architecture, automation, best practices, clean code, coding, collaboration, compliance, data transform, database migration, debugging, design patterns, development, documentation, efficiency, git, optimization, productivity, programming, project management, quality assurance, refactoring, software engineering, standards, testing, utilities, version control, workflow]      - etl
---

# 🔄 Data Transformation (ETL/ELT)

> Veri dönüşümü, boru hatları ve optimizasyon rehberi.

---

## 🏗️ Transformation Architectures

### ETL (Extract, Transform, Load)
- **Use Case**: Traditional data warehousing.
- **Tools**: Python (Pandas/Polars), Spark.
- **Benefit**: Cleaner data in early stages.

### ELT (Extract, Load, Transform)
- **Use Case**: Modern cloud data warehouses (Snowflake, BigQuery).
- **Tools**: dbt, SQL.
- **Benefit**: Scalability and flexibility.

---

## 📊 Pipeline Checklist

```markdown
- [ ] Schema validation at source
- [ ] Idempotent transformations
- [ ] Error handling & dead-letter queues
- [ ] Data quality tests (dbt tests)
- [ ] Documentation of lineage
```

## Detailed Topics

### Incremental Processing

```python
def extract_incremental(last_run_date):
    query = f"""
        SELECT * FROM source_table
        WHERE updated_at > '{last_run_date}'
    """
    return pd.read_sql(query, conn)
```

### Error Handling

```python
def safe_transform(data):
    try:
        transformed = transform_data(data)
        return transformed
    except Exception as e:
        logger.error(f"Transform failed: {e}")
        send_alert(f"Pipeline failed: {e}")
        raise
```

## 🔄 Workflow

> **Kaynak:** [dbt Labs - Best Practices](https://docs.getdbt.com/best-practices) & [Polars Performance Guide](https://pola-rs.github.io/polars-book/user-guide/optimizations/lazy/)

### Aşama 1: Data Contract & Source Audit
- [ ] **Data Contracts**: Veri kaynağı (Source) ve hedef (Target) arasındaki şemayı sabitle.
- [ ] **Profiling**: Ham verideki eksikleri, null oranlarını ve tipleri (Profiling) analiz et.
- [ ] **Pattern Selection**: Veri boyutuna göre ETL (Pandas/Polars) veya ELT (SQL/dbt) seçimi yap.

### Aşama 2: Transformation Engine Setup
- [ ] **Infrastructure**: `dbt-core` profilini kur veya Cloud IDE yapılandır.
- [ ] **Modular Modeling**: Veriyi Staging (Renaming), Intermediate (Logic) ve Marts (Final) katmanlarına ayır.
- [ ] **Polars Optimization**: Python tabanlı dönüşümlerde `lazy` modunu (`scan_csv` / `collect`) kullanarak bellek ve hız optimizasyonu yap.

### Aşama 3: Testing & Orchestration
- [ ] **Unit Tests**: Kritik dönüşüm mantığı için `dbt tests` veya `Great Expectations` ile validation yaz.
- [ ] **Idempotency**: Boru hattının (Pipeline) hata durumunda tekrar çalıştırılabilir (Idempotent) olduğundan emin ol.
- [ ] **Orchestration**: İş akışını Airflow veya Dagster üzerinde takvime bağla ve hata bildirimlerini kur.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Dönüşüm sonrası veri kaybı yaşandı mı? (Check Sum) |
| 2 | dbt modellerinde `ref` fonksiyonu dışında hardcoded tablo ismi kullanıldı mı? |
| 3 | Pipeline başarısız olduğunda "Rollback" veya "Reprocessing" stratejisi var mı? |

---
*Data Transformation v2.0 - With Workflow*
