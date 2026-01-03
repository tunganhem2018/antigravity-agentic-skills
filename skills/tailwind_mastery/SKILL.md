---
name: tailwind_mastery
router_kit: FullStackKit
description: Tailwind CSS ileri seviye kullanımı, yapılandırma, JIT ve plugin geliştirme.
metadata:
  skillport:
    category: development
    tags: [accessibility, api integration, backend, browser apis, client-side, components, css3, debugging, deployment, frameworks, frontend, fullstack, html5, javascript, libraries, node.js, npm, performance optimization, responsive design, seo, state management, tailwind mastery, testing, typescript, ui/ux, web development]      - css-frameworks
---

# 🌊 Tailwind Mastery

> Modern ve hızlı UI geliştirme için yüksek performanslı CSS yönetimi.

---

*Tailwind Mastery v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [Tailwind CSS Documentation](https://tailwindcss.com/docs) & [Refactoring UI (Adam Wathan)](https://www.refactoringui.com/)

### Aşama 1: Configuration & Design System
- [ ] **Theme**: `tailwind.config.js` içinde kurumsal renkler, fontlar ve spacing değerlerini tanımla.
- [ ] **Plugins**: Formlar, Typography veya Container Queries gibi resmi eklentileri aktif et.
- [ ] **Presets**: Farklı projelerde paylaşılabilecek yapılandırma setlerini (Presets) hazırla.

### Aşama 2: Layout & Component Development
- [ ] **Utility-First**: HTML içinde doğrudan utility class'larını kullanarak hızlıca layout kur.
- [ ] **Complex Selectors**: `peer-*`, `group-*` ve `has-*` gibi ileri seviye seçicileri kullan.
- [ ] **Animations**: `animate-pulse`, `animate-bounce` veya custom transitionları ekle.

### Aşama 3: Optimization & Extraction
- [ ] **Reuse**: Çok sık kullanılan kombinasyonları bileşenlere (React/Vue vb.) ayır. `@apply` kullanımını minimumda tut.
- [ ] **Purge/JIT**: Kullanılmayan CSS'lerin atıldığını ve bundle boyutunun küçük olduğunu doğrula.
- [ ] **Intellisense**: VS Code üzerinde Tailwind CSS IntelliSense eklentisinin çalıştığından emin ol.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Class karmaşasını (Class soup) önlemek için bileşen mimarisi kullanıldı mı? |
| 2 | Tasarım tam responsive mi? (Prefixler: `sm:`, `md:`, `lg:` vb.). |
| 3 | Özel renkler (Arbitrary values `-[...]`) yerine config'deki değerler mi kullanıldı? |
