---
name: incident_response
router_kit: DevOpsKit
description: Güvenlik olaylarına müdahale, kriz yönetimi ve kök neden analizi.
metadata:
  skillport:
    category: quality
    tags: [architecture, automation, best practices, clean code, coding, collaboration, compliance, debugging, design patterns, development, documentation, efficiency, git, incident response, optimization, productivity, programming, project management, quality assurance, refactoring, software engineering, standards, testing, utilities, version control, workflow]      - resilience
---

# 🛡️ Incident Response

> Güvenlik ihlallerine ve sistem kesintilerine karşı müdahale planı.

---

*Incident Response v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [NIST SP 800-61 Rev. 2](https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final) & [SANS Incident Handler's Handbook](https://www.sans.org/white-papers/33901/)

### Aşama 1: Preparation & Identification
- [ ] **Triage**: Olayı sınıflandır (Severity 1-5) ve ekibi topla.
- [ ] **Scope**: Etkilenen sistemleri ve veri türünü belirle.
- [ ] **Logs**: Firewall, IDS/IPS ve App loglarını güvenli bir yere kopyala (Evidence Preservation).

### Aşama 2: Containment & Eradication
- [ ] **Isolate**: Etkilenen sunucuyu ağdan kes (fişi çekme, portu kapat).
- [ ] **Patch**: Güvenlik açığını kapat (Hotfix, WAF kuralı).
- [ ] **Clean**: Malware temizliği yap veya sistemi güvenli backup'tan geri dön.

### Aşama 3: Recovery & Follow-up
- [ ] **Restore**: Sistemleri kademeli olarak ve izleyerek devreye al.
- [ ] **Report**: "Lessons Learned" raporu yaz (Kök neden, ne iyi gitti, ne kötü gitti).

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Saldırganın hala içeride olma ihtimali var mı? |
| 2 | Hukuki süreç için loglar imzalandı/hashlendi mi? |
| 3 | Benzer bir saldırı yarın olsa engelleyebilir miyiz? |
