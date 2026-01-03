---
name: context_engineering
router_kit: AIKit
description: LLM context window yönetimi, prompt context injection ve token optimization.
metadata:
  skillport:
    category: ai
    tags: [agents, algorithms, artificial intelligence, automation, chatbots, cognitive services, context engineering, deep learning, embeddings, frameworks, generative ai, inference, large language models, llm, machine learning, model fine-tuning, natural language processing, neural networks, nlp, openai, prompt engineering, rag, retrieval augmented generation, tools, vector databases, workflow automation]      - prompt-design
---

# 🧠 Context Engineering

> LLM context yönetimi ve optimizasyonu.

---

*Context Engineering v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [Context and Token Management (OpenAI)](https://platform.openai.com/docs/guides/prompt-engineering)

### Aşama 1: Context Selection
- [ ] **Relevance**: Sadece konuyla doğrudan alakalı bilgileri seç.
- [ ] **Pruning**: Gereksiz detayları ve tekrarları temizle.

### Aşama 2: Structuring
- [ ] **Metadata**: Bilgileri yapılandırılmış formatta (JSON/Markdown) sun.
- [ ] **Priority**: En önemli bilgileri context'in başına veya sonuna koy (Lost-in-the-middle riski).

### Aşama 3: Token Optimization
- [ ] **Encoding**: Tiktoken vb. araçlarla token sayısını hesapla.
- [ ] **Summarization**: Çok uzun metinleri özetleyerek context'e dahil et.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Context penceresi (Window) aşılmadı mı? |
| 2 | Model talimatları unuttu mu? |
| 3 | Token kullanım maliyeti optimize edildi mi? |
