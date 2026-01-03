---
name: rag_architecture
router_kit: AIKit
description: Retrieval Augmented Generation (RAG) mimarisi, vector DB seçimi ve retrieval optimizasyonu.
metadata:
  skillport:
    category: ai
    tags: [ai, algorithms, artificial intelligence, automation, chatbots, cognitive services, deep learning, embeddings, frameworks, generative ai, inference, large language models, llm, machine learning, model fine-tuning, natural language processing, neural networks, nlp, openai, prompt engineering, rag, rag architecture_1, retrieval augmented generation, workflow automation]      - search-and-retrieval
---

# 🏗️ RAG Architecture

> Kurumsal verilerle LLM zenginleştirme mimarisi ve optimizasyon rehberi.

---

## 🧩 Modüler Bileşenler

### 1. Ingestion (Veri Girişi)
- **Loaders**: PDF, JSON, Notion, Database verilerinin çekilmesi.
- **Chunking**: Verinin anlamlı parçalara (Recursive, Semantic, Fixed-size) bölünmesi.

### 2. Retrieval (Veri Çekme)
- **Embeddings**: Metnin vektöre çevrilmesi (OpenAI, HuggingFace).
- **Vector DB**: Pinecone, Milvus, Weaviate veya Chroma ile indexing.
- **Search**: Similarity search (Cosine) + Metadata filtering.

### 3. Generation (Cevap Üretimi)
- **Context Injection**: Çekilen verinin prompta eklenmesi.
- **Answer Synthesis**: Modelin sadece verilen veriye sadık kalarak cevap üretmesi.

---

## 🚀 Advanced RAG Techniques

- **Hybrid Search**: Semantic search + Keyword search (BM25) birleşimi.
- **Re-ranking**: Çekilen ilk 10 dökümanın Cohere vb. ile tekrar önem sırasına dizilmesi.
- **Query Expansion**: Kullanıcı sorusunu model yardımıyla 3 farklı versiyona çevirip arama yapmak.

---

## 🔧 Workflow

> **Kaynak:** [LangChain RAG Documentation](https://python.langchain.com/docs/use_cases/question_answering/) & [Pinecone RAG Guide](https://www.pinecone.io/learn/retrieval-augmented-generation/)

### Aşama 1: Data Strategy & Indexing
- [ ] **Audit**: Kaynak veriyi temizle (Gürültülü veri, duplicate içerik).
- [ ] **Chunking Strategy**: Doküman tipine göre chunk size ve overlap oranını belirle.
- [ ] **Embedding Selection**: Veri diline ve alanına (Domain) uygun embedding modelini seç.

### Aşama 2: Retrieval Optimization
- [ ] **Index Health**: Vector DB'de doğru metrik (Cosine, L2) ve index tipini (HNSW) kullan.
- [ ] **Hybrid Pipeline**: Vektör araması yanına full-text search katmanını ekle.
- [ ] **Filtering**: Metadata üzerinden ("Sadece 2023 raporları") ön filtreleme yap.

### Aşama 3: Evaluation (RAGAS)
- [ ] **Faithfulness**: Cevap gerçekten kaynak dökümanda var mı?
- [ ] **Relevancy**: Çekilen döküman soruyla ne kadar alakalı?
- [ ] **Iteration**: Kötü sonuçlarda chunking veya embedding modelini değiştirerek döngüyü kolapat.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Halüsinasyon oranı % kaç? (Groundedness check). |
| 2 | Veri gizliliği (PII) ingestion sırasında korunuyor mu? |
| 3 | Uçtan uca (End-to-end) gecikme süresi (Latency) < 2s mi? |

---

*RAG Architecture v1.1 - Enhanced*
