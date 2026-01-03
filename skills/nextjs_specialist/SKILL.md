---
name: nextjs_specialist
router_kit: FullStackKit
description: Next.js App Router, SSR/SSG stratejileri ve Vercel deployment.
metadata:
  skillport:
    category: development
    tags: [accessibility, api integration, backend, browser apis, client-side, components, css3, debugging, deployment, frameworks, frontend, fullstack, html5, javascript, libraries, nextjs specialist, node.js, npm, performance optimization, responsive design, seo, state management, testing, typescript, ui/ux, web development]      - fullstack-react
---

# ⚛️ Next.js Specialist

> Modern React framework'ü ile tam kapsamlı web uygulamaları.

---

*Nextjs Specialist v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [Next.js Documentation - App Router Architecture](https://nextjs.org/docs/app)

### Aşama 1: Route & Layout Design
- [ ] **App Router**: Klasör tabanlı (Folder-based) rotaları oluştur.
- [ ] **Layouts**: Ortak UI parçalarını (Navbar, Footer) iç içe (nested) layoutlar ile yönet.
- [ ] **Special Files**: `loading.tsx`, `error.tsx` ve `not-found.tsx` dosyalarını hazırla.

### Aşama 2: Data Fetching (Server First)
- [ ] **Server Components**: Veri çekme işlemlerini varsayılan olarak Server Component'lerde yap.
- [ ] **Caching**: `fetch` opsiyonları (`force-cache`, `revalidate`) ile önbellekleme stratejisini belirle.
- [ ] **Server Actions**: Form işlemleri ve mutasyonlar için "use server" fonksiyonlarını kullan.

### Aşama 3: Optimization & Deploy
- [ ] **Images**: `next/image` ile otomatik boyutlandırma ve lazy load sağla.
- [ ] **Metadata**: SEO için dinamik veya statik metadata objelerini ekle.
- [ ] **Middleware**: Edge runtime üzerinde auth ve yönlendirme kontrollerini yap.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | "Hydration Error" alınıyor mu? |
| 2 | Gereksiz yere "use client" kullanıldı mı (Server components önceliği)? |
| 3 | LCP ve CLS değerleri optimize mi? |
