---
name: algorithmic_art
router_kit: UniversalKit
description: Kod ve algoritmalar kullanarak sanatsal görseller ve desenler üretme teknikleri.
metadata:
  skillport:
    category: creative
    tags: [generative-art, p5js, canvas, algorithms, creative-coding]
---

# 🎨 Algorithmic Art

Matematiksel formüller ve algoritmalar ile görsel yaratım süreci.

---

## 🔄 Workflow

> **Kaynak:** [The Book of Shaders](https://thebookofshaders.com/) & [p5.js Reference](https://p5js.org/reference/)

### Aşama 1: Matematiksel Temel (Mathematical Foundation)
- [ ] **Algoritma Seçimi:** Perlin Noise, L-Systems, Particle Systems veya Fractals gibi temel tekniği belirle.
- [ ] **Parametre Tanımlama:** Görselin değişkenlerini (Renk paleti, hız, yoğunluk, şans faktörü) tanımla.
- [ ] **Kanvas Hazırlığı:** Çözünürlük ve render motoru (Canvas API, WebGL, SVG) seçimini yap.

### Aşama 2: Generatif Döngü (Generative Lifecycle)
- [ ] **Render Loop:** `requestAnimationFrame` veya `draw()` döngüsünü kurarak dinamik değişimi sağla.
- [ ] **Randomness vs Order:** Rastgelelik (Random) ve düzen (Noise) arasındaki dengeyi ayarla.
- [ ] **User Interaction:** Kullanıcı hareketlerine (Mouse, Keyboard) göre sanatı etkileyen reaktif katmanları ekle.

### Aşama 3: Optimizasyon ve Export (Polish & Export)
- [ ] **Performance Audit:** Yüksek partikül sayılarında CPU/GPU yükünü optimize et (Instancing, Shaders).
- [ ] **Post-Processing:** Görsele Bloom, Grain veya Blur gibi sanatsal filtreler ekle.
- [ ] **High-Res Export:** Görseli PNG, MP4 veya SVG olarak yüksek kalitede kaydetme fonksiyonlarını yaz.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1     | Algoritma beklenmedik (Infinite) bir hesaplama döngüsüne giriyor mu? |
| 2     | Renk paleti harmonik bir yapıda mı? |
| 3     | Kanvas boyutu değiştiğinde (Responsive) sanat bozuluyor mu? |

---
*Algorithmic Art v1.1 - Evidence-Based Update*
