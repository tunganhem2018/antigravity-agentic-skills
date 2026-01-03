---
name: react_expert
router_kit: FullStackKit
description: React advanced patterns, rendering optimization, state management ve custom hooks.
metadata:
  skillport:
    category: frontend
    tags: [architecture, automation, best practices, cleanup, coaching, coding, collaboration, compliance, debugging, deployment, design patterns, development, documentation, efficiency, frontend, git, maintainability, optimization, performance, productivity, programming, project management, quality assurance, react, react expert_1, react hooks, react performance, refactoring, scalability, software engineering, standards, testing, typescript, utilities, version control, workflow]      - client-side-react
---

# ⚛️ React Expert

> Yüksek performanslı, scalable ve maintainable React uygulamaları.

---

## 🏗️ Advanced Patterns

### Composition over Inheritance
- Slot pattern ve Render Props kullanımı.
- HOC (High Order Components) yerine Hooks ve Composition tercihi.

### Custom Hooks
Business logic'in UI'dan ayrılması.
```typescript
function useUserStatus(userId: string) {
  const [isOnline, setIsOnline] = useState(null);
  useEffect(() => {
    // Subscription logic
  }, [userId]);
  return isOnline;
}
```

---

## ⚡ Performance Optimization

### Rendering Control
- **`React.memo`**: Props değişmediği sürece render engelleme.
- **`useMemo`**: Pahalı hesaplamaların cache'lenmesi.
- **`useCallback`**: Fonksiyon referanslarının korunması.

### Virtualization
Binlerce satırlık listeler için `react-window` veya `react-virtuoso` kullanımı.

---

## 🔧 Workflow

> **Kaynak:** [React Official Documentation](https://react.dev/) & [Bulletproof React Architecture](https://github.com/alan2207/bulletproof-react)

### Aşama 1: Component Design & State
- [ ] **Atomic Design**: Component'leri Atom, Molecule, Organism seviyesinde modüler tasarla.
- [ ] **State Colocation**: State'i mümkün olan en alt (Leaf) component'te tut (Gereksiz top-level render engelleme).
- [ ] **Logic Separation**: UI component'lerinden business logic'i `Custom Hooks` içine taşı.

### Aşama 2: Performance Audit
- [ ] **DevTools**: Profiler ile "Wasted Renders" ve "Long Tasks" analizi yap.
- [ ] **Code Splitting**: `React.lazy` ve `Suspense` ile bundle boyutunu optimize et.
- [ ] **Optimization**: Sadece gerekli yerlerde `memo`, `useMemo` ve `useCallback` kullan (Aşırı kullanım maliyetlidir).

### Aşama 3: Robustness & DX
- [ ] **Type Safety**: Tüm component ve hook'ları TypeScript interface'leri ile koru.
- [ ] **Error Boundaries**: Uygulamanın çökmesini engellemek için kritik bölgeleri `ErrorBoundary` ile sarmala.
- [ ] **Testing**: Kritik UI logic'ini `React Testing Library` (RTL) ile "User Behavior" odaklı test et.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | `useEffect` içindeki dependency listeleri eksiksiz mi? (No stale closures). |
| 2 | Context API "Prop Drilling" çözümü için mi kullanılıyor? (Eğer sık değişiyorsa performance check). |
| 3 | Accessibility (Aria-labels, Keyboard nav) kurallarına uyuldu mu? |

---

*React Expert v1.1 - Enhanced*
