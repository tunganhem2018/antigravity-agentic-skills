---
name: peer_review
router_kit: ManagementKit
description: Kod ve dökümantasyon review standartları, geri bildirim teknikleri ve kalite kontrol.
metadata:
  skillport:
    category: leadership
    tags: [architecture, automation, best practices, cleanup, coaching, collaboration, debugging, development, documentation, efficiency, leadership, maintainability, optimization, peer review, performance, productivity, quality assurance, software engineering, standards, testing, version control, workflow]      - software-quality
---

# 🔎 Peer Review & Code Quality

> Profesyonel kod denetimi ve yapıcı geri bildirim rehberi.

---

## 📋 Review Focus Areas

### 1. Correctness (Doğruluk)
- Kod isterleri karşılıyor mu?
- Edge case'ler (null values, error states) düşünüldü mü?

### 2. Readability (Okunabilirlik)
- Değişken isimleri açıklayıcı mı?
- Fonksiyonlar tek bir iş yapıyor mu (SRP)?
- Karmaşık logic'ler için yeterli yorum satırı var mı?

### 3. Maintainability (Bakım Yapılabilirlik)
- DRY (Don't Repeat Yourself) kuralına uyulmuş mu?
- Hard-coded değerler yerine sabitler/config kullanılıyor mu?

---

## 💬 Feedback Etiquette

| Tip | Yanlış Yaklaşım | Doğru Yaklaşım |
|-----|-----------------|----------------|
| **Üslup** | "Bu kod çok yavaş." | "Burada O(n²) yerine O(n) kullanarak performansı artırabilir miyiz?" |
| **Öznellik** | "Bence böyle daha iyi." | "Ekibimizin stil rehberine (link) göre bu formatı tercih ediyoruz." |
| **Kapsam** | Sadece hata bulmak. | İyi yazılmış bölümleri de övüp "Nice work!" demek. |

---

## 🔧 Checklist for Reviewers

```checklist
- [ ] Kod çalışıyor mu? (Build & Test pass)
- [ ] Güvenlik açığı (SQL Injection, XSS) var mı?
- [ ] Test coverage yeterli mi?
- [ ] Yeni eklenen kodun dökümantasyonu yapıldı mı?
- [ ] Style guide uyumu (Prettier/ESLint).
```

---

*Peer Review v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [Google Engineeer's Guide to Code Reviews](https://google.github.io/eng-practices/review/) & [Conventional Comments](https://conventionalcomments.org/)

### Aşama 1: Self-Review (Author)
- [ ] **Clean-up**: Gereksiz `console.log`'ları, yorum satırlarını ve kullanılmayan import'ları temizle.
- [ ] **Description**: Pull Request (PR) açıklamasını "Neden yapıldı?" ve "Nasıl test edilir?" detaylarıyla doldur.
- [ ] **Tests**: Kendi lokalinde build ve unit testlerin geçtiğini doğrula.

### Aşama 2: Review Process (Reviewer)
- [ ] **Context**: PR açıklamasını oku, jira/task kartıyla eşle.
- [ ] **Automation**: Linter ve CI sonuçlarını bekle (Hataları manuel söylemek yerine otomasyona bırak).
- [ ] **Comments**: `Nitpick` (Küçük detay), `Issue` (Hata), `Question` (Anlaşılmayan yer) etiketlerini kullanarak yorum yaz.

### Aşama 3: Resolution & Merge
- [ ] **Discussions**: Anlaşmazlık varsa yüz yüze veya senkron bir görüşme yap (Thread uzamasın).
- [ ] **Follow-up**: Değişiklikler yapıldıktan sonra "Re-request review" yap.
- [ ] **Final Check**: Onay (Approve) ver ve merge kriterlerinin sağlandığını doğrula.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | PR çok mu büyük? (+500 satır ise parçalamayı öner). |
| 2 | Yorumlar kişisel mi yoksa koda mı yönelik? |
| 3 | Bir hata (Bug) düzeltilirken yeni bir hata yaratıldı mı? |
