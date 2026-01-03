---
name: nextjs_specialist
router_kit: FullStackKit
description: Next.js (App Router), Server Components, Server Actions ve SSR/SSG/ISR stratejileri.
metadata:
  skillport:
    category: frontend
    tags: [architecture, automation, best practices, clean code, coding, collaboration, compliance, debugging, design patterns, development, documentation, efficiency, frontend, git, maintainability, next.js, nextjs, nextjs specialist, optimization, productivity, programming, project management, quality assurance, react, refactoring, scalability, software engineering, standards, testing, typescript, utilities, version_control, workflow]      - fullstack-react
---

# 🚀 Next.js Specialist

> Modern React framework'ü ile performanslı ve scalable web uygulamaları.

---

## 🏗️ Architecture (App Router)

### Server vs. Client Components
- **Server Components (Default)**: Veri çekme, sensitive info kullanımı. Minimal client-side JS bundle.
- **Client Components (`'use client'`)**: Interactive UI, Event listeners (`onClick`), Browser APIs (`useEffect`).

### Data Fetching
```typescript
// Server Component logic
async function Page() {
  const res = await fetch('https://api.example.com/data', { 
    next: { revalidate: 3600 } // ISR
  });
  const data = await res.json();
  return <DataList items={data} />;
}
```

---

## 🛠️ Performance & SEO

### Rendering Stratejileri
- **ISR (Incremental Static Regeneration)**: Statik sayfada belirli aralıklarla veri güncelleme.
- **Streaming & Suspense**: Sayfanın bölümlerini yüklendikçe gösterme.
- **PPR (Partial Pre-rendering)**: Statik ve dinamik kısımların hibrit sunulması.

### Optimization
- **`next/image`**: Otomatik resizing, webp conversion, lazy loading.
- **`next/font`**: Zero layout shift font yükleme.
- **Middleware**: Authentication ve redirection için edge-side kontrol.

---

## 🔐 Security & Forms

### Server Actions
Form verilerini doğrudan server'da işleme.
```typescript
async function createInvoice(formData: FormData) {
  'use server';
  const rawFormData = {
    amount: formData.get('amount'),
    // ... logic
  };
}
```

---

*Next.js Specialist v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [Next.js Documentation](https://nextjs.org/docs) & [React Server Components](https://react.dev/reference/react/use-client)

### Aşama 1: Routing & Component Architecture
- [ ] **Structure**: `layout.tsx`, `page.tsx` ve `loading.tsx` dosyalarıyla dosya tabanlı routing yapısını kur.
- [ ] **Boundary**: Server ve Client component sınırlarını ("use client") doğru belirle (Client'ı ağacın en ucuna koy).
- [ ] **Parallel Routes**: Gerekiyorsa `@modal` gibi paralel route'lar kullan.

### Aşama 2: Data & State Management
- [ ] **Fetching**: Server component içinde `async/await` ile doğrudan DB/API erişimi yap (State yönetimi gerekmez).
- [ ] **Caching**: Next.js `fetch` cache mekanizmasını (`force-cache`, `no-store`) ihtiyaca göre ayarla.
- [ ] **Actions**: Form işlemleri için `useFormStatus` ve `useFormState` ile Server Actions kullan.

### Aşama 3: Optimization & Deployment
- [ ] **SEO**: `Metadata` API kullanarak dinamik sayfa başlıkları ve OG tagleri ekle.
- [ ] **Vitals**: Image ve Font optimizasyonları ile Core Web Vitals (LCP, CLS) puanlarını kontrol et.
- [ ] **Middleware**: Edge runtime'da auth kontrolünü sağla.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Client component içine büyük kütüphaneler (lodash vb.) import edildi mi? (Bundle size riski). |
| 2 | Dinamik route'lar için `generateStaticParams` kullanılıyor mu? |
| 3 | Server Action'larda input validation (Zod vb.) yapıldı mı? |
