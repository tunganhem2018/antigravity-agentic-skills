---
name: prompt_engineering
router_kit: AIKit
description: LLM'lerden en iyi sonucu almak için ileri seviye prompt tasarım teknikleri.
metadata:
  skillport:
    category: ai
    tags: [agents, algorithms, artificial intelligence, automation, chatbots, cognitive services, deep learning, embeddings, frameworks, generative ai, inference, large language models, llm, machine learning, model fine-tuning, natural language processing, neural networks, nlp, openai, prompt engineering, rag, retrieval augmented generation, tools, vector databases, workflow automation]      - prompt-design
---

# 🧠 Prompt Engineering

> AI modelleriyle etkileşimi maksimize eden sistematik tasarım süreci.

---

*Prompt Engineering v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [Learn Prompting](https://learnprompting.org/docs/intro) & [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)

### Aşama 1: Context & Role Framing
- [ ] **Persona**: AI'a net bir uzmanlık rolü ("Sen bir senior yazılımcısın...") ata.
- [ ] **Context**: Görevi tamamlamak için gerekli tüm arka plan bilgisini sun.

### Aşama 2: Strategy selection
- [ ] **Zero-Shot**: Basit görevler için doğrudan talimat ver.
- [ ] **Few-Shot**: Karmaşık yapılar için 2-3 adet örnek (input/output) göster.
- [ ] **CoT**: AI'dan adım adım düşünmesini (Chain of Thought) iste.

### Aşama 3: Iteration & Output Control
- [ ] **Formatting**: Çıktıyı JSON, Markdown veya XML tagleri ile sınırlı tut.
- [ ] **Negative Prompts**: AI'ın ne yapmaması gerektiğini (Hata/Kısıtlama) açıkça belirt.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Prompt "belirsizlik" (ambiguity) içeriyor mu? |
| 2 | Modelin "hallucination" yapmasını engelleyecek bariyerler var mı? |
| 3 | Prompt farklı modellerde (GPT-4 vs Clause 3) tutarlı sonuç veriyor mu? |
