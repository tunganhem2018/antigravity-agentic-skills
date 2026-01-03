---
name: mobile_react_native
router_kit: FullStackKit
description: React Native/Expo best practices, Reanimated ve performance optimization.
metadata:
  skillport:
    category: development
    tags: [accessibility, api integration, backend, browser apis, client-side, components, css3, debugging, deployment, frameworks, frontend, fullstack, html5, javascript, libraries, mobile react native, node.js, npm, performance optimization, responsive design, seo, state management, testing, typescript, ui/ux, web development]      - mobile-flutter
---

# 📱 Mobile React Native

> React Native/Expo best practices ve performance optimization.

---

*Mobile React Native v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [React Native Performance Guide](https://reactnative.dev/docs/performance) & [Expo Best Practices](https://docs.expo.dev/guides/best-practices/)

### Aşama 1: Environment & Architecture
- [ ] **Setup**: Expo (Managed) veya CLI (Bare) seçimini ihtiyaca göre yap.
- [ ] **Structure**: Klasör yapısını (Feature-based) kur ve `src/` klasöründe topla.
- [ ] **Navigation**: `React Navigation` veya `Expo Router` ile yapılandır.

### Aşama 2: UI & Animations
- [ ] **Animations**: 60 FPS akıcılık için `React Native Reanimated` (UI thread) kullan.
- [ ] **Components**: `FlashList` (Shopify) gibi yüksek performanslı liste bileşenlerini seç.
- [ ] **Styling**: `StyleSheet.create` kullanarak bellek kullanımını optimize et.

### Aşama 3: Performance & Offline
- [ ] **Bridge**: Bridge trafiğini azaltmak için JSI (JavaScript Interface) kullanan modülleri tercih et.
- [ ] **Storage**: `MMKV` gibi hızlı veri depolama çözümlerini kullan.
- [ ] **Profiles**: `Hermes` engine ve `Flipper` ile performans profillemesi yap.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Görseller `FastImage` vb. ile cache'leniyor mu? |
| 2 | Gereksiz re-render'lar `memo` ile engellendi mi? |
| 3 | Uygulama boyutu (Bundle size) optimize edildi mi? |
