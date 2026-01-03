---
name: auth_patterns
router_kit: SecurityKit
description: Master authentication and authorization patterns including JWT, OAuth2, session management, and RBAC to build secure, scalable access control systems. Use when implementing auth systems, securing APIs, or debugging security issues.
metadata:
  skillport:
    category: auto-healed
    tags: [accessibility, api integration, auth patterns, backend, browser apis, client-side, components, css3, debugging, deployment, frameworks, frontend, fullstack, html5, javascript, libraries, node.js, npm, performance optimization, responsive design, seo, state management, testing, typescript, ui/ux, web development]      - auth_patterns
---

# Authentication & Authorization Implementation Patterns

Build secure, scalable authentication and authorization systems using industry-standard patterns and modern best practices.

---

*Auth Patterns v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [OWASP Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)

### Aşama 1: Strategy Selection
- [ ] **Context**: SPA/Mobile -> JWT. SSR/Traditional -> Session. Enterprise -> OAuth2/SAML.
- [ ] **Data Sensitivity**: Yüksek güvenlik gerekirse -> Short-lived tokens + Rotation.
- [ ] **Scale**: Horizontal scaling gerekirse -> Stateless JWT.

### Aşama 2: Core Implementation
- [ ] **Storage**: Database şeması (Users, RefreshTokens).
- [ ] **Hashing**: `bcrypt` veya `argon2` kurulumu.
- [ ] **Middleware**: `verifyToken` veya `requireAuth` fonksiyonları.

### Aşama 3: Hardening (Hard-Requirements)
- [ ] **Transport**: HTTPS zorunlu.
- [ ] **Rate Limiting**: Login endpoint koruması (Brute-force).
- [ ] **Input Validation**: Email/Password regex (Zod/Joi).

### Aşama 4: Audit Steps
- [ ] **Token Storage**: LocalStorage'da access token var mı? (Varsa XSS riski -> HttpOnly Cookie kullan).
- [ ] **CSRF**: State modifier requestlerde koruma var mı?
- [ ] **Logs**: Şifreler loglara düşüyor mu? (Asla düşmemeli).

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Strateji mimariye uygun (Over-engineering değil) |
| 2 | Şifreler hash'li saklanıyor |
| 3 | Login endpoint'inde Rate Limit aktif |
| 4 | Penetration test adımları (XSS/CSRF) temiz |
