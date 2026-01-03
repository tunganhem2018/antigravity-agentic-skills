---
name: refactoring_patterns
router_kit: FullStackKit
description: Martin Fowler refactoring desenleri, karmaşık kodu temizleme ve basitleştirme.
metadata:
  skillport:
    category: quality
    tags: [architecture, automation, best practices, clean code, coding, collaboration, compliance, debugging, design patterns, development, documentation, efficiency, git, optimization, productivity, programming, project management, quality assurance, refactoring patterns, refactoring, software engineering, standards, testing, utilities, version control, workflow]      - clean-code
---

# 🛠️ Refactoring Patterns

> Kodu bozmadan iç yapısını iyileştirme desenleri.

---

*Refactoring Patterns v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [Refactoring (Martin Fowler)](https://refactoring.com/) & [Refactoring.Guru](https://refactoring.guru/)

### Aşama 1: Identification (Code Smells)
- [ ] **Smells**: "Long Method", "Large Class" veya "Primitive Obsession" gibi kokuları tespit et.
- [ ] **Safety**: Refactoring öncesi mevcut testlerin geçip geçmediğini kontrol et (Test yoksa önce test yaz).

### Aşama 2: Composing Methods
- [ ] **Extract Method**: Çok uzun metodları anlamlı parçalara böl.
- [ ] **Inline Method**: Gereksiz derecede basit/dolaylı metodları birleştir.
- [ ] **Replace Temp with Query**: Geçici değişkenler yerine metod çağrılarını kullan.

### Aşama 3: Organizing Data & Logic
- [ ] **Move Method/Field**: Sorumluluğu ait olduğu sınıfa taşı.
- [ ] **Rename**: Değişken ve fonksiyon isimlerini niyetini belli edecek şekilde (Intention-revealing) güncelle.
- [ ] **Decompose Conditional**: Karmaşık IF bloklarını isimlendirilmiş metodlara taşı.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Her küçük adımdan sonra testler hala yeşil mi? |
| 2 | Kodun okunabilirliği (Cognitive load) azaldı mı? |
| 3 | Yeni bir davranış (Feature) eklendi mi? (Cevap 'HAYIR' olmalı). |
