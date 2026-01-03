---
name: plan_work
router_kit: AIKit
description: İş planlama, task breakdown ve LLM tabanlı proje yönetimi stratejileri.
metadata:
  skillport:
    category: productivity
    tags: [architecture, automation, best practices, cleanup, coaching, collaboration, development, documentation, efficiency, focus, integrations, maintainability, metadata, open-source, optimization, performance, plan work_1, planning, prioritization, productivity, project management, quality assurance, scalability, software engineering, standards, testing, version control, web development, workflow]      - planning
---

# 📅 Plan Work & Task Breakdown

> Karmaşık projeleri yönetilebilir adımlara bölme ve planlama rehberi.

---

## 🏗️ Adım Adım Planlama

### 1. Requirements Analysis
- Müşteri veya proje dökümanını "Anlamda" (Intent) bazında analiz et.
- "Gizli" gereksinimleri (NFR - Non-functional requirements) bul.

### 2. Task Decomposition
- Büyük bir işi (Epic) en fazla 1-2 gün sürecek küçük işlere (Tasks) böl.
- Task'ların "Bağımsız" (Atomic) olmasına dikkat et.

### 3. Prioritization (MoSCoW)
- **Must Have**: Olmazsa olmaz.
- **Should Have**: Önemli ama acil değil.
- **Could Have**: Olsa güzel olur.
- **Won't Have**: Bu aşamada yapılmayacak.

---

## 🔧 Workflow

> **Kaynak:** [The Pragmatic Programmer](https://pragprog.com/titles/tpp20/the-pragmatic-programmer-20th-anniversary-edition/) & [Google Project Management](https://grow.google/certificates/project-management/)

### Aşama 1: Discovery & Intake
- [ ] **Gathering**: Tüm kısıtları (Deadline, Budget, Tech Stack) bir araya getir.
- [ ] **Ambiguity Check**: Net olmayan yerleri (Unknowns) listele ve soru sorarak netleştir.
- [ ] **Scope Boundary**: Nelerin yapılacağını değil, nelerin *yapılmayacağını* (Out of scope) da belirle.

### Aşama 2: Structuring & Estimating
- [ ] **WBS (Work Breakdown Structure)**: İşi hiyerarşik bir ağaca böl.
- [ ] **Estimation**: En iyi, en kötü ve en olası (PERT) süre tahminlerini yap. %20 buffer (tampon süre) ekle.
- [ ] **Dependencies**: Hangi işin hangisinden sonra geleceğini (Critical Path) belirle.

### Aşama 3: Execution & Tracking
- [ ] **Task Mapping**: İşleri panoya (Kanban/Scrum) taşı.
- [ ] **Checkpointing**: Her %25 ilerlemede bir kontrol noktası (Milestone) koy.
- [ ] **Retrospective**: Biten iş sonrası "Plan neydi, ne oldu?" analizi yap ve bir sonraki planı iyileştir.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | "Tanım" (Definition of Done) her task için net mi? |
| 2 | Tek bir kişi üzerinde darboğaz (Bottleneck) oluşuyor mu? |
| 3 | En riskli iş (Riskiest task) en başa alındı mı? |

---

*Plan Work v1.1 - Enhanced*
