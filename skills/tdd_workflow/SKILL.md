---
name: tdd_workflow
router_kit: QualityKit
description: Test-Driven Development (Red-Green-Refactor) döngüsü ve Unit Testing pratikleri.
metadata:
  skillport:
    category: quality
    tags: [architecture, automation, best practices, clean code, coding, collaboration, compliance, debugging, design patterns, development, documentation, efficiency, git, optimization, productivity, programming, project management, quality assurance, refactoring, software engineering, standards, tdd workflow, testing, utilities, version control, workflow]      - software-testing
---

# 🧪 TDD Workflow

> Hata payını azaltan ve kod kalitesini garantiye alan "Önce Test" yaklaşımı.

---

*TDD Workflow v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [Kent Beck - Test Driven Development by Example](https://www.oreilly.com/library/view/test-driven-development/0321146530/) & [Google Testing Blog](https://testing.googleblog.com/)

### Aşama 1: RED - Test-First Approach
- [ ] **Interface Design**: Kodun nasıl çalışması gerektiğini (Input/Output) belirle ve testi yaz.
- [ ] **Fail Confirmation**: Testi çalıştır ve kod henüz yazılmadığı için başarısız (Red) olduğunu gör.
- [ ] **Assertion Clarity**: Testin neden başarısız olduğunu açıklayan net bir hata mesajı aldığından emin ol.

### Aşama 2: GREEN - Implementation
- [ ] **Minimal Code**: Sadece testin geçmesi için gereken en basit/minimal kodu yaz.
- [ ] **Pass Verification**: Tüm testlerin "Yeşil" döndüğünü doğrula.
- [ ] **Avoid Over-Engineering**: Test kapsamı dışında kalan özellikleri implement etme.

### Aşama 3: REFACTOR - Clean Code
- [ ] **Code Cleanup**: Kodu SOLID prensiplerine göre optimize et, isimlendirmeleri düzelt.
- [ ] **Test Refinement**: Testlerin okunabilirliğini artır, tekrarları (`setup/teardown`) optimize et.
- [ ] **Regression Check**: Her refactoring adımından sonra testlerin hala yeşil olduğunu doğrula.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Testler "Implementation Details" yerine "Behavior"ı mı test ediyor? |
| 2 | Her test fonksiyonu bağımsız (Isolated) mı? |
| 3 | Kod coverage hedefine (%80+) ulaşıldı mı? |
