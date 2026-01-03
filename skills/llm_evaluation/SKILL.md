---
name: llm_evaluation
router_kit: AIKit
description: LLM çıktı kalitesini ölçme, benchmarking, RAG evaluation ve model karşılaştırma teknikleri.
metadata:
  skillport:
    category: ai
    tags: [ai metrics, ai monitoring, benchmarks, bias detection, bleue, evaluation, hallucination, llm evaluation, model alignment, model performance, nlp evaluation, quality assurance, rag evaluation, reliability, rouge, safety, testing, validation]      - prompt-engineering
---

# 📊 LLM Evaluation

> LLM çıktılarının kalitesini, doğruluğunu ve güvenilirliğini ölçme.

---

## 📏 Evaluation Metrics

### 1. NLP Metrics (Automated)
- **ROUGE/BLEU**: Metin benzerliği (Özetleme/Çeviri için).
- **Exact Match (EM)**: Soru-cevap testlerinde doğrudan eşleşme.

### 2. Model-based Metrics
- **LLM-as-a-Judge**: Güçlü bir modeli (GPT-4), diğer modelin çıktısını 1-10 arası puanlamak için kullanma.
- **RAGAS**: RAG sistemleri için (faithfulness, answer relevance).

### 3. Human Evaluation
- **Elo Rating**: İki modelin çıktısını körleme test (Blind test) ile karşılaştırma.

---

## 🏗️ Evaluation Categories

| Kategori | Ne Ölçülür? |
|----------|-------------|
| **Accuracy** | Üretilen bilgi doğru mu? |
| **Hallucination** | Model uyduruyor mu? |
| **Safety/Bias** | Zararlı veya yanlı içerik var mı? |
| **Format** | Çıktı istenen formatta (JSON/XML) mı? |
| **Latency** | Yanıt hızı üretim için uygun mu? |

---

*LLM Evaluation v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [Ragas Documentation](https://docs.ragas.io/en/stable/) & [OpenAI Evals](https://github.com/openai/evals)

### Aşama 1: Benchmark Dataset (Gold Set)
- [ ] **Samples**: El ile doğrulanmış 50-100 adetlik "soru-cevap" veri seti oluştur.
- [ ] **Edge Cases**: Modelin zorlanabileceği "trick questions" veya boş yanıt gerektiren durumları ekle.

### Aşama 2: RAG Evaluation
- [ ] **Faithfulness**: Yanıt, sağlanan context'e dayanıyor mu?
- [ ] **Answer Relevance**: Yanıt soruyla ne kadar alakalı?
- [ ] **Context Precision**: Sağlanan context içinde doğru bilgi ne kadar yukarda?

### Aşama 3: Automated Pipeline
- [ ] **CI/CD Integration**: Her prompt değişikliğinde eval setini otomatik çalıştır.
- [ ] **Thresholds**: Metrikler belirlenen sınırın altına düşerse (örn: Accuracy < %80) uyarı ver.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Puanlayan model (Judge) ile test edilen model aynı mı? (Yapılmamalı!) |
| 2 | Eval seti gerçek kullanıcı verilerini temsil ediyor mu? |
| 3 | Halüsinasyon oranı kritik seviyenin altında mı? |
