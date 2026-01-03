---
name: image_enhancer
router_kit: FullStackKit
description: Görsel işleme, resizing, format dönüştürme ve görsel kalite iyileştirme teknikleri.
metadata:
  skillport:
    category: development
    tags: [accessibility, api integration, backend, browser apis, client-side, components, css3, debugging, deployment, frameworks, frontend, fullstack, html5, image enhancer, javascript, libraries, node.js, npm, performance optimization, responsive design, seo, state management, testing, typescript, ui/ux, web development]      - graphics
---

# 🖼️ Image Enhancer

> Görsel kaliteyi artırma ve web optimizasyonu.

---

*Image Enhancer v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [Google Web Fundamentals - Image Optimization](https://web.dev/learn/design/responsive-images) & [Sharp Documentation](https://sharp.pixelplumbing.com/)

### Aşama 1: Analysis & Selection
- [ ] **Identify**: Optimizasyon ihtiyacı olan görselleri (büyük boyutlu, düşük kaliteli) belirle.
- [ ] **Tool**: `Sharp` (Node.js) veya `Pillow` (Python) gibi kütüphaneleri seç.

### Aşama 2: Processing (Resizing & Formatting)
- [ ] **Scale**: Cihaz çözünürlüğüne göre yeniden boyutlandır.
- [ ] **Format**: Web uyumlu `WebP` veya `AVIF` formatlarına dönüştür.
- [ ] **Compression**: Kalite kaybı minimum olacak şekilde sıkıştırma yap.

### Aşama 3: Delivery (Enhancement)
- [ ] **Lazy Loading**: "Above the fold" olmayan resimler için gecikmeli yükleme kur.
- [ ] **CDN**: Görselleri CDN üzerinden servis etmeye hazırla.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Görsel netliği (Blur) bozuldu mu? |
| 2 | Meta veriler (Exif) gereksiz yer kaplıyor mu? |
| 3 | Dosya boyutu web kullanımı için uygun mu (<200KB)? |
