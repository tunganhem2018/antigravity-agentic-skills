---
name: platform_engineering
router_kit: FullStackKit
description: Developer Experience (DevEx) optimizasyonu, Internal Developer Platform (IDP) ve self-service altyapı.
metadata:
  skillport:
    category: operations
    tags: [architecture, automation, aws, azure, best practices, cloud, cloud computing, cluster management, containerization, deployment, devops, docker, gcp, infrastructure as code, kubernetes, monitoring, orchestration, platform engineering, platform engineering_1, reliability, scalability, security, software engineering, terraform, workflow]      - devops
---

# 🏗️ Platform Engineering

> Yazılım ekipleri için self-service altyapı ve Developer Experience (DevEx) rehberi.

---

## 🚀 Core Objectives

### 1. Developer Self-Service
Geliştiricilerin bilet (Ticket) açmadan kendi altyapılarını (DB, Cache, Environment) kurabilmesi.
- **Araç**: Backstage, Humanitec, Port.

### 2. Cognitive Load Reduction
Geliştiricinin altyapı karmaşıklığıyla (K8s, Cloud, Networking) boğuşmasını önleme.
- **Altın Yol**: "Golden Paths" (Önceden tanımlanmış, güvenli ve standart yollar).

### 3. Consistency & Security
Tüm ekiplerin aynı standartlarda, güvenli ve denetlenebilir bir altyapıda çalışması.

---

## 🛠️ IDP (Internal Developer Platform) Components

| Katman | Örnek Araçlar |
|--------|---------------|
| **Portal** | Backstage, Compass |
| **Ci/CD** | GitHub Actions, ArgoCD |
| **IaC** | Terraform, Pulumi, Crossplane |
| **Orchestration** | Kubernetes, Nomad |
| **Security** | Vault, Trivy |

---

## 🔧 Workflow

> **Kaynak:** [What is Platform Engineering?](https://platformengineering.org/blog/what-is-platform-engineering) & [The Platform Engineering Guide](https://internaldevplatform.org/)

### Aşama 1: Discovery & Standardization
- [ ] **Needs Analysis**: Geliştiricilerin en çok zaman kaybettiği alanları (Örn: Env setup) belirle.
- [ ] **Establish Patterns**: Standart uygulama şablonlarını (Base images, Helm charts) oluştur.
- [ ] **Golden Paths**: En yaygın senaryolar için uçtan uca otomatize edilmiş "Altın Yolları" dökümante et.

### Aşama 2: Platform Building (IDP)
- [ ] **Abstraction**: Altyapıyı (Infrastructure) basitleştiren bir API veya Portal katmanı kur.
- [ ] **GitOps Integration**: Altyapı değişikliklerinin Git üzerinden (`ArgoCD` veya `Flux`) yönetilmesini sağla.
- [ ] **Policy as Code**: Güvenlik ve maliyet politikalarını (`OPA` veya `Kyverno`) otomatik denetle.

### Aşama 3: Adoption & Measurement
- [ ] **Onboarding**: Ekiplerin yeni platforma geçişini eğitim ve dökümantasyon ile destekle.
- [ ] **DORA Metrics**: Platformun etkisini ölç (Deployment Frequency, Lead Time for Changes).
- [ ] **Iterate**: Geliştirici geri bildirimleriyle platformu sürekli iyileştir (Product mindset).

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Platform geliştiriciler için işleri zorlaştırıyor mu kolaylaştırıyor mu? |
| 2 | "Shadow Ops" (Gizli operasyonlar) hala devam ediyor mu? |
| 3 | Altyapı maliyetleri platform üzerinden izlenebiliyor mu? |

---

*Platform Engineering v1.1 - Enhanced*
