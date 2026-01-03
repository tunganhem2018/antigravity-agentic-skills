---
name: docs_code
router_kit: FullStackKit
description: JSDoc, TSDoc ve kod içi dokümantasyon standartları.
metadata:
  skillport:
    category: documentation
    tags: [architecture, automation, best practices, clean code, coding, collaboration, compliance, debugging, design patterns, development, docs code, documentation, efficiency, git, optimization, productivity, programming, project management, quality assurance, refactoring, software engineering, standards, testing, utilities, version control, workflow]      - comments
---

# 📝 Code Documentation

> Okunabilir ve sürdürülebilir kod içi dokümantasyon.

---

*Code Documentation v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [TSDoc Standard](https://tsdoc.org/)

### Aşama 1: Documentation Strategy
- [ ] **Analyze**: Hangi fonksiyonların/sınıfların dokümante edilmesi gerektiğini belirle (Public API'lar öncelikli).
- [ ] **Standards**: JSDoc veya TSDoc standartlarından birini seç.

### Aşama 2: Implementation (TSDoc)
- [ ] **Summary**: Fonksiyonun ne yaptığını tek cümlede açıkla.
- [ ] **Params**: `@param` ile tüm girdileri ve tiplerini açıkla.
- [ ] **Returns**: `@returns` ile çıktıyı tanımla.
- [ ] **Examples**: `@example` bloğu ile kullanım örneği sun.

### Aşama 3: Linting & Verification
- [ ] **Lint**: `eslint-plugin-jsdoc` ile eksik dokümantasyonu tespit et.
- [ ] **Extraction**: Gerekiyorsa `TypeDoc` ile statik doküman sayfaları üret.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Dokümantasyon "Nasıl"dan ziyade "Neden"i açıklıyor mu? |
| 2 | Parametre açıklamaları güncel mi? |
| 3 | Kod okunduğunda dokümana ihtiyaç duyulmayacak kadar temiz mi (Clean Code)? |
