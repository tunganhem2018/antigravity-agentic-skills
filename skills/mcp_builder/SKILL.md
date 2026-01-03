---
name: mcp_builder
router_kit: ManagementKit
description: Model Context Protocol (MCP) server inşa etme, resource ve tool tanımlama rehberi.
metadata:
  skillport:
    category: operations
    tags: [api integration, automation, backend, best practices, development, frameworks, javascript, mcp builder, mcp server, model context protocol, node.js, npm, optimization, software engineering, standards, typescript, utilities, workflow]      - mcp-server-developer
---

# 🛠️ MCP Builder

> Model Context Protocol (MCP) server oluşturma ve araç (tool) geliştirme.

---

## 🏗️ MCP Core Concepts

- **Resources**: LLM'in okuyabileceği statik veriler (örn: dosyalar, DB kayıtları).
- **Tools**: LLM'in çalıştırabileceği aksiyonlar (örn: API call, dosya yazma).
- **Prompts**: LLM'e sunulan özel talimat şablonları.

---

## 🚀 Creating a Tool

```typescript
server.tool(
  "calculate_sum",
  "Calculates the sum of two numbers",
  {
    a: z.number(),
    b: z.number()
  },
  async ({ a, b }) => {
    return {
      content: [{ type: "text", text: (a + b).toString() }]
    };
  }
);
```

---

## 📦 Implementation Details

| Adım | İşlem |
|------|-------|
| **Setup** | `npx @modelcontextprotocol/create-server` |
| **Define** | Resource ve tool'ları tanımla. |
| **Logic** | Tool içerisindeki iş mantığını (Business logic) yaz. |
| **Build** | `npm run build` ile derle. |
| **Config** | Claude / IDE config dosyasına server'ı ekle. |

---

*MCP Builder v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [Model Context Protocol (MCP) Documentation](https://modelcontextprotocol.io/)

### Aşama 1: Scope & Definition
- [ ] **Identify**: LLM'in hangi yeteneğe/veriye ihtiyacı var? (Dosya okuma? API erişimi?).
- [ ] **Capabilities**: Resource mu (Read-only) yoksa Tool mu (Action) olacağına karar ver.
- [ ] **Schema**: Girdi parametrelerini `zod` ile sıkı şekilde tanımla.

### Aşama 2: Development & Testing
- [ ] **Server Setup**: `StdioServerTransport` veya `HttpServerTransport` seç.
- [ ] **Error Handling**: Beklenmedik durumlarda LLM'e anlamlı hata mesajları dön.
- [ ] **Inspector**: `mcp-inspector` kullanarak server'ı LLM dışında test et.

### Aşama 3: Deployment & Config
- [ ] **Binary**: Server'ı global bir paket veya executable haline getir.
- [ ] **Integration**: `claude_desktop_config.json` içine server yolunu ve environment variable'ları ekle.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Tool açıklamaları (description) LLM için yeterince açıklayıcı mı? |
| 2 | Hassas veriler (API Key) loglara sızıyor mu? |
| 3 | Tool, uzun süren işlemlerde timeout'a düşüyor mu? |
