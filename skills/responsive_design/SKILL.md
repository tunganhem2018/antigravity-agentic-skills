---
name: responsive_design
router_kit: FullStackKit
description: Mobile-first tasarım, CSS Grid/Flexbox ve modern responsive teknikler.
metadata:
  skillport:
    category: development
    tags: [accessibility, api integration, backend, browser apis, client-side, components, css3, debugging, deployment, frameworks, frontend, fullstack, html5, javascript, libraries, node.js, npm, performance optimization, responsive design, seo, state management, testing, typescript, ui/ux, web development]      - mobile-first
---

# 📱 Responsive Design

> Her ekran boyutunda kusursuz kullanıcı deneyimi.

---

*Responsive Design v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [A List Apart: Responsive Web Design (Ethan Marcotte)](https://alistapart.com/article/responsive-web-design/) & [MDN Responsive Design](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Responsive_Design)

### Aşama 1: Mobile-First Strategy
- [ ] **Base Styles**: Tasarıma en küçük ekran boyutundan başla (Base CSS).
- [ ] **Grid/Flex**: Esnek layout yapılarını (`display: flex` veya `grid`) kur.

### Aşama 2: Breakpoints & Media Queries
- [ ] **Breakpoints**: Cihaz ismine göre değil, içeriğin bozulduğu noktaya (Content-based) göre breakpoint belirle.
- [ ] **Queries**: `@media (min-width: ...)` kullanarak stilleri genişlet.
- [ ] **Logical Units**: Fixed pixel yerine `rem`, `em`, `vw`, `vh` ve `%` kullan.

### Aşama 3: Assets & Testing
- [ ] **Images**: `srcset` ve `<picture>` tagleri ile ekran çözünürlüğüne uygun görsel yükle.
- [ ] **Touch Targets**: Mobilde tıklama alanlarının (Buttons, Links) yeterince büyük (min 44x44px) olduğundan emin ol.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Yatay kaydırma (Horizontal scroll) çubuğu çıkıyor mu? |
| 2 | Okunabilirlik (Font size) küçük ekranlarda korunuyor mu? |
| 3 | Cihaz döndürüldüğünde (Landscape/Portrait) layout patlıyor mu? |
