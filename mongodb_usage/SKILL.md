---
name: mongodb_usage
router_kit: FullStackKit
description: MongoDB data modeling, aggregation framework, query optimization ve indexing rehberi.
metadata:
  skillport:
    category: database
    tags: [aggregation framework, architecture, automation, backend, best practices, database, database design, design patterns, development, efficiency, indexing, mongodb, nosql, optimization, performance, scalability, schema design, software engineering, testing, workflow]      - nosql
---

# 🍃 MongoDB Usage & Optimization

> MongoDB veri modelleme, aggregation ve performans rehberi.

---

## 📋 İçindekiler

1. [Schema Design (Data Modeling)](#1-schema-design-data-modeling)
2. [Indexing Stratejileri](#2-indexing-stratejileri)
3. [Aggregation Framework](#3-aggregation-framework)
4. [Performance Optimization](#4-performance-optimization)
5. [Common Operations](#5-common-operations)

---

## 1. Schema Design (Data Modeling)

### Embedding vs. Referencing
| Yaklaşım | Ne Zaman Kullanılır? | Avantajı |
|----------|----------------------|----------|
| **Embedding** | 1:1 veya 1:Few (Sınırlı) | Tek sorgu ile veri çekme (Speed) |
| **Referencing** | 1:Many (Büyük) veya Many:Many | Data duplication önleme, flexibility |

### Best Practices
- **Max Document Size**: 16MB limitine dikkat et.
- **Data Growth**: Array'lerin kontrolsüz büyümesinden (Unbounded arrays) kaçın.
- **Atomicity**: Tek doküman seviyesindeki işlemleri tercih et.

---

## 2. Indexing Stratejileri

### Temel Index'ler
```javascript
// Single Field Index
db.users.createIndex({ email: 1 });

// Compound Index (Order matters!)
db.orders.createIndex({ status: 1, createdAt: -1 });

// Multi-key Index (Array field)
db.products.createIndex({ tags: 1 });
```

### Advanced Index'ler
- **TTL Index**: Otomatik silinen dökümanlar (Loglar, sessionlar).
- **Text Index**: Basit search işlemleri için.
- **Partial Index**: Sadece belirli şartı sağlayan dökümanları indexle (Storage saving).

---

## 3. Aggregation Framework

### Örnek Pipeline
```javascript
db.orders.aggregate([
  { $match: { status: "completed" } },
  { $group: { 
      _id: "$userId", 
      totalSpent: { $sum: "$amount" },
      orderCount: { $count: {} }
    } 
  },
  { $sort: { totalSpent: -1 } },
  { $limit: 10 }
]);
```

### Stage'ler
- `$match`: Filtreleme (Mutlaka pipeline başında olmalı!).
- `$lookup`: Join işlemi.
- `$unwind`: Array parçalama.
- `$facet`: Aynı veri üzerinde paralel analiz.

---

## 4. Performance Optimization

### Query Profiling
```javascript
// Explain plan
db.collection.find({ query }).explain("executionStats");

// Slow query logging
db.setProfilingLevel(1, { slowms: 100 });
```

### Yazma / Okuma Stratejileri
- **Write Concern**: Verinin kaç node'a yazılacağı (Ack/Majority).
- **Read Preference**: Verinin hangi node'dan okunacağı (Primary/Secondary).
- **Bulk Operations**: Toplu yazma işlemleri (`bulkWrite`).

---

## 5. Common Operations

### Mongoose Snippets (Node.js)
```javascript
// Middleware (Pre-save)
userSchema.pre('save', async function(next) {
  if (this.isModified('password')) {
    this.password = await bcrypt.hash(this.password, 10);
  }
  next();
});

// Virtuals (Populate)
orderSchema.virtual('user', {
  ref: 'User',
  localField: 'userId',
  foreignField: '_id',
  justOne: true
});
```

---

*MongoDB Usage v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [MongoDB University](https://university.mongodb.com/) & [Data Modeling Introduction](https://www.mongodb.com/docs/manual/core/data-modeling-introduction/)

### Aşama 1: Schema Design & Modeling
- [ ] **Access Patterns**: Veriyi nasıl okuyacağını (Query patterns) listele. Tasarımı okuma hızına göre yap.
- [ ] **Model Selection**: Embedding (Hız) ile Referencing (Esneklik) arasındaki dengeyi kur.
- [ ] **Consistency**: Uygulama seviyesinde schema validation (Mongoose veya JSON Schema) kullan.

### Aşama 2: Query & Indexing
- [ ] **Index Coverage**: Sık kullanılan sorgu alanlarını (Sorgu sırasına göre) Compound Index ile kapsa.
- [ ] **Explain Analysis**: Ağır sorgularda `explain()` kullanarak "COLLSCAN" (Tüm koleksiyonu tarama) olup olmadığını kontrol et.
- [ ] **ESR Rule**: Index oluştururken Equality -> Sort -> Range kuralına uy.

### Aşama 3: Scaling & Monitoring
- [ ] **Write Concern**: Kritik veriler için `w: "majority"` ayarını kontrol et.
- [ ] **Connection Pooling**: Driver seviyesinde maxPoolSize ayarını optimize et.
- [ ] **Monitoring**: Atlas kullanıyorsan "Performance Advisor" önerilerini incele.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Unbounded array riski (Döküman büyümesi) var mı? |
| 2 | Her sorgu bir index kullanıyor mu? |
| 3 | Join ($lookup) işlemleri performansı nasıl etkiliyor? |
