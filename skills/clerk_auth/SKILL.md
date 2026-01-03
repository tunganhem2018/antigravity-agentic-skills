---
name: clerk_auth
router_kit: FullStackKit
description: Clerk Authentication ile kullanıcı yönetimi, oturumlar ve korumalı rotalar.
metadata:
  skillport:
    category: security
    tags: [auth, clerk, nextjs, react, security]
---

# 👤 Clerk Auth

Modern, hazır UI bileşenli ve güvenli kimlik doğrulama servisi kullanımı.

---

## 🔄 Workflow

> **Kaynak:** [Clerk Documentation](https://clerk.com/docs) & [Clerk Next.js Guide](https://clerk.com/docs/references/nextjs/overview)

### Aşama 1: Entegrasyon ve Middleware (Integration)
- [ ] **Project Setup:** Clerk Dashboard'dan API anahtarlarını al ve `.env.local` dosyasına ekle.
- [ ] **Provider Setup:** Uygulamayı `<ClerkProvider>` ile sar.
- [ ] **Middleware Guard:** `clerkMiddleware()` kullanarak public ve private rotaları tanımla.

### Aşama 2: UI ve Kullanıcı Akışları (UI Components)
- [ ] **Auth Pages:** `<SignIn />`, `<SignUp />` ve `<UserButton />` bileşenlerini yerleştir.
- [ ] **Customization:** Clerk Appearance API kullanarak markanızın renklerini ve tipografisini uyarla.
- [ ] **User Metadata:** Kullanıcı profiline özel roller veya metadata ekle.

### Aşama 3: Server Side ve Webhooks (Server & Webhooks)
- [ ] **Server Session:** `auth()` fonksiyonu ile Server Componentlarda oturum durumunu kontrol et.
- [ ] **Webhooks:** Veritabanını Clerk ile senkronize tutmak için Svix ile webhook dinleyicileri (user.created, user.updated) kur.
- [ ] **Organization Management:** İhtiyaç varsa Clerk Organizations özelliğini aktif ederek ekip yönetimini sağla.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1     | Korumalı sayfalara giriş yapmadan erişilebiliyor mu? (Middleware testi) |
| 2     | Webhook'lar güvenli (Signature verification) şekilde doğrulanıyor mu? |
| 3     | Kullanıcı çıkış yaptığında tokenlar ve sessionlar tamamen temizleniyor mu? |

---
*Clerk Auth v1.3 - Evidence-Based Update*
