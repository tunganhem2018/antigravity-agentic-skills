---
name: prompt_engineering
router_kit: AIKit
description: LLM prompt tasarımı, Few-shot learning, Chain-of-Thought ve sistematik iterasyon rehberi.
metadata:
  skillport:
    category: artificial intelligence
    tags: [ai, algorithms, artificial intelligence, automation, chatbots, cognitive services, deep learning, embeddings, frameworks, generative ai, inference, large language models, llm, machine learning, model fine-tuning, natural language processing, neural networks, nlp, openai, prompt engineering, prompt engineering_1, rag, retrieval augmented generation, workflow automation]      - prompt-design
---

# 🧠 Prompt Engineering

> LLM modellerinden maksimum verim alma ve sistematik prompt tasarımı.

---

## 🏗️ Prompt Yapısı (Components)

### 1. Persona (Role)
Modelin hangi kimlikle konuşacağını belirle.
- **Örnek**: "Kıdemli bir React mühendisi gibi davran."

### 2. Context (Bağlam)
İş için gerekli arka plan bilgisi.
- **Örnek**: "Bu kod bir e-ticaret sitesinin sepet sayfasında çalışacak."

### 3. Task (Görev)
Net ve eylem odaklı komut.
- **Örnek**: "Aşağıdaki fonksiyonu TypeScript ile refactor et."

### 4. Constraints (Kısıtlar)
Yapılmaması gerekenler veya format zorunlulukları.
- **Örnek**: "Dış kütüphane kullanma, çıktı sadece JSON olsun."

---

## 🧪 Advanced Techniques

- **Few-Shot**: Modele 3-5 tane örnek (Input/Output çifti) ver.
- **Chain-of-Thought (CoT)**: "Adım adım düşün" diyerek modelin mantık yürütmesini sağla.
- **Delimiters**: Bölümleri ayırmak için `###`, `---` veya XML tag'leri (`<context>`, `<code>`) kullan.

---

## 🔧 Workflow

> **Kaynak:** [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering) & [Learn Prompting](https://learnprompting.org/)

### Aşama 1: Design & Drafting
- [ ] **Goal**: Promptun amacını tek cümlede tanımla.
- [ ] **Structure**: Persona, Context, Task ve Output formatını içeren bir taslak oluştur.
- [ ] **Clear Language**: Belirsiz kelimeler (Biraz, akıllıca vb.) yerine spesifik ölçütler (En fazla 100 kelime, p99 odaklı vb.) kullan.

### Aşama 2: Testing & Iteration
- [ ] **Zero-Shot**: Önce hiçbir örnek vermeden dene.
- [ ] **Iterate**: Aldığın cevaba göre prompta negatif kısıtlar ("Şunu yapma") veya ek bağlam ekle.
- [ ] **Variables**: Promptu dinamik hale getir (`{{USER_INPUT}}` gibi).

### Aşama 3: Evaluation & Refinement
- [ ] **Testing Set**: Aynı promptu 5-10 farklı girdi ile test ederek tutarlılığını (Consistency) ölç.
- [ ] **Failure Analysis**: Modelin nerede ve neden yanıldığını analiz et (Bias, hallucinations).
- [ ] **Refinement**: Modeli daha iyi yönlendirmek için "Self-Refinement" tekniğini (Modele kendi hatasını buldurup düzelttirme) prompta ekle.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Prompt "Token limit" içinde mi? |
| 2 | Çıktı formatı (JSON/Markdown) her seferinde aynı mı? |
| 3 | Model üzerinde "Prompt Injection" denemesi yapıldı mı? |

---

*Prompt Engineering v1.1 - Enhanced*
