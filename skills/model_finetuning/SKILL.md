---
name: model_finetuning
router_kit: AIKit
description: LLM fine-tuning techniques (LoRA, QLoRA), dataset preparation ve alignment strategies (DPO, RLHF).
metadata:
  skillport:
    category: ai
    tags: [alignment, artificial intelligence, automation, dataset preparation, deep learning, dpo, fine-tuning, generative ai, huggingface, large language models, llm, lora, machine learning, model finetuning, natural language processing, neural networks, nlp, optimization, performance, prompt engineering, qlora, rlhf, sft, training, workflow]      - huggingface-transformers
---

# 🧠 Model Fine-Tuning

> Büyük dil modellerine (LLM) yeni bilgiler öğretme veya davranışlarını özelleştirme.

---

## 🚀 Fine-Tuning Stages

1. **SFT (Supervised Fine-Tuning)**: Modelin "Soru-Cevap" veya "Talimat" formatını öğrenmesi.
2. **Alignment (Hizalama)**: Modelin insan tercihlerine göre eğitilmesi.
   - **DPO (Direct Preference Optimization)**: Basit ve verimli tercih optimizasyonu (Önerilen).
   - **RLHF (Reinforcement Learning from Human Feedback)**: Karmaşık ödül mekanizmaları.

---

## 🛠️ Parameter Efficient Fine-Tuning (PEFT)

Tüm modeli eğitmek yerine sadece küçük bir kısmını eğiterek kaynak tasarrufu sağlayan yöntemler.

| Teknik | Açıklama |
|--------|----------|
| **LoRA** | Ağırlık matrislerine düşük rütbeli (Low-Rank) katmanlar ekler. |
| **QLoRA** | LoRA'yı 4-bit quantization ile birleştirir (Minimum RAM). |

---

## 📊 Dataset Preparation

Veri seti kalitesi, veri miktarından daha önemlidir.
- **Format**: `{"instruction": "...", "input": "...", "output": "..."}`
- **Diversity**: Farklı senaryoları kapsayan çeşitlilik.
- **Cleaning**: Hatalı, tekrarlı ve düşük kaliteli verilerin temizlenmesi.

---

*Model Finetuning v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [HuggingFace TRL Docs](https://huggingface.co/docs/trl/index) & [DeepLearning.ai LLM Engineering](https://www.deeplearning.ai/)

### Aşama 1: Preparation (Data-Centric AI)
- [ ] **Data Cleaning**: Veri setini deduplicate et ve kalite kontrolü yap (PII temizliği).
- [ ] **Format**: Dataset'i modele uygun formata (ShareGPT, Alpaca vb.) dönüştür.
- [ ] **Baseline**: Base modelin performansını (Zero-shot) ölç ve kaydet.

### Aşama 2: Training (Parameter Efficient)
- [ ] **LoRA/QLoRA**: Full fine-tuning yerine LoRA (Rank 16-64) kullan (Daha az VRAM, %95+ performans).
- [ ] **Monitoring**: WandB veya MLflow ile Loss eğrilerini ve eval metriklerini canlı izle.
- [ ] **Checkpointing**: Her epoch veya belirli stepte model ağırlıklarını kaydet.

### Aşama 3: Alignment & Evaluation
- [ ] **Alignment**: SFT sonrası gerekiyorsa DPO veya PPO ile insan tercihlerine hizala.
- [ ] **Evaluation**: `llm_evaluation` skill'ini kullanarak otomatik ve manuel testler yap.
- [ ] **Merging**: LoRA adaptörlerini base modele merge et ve quantize (GGUF/AWQ) yap.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Training Loss düşerken Validation Loss artıyor mu (Overfitting)? |
| 2 | Model "Catastrophic Forgetting" yaşıyor mu (Eski yeteneklerini kaybetti mi)? |
| 3 | Inference hızı ve belleği (VRAM) deployment ortamına uygun mu? |
