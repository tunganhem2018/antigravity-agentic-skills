---
name: canvas_design
router_kit: UniversalKit
description: HTML5 Canvas ve WebGL ile performanslı grafik dökümantasyonu ve etkileşim tasarımı.
metadata:
  skillport:
    category: frontend
    tags: [canvas, graphics, webgl, performance, animation]
---

# 🖌️ Canvas Design

Web üzerinde piksel tabanlı grafik ve animasyon yönetimi.

---

## 🔄 Workflow

> **Kaynak:** [HTML5 Canvas API (MDN)](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API) & [Three.js Documentation](https://threejs.org/docs/)

### Aşama 1: Kurulum ve Koordinat Sistemi (Setup & Space)
- [ ] **DPI Scaling:** Retina ekranlarda bulanıklığı önlemek için `devicePixelRatio` ayarını yap.
- [ ] **Context Selection:** 2D mi yoksa 3D (WebGL) mi çalışılacağını belirle.
- [ ] **Coordinate Architecture:** Grafiklerin ekranın neresinden başlayıp nasıl ölçekleneceğini kurgula.

### Aşama 2: Çizim ve Animasyon (Drawing & Motion)
- [ ] **Primitive Drawing:** Path, Arc, Rectangle ve Gradient yapılarını oluştur.
- [ ] **Optimization Loop:** Animasyonlar için `requestAnimationFrame` kullan ve gereksiz render'lardan kaçın.
- [ ] **Offscreen Canvas:** Ağır hesaplamaları ana thread'i engellememek için `OffscreenCanvas` ile yap.

### Aşama 3: Etkileşim ve Export (Interaction & Export)
- [ ] **Hit Detection:** Kullanıcının hangi grafiğe tıkladığını saptama mantığını (Intersection) kur.
- [ ] **Performance Audit:** Frame-rate (FPS) takibi yap ve `willReadFrequently` gibi optimizasyonları uygula.
- [ ] **Image Generation:** Canvas içeriğini `toDataURL` ile resim olarak kaydetme özelliğini ekle.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1     | Yüksek çözünürlüklü ekranlarda grafikler keskin mi? |
| 2     | Mobil cihazlarda batarya tüketimi/performans dengesi gözetildi mi? |
| 3     | Bellek sızıntısı (Memory Leak) için `clearRect` doğru yerde kullanılıyor mu? |

---
*Canvas Design v1.1 - Evidence-Based Update*
