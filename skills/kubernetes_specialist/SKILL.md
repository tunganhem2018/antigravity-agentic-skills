---
name: kubernetes_specialist
router_kit: DevOpsKit
description: Kubernetes cluster yönetimi, Helm, Kustomize ve GitOps (ArgoCD) stratejileri.
metadata:
  skillport:
    category: devops
    tags: [automation, aws, bash scripting, ci/cd, cloud computing, containerization, deployment strategies, devops, docker, gitops, infrastructure, infrastructure as code, kubernetes, kubernetes specialist, linux, logging, microservices, monitoring, orchestration, pipelines, reliability, scalability, security, server management, terraform]      - k8s
---

# ☸️ Kubernetes Specialist

> Ölçeklenebilir konteyner orkestrasyonu ve yönetimi.

---

*Kubernetes Specialist v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [Kubernetes Best Practices](https://kubernetes.io/docs/setup/best-practices/) & [GitOps Working Group](https://opengitops.dev/)

### Aşama 1: Cluster & Resource Design
- [ ] **Provisioning**: Managed (EKS, GKE, AKS) veya Self-managed cluster kurulumunu yap.
- [ ] **Resources**: CPU/Memory limitlerini (`Resources & Limits`) her pod için tanımla.
- [ ] **Network**: Ingress controller ve NetworkPolicy kurallarını belirle.

### Aşama 2: Manifest & Package (Helm)
- [ ] **Templates**: Helm chart veya Kustomize ile manifestleri parametrize et.
- [ ] **Config**: Secret ve ConfigMap yönetimini (External Secrets vb.) yapılandır.

### Aşama 3: GitOps & CI/CD
- [ ] **ArgoCD/Flux**: Git reposundaki değişikliklerin otomatik cluster'a yansımasını sağla.
- [ ] **HPA**: Trafiğe göre otomatik ölçekleme (Horizontal Pod Autoscaler) kur.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Podlar "Non-root" olarak çalışıyor mu? |
| 2 | Liveness ve Readiness probelar doğru ayarlandı mı? |
| 3 | Cluster upgrade stratejisi (Canary/Blue-Green) hazır mı? |
