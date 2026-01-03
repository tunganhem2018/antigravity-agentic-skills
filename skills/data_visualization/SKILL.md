---
name: data_visualization
router_kit: FullStackKit
description: Veri görselleştirme prensipleri, grafik türleri ve 2025 dashboard tasarım standartları.
metadata:
  skillport:
    category: data
    tags: [big data, charts, cleaning, csv, d3, dashboard, data analysis, data engineering, data science, data visualization, database, etl pipelines, export, import, json, machine learning basics, migration, nosql, numpy, pandas, python data stack, query optimization, recharts, reporting, schema design, sql, statistics, transformation, victory, visualization]
---

# 📊 Data Visualization

> Veri görselleştirme ve içgörü sunumu rehberi.

---

## 🎨 Visualization Selection Matrix

| Goal | Best Chart | Why? |
|------|------------|------|
| **Comparison** | Bar Chart / Line | High precision |
| **Trend** | Line / Area | Shows change over time |
| **Distribution** | Histogram / Scatter | Shows density |
| **Composition** | Stacked Bar / Pie | Parts of a whole |

---

## 📈 Dashboard Principles (2025)

```markdown
- [ ] Minimalist design (Data-to-ink ratio)
- [ ] Accessible color palettes
- [ ] Responsive layouts
- [ ] Interactive filtering
- [ ] Clear typography and labeling
```

---

## 🔧 Workflow

> **Kaynak:** [Financial Times Visual Vocabulary](https://ft.com/vocabulary)

### Aşama 1: Data Profiling
- [ ] **Type Check**: Veri kategorik mi, sayısal mı, zaman serisi mi?
- [ ] **Volume**: Veri noktası sayısı (az ise Bar, çok ise Scatter/Line).
- [ ] **Goal**: Amaç karşılaştırma (Bar), dağılım (Hist), ilişki (Scatter) veya kompozisyon (Pie/Stack) mu?

### Aşama 2: Drafting
- [ ] **Library**: Python için `matplotlib`/`seaborn`, Web için `D3.js`/`Recharts`.
- [ ] **Mapping**: X/Y eksenlerini ve renk kodlarını (hue) ata.
- [ ] **Scale**: Eksenleri sıfırdan başlat (Zorunlu olmayan durumlar hariç).

### Aşama 3: Refinement (Design)
- [ ] **Clutter**: Gereksiz çizgileri (gridlines) ve çerçeveleri kaldır.
- [ ] **Labels**: Eksenleri ve başlığı net bir şekilde etiketle.
- [ ] **Access**: Renk körleri için uygun palet kullan (ColorOracle ile test et).

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Seçilen grafik türü veri tipine uygun mu? (Örn: Zaman serisi için Bar değil Line) |
| 2 | Veri "ink-to-data ratio" yüksek mi? (Gereksiz süsleme yok) |
| 3 | Eksenler manipülatif değil mi? (Truncated Y-axis uyarısı) |

---
*Data Visualization v1.1 - Enhanced*
