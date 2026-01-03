---
name: agent_orchestration
router_kit: AIKit
description: Transform clarified user requests into structured delegation prompts optimized for specialist agents (cto-architect, strategic-cto-mentor, cv-ml-architect). Use after clarification is complete, before routing to specialist agents. Ensures agents receive complete context for effective work.
metadata:
  skillport:
    category: auto-healed
    tags: [agent orchestration, agents, algorithms, artificial intelligence, automation, chatbots, cognitive services, deep learning, embeddings, frameworks, generative ai, inference, large language models, llm, machine learning, model fine-tuning, natural language processing, neural networks, nlp, openai, prompt engineering, rag, retrieval augmented generation, tools, vector databases, workflow automation]      - agent_orchestration
---

# Delegation Prompt Crafter

Creates structured, context-rich prompts for specialist agents that maximize their effectiveness and minimize back-and-forth.

## 🔄 Workflow

> **Kaynak:** [Multi-Agent Patterns (Microsoft)](https://microsoft.github.io/multi-agent-reference-architecture/docs/reference-architecture/Patterns.html)

### Aşama 1: Orchestration Design
- [ ] **Select Pattern**: Choose architecture (Hierarchical, Joint-Chat, Dynamic).
- [ ] **Define Roles**: Map required skills to distinct agent personas.
- [ ] **Boundary Check**: Ensure no overlap in agent responsibilities.

### Aşama 2: Prompt Engineering (Delegation)
- [ ] **Context Injection**: Prepare global context (Project, Constraints).
- [ ] **Task Definition**: Draft clear "Primary Deliverable" for each agent.
- [ ] **Guardrails**: Define "Out of scope" explicit boundaries.

### Aşama 3: Routing Logic
- [ ] **Router Config**: Define intent classification rules (Semantic/Keyword).
- [ ] **Handoff Protocol**: Define how Agent A transfers context to Agent B.
- [ ] **Fallback**: Define behavior when no agent matches intent.

### Aşama 4: Validation & Simulation
- [ ] **Dry Run**: Simulate conversation flow manually.
- [ ] **Loop Detection**: Verify agents don't get stuck in "Asking clarification" loops.
- [ ] **Token Audit**: Check context window usage per step.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Mimari diyagramı net, roller ayrışık |
| 2 | Prompt'lar "Delegation Structure" formatında |
| 3 | Router doğru ajana yönlendiriyor (>90% accuracy) |
| 4 | Sonsuz döngü veya bağlam kaybı yok |
