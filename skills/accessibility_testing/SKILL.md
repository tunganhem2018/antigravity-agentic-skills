---
name: accessibility_testing
router_kit: UniversalKit
description: Web uygulamalarında erişilebilirlik (A11y) standartlarına uyumluluk denetimi ve testi.
metadata:
  skillport:
    category: quality
    tags: [accessibility, aria, testing, web, html]
---

# ♿ Accessibility Testing

Web uygulamalarının engelli kullanıcılar için erişilebilir olmasını sağlamak için standartlar ve araçlar.

---

## 🔄 Workflow

> **Kaynak:** [W3C WAI (Web Accessibility Initiative)](https://www.w3.org/WAI/) & [Axe-core documentation](https://github.com/dequelabs/axe-core)

### Aşama 1: Ortam ve Keşif (Environment & Reconnaissance)
- [ ] **Araç Kurulumu:** `axe-core`, `pa11y` veya tarayıcı eklentilerini (Lighthouse, Axe DevTools) hazırla.
- [ ] **Kapsam Belirleme:** Hangi sayfaların ve komponentlerin WCAG 2.1 (AA seviyesi) kriterlerine göre test edileceğini seç.
- [ ] **Manuel Kontrol:** Klavye navigasyonu (Tab sırası) ve ekran okuyucu (Screen Reader) uyumluluğunu ön kontrol et.

### Aşama 2: Otomatik ve Yarı-Otomatik Testler (Scripting & Automation)
- [ ] **Statik Analiz:** HTML yapısında eksik `alt` tagleri, `aria-label` ve form label eşleşmelerini tara.
- [ ] **Renk Kontrastı:** Metin ve arka plan arasındaki kontrast oranının en az 4.5:1 olduğunu doğrula.
- [ ] **Dinamik Testler:** Javascript ile değişen içeriklerin (modallar, bildirimler) `aria-live` veya `role` özniteliklerini kontrol et.

### Aşama 3: Hata Ayıklama ve Raporlama (Debug & Reporting)
- [ ] **Hata Giderme:** Tespit edilen "Violations" noktalarını onar (Örn: `TABINDEX` hataları).
- [ ] **Yeniden Test:** Yapılan düzeltmelerin yeni bir erişilebilirlik hatasına yol açmadığını doğrula.
- [ ] **Final Raporu:** WCAG uyumluluk skorunu ve kalan manuel iyileştirme önerilerini dökümante et.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1     | Sayfada hiç "Critical" seviyeli Axe hatası kaldı mı? |
| 2     | Tüm resimlerin anlamlı bir `alt` açıklaması var mı? |
| 3     | Form alanları ekran okuyucular tarafından doğru isimlendiriliyor mu? |

---
*Accessibility Testing v1.5 - Evidence-Based Update*
