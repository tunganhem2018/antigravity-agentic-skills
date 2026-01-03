---
name: drizzle_orm
router_kit: FullStackKit
description: Drizzle ORM kullanımı, şema tasarımı ve tip güvenli SQL sorguları.
metadata:
  skillport:
    category: database
    tags: [architecture, automation, best practices, clean code, coding, collaboration, compliance, debugging, design patterns, development, documentation, drizzle orm, efficiency, git, optimization, productivity, programming, project management, quality assurance, refactoring, software engineering, standards, testing, utilities, version control, workflow]      - sql
---

# 💧 Drizzle ORM

> Tip güvenli ve "SQL-like" veritabanı erişimi.

---

*Drizzle ORM v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [Drizzle ORM Documentation](https://orm.drizzle.team/docs/overview)

### Aşama 1: Schema Definition
- [ ] **Tables**: `db/schema.ts` içinde tablo yapılarını tanımla.
- [ ] **Relations**: `relations` fonksiyonu ile tablolar arası bağları kur.
- [ ] **Types**: Şemadan TypeScript tiplerini (`InferSelectModel` vb.) üret.

### Aşama 2: Migration & Connectivity
- [ ] **Config**: `drizzle.config.ts` ayarlarını yap.
- [ ] **Migrate**: `drizzle-kit generate` ve `push` (veya migrate) ile DB'yi güncelle.
- [ ] **Client**: Database bağlantısını (Postgres, MySQL, SQLite) başlat.

### Aşama 3: Querying
- [ ] **Select/Insert**: CRUD işlemlerini tip güvenli metodlarla gerçekleştir.
- [ ] **Filters**: Koşullu sorguları build et.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Şema ile veritabanı senkronize mi? |
| 2 | Sorgular tip hatası veriyor mu? |
| 3 | Performans (Raw SQL hızı) korunuyor mu? |
