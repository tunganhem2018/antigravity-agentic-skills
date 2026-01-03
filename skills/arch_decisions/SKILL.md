---
name: arch_decisions
router_kit: FullStackKit
description: Yazılım mimarisi kararlarının (ADR) alınması, dökümante edilmesi ve gerekçelendirilmesi.
metadata:
  skillport:
    category: architecture
    tags: [architecture, adr, documentation, decision-making, engineering-design]
---

# 🏛️ Architecture Decisions (ADR)

Mühendislik tercihlerinin nedenlerini ve sonuçlarını dökümante etme süreci.

---

## 🔄 Workflow

> **Kaynak:** [Architectural Decision Records (ADR)](https://adr.github.io/) & [Joelonsoftware - Functional Specs](https://www.joelonsoftware.com/2000/10/02/pain-free-functional-specifications-part-1-why-bother/)

### Aşama 1: Problem ve Bağlam (Problem & Context)
- [ ] **Problem Tanımı:** Çözülmek istenen teknik sorunu veya ihtiyacı net bir şekilde ifade et.
- [ ] **Kısıtlar:** Bütçe, zaman, mevcut teknoloji yığını veya performans gibi kısıtları listele.
- [ ] **Alternatifler:** Değerlendirilen diğer tüm yolları (Örn: RabbitMQ vs Redis) kısaca belirt.

### Aşama 2: Karar ve Gerekçe (Decision & Rationale)
- [ ] **Seçilen Yol:** Hangi teknolojinin veya yöntemin seçildiğini yaz.
- [ ] **Neden Seçildi?:** Seçimin arkasındaki güçlü nedenleri (Trade-offs) açıkla.
- [ ] **Riskler:** Seçilen yolun beraberinde getirdiği teknik borçları veya riskleri dürüstçe belirt.

### Aşama 3: Statü ve Takip (Status & Tracking)
- [ ] **ADR Dosyası:** Kararı `docs/adr/0001-choosing-nextjs.md` formatında dökümante et.
- [ ] **Status:** Kararın durumunu (Proposed, Accepted, Deprecated, Superceded) işaretle.
- [ ] **Ekip Onayı:** Kararın paydaşlar (Stakeholders) tarafından gözden geçirilmesini sağla.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1     | Karar dökümanı "Neden?" sorusuna 12 ay sonra bile cevap verebiliyor mu? |
| 2     | Kararın maliyeti (Cost) ve bakım zorluğu (Maintenance) hesaba katıldı mı? |
| 3     | ADR dosyası herkes için erişilebilir (Version Control) bir yerde mi? |

---
*Arch Decisions v1.2 - Evidence-Based Update*
