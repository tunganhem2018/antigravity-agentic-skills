---
name: aws_architect
router_kit: DevOpsKit
description: AWS servisleri (EC2, S3, Lambda, RDS) ile ölçeklenebilir ve güvenli cloud mimarileri.
metadata:
  skillport:
    category: operations
    tags: [aws, cloud, architecture, devops, serverless]
---

# ☁️ AWS Architect

Amazon Web Services üzerinde güvenli, ölçeklenebilir ve maliyet odaklı mimari tasarımı.

---

## 🔄 Workflow

> **Kaynak:** [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) & [AWS Solutions Architecture Patterns](https://aws.amazon.com/architecture/)

### Aşama 1: Planlama ve Temeller (Foundation & VPC)
- [ ] **VPC Design:** Public ve Private subnetleri, NAT Gateway ve Security Group kurallarını tanımla.
- [ ] **Compute Strategy:** EC2 (IaaS), ECS/EKS (Containers) veya Lambda (Serverless) arasında seçim yap.
- [ ] **Identity Management (IAM):** "Least Privilege" prensibiyle minimal izinli IAM Roller ve Politikaları oluştur.

### Aşama 2: Ölçeklenebilirlik ve Depolama (Scalability & Storage)
- [ ] **Load Balancing (ELB):** Trafiği dağıtmak için ALB/NLB kurulumunu planla.
- [ ] **Data Management:** RDS (SQL), DynamoDB (NoSQL) veya S3 (Object Storage) konfigürasyonlarını yap.
- [ ] **Auto Scaling:** Yük durumuna göre kaynakların otomatik artıp azalması için kuralları belirle.

### Aşama 3: Monitoring ve Optimizasyon (Ops & Cost)
- [ ] **Observability:** CloudWatch ile metrikleri, CloudTrail ile audit loglarını takip et.
- [ ] **Disaster Recovery:** Backup planlarını (Snapshots, Multi-AZ) ve RPO/RTO hedeflerini saptama.
- [ ] **Cost Audit:** AWS Cost Explorer ile maliyetleri izle ve "Reserved Instances" veya "Savings Plans" değerlendir.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1     | Veritabanı ve kritik servisler "Private Subnet" içinde mi? |
| 2     | IAM kullanıcılarına Root yetkisi verilmediğinden emin misin? |
| 3     | "Single Point of Failure" (Tek arıza noktası) var mı? (Multi-AZ kontrolü) |

---
*AWS Architect v1.2 - Evidence-Based Update*
