---
name: pptx
router_kit: ManagementKit
description: PowerPoint (.pptx) otomasyonu, slide generation, layout management ve template manipülasyonu.
metadata:
  skillport:
    category: operations
    tags: [automation, best practices, business, collaboration, compliance, documentation, efficiency, legal, optimization, pptx, presentation, productivity, quality assurance, software engineering, standards, utilities, workflow, writing]      - presentations
---

# 📊 PPTX Management & Automation

> PowerPoint döküman otomasyonu ve dinamik sunum oluşturma.

---

## 🛠️ PPTX Generation (Node.js)

### PptxGenJS (Hızlı & Kolay)
Web ve Node.js üzerinde çalışan, API tabanlı sunum oluşturma.
```javascript
let pres = new PptxGenJS();
let slide = pres.addSlide();
slide.addText("Hello World!", { x: 1, y: 1, fontSize: 18 });
pres.writeFile({ fileName: "Sample.pptx" });
```

---

## 🔍 Advanced Manipulation (Python)

### Python-pptx
Mevcut sunumları düzenlemek ve template'leri doldurmak için en güçlü kütüphane.
```python
from pptx import Presentation

prs = Presentation('template.pptx')
for slide in prs.slides:
    for shape in slide.shapes:
        if shape.has_text_frame:
            # Placeholder replace logic
            shape.text = shape.text.replace('{{DATE}}', '2024-01-01')

prs.save('output.pptx')
```

---

## 🎨 Best Practices

- **Master Slides**: Tek tek slide düzenlemek yerine "Master Slide" yapılarını kullan.
- **Aspect Ratio**: 16:9 (Geniş ekran) standartlarına uy.
- **Embedded Data**: Chart'ları resim yerine "Excel-backed chart" olarak ekle.

---

*PPTX Management v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [Python-pptx Documentation](https://python-pptx.readthedocs.io/) & [PptxGenJS Documentation](https://gitbrent.github.io/PptxGenJS/)

### Aşama 1: Template Selection
- [ ] **Baseline**: Şirket standartlarına uygun (Logo, Fontlar, Renk paleti) bir `.pptx` template'i al.
- [ ] **Layout Mapping**: Slide master içindeki layout isimlerini ve placeholder index'lerini (0: Title, 1: Body vb.) belirle.
- [ ] **Assets**: Sunumda kullanılacak resim, video ve grafik verilerini (Excel/JSON) hazırla.

### Aşama 2: Dynamic Generation
- [ ] **Automation**: Template üzerindeki placeholder'ları regex veya ID bazlı verilerle doldur.
- [ ] **Tables/Charts**: Karmaşık verileri `native objects` (Tablo/Grafik) olarak ekle (Resimden kaçın).
- [ ] **Iterative Rendering**: Birden fazla slide gerektiren işlerde "Sayfa bölme" (Overflow) logic'ini uygula.

### Aşama 3: Export & Polishing
- [ ] **Conversion**: PDF veya Image (Thumbnail) export ihtiyacı varsa `LibreOffice` veya `Office Interop` araçlarını kur.
- [ ] **Validation**: Font uyumsuzluklarını ve taşan metinleri (Text overflow) kontrol et.
- [ ] **Protection**: Dökümanı "Read-only" veya "Final" olarak işaretle.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Fontlar hedef bilgisayara gömüldü (Embedded) mü? |
| 2 | Resimler optimize edildi mi? (Dosya boyutu kontrolü). |
| 3 | Chart renkleri template'e uyumlu mu? |
