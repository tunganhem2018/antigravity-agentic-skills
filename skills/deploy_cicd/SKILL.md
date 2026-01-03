---
name: deploy_cicd
description: Modern CI/CD pipeline tasarımı, güvenliği ve v2.0 otomasyon standartları rehberi.
metadata:
  skillport:
    category: operations
    tags: [architecture, automation, best practices, clean code, coding, collaboration, compliance, deploy cicd, design patterns, development, documentation, efficiency, git, optimization, productivity, programming, project management, quality assurance, refactoring, software engineering, standards, testing, utilities, version control, workflow]      - devops
---

# 🚀 Deploy CI/CD

> Modern CI/CD ve otomasyon rehberi.

---

## 🏗️ Pipeline Architecture

### 1. Build & Test
- Linting (ESLint/Prettier)
- Unit Testing (Vitest/Jest)
- Security Scan (Snyk/Trivy)

### 2. Artifact Creation
- Docker image building
- Registry push (ECR/GCR)

### 3. Deployment
- Staging/Production environments
- Green-Blue or Canary deployments

---

## 🔒 Security Best Practices

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      id-token: write  # For OIDC
    steps:
      - uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: arn:aws:iam::123456789012:role/GitHubActionsRole
          aws-region: us-east-1
```

---

## 📊 Deployment Strategy Template

| Strategy | Risk | Speed | Complexity |
|----------|------|-------|------------|
| **Recreate** | High | Fast | Low |
| **Rolling** | Med | Med | Med |
| **Blue-Green** | Low | Slow| High |
| **Canary** | V. Low| Slow| V. High |

---

## 🔄 Workflow

> **Kaynak:** [DORA Research (DORA.dev)](https://dora.dev/) & [GitHub Actions Hardening Guide](https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions)

### Aşama 1: Pipeline Orchestration & Security
- [ ] **Workflow Design**: Test, Güvenlik (SAST) ve Deploy adımlarını mantıksal job'lara ayır.
- [ ] **Security Hardening**: `permissions: read-all` veya minimal izin prensibini uygula. 3. parti action'ları commit SHA ile sabitle.
- [ ] **Secrets Management**: Hassas verileri asla YAML içinde saklama; GitHub Secrets veya HashiCorp Vault kullan.

### Aşama 2: Testing & Artifact Management
- [ ] **Parallel Testing**: Testleri matrix build kullanarak farklı ortam ve versiyonlarda paralel çalıştır.
- [ ] **Caching**: `npm` veya `pip` bağımlılıklarını cache'leyerek pipeline süresini %40+ iyileştir.
- [ ] **Artifact Creation**: Deploy edilebilir paketi (Docker image/Binary) oluştur ve bir registry'ye (ECR/GCR) yükle.

### Aşama 3: Deployment & DORA Tracking
- [ ] **Deployment Strategy**: Canary veya Blue-Green stratejisini seç. Rolling update ile kesinti süresini minimize et.
- [ ] **Environments**: Production deploy öncesi `environment protection rules` (manuel onay) ekle.
- [ ] **Metric Collection**: DORA metriklerini (Deployment Frequency, Lead Time for Changes) otomatik takip et.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Pipeline başarısız olduğunda sistem güvenli bir halde kalıyor mu? |
| 2 | Her PR'da otomatik "Linter" ve "Unit Test" çalışıyor mu? |
| 3 | Deploy sonrası otomatik bir "Smoke Test" mevcut mu? |

---
*Deploy CI/CD v2.0 - With Workflow*
