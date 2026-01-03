---
name: auth_patterns
router_kit: SecurityKit
description: Modern kimlik doğrulama (OAuth2, JWT, Passwordless) ve yetkilendirme (RBAC, ABAC) desenleri.
metadata:
  skillport:
    category: backend
    tags: [security, authentication, authorization, jwt, oauth2]
---

# 🔐 Auth Patterns

Kimlik doğrulama ve yetkilendirme sistemleri için güvenli ve standart yapılar.

---

## 🔄 Workflow

> **Kaynak:** [OWASP Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html) & [Auth0 - Identity Standards](https://auth0.com/docs/get-started/identity-fundamentals)

### Aşama 1: Strateji ve Protokol Seçimi (Strategy Selection)
- [ ] **İhtiyaç Belirleme:** Session-based (Stateful) mı yoksa Token-based (Stateless) mı gerekli?
- [ ] **Protokol Belirleme:** OAuth2/OIDC (Sosyal Login), JWT (API) veya Magic Link (Passwordless) seç.
- [ ] **Yol Haritası:** Kullanıcı kaydı, şifre sıfırlama ve MFA (Multi-Factor) akışlarını planla.

### Aşama 2: Güvenli Uygulama (Secure Implementation)
- [ ] **Password Hashing:** Şifreleri Argon2 veya BCrypt ile "salt"layarak kaydet.
- [ ] **Token Security:** JWT'leri güvenle imzala, `exp` (Expire) süresini kısa tut ve `refresh token` mekanizmasını kur.
- [ ] **Access Control:** RBAC (Role-Based) veya ABAC (Attribute-Based) yetki ağacını kodla.

### Aşama 3: Denetim ve Hardenning (Audit & Hardening)
- [ ] **Vulnerability Check:** CSRF, Session Hijacking ve Brute Force saldırılarına karşı önlemleri test et.
- [ ] **Secure Storage:** Tokenları tarayıcıda `HttpOnly` ve `Secure` cookielerde sakla.
- [ ] **Logging:** Kritik güvenlik olaylarını (başarısız girişler, yetki değişimleri) anonim şekilde logla.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1     | Şifreler veritabanında "Plain Text" (açık metin) olarak asla tutulmuyor değil mi? |
| 2     | Token çalınması durumuna karşı `Revocation` (iptal) listesi veya mekanizması var mı? |
| 3     | MFA (Çift aşamalı doğrulama) kritik işlemler için zorunlu kılınabiliyor mu? |

---
*Auth Patterns v1.4 - Evidence-Based Update*
