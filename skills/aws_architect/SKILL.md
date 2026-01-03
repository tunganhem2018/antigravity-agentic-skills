---
name: aws_architect
router_kit: DevOpsKit
description: Expert AWS solution architecture for startups focusing on serverless, scalable, and cost-effective cloud infrastructure with modern DevOps practices and infrastructure-as-code
metadata:
  skillport:
    category: auto-healed
    tags: [automation, aws, aws architect, bash scripting, ci/cd, cloud computing, containerization, deployment strategies, devops, docker, gitops, infrastructure, infrastructure as code, kubernetes, linux, logging, microservices, monitoring, orchestration, pipelines, reliability, scalability, security, server management, terraform]      - aws_architect
---

# AWS Solution Architect for Startups

This skill provides comprehensive AWS architecture design expertise for startup companies, emphasizing serverless technologies, scalability, cost optimization, and modern cloud-native patterns.

---

*AWS Architect v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/)

### Aşama 1: Operational Excellence & Security
- [ ] **Ops**: Runbooks hazır mı? Hata durumunda (Rollback) süreç net mi?
- [ ] **Security**: IAM "Least Privilege" uygulandı mı? S3 Public Access kapalı mı?
- [ ] **Encryption**: Veri at-rest (KMS) ve in-transit (HTTPS) şifreli mi?

### Aşama 2: Reliability & Performance
- [ ] **Backup**: Veritabanı PITR (Point-in-Time Recovery) açık mı?
- [ ] **Scaling**: Auto-scaling tetikleyicileri (CPU/RAM/Requests) test edildi mi?
- [ ] **Caching**: CloudFront/ElastiCache katmanları doğru yapılandırıldı mı?

### Aşama 3: Cost Optimization
- [ ] **Right-Sizing**: Instance/Lambda boyutları CPU/RAM kullanımına uygun mu?
- [ ] **Lifecycle**: S3 verileri için Lifecycle kuralları (IA/Glacier) var mı?
- [ ] **Alerts**: Bütçe alarmları (AWS Budgets) kuruldu mu?

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Security Score > %90 (Trusted Advisor / Security Hub) |
| 2 | Yük testinde (Load Testing) %99.9 availability sağlandı |
| 3 | Tahmini maliyet bütçe sınırları içinde |
