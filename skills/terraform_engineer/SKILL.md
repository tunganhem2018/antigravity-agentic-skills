---
name: terraform_engineer
router_kit: DevOpsKit
description: Infrastructure as Code (IaC) tasarımı, Terraform modülleri ve state yönetimi.
metadata:
  skillport:
    category: devops
    tags: [architecture, automation, best practices, clean code, coding, collaboration, compliance, debugging, design patterns, development, documentation, efficiency, git, optimization, productivity, programming, project management, quality assurance, refactoring, software engineering, standards, terraform engineer, testing, utilities, version control, workflow]      - iac
---

# 🏗️ Terraform Engineer

> Altyapıyı kod olarak (IaC) yönetme, provision etme ve ölçekleme.

---

*Terraform Engineer v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [HashiCorp Terraform Best Practices](https://developer.hashicorp.com/terraform/docs/best-practices) & [Google Cloud IaC Foundation](https://cloud.google.com/docs/terraform/best-practices-for-terraform)

### Aşama 1: Infrastructure Analysis & Modularization
- [ ] **Resource Inventory**: Provision edilecek kaynakları ve bağımlılıklarını (VPC, Security Groups, IAM) haritalandır.
- [ ] **Component Separation**: Altyapıyı bağımsız modüllere (Network, Compute, Database) ayırarak tekrar kullanılabilirliği sağla.
- [ ] **Variable Schema**: Input ve Output şemalarını (`validation` blokları dahil) tanımla.

### Aşama 2: State Lifecycle & Security
- [ ] **Remote Backend**: State dosyasını güvenli bir merkezde (S3/Azure Blob) locking (`DynamoDB`) ile yapılandır.
- [ ] **Encryption & Secrets**: Hassas verileri `Sensitive = true` olarak işaretle ve `KMS/Vault` entegrasyonu sağla.
- [ ] **Provider Locking**: `required_providers` bloğuyla provider versiyonlarını sabitle.

### Aşama 3: Validation & CI/CD Orchestration
- [ ] **Policy as Code**: `TFLint` veya `Open Policy Agent (OPA)` ile altyapı güvenlik kurallarını (Policy check) doğrula.
- [ ] **Execution Plan**: `terraform plan` çıktısını incele ve "Destructive change" risklerini analiz et.
- [ ] **Automation**: Altyapı değişikliklerini GitHub Actions/GitLab CI üzerinden otomatik ve izlenebilir şekilde uygula (`apply`).

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Modüller "DRY" (Don't Repeat Yourself) prensibine uygun mu? |
| 2 | State dosyası şifreli (Encypted-at-rest) olarak mı saklanıyor? |
| 3 | Plan aşamasında beklenmedik kaynak silinmesi (Resource deletion) var mı? |
