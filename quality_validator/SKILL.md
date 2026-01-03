---
name: quality_validator
router_kit: ManagementKit
description: Kod ve döküman kalitesini ölçme, checklist uygulama ve standart denetimi.
metadata:
  skillport:
    category: quality
    tags: [architecture, automation, best practices, cleanup, coaching, coding, collaboration, compliance, debugging, deployment, design patterns, development, documentation, efficiency, git, maintainability, management, metrics, optimization, performance, productivity, programming, project management, quality assurance, quality validator_1, refactoring, scalability, software engineering, standards, testing, utilities, version control, workflow]      - audit
---

# ✅ Quality Validator

> En üst düzey mühendislik ve içerik standartlarının denetimi.

---

## 📋 Quality Standards

### 1. Accuracy (Doğruluk)
- Verilen bilgiler güncel teknik dökümanlarla (Official docs) uyuşuyor mu?
- Kod örnekleri syntax hatası içermeden çalışıyor mu?

### 2. Consistency (Tutarlılık)
- Adlandırma kuralları (PascalCase, camelCase vb.) dosya boyunca sabit mi?
- Tonlama ve dil kullanımı (Biz dili, teknik dil vb.) uyumlu mu?

### 3. Completeness (Bütünlük)
- Tüm bölümler (`name`, `workflow`, `checklist` vb.) eksiksiz mi?
- Her skill en az 3-4 adımlı bir iş akışına sahip mi?

---

## 🧪 Validation Process

### Automated Checks
- **Linter**: Kod standartları.
- **Spell Checker**: Yazım kuralları.
- **Link Checker**: Dış referansların çalışabilirliği.

### Manual Audit
- "Kullanıcı bu dökümanı okuyarak işi bitirebilir mi?" testi.
- Referans kaynakların güvenilirliği.

---

## 🔧 Workflow

> **Kaynak:** [ISO/IEC 25010 Software Quality Model](https://iso25000.com/index.php/en/iso-25000-standards/iso-25010) & [Google Developer Documentation Style Guide](https://developers.google.com/style)

### Aşama 1: Criteria Definition
- [ ] **Rubric**: Denetlenecek öğe için (Örn: Markdown, Python Code) bir başarı kriteri (Rubric) seti seç.
- [ ] **Checklist**: Denetim sırasında gözden kaçmaması gereken kritik noktaları listele.
- [ ] **Threshold**: Kabul edilebilir hata limitini (Örn: 0 kritik hata, max 2 stil hatası) belirle.

### Aşama 2: Execution & Gap Analysis
- [ ] **Scan**: Otomatik araçlarla (Static Analysis) ilk taramayı yap.
- [ ] **Deep Dive**: Bilginin doğruluğunu (Fact-checking) orijinal kaynaklardan (Repo, Docs) teyit et.
- [ ] **Reporting**: Tespit edilen eksikleri "Bulgu" -> "Risk" -> "Öneri" şeklinde raporla.

### Aşama 3: Remediation & Verification
- [ ] **Action Plan**: Eksiklerin giderilmesi için görevleri (Tasks) tanımla.
- [ ] **Re-audit**: Düzeltmelerden sonra denetimi tekrarla.
- [ ] **Final Approval**: Standartlara tam uyum sağlandığında "Approved" damgasını vur.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Denetim objektif verilere mi dayanıyor yoksa kişisel yorum mu? |
| 2 | En kritik 3 kural (Must-haves) sağlandı mı? |
| 3 | Yapılan düzeltmeler yeni hatalar (Side effects) tetikledi mi? |

---

*Quality Validator v1.1 - Enhanced*
