---
name: react_expert
router_kit: FullStackKit
description: React 18/19 best practices, Hooks, Server Components ve Context API.
metadata:
  skillport:
    category: development
    tags: [accessibility, api integration, backend, browser apis, client-side, components, css3, debugging, deployment, frameworks, frontend, fullstack, html5, javascript, libraries, node.js, npm, performance optimization, react expert, responsive design, seo, state management, testing, typescript, ui/ux, web development]      - frontend-mastery
---

# ⚛️ React Expert

> Yüksek performanslı ve ölçeklenebilir React uygulamaları geliştirme.

---

*React Expert v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [React Documentation - Thinking in React](https://react.dev/learn/thinking-in-react) & [Kent C. Dodds - Advanced React Patterns](https://kentcdodds.com/blog/advanced-react-patterns)

### Aşama 1: component Design & State
- [ ] **Atomicity**: Bileşenleri "Single Responsibility" prensibine göre küçük parçalara ayır.
- [ ] **State Location**: State'i "Lifting State Up" veya `Context API` ile doğru yere yerleştir.
- [ ] **Immutability**: Veriyi mutasyona uğratmak yerine her zaman yeni kopyasını (spread operator vb.) kullan.

### Aşama 2: Hooks & Effects
- [ ] **Custom Hooks**: Tekrarlayan mantıkları (Data fetching, Logic) custom hook'lara taşı.
- [ ] **Dependency**: `useEffect` bağımlılık dizisini eksizsiz doldur ve sonsuz döngüleri engelle.
- [ ] **Memoization**: `useMemo` ve `useCallback` ile ağır hesaplamaları ve gereksiz re-render'ları optimize et.

### Aşama 3: Performance & Modern Features
- [ ] **Code Splitting**: `React.lazy` ve `Suspense` ile bundle boyutunu düşür.
- [ ] **Server Components**: Veri çeken ağır bileşenleri Server Side'a taşı (Next.js vb. ile).

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | "Hydration issues" yaşanıyor mu? |
| 2 | Gereksiz re-render'lar (DevTools Profiler ile) kontrol edildi mi? |
| 3 | Hook kurallarına (Rules of Hooks) uyuldu mu? |
