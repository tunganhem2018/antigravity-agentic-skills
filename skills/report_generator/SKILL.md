---
name: report_generator
router_kit: FullStackKit
description: Executive rapor, stakeholder presentation ve comprehensive documentation oluşturma rehberi.
metadata:
  skillport:
    category: business
    tags: [big data, cleaning, csv, data analysis, data engineering, data science, database, etl pipelines, export, import, json, machine learning basics, migration, nosql, numpy, pandas, python data stack, query optimization, report generator, reporting, schema design, sql, statistics, transformation, visualization]      - presentation
---

# 📄 Report Generator

> Executive rapor ve dokümantasyon rehberi.

---

*Report Generator v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [Pandas Reporting](https://pandas.pydata.org/docs/user_guide/style.html) & [WeasyPrint Docs](https://doc.courtbouillon.org/weasyprint/)

### Aşama 1: Data Preparation (Automated)
- [ ] **Validation**: Gelen veriyi (CSV/JSON/SQL) Pydantic veya Pandera ile şema kontrolünden geçir.
- [ ] **Aggregation**: Detay veriyi (Raw Data) özetle (Pivot Table, GroupBy). Asla milyon satırı rapora basma.
- [ ] **Anonymization**: Hassas verileri (PII) maskele veya hashle.

### Aşama 2: Generation Architecture
- [ ] **Template Engine**: Jinja2 (Python) veya Handlebars (JS) kullanarak logik ile sunumu ayır.
- [ ] **Format Agnostic**: İçeriği Markdown veya HTML olarak üret, sonra PDF/Excel'e çevir (Single Source).
- [ ] **Styling**: CSS (Print CSS) kullanarak sayfa yapısını (@page), header/footer'ı yönet.

### Aşama 3: Delivery & Feedback
- [ ] **Compression**: Çıktı dosyalarını (PDF/HTML) sıkıştır.
- [ ] **Distribution**: Raporu otomatik e-posta, Slack veya S3 bucket'a gönder.
- [ ] **Actionable**: Raporun başına "Executive Summary" ve "Action Items" ekle.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Rapor oluşturma süresi kabul edilebilir mi? (Async Job kullanılıyor mu?). |
| 2 | Mobil cihazlarda okunabilir mi? (HTML raporlar için Responsive Design). |
| 3 | Veriler güncel mi? (Rapor tarihi ve Veri çekim zamanı rapora yazıyor mu?). |
