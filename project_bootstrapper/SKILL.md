---
name: project_bootstrapper
router_kit: FullStackKit
description: Yeni projelerin hızlı kurulumu, boilerplate yönetimi ve standart proje yapısı.
metadata:
  skillport:
    category: productivity
    tags: [architecture, automation, best practices, cleanup, coaching, collaboration, configuration, deployment, development, documentation, efficiency, integrations, maintainability, metadata, open-source, optimization, performance, productivity, project bootstrapper_1, quality assurance, scalability, software engineering, standards, testing, version control, web development, workflow]      - scaffolding
---

# 🚀 Project Bootstrapper

> Yeni projelere ışık hızında ve standartlara uygun başlama rehberi.

---

## 🛠️ Tooling & Frameworks

### Frontend (React/Next.js)
```bash
npx create-next-app@latest my-app --typescript --tailwind --eslint
```

### Backend (NestJS)
```bash
npm i -g @nestjs/cli
nest new my-project
```

### Monorepo (Turborepo)
```bash
npx create-turbo@latest
```

---

## 🧱 Standard File Structure

```text
├── .github/          # CI/CD Workflows
├── src/
│   ├── components/   # UI Blocks
│   ├── lib/          # Shared Utilities
│   ├── hooks/        # Custom React Hooks
│   ├── types/        # TypeScript Definitions
│   └── services/     # API / logic layer
├── .env.example      # Template for environment variables
├── README.md         # Documentation
└── package.json
```

---

## 🔧 Workflow

> **Kaynak:** [Next.js Deployment Guide](https://nextjs.org/docs/app/building-your-application/deploying) & [NestJS Architecture](https://docs.nestjs.com/first-steps)

### Aşama 1: Scaffolding & Config
- [ ] **Framework**: Proje tipine göre (Web, Mobile, CLI) doğru CLI aracını seç.
- [ ] **TypeScript**: `tsconfig.json` ayarlarını (`strict: true`, `baseUrl`) standartlara göre düzenle.
- [ ] **Linter/Formatter**: `ESLint`, `Prettier` ve `Husky` (pre-commit hooks) kurulumlarını yap.

### Aşama 2: Base Infrastructure
- [ ] **Environments**: `.env.example` oluştur ve `Zod` gibi kütüphanelerle env validation ekle.
- [ ] **Auth/DB**: `Clerk`, `Supabase` veya `Prisma` gibi temel servis bağlantılarını kur.
- [ ] **UI Library**: `TailwindCSS` ve `shadcn/ui` bileşen kütüphanesini hazırla.

### Aşama 3: CI/CD & Documentation
- [ ] **Git Setup**: `.gitignore` dosyasını kontrol et ve ilk commit'i `feat: initial commit` ile at.
- [ ] **CI Pipeline**: GitHub Actions üzerinden `build` ve `lint` check'lerini aktifleştir.
- [ ] **Documentation**: `README.md` dosyasını kurulum (Setup) ve çalışma (Run) talimatlarıyla doldur.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Proje "Out-of-the-box" çalışıyor mu? (Clone -> Install -> Run). |
| 2 | Hassas veriler (Secrets) yanlışlıkla git'e eklendi mi? |
| 3 | Bağımlılıklar (Versions) güncel ve stabil mi? |

---

*Project Bootstrapper v1.1 - Enhanced*
