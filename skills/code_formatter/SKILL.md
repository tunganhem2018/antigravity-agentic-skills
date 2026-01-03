---
name: code_formatter
router_kit: UniversalKit
description: Prettier, ESLint ve dile özgü formatterlar ile kod standardizasyonu.
metadata:
  skillport:
    category: development
    tags: [formatting, linting, prettier, eslint, standards]
---

# 📏 Code Formatter

Ekip içindeki kod stilini eşitleyen ve hataları oto-fix eden sistemler.

---

## 🔄 Workflow

> **Kaynak:** [Prettier Docs](https://prettier.io/docs/en/) & [ESLint Configuration Guide](https://eslint.org/docs/latest/use/configure/)

### Aşama 1: Konfigürasyon ve Kurallar (Project Standards)
- [ ] **Formatter Choice:** Prettier, Biome veya dile özgü (gofmt, black) araçları seç.
- [ ] **ConfigFile:** `.prettierrc` ve `.eslintrc.json` dosyalarını oluştur, ekip standartlarını (tab-width, semi, singleQuote) gir.
- [ ] **Conflict Resolution:** Formatter ile Linter'ın çakışmaması için `eslint-config-prettier` gibi eklentileri ayarla.

### Aşama 2: IDE ve Local Entegrasyon (Local Enforcement)
- [ ] **Format on Save:** VS Code veya Cursor üzerinde her kayıtta otomatik formatlamayı aktif et.
- [ ] **Git Hooks:** `husky` ve `lint-staged` ile sadece değiştirilen dosyaların commit öncesi formatlanmasını sağla.
- [ ] **Ignore Files:** `.prettierignore` ile build klasörlerini ve bağımlılıkları hariç tut.

### Aşama 3: CI/CD Pipeline Denetimi (Pipeline Check)
- [ ] **Lint Step:** CI sürecine `lint` komutunu ekleyerek standart dışı kodun merge edilmesini engelle.
- [ ] **Check Mode:** Formatta düzeltme yapmak yerine sadece kontrol eden `prettier --check` komutunu çalıştır.
- [ ] **Custom Rules:** Projeye özel isimlendirme veya yapı kuralları ekle.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1     | Farklı geliştiriciler aynı dosyayı kaydettiğinde "diff" oluşuyor mu? |
| 2     | Linter hataları (Errors vs Warnings) anlamlı bir şekilde ayrılmış mı? |
| 3     | Otomatik düzeltilemeyen (Unfixable) hatalar için döküman linki veriliyor mu? |

---
*Code Formatter v1.1 - Evidence-Based Update*
