---
name: notion_integration
router_kit: AIKit
description: Notion API integration, database management, page manipulation ve automation workflow rehberi.
metadata:
  skillport:
    category: operations
    tags: [ai, automation, best practices, cleanup, collaboration, development, documentation, integrations, maintainability, metadata, notion, notion integration, open-source, optimization, performance, productivity, project management, quality assurance, scalability, software engineering, standards, testing, version control, web development, workflow]      - business-automation
---

# 📓 Notion Integration

> Notion API ile otomasyon, dökümantasyon ve database yönetimi.

---

## 🚀 Setup & Auth

### Integration Secret
- [Notion Developers](https://www.notion.so/my-integrations) panelinden yeni bir integration oluştur.
- `Internal Integration Token` al.
- Hedeflenen page veya database'e integration'ı "Connect To" ile ekle.

### SDK Installation
```bash
npm install @notionhq/client
```

---

## 🔧 Database Operations

### Query Database
```javascript
const response = await notion.databases.query({
  database_id: "YOUR_DATABASE_ID",
  filter: {
    property: "Status",
    status: { equals: "Done" },
  },
});
```

### Create Page (Insert Row)
```javascript
await notion.pages.create({
  parent: { database_id: "..." },
  properties: {
    Name: { title: [{ text: { content: "New Task" } }] },
    Tags: { multi_select: [{ name: "Automated" }] },
  },
});
```

---

## 🧱 Block Manipulation

Notion dökümanları block'lardan oluşur:
- **Heading**: `heading_1`, `heading_2`...
- **Text**: `paragraph`
- **Lists**: `bulleted_list_item`, `numbered_list_item`
- **Images**: `image` (external url veya file).

---

*Notion Integration v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [Notion API Reference](https://developers.notion.com/reference) & [Notion Developers Guide](https://developers.notion.com/docs/getting-started)

### Aşama 1: Connection & Permissions
- [ ] **Integration**: `Internal Integration Token` oluştur ve sadece gerekli sayfaları ("Share" menüsü üzerinden) bağla.
- [ ] **Capabilities**: Integration'ın sadece okuma (Read) mı yoksa yazma (Write) yetkisi mi olacağını panelden belirle.
- [ ] **ID Mapping**: Database veya Page ID'lerini (URL'den 32 karakterlik ID) belirle.

### Aşama 2: API Interaction (SDK)
- [ ] **Client Setup**: `@notionhq/client` ile bağlantıyı kur.
- [ ] **Schema Mapping**: Notion'daki Property tiplerini (Select, Relation, Formula) koda map et.
- [ ] **Block Structure**: İçerik eklerken Notion'ın karmaşık JSON block yapısını (Rich text array'leri dahil) oluştur.

### Aşama 3: Automation & Logic
- [ ] **Webhooks?**: Notion henüz native webhook desteklemediği için `Poll` mekanizması veya "Notion-Automate" gibi araçlar kullan.
- [ ] **Sync**: Notion verisi ile harici DB arasındaki senkronizasyon (Upsert) logic'ini kur.
- [ ] **Error Handling**: Rate limit (3 requests/sec) hatalarını yönetmek için retry mekanizması ekle.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Integration Token `GIT_IGNORE` içinde mi? (Asla hardcode etme). |
| 2 | Database şeması değiştiğinde kod kırılıyor mu? (Schema check ekle). |
| 3 | Rich text limitleri (2000 chars per block) kontrol ediliyor mu? |
