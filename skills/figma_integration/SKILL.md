---
name: figma_integration
router_kit: FullStackKit
description: Figma design-to-code, design system extraction ve component generation rehberi.
metadata:
  skillport:
    category: design
    tags: [architecture, automation, best practices, clean code, coding, collaboration, compliance, debugging, design patterns, development, documentation, efficiency, figma integration, git, optimization, productivity, programming, project management, quality assurance, refactoring, software engineering, standards, testing, utilities, version control, workflow]      - design-system
---

# 🎨 Figma Integration

> Figma design-to-code workflow rehberi.

---

*Figma Integration v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [Figma for Developers](https://www.figma.com/best-practices/developer-handoff-guide/)

### Aşama 1: Inspection
- [ ] **Dev Mode**: Figma Dev Mode'u aç ve CSS/iOS/Android kodunu incele.
- [ ] **Assets**: Görselleri SVG veya 2x/3x PNG olarak export et.
- [ ] **Variables**: Renk/Spacing token'larını `theme.ts` veya `tailwind.config`'e ekle.

### Aşama 2: component Build
- [ ] **Structure**: Frame yapısını `Flex` veya `Grid` olarak koda dök.
- [ ] **Props**: Varyantları (Primary/Secondary) component prop'u yap.
- [ ] **Responsive**: Auto Layout constraint'lerine göre responsive davranışı kodla.

### Aşama 3: Verification
- [ ] **Pixel Perfect**: Overlay ile tasarım ve kodu üst üste kontrol et.
- [ ] **States**: Hover, Focus, Active, Disabled durumlarını atlama.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Tüm renkler hardcoded hex yerine variable mı? |
| 2 | Component Figma'daki gibi esniyor (resize) mu? |
| 3 | Yazı tipleri ve satır aralıkları birebir aynı mı? |
