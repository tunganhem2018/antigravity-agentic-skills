---
name: mcp_server_developer
router_kit: AIKit
description: TypeScript/Python ile yüksek performanslı MCP server geliştirme.
metadata:
  skillport:
    category: development
    tags: [agents, algorithms, artificial intelligence, automation, chatbots, cognitive services, deep learning, embeddings, frameworks, generative ai, inference, large language models, llm, machine learning, mcp server developer, model fine-tuning, natural language processing, neural networks, nlp, openai, prompt engineering, rag, retrieval augmented generation, tools, vector databases, workflow automation]      - backend
---

# 💻 MCP Server Developer

> Özel Model Context Protocol (MCP) sunucuları geliştirme.

---

*MCP Server Developer v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [MCP SDK Reference (Node.js)](https://github.com/modelcontextprotocol/typescript-sdk)

### Aşama 1: Service Design (Interface)
- [ ] **API Design**: Paylaşılacak tool'ların parametrelerini (Zod schema) tanımla.
- [ ] **State**: Server'ın durumlu mu (Stateful) yoksa durumsuz mu (Stateless) olacağına karar ver.

### Aşama 2: Implementation (Coding)
- [ ] **Handler**: Tool çağrılarını işleyecek mantığı (Business logic) yaz.
- [ ] **Security**: Local dosya erişimi vb. için "Sandboxing" önlemlerini al.
- [ ] **Metadata**: Tool açıklamalarını AI'ın anlayacağı kadar detaylı yaz.

### Aşama 3: Testing & Deployment
- [ ] **Unit Tests**: Her tool fonksiyonunu bağımsız test et.
- [ ] **Deploy**: `npm link` veya Docker ile imajı dağıt.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Response süresi 2 saniyenin altında mı? |
| 2 | AI yanlış parametre gönderince hata yönetimi (Validation) çalışıyor mu? |
| 3 | Loglama ve İzlenebilirlik (Tracing) aktif mi? |
