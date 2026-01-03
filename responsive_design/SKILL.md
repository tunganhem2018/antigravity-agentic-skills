---
name: responsive_design
router_kit: FullStackKit
description: Mobil öncelikli (Mobile-First) tasarım, media queries, fluid layouts ve cross-device uyumu.
metadata:
  skillport:
    category: frontend
    tags: [accessibility, architecture, automation, best practices, cleanup, coding, collaboration, compliance, css, debugging, deployment, design patterns, development, documentation, efficiency, frontend, git, maintainability, optimization, performance, productivity, programming, quality assurance, responsive design, responsive design_1, scalability, software engineering, standards, testing, typescript, ui/ux, utilities, version control, web development, workflow]      - mobile-web
---

# 📱 Responsive Design

> Her ekran boyutunda kusursuz kullanıcı deneyimi ve fluid layouts.

---

## 📐 Core Principles

### 1. Mobile-First Approach
Tasarımı önce en küçük ekrandan (320px) başlat, sonra büyüterek genişlet.
- **Avantaj**: Daha temiz kod, daha az "override" işlemi.

### 2. Fluid Layouts (Relative Units)
- `px` yerine `rem`, `%`, `vw`, `vh` kullan.
- `max-width` ile taşmaları önle.

### 3. Breakpoints (Media Queries)
- **Small**: 640px (Mobile Landscape)
- **Medium**: 768px (Tablets)
- **Large**: 1024px (Desktops)
- **Extra Large**: 1280px+ (Large Screens)

---

## 🛠️ Code Snippets

### Media Query (Standard)
```css
.container { width: 100%; }

@media (min-width: 768px) {
  .container { width: 750px; }
}
```

### TailwindCSS Approach
```html
<div class="w-full md:w-1/2 lg:w-1/3 p-4">
  <!-- Content -->
</div>
```

---

## 🔧 Workflow

> **Kaynak:** [Google Web Fundamentals](https://developers.google.com/web/fundamentals/design-and-ux/responsive) & [CSS-Tricks: Responsive Design](https://css-tricks.com/snippets/css/media-queries-for-standard-devices/)

### Aşama 1: Layout & Breakpoints
- [ ] **Base Style**: Media query dışındaki tüm stillerin "Mobil" (min-width: 0) olduğundan emin ol.
- [ ] **Breakpoint Selection**: Standartları (Tailwind/Bootstrap) takip et, gerekmedikçe custom breakpoint ekleme.
- [ ] **Container Management**: `max-width` ve `mx-auto` ile büyük ekranlarda içeriğin aşırı yayılmasını önle.

### Aşama 2: Interactive Elements & Assets
- [ ] **Touch Targets**: Link ve butonların mobilde en az 44x44px genişlikte olmasını sağla.
- [ ] **Images**: `srcset` veya `object-fit: cover` kullanarak resimlerin bozulmadan sığmasını sağla.
- [ ] **Navigation**: Mobil için Hamburger Menu veya Bottom Nav yapılarını kur.

### Aşama 3: Verification & Edge Cases
- [ ] **Device Simulation**: Chrome DevTools ile 320px (iPhone SE) ve 1280px (Macbook) arası tüm skalayı tara.
- [ ] **Orientation**: Cihaz yan çevrildiğinde (Landscape) layout'un kırılmadığını kontrol et.
- [ ] **Performance**: Gereksiz "display: none" yerine component-level rendering ile DOM boyutunu koru.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Yatay kaydırma (Horizontal Scroll) oluşuyor mu? |
| 2 | Yazı boyutları (Font-size) mobilde okunabilir mi? (Min 16px tavsiye edilir). |
| 3 | Görseller ekranı aşıyor mu? |

---

*Responsive Design v1.1 - Enhanced*
