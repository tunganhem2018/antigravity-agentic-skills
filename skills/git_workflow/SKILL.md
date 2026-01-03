---
name: git_workflow
router_kit: FullStackKit
description: Git branching modelleri (Gitflow, Trunk-based), commit kuralları ve merge stratejileri.
metadata:
  skillport:
    category: development
    tags: [architecture, automation, best practices, clean code, coding, collaboration, compliance, debugging, design patterns, development, documentation, efficiency, git, git workflow, optimization, productivity, programming, project management, quality assurance, refactoring, software engineering, standards, testing, utilities, version control, workflow]      - version-control
---

# 🌿 Git Workflow

> Etkin sürüm kontrolü ve işbirliği stratejileri.

---

*Git Workflow v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [Gitflow Workflow (Atlassian)](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow) & [Conventional Commits](https://www.conventionalcommits.org/)

### Aşama 1: Branching Strategy
- [ ] **Select Model**: Trunk-based (Küçük/Hızlı) veya Gitflow (Düzenli sürüm) seçimini yap.
- [ ] **Branch Naming**: `feat/`, `fix/`, `chore/` prefix kurallarını belirle.

### Aşama 2: Development & Committing
- [ ] **Atomic Commits**: Her değişikliği küçük, bağımsız commit'lere böl.
- [ ] **Conventional Commits**: Mesaj formatını (`type: description`) takip et.

### Aşama 3: Pull Request & Review
- [ ] **Review**: Kodu ana branch ile birleştirmeden önce PR aç ve review iste.
- [ ] **Merge**: Merge, Squash veya Rebase yöntemlerinden uygun olanı kullan.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Commit mesajları projeyi bilmeyen biri için anlaşılır mı? |
| 2 | Kod çakışmaları (Conflicts) ana branch'e dokunmadan çözüldü mü? |
| 3 | Merge sonrası commit geçmişi (History) temiz mi? |
