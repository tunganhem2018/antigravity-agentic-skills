---
name: multi_agent_patterns
router_kit: AIKit
description: Çoklu agent sistemleri tasarımı, görev bölüşümü ve ekip işbirliği (LangGraph, CrewAI).
metadata:
  skillport:
    category: ai
    tags: [agents, algorithms, artificial intelligence, automation, chatbots, cognitive services, deep learning, embeddings, frameworks, generative ai, inference, large language models, llm, machine learning, model fine-tuning, multi agent patterns, natural language processing, neural networks, nlp, openai, prompt engineering, rag, retrieval augmented generation, tools, vector databases, workflow automation]      - swarm-ai
---

# 🤖 Multi-Agent Patterns

> Birden fazla uzman AI agent'ın işbirliği yaptığı sistemler.

---

*Multi Agent Patterns v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [LangGraph Documentation](https://python.langchain.com/docs/langgraph/) & [CrewAI Best Practices](https://docs.crewai.com/)

### Aşama 1: Role Definition (Specialists)
- [ ] **Breakdown**: Karmaşık görevi alt uzmanlık alanlarına (Örn: Researcher, Coder, Reviewer) böl.
- [ ] **Personas**: Her agent'a net bir görev (Task) ve yetki (Tools) tanımla.

### Aşama 2: Orchestration (Hierarchy vs Choreography)
- [ ] **Manager**: Bir "Yönetici Agent" üzerinden mi yoksa dairesel bir sıra (Peer-to-peer) ile mi çalışacaklarını seç.
- [ ] **State**: Agent'lar arası paylaşılan bir hafıza (Shared State) kur.

### Aşama 3: Control & Feedback
- [ ] **Cycles**: Sonsuz döngüleri engellemek için maksimum adım (Recursion limit) koy.
- [ ] **Human-in-the-loop**: Kritik kararlarda insan onayı adımı ekle.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Agent'lar birbirinin görevini gasp ediyor mu? |
| 2 | Hatalı çıktı durumunda "Self-correction" (Kendi kendini düzeltme) mekanizması var mı? |
| 3 | Token tüketimi kontrol altında mı? |
