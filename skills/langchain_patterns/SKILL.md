---
name: langchain_patterns
router_kit: AIKit
description: LangChain framework usage, chains, memory, agents ve vector store integration patterns.
metadata:
  skillport:
    category: ai
    tags: [agents, algorithms, artificial intelligence, automation, chatbots, cognitive services, deep learning, embeddings, frameworks, generative ai, inference, langchain patterns, large language models, llm, machine learning, model fine-tuning, natural language processing, neural networks, nlp, openai, prompt engineering, rag, retrieval augmented generation, tools, vector databases, workflow automation]      - prompt-engineering
---

# 🦜 LangChain Patterns

> LangChain ile LLM uygulama geliştirme ve tasarım kalıpları.

---

## 🏗️ Core components

### 1. LLMChain (Basic)
Prompt, Model ve Output Parser birleşimi.

```python
from langchain.chains import LLMChain
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate

template = "Tell me a joke about {topic}."
prompt = PromptTemplate.from_template(template)
chain = LLMChain(llm=OpenAI(), prompt=prompt)
```

### 2. LCEL (LangChain Expression Language)
Yeni ve önerilen zincirleme (piping) yöntemi.

```python
chain = prompt | model | parser
response = chain.invoke({"topic": "bears"})
```

---

## 💾 Memory Patterns

| Tip | Kullanım |
|-----|----------|
| **Buffer** | Tüm konuşma geçmişini tutar. |
| **Summary** | Konuşmayı özetleyerek tutar (token tasarrufu). |
| **Window** | Sadece son K mesajı tutar. |
| **VectorStore** | Benzerlik araması ile geçmişten ilgili parçayı çeker. |

---

## 🤖 Agents & Tools

LLM'in dış araçları (Arama, DB, Hesap makinesi) kullanmasını sağlar.

```python
from langchain.agents import initialize_agent, Tool
agent = initialize_agent(tools, llm, agent="zero-shot-react-description")
```

---

*LangChain Patterns v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [LangChain Documentation](https://python.langchain.com/docs/get_started/introduction) & [DeepLearning.ai LangChain Course](https://www.deeplearning.ai/short-courses/langchain-for-llm-application-development/)

### Aşama 1: Architecture selection
- [ ] **Method**: Basit bir akış mı (Chain) yoksa dinamik karar veren bir yapı mı (Agent) gerekiyor?
- [ ] **Memory**: Konuşma geçmişi ne kadar kritik? (Token maliyetini düşün).
- [ ] **Output**: Modelden "JSON" mı "Text" mi bekliyorsun? (PydanticOutputParser kullan).

### Aşama 2: RAG Pipeline (Data Integration)
- [ ] **Ingestion**: Verileri chunklara böl (RecursiveCharacterTextSplitter) ve embedding oluştur.
- [ ] **VectorDB**: Pinecone/Chroma/FAISS seçimini yap.
- [ ] **Retrieval**: `multi_query` veya `parent_document` gibi gelişmiş retrieval tekniklerini kullan.

### Aşama 3: Tracing & Monitoring
- [ ] **LangSmith**: Zincirin her adımını izlemek (Debug) için LangSmith entegrasyonu yap.
- [ ] **Evaluation**: Çıktı kalitesini `QAEvalChain` ile doğrula.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Zincirdeki bir adım hata aldığında sistem nasıl tepki veriyor (Error handling)? |
| 2 | Token kullanımı limitler dahilinde mi? |
| 3 | Agent sonsuz döngüye (Infinite Loop) girerse durdurma mekanizması var mı? |
