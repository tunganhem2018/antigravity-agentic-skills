---
name: mcp_builder
router_kit: AIKit
description: Model Context Protocol (MCP) server ve client yapılandırma rehberi.
metadata:
  skillport:
    category: protocol
    tags: [agents, algorithms, artificial intelligence, automation, chatbots, cognitive services, deep learning, embeddings, frameworks, generative ai, inference, large language models, llm, machine learning, mcp builder, model fine-tuning, natural language processing, neural networks, nlp, openai, prompt engineering, rag, retrieval augmented generation, tools, vector databases, workflow automation]      - server-setup
---

# 🛠️ MCP Builder

> Model Context Protocol (MCP) server ve araç entegrasyonu.

---

*MCP Builder v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [Model Context Protocol Specification](https://modelcontextprotocol.io/)

### Aşama 1: Environment Setup
- [ ] **Install**: MCP SDK (Node.js/Python) kurulumunu yap.
- [ ] **Inspector**: MCP Inspector aracını debug için hazırla.

### Aşama 2: Capability Definition
- [ ] **Resources**: Paylaşılacak veri kaynaklarını (File, DB, API) tanımla.
- [ ] **Tools**: AI'ın çağırabileceği fonksiyonları (Action) belirle.
- [ ] **Prompts**: Hazır prompt şablonlarını sisteme ekle.

### Aşama 3: Configuration & Launch
- [ ] **Config**: `mcp-config.json` dosyasını oluştur.
- [ ] **Connection**: Stdio veya HTTP transport katmanını seç.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | `mcp-inspector` tüm tool ve resourceları görüyor mu? |
| 2 | AI "schema mismatch" hatası alıyor mu? |
| 3 | Yetkilendirme (Auth) katmanı çalışıyor mu? |
