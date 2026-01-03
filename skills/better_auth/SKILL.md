---
name: better_auth
router_kit: SecurityKit
description: Better-Auth kütüphanesi ile hızlı, güvenli ve modern kimlik doğrulama çözümleri.
metadata:
  skillport:
    category: security
    tags: [auth, better-auth, typescript, nextjs, security]
---

# 🛡️ Better-Auth

TypeScript tabanlı, esnek ve "Developer Friendly" kimlik doğrulama kütüphanesi kullanımı.

---

## 🔄 Workflow

> **Kaynak:** [Better-Auth Documentation](https://better-auth.com/) & [Next.js Auth Best Practices](https://nextjs.org/docs/app/building-your-application/authentication)

### Aşama 1: Kurulum ve Adaptör (Setup & Adapter)
- [ ] **Initialization:** `better-auth` paketini kur ve Prisma/Drizzle adaptörünü bağla.
- [ ] **Schema Sync:** Veritabanı tablolarını (`User`, `Session`, `Account`) Better-Auth standartlarına göre güncelle.
- [ ] **Base Config:** `baseUrl` ve `secret` değerlerini environment variables üzerinden tanımla.

### Aşama 2: Sağlayıcılar ve Client (Providers & Client)
- [ ] **Provider Selection:** Google, GitHub, Email-Password veya Passkey sağlayıcılarını aktif et.
- [ ] **Client Setup:** Frontend tarafında `createAuthClient` ile hooks yapısını kur.
- [ ] **Middleware:** Sayfa koruma (Route protection) için Next.js middleware entegrasyonunu yap.

### Aşama 3: Özelleştirme ve Eklentiler (Plugins & customization)
- [ ] **Plugins:** Admin yetkileri (RBAC), Organizasyonlar veya MFA eklentilerini ihtiyaca göre ekle.
- [ ] **Custom Fields:** Kullanıcı modeline özel alanlar (Bio, Avatar vb.) ekleyerek şemayı genişlet.
- [ ] **Testing:** Giriş yapma, çıkış yapma ve yetkisiz erişim senaryolarını doğrula.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1     | Secret key'ler `BETTER_AUTH_SECRET` olarak güvenli saklanıyor mu? |
| 2     | `Better-Auth` tarafından sağlanan hazır UI komponentleri doğru şekilde stilize edildi mi? |
| 3     | Session'lar sunucu tarafında (Server Components) doğru şekilde okunuyor mu? |

---
*Better-Auth v1.0 - Evidence-Based Update*
