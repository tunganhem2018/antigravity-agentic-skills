---
name: agent_orchestration
router_kit: AIKit
description: Çoklu AI ajanlarının birlikte çalışması, görev dağılımı ve senkronizasyonu yönetimi.
metadata:
  skillport:
    category: ai
    tags: [agents, orchestration, automation, multi-agent, ai-engineering]
---

# 🤖 Agent Orchestration

Karmaşık görevleri alt parçalara bölen ve uzman ajanları koordine eden sistemler.

---

## 🔄 Workflow

> **Kaynak:** [AutoGen Framework](https://github.com/microsoft/autogen) & [LangChain Multi-Agent Systems](https://python.langchain.com/docs/modules/agents/agent_types/multi_agent_systems)

### Aşama 1: Tasarım ve Rol Tanımlama (Design & Persona)
- [ ] **Rol Belirleme:** Ana görevi (Coordinator) ve alt uzmanlık alanlarını (Coder, Reviewer, Researcher) tanımla.
- [ ] **İletişim Protokolü:** Ajanlar arası mesajlaşma formatını (JSON, Structured Text) ve sıra (Round-robin, Hierarchical) mantığını belirle.
- [ ] **Context Injection:** Her ajanın kendi uzmanlık alanına dair başlangıç "System Prompt"larını hazırla.

### Aşama 2: Görev Dağılımı ve Yürütme (Tasking & Execution)
- [ ] **Decomposition:** Büyük bir isteği küçük, yönetilebilir ve atomik alt görevlere (Micro-tasks) böl.
- [ ] **Parallelization:** Birbirinden bağımsız görevleri aynı anda farklı ajanlara ata.
- [ ] **Conflict Resolution:** Ajanlar arası çelişkili bilgiler oluştuğunda kimin (Boss Agent) son kararı vereceğini kurgula.

### Aşama 3: Doğrulama ve Feedback (Validation & Loop)
- [ ] **Output Verification:** Ajanlardan gelen çıktıların format (JSON Schema) ve içerik doğruluğunu kontrol et.
- [ ] **Self-Correction:** Hatalı çıktıları ilgili ajana geri göndererek (Reflection) düzeltmesini iste.
- [ ] **Final Assembly:** Tüm alt sonuçları birleştirerek tek bir tutarlı çıktı oluştur.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1     | Her ajanın sorumluluk alanı net ve çakışmıyor mu? |
| 2     | Sonsuz döngüleri (Infinite Loop) engelleyen timeout/iteration limitleri var mı? |
| 3     | Ajanlar arası bilgi aktarımı (State Sharing) doğru yapılıyor mu? |

---
*Agent Orchestration v1.2 - Evidence-Based Update*
