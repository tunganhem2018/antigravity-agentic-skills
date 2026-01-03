---
name: opportunity_scorer
router_kit: ManagementKit
description: İş fırsatlarını puanlama, önceliklendirme ve ROI analizi.
metadata:
  skillport:
    category: business
    tags: [architecture, automation, best practices, clean code, coding, collaboration, compliance, debugging, design patterns, development, documentation, efficiency, git, opportunity scorer, optimization, productivity, programming, project management, quality assurance, refactoring, software engineering, standards, testing, utilities, version control, workflow]      - decision-making
---

# ⚖️ Opportunity Scorer

> İş fırsatlarını ve projeleri bilimsel yöntemlerle önceliklendirme.

---

*Opportunity Scorer v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [RICE Prioritization Framework (Intercom)](https://www.intercom.com/blog/rice-simple-prioritization-for-product-managers/)

### Aşama 1: Evaluation Criteria (RICE)
- [ ] **Reach**: Bu fırsat kaç kişiyi etkileyecek? (Ayda kaç kullanıcı?).
- [ ] **Impact**: Etki düzeyi ne? (Minimal: 0.5, Büyük: 3).
- [ ] **Confidence**: Verilere ne kadar güveniyoruz? (%50, %80, %100).
- [ ] **Effort**: Ne kadar zaman/kaynak alacak? (Kişi-ay).

### Aşama 2: Scoring Calculation
- [ ] **Formula**: `(Reach * Impact * Confidence) / Effort` formülüyle puanları hesapla.
- [ ] **Ranking**: Fırsatları en yüksek RICE puanından en düşüğe sırala.

### Aşama 3: Decision & Roadmap
- [ ] **Trade-off**: Stratejik öneme sahip ama düşük puanlı işleri (Opsiyonel) değerlendir.
- [ ] **Commit**: İlk 3 fırsatı ürün yol haritasına (Roadmap) ekle.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Puanlama duygusal mı yoksa veriye mi dayanıyor? |
| 2 | "Yüksek Etki / Düşük Efor" (Quick Wins) fırsatları kaçırıldı mı? |
| 3 | Kaynak kapasitesi (Team velocity) ile efor puanları örtüşüyor mu? |
