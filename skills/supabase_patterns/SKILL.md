---
name: supabase_patterns
router_kit: FullStackKit
description: Supabase Auth, Database, Realtime ve Edge Functions kullanımı.
metadata:
  skillport:
    category: database
    tags: [architecture, automation, best practices, clean code, coding, collaboration, compliance, debugging, design patterns, development, documentation, efficiency, git, optimization, productivity, programming, project management, quality assurance, refactoring, software engineering, standards, supabase patterns, testing, utilities, version control, workflow]      - baas
---

# ⚡ Supabase Patterns

> Supabase ile hızlı ve ölçeklenebilir backend-as-a-service kullanımı.

---

*Supabase Patterns v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [Supabase Documentation](https://supabase.com/docs) & [Supabase Launch Week Highlights](https://supabase.com/launch-week)

### Aşama 1: Database & RLS
- [ ] **Schema**: Dashboard veya SQL Editor üzerinden tabloları ve ilişkilerini kur.
- [ ] **RLS Policies**: Her tablo için Row Level Security kurallarını (Kim hangi veriyi görebilir?) tanımla.
- [ ] **Functions**: Veritabanı tarafında tetiklenecek `PostgreSQL Functions` ve `Triggers` oluştur.

### Aşama 2: Authentication & Realtime
- [ ] **Auth**: `supabase.auth` ile Login (Email, Social, Magic Link) sistemini kur.
- [ ] **Realtime**: Veritabanı değişikliklerini anlık dinlemek için `.on('postgres_changes', ...)` aboneliklerini yap.
- [ ] **Storage**: Dosya yükleme ve kova (Bucket) izinlerini yapılandır.

### Aşama 3: Edge Functions & Integration
- [ ] **Functions**: Sunucusuz (Serverless) mantıklar için `Supabase Edge Functions` (Deno) yaz.
- [ ] **Security**: API key'leri ve `service_role` yetkilerini güvenli şekilde kullan.
- [ ] **Monitoring**: Dashboard üzerinden logları ve veritabanı performansını takip et.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | RLS aktif mi? (Aktif değilse tablo tüm internete açıktır!). |
| 2 | Veritabanı index'leri sorgu hızına göre optimize edildi mi? |
| 3 | Edge functionlarda `environment variables` güvenli mi? |
