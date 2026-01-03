---
name: code_review
router_kit: UniversalKit
description: Kod kalitesi, güvenlik ve performans odaklı profesyonel code review süreçleri.
metadata:
  skillport:
    category: quality
    tags: [code-review, quality-assurance, peer-review, standards]
---

# 🔍 Code Review

Yazılım kalitesini artırmak için meslektaş denetimi ve geri bildirim süreci.

---

## 🔄 Workflow

> **Kaynak:** [Google's Engineering Practices - Code Review](https://google.github.io/eng-practices/review/) & [GitHub - Best Practices for Code Review](https://github.com/features/code-review)

### Aşama 1: Ön Kontrol ve Bağlam (Context & Self-Review)
- [ ] **PR Description:** Değişikliğin nedenini, neyi düzelttiğini ve nasıl test edileceğini net yaz.
- [ ] **Self-Audit:** Reviewer'a göndermeden önce formatter ve linter hatalarını temizle.
- [ ] **Minimal Size:** PR'ları küçük tut (Atomic PR), devasa değişikliklerden kaçın.

### Aşama 2: Teknik Denetim (Technical Review)
- [ ] **Logic & Correctness:** Kodlanan algoritma gerçekten istendiği gibi çalışıyor mu? (Edge cases).
- [ ] **Complexity:** Kod daha basit yazılabilir miydi? (DRY, KISS prensipleri).
- [ ] **Security:** SQL Injection, XSS veya hassas veri sızıntısı riski var mı?

### Aşama 3: İletişim ve Onay (Communication & Approval)
- [ ] **Constructive Feedback:** "Bu yanlış" demek yerine "Şu nedenle şuna çevirmek daha iyi olabilir" şeklinde yapıcı ol.
- [ ] **Actionable Comments:** Yorumları havada bırakma, net bir aksiyon öner.
- [ ] **Resolution:** Tüm yorumlar çözüldüğünde (Resolved) ve CI testleri yeşil olduğunda onayla (Approve).

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1     | PR dökümantasyonu okuyan biri değişikliğin amacını hemen anlayabiliyor mu? |
| 2     | Reviewer, kodun performans etkisini (Complexity) değerlendirdi mi? |
| 3     | Test kapsamı (Test Coverage) bu değişiklik için yeterli mi? |

---
*Code Review v1.4 - Evidence-Based Update*
