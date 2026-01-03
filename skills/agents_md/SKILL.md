---
name: agents_md
router_kit: AIKit
description: AGENTS.md dosyaları oluşturma, monorepo yapılandırma ve agent instruction yönetimi rehberi.
metadata:
  skillport:
    category: development
    tags: [agents, agents md, algorithms, artificial intelligence, automation, chatbots, cognitive services, deep learning, embeddings, frameworks, generative ai, inference, large language models, llm, machine learning, model fine-tuning, natural language processing, neural networks, nlp, openai, prompt engineering, rag, retrieval augmented generation, tools, vector databases, workflow automation]      - conventions
---

# 🤖 AGENTS.md

> Agent instruction ve conventions dosyaları oluşturma rehberi.

---

## 📋 AGENTS.md Nedir?

AGENTS.md, AI coding assistant'ların proje özelinde kurallara uymasını sağlayan convention dosyasıdır.

---

*AGENTS.md v1.0 - Convention Over Configuration*

## 🔄 Workflow

> **Kaynak:** [AGENTS.md Best Practices](https://agents.md)

### Aşama 1: Context Extraction
- [ ] **Read Project Config**: `package.json`, `tsconfig.json`, `.eslintrc`.
- [ ] **Map Directory Structure**: Identify key folders (`src`, `app`, `lib`).
- [ ] **Identify Unwritten Rules**: Look at existing code for naming patterns (PascalCase vs camelCase).

### Aşama 2: Root Creation (`/AGENTS.md`)
- [ ] **Project Overview**: One sentence goal description.
- [ ] **Tech Stack**: List core frameworks and libraries.
- [ ] **Architecture**: High-level map of the system.
- [ ] **Conventions**: Explicit naming and coding rules.

### Aşama 3: Rule Definitions
- [ ] **Must Haves**: "Always use TypeScript strict mode", "Always use Zod".
- [ ] **Must Nots**: "No `any`", "No `console.log` in prod", "No class components".
- [ ] **Preferred**: "Prefer functional components", "Prefer arrow functions".

### Aşama 4: Nested & Maintenance
- [ ] **Sub-modules**: Create specific `AGENTS.md` for `src/components`, `src/api` if complex.
- [ ] **Sync**: Update `AGENTS.md` when adding new tech or changing patterns.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Proje yapısı doğru anlaşılmış |
| 2 | Root dosya mevcut ve okunabilir |
| 3 | AI kuralları ihlal etmiyor (test et) |
