---
name: prisma_orm
router_kit: FullStackKit
description: Prisma ORM setup, schema design, migrations, type-safety ve performance optimization.
metadata:
  skillport:
    category: backend
    tags: [architecture, automation, backend, best practices, cleanup, coding, collaboration, compliance, database, database design, debugging, deployment, design patterns, development, documentation, efficiency, git, maintainability, optimization, performance, prisma, prisma orm_1, productivity, programming, quality assurance, software engineering, standards, testing, typescript, utilities, version control, workflow]      - type-safe-orm
---

# ◭ Prisma ORM

> Tip güvenli (Type-safe), modern Node.js ve TypeScript ORM rehberi.

---

## 🚀 Setup & Schema

### Kurulum
```bash
npm install prisma --save-dev
npx prisma init
```

### schema.prisma
```prisma
model User {
  id    Int     @id @default(autoincrement())
  email String  @unique
  name  String?
  posts Post[]
}

model Post {
  id        Int     @id @default(autoincrement())
  title     String
  author    User    @relation(fields: [authorId], references: [id])
  authorId  Int
}
```

---

## 🛠️ CRUD Operations

### Querying
```typescript
const users = await prisma.user.findMany({
  where: { email: { contains: 'prisma.io' } },
  include: { posts: true } // Joins
});
```

### Transactions
```typescript
const [user, post] = await prisma.$transaction([
  prisma.user.create({ data: { ... } }),
  prisma.post.create({ data: { ... } })
]);
```

---

## 🔧 Workflow

> **Kaynak:** [Prisma Documentation](https://www.prisma.io/docs) & [Best Practices](https://github.com/prisma/prisma-examples)

### Aşama 1: Schema Design & Migrations
- [ ] **Modeling**: Veri modelini `schema.prisma` üzerinde tanımla. İlişkileri (`@relation`) ve index'leri (`@@index`) belirle.
- [ ] **Migration**: `npx prisma migrate dev --name <name>` ile veritabanı şemasını güncel tut. Geçmişi asla manuel değiştirme.
- [ ] **Generation**: Her şema değişikliğinden sonra `npx prisma generate` ile TypeScript tiplerini güncelle.

### Aşama 2: Application Integration
- [ ] **Instance**: `PrismaClient`'ı tek bir instance (Singleton) olarak oluştur (Connection pool yönetimi için).
- [ ] **Typed Queries**: Type-safety avantajını kullanarak runtime hatalarını önle.
- [ ] **Relations**: "N+1" sorununu önlemek için `include` (Join) veya `select` kullan.

### Aşama 3: Advanced Optimization
- [ ] **Performance**: Ağır sorgular için `prisma.$queryRaw` (Raw SQL) veya `Fluent API` tercih et.
- [ ] **Middlewares/Extensions**: Loglama, Soft-delete veya veri şifreleme için Prisma Extensions kullan.
- [ ] **Deployment**: Production'da `prisma migrate deploy` komutunu CI/CD pipeline'ına ekle.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | `DATABASE_URL` .env dosyasında ve gitignore'da mı? |
| 2 | Gereksiz `include` kullanımı (Over-fetching) var mı? |
| 3 | Migration'lar veri kaybına (Data loss) neden oluyor mu? (Check warning). |

---

*Prisma ORM v1.1 - Enhanced*
