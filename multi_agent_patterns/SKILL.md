---
name: multi_agent_patterns
router_kit: AIKit
description: Multi-agent orchestration, communication protocols ve task decomposition stratejileri.
metadata:
  skillport:
    category: ai
    tags: [agents, algorithms, artificial intelligence, automation, chatbots, cognitive services, deep learning, embeddings, frameworks, generative ai, inference, large language models, llm, machine learning, model fine-tuning, multi-agent patterns, natural language processing, neural networks, nlp, openai, prompt engineering, rag, retrieval augmented generation, workflow automation]      - agents
---

# 🤖 Multi-Agent Patterns

> Çoklu agent sistemleri, orkestrasyon ve iletişim protokolleri.

---

## 📋 Mimari Pattern'ler

### 1. Sequential (Sıralı)
Agent'lar işi bir zincir halinde birbirine aktarır.
- **Örnek**: Writer -> Editor -> Publisher.
- **Kullanım**: Belirli bir iş akışının katı adımlarla izlenmesi gerektiğinde.

### 2. Hierarchical (Hiyerarşik)
Bir "Manager Agent" (Orchestrator) işleri parçalar ve "Worker Agent"lara dağıtır.
- **Örnek**: Manager -> [Researcher, Coder, Reviewer].
- **Kullanım**: Karmaşık işlerin dinamik olarak planlanması gerektiğinde.

### 3. Joint (Ortaklaşa) - Blackboard
Tüm agent'lar merkezi bir "Blackboard" (Memory/State) üzerine yazarak işbirliği yapar.
- **Örnek**: Tartışma paneli veya karmaşık problem çözme.
- **Kullanım**: Adımların önceden kestirilemediği durumlarda.

---

## 🔧 İletişim Stratejileri

### Task Decomposition
Agent'lar karmaşık hedefleri daha küçük, yönetilebilir sub-task'lara böler.
- **Direct Loop**: Hedef -> Plan -> Execute -> Evaluate.

### Conflict Resolution
Agent'lar arası çelişen sonuçları çözme.
- **Voting**: Çoğunluk kararı.
- **Criticism Loop**: Bir agent'ın çıktısını diğerinin eleştirmesi ve düzeltmesi.

---

## 🛠️ Framework Entegrasyonları

### LangChain (LangGraph)
```python
# State definition
class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], operator.add]

# Graph definition
workflow = StateGraph(AgentState)
workflow.add_node("agent", call_model)
workflow.add_node("action", call_tool)
```

### CrewAI
```python
crew = Crew(
  agents=[researcher, writer],
  tasks=[task1, task2],
  process=Process.sequential # or Process.hierarchical
)
```

---

*Multi-Agent Patterns v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [AutoGPT Multi-Agent Systems](https://github.com/Significant-Gravitas/AutoGPT) & [OpenAI Assistants API](https://platform.openai.com/docs/assistants/overview)

### Aşama 1: Role Definition & Scope
- [ ] **Specialization**: Agent'ları genelci değil, uzman (Örn: Sadece Security Auditor) olarak tanımlama.
- [ ] **System Prompts**: Her agent'ın sınırlarını (Boundaries) ve yetkilerini (Tools) netleştir.
- [ ] **State Schema**: Agent'lar arası paylaşılan veri şemasını (Shared context) belirle.

### Aşama 2: Orchestration Design
- [ ] **Decomposition**: Büyük görevi agent'ların yapabileceği seviyeye parçala (Sub-tasking).
- [ ] **Communication**: `Sequential`, `Circular` veya `Manager-led` akışlardan birini seç.
- [ ] **Feedback Loop**: Agent'ların birbirini denetlediği (Audit) mekanizmayı tasarla.

### Aşama 3: Guardrails & Stability
- [ ] **Max Loops**: Sonsuz döngüleri (Infinite loops) engellemek için `max_iterations` sınırı koy.
- [ ] **Hallucination Check**: Çıktıları doğrulamak için bir "Verifier" agent veya dış araç (RAG) kullan.
- [ ] **Reliability**: Fail her agent için `retry` ve `fallback` stratejilerini uygula.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Agent'lar arası redundant (gereksiz) iletişim var mı? |
| 2 | Manager Agent, Worker'lardan gelen hataları yakalayabiliyor mu? |
| 3 | Shared memory (context) token limitini aşıyor mu? |
