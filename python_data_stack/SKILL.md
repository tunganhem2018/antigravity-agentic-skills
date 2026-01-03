---
name: python_data_stack
router_kit: AIKit
description: Veri analizi ve bilimi için Python araçları - Pandas, NumPy, Scikit-learn ve Matplotlib.
metadata:
  skillport:
    category: science
    tags: [algorithms, artificial intelligence, automation, backend, big data, cleanup, data analysis, data science, data visualization, deep learning, development, efficiency, machine learning, matplotlib, numpy, optimization, pandas, performance, python, python data stack_1, quality assurance, scikit-learn, software engineering, statistics, testing, workflow]      - data-science
---

# 📊 Python Data Stack

> Veri analizi, işleme ve görselleştirme için Python ekosistemi rehberi.

---

## 🛠️ Core Libraries

### NumPy (Numerical Python)
Çok boyutlu diziler ve matematiksel işlemler.
```python
import numpy as np
arr = np.array([1, 2, 3])
mean = np.mean(arr)
```

### Pandas (Data Analysis)
Tabular veri yönetimi ve manipülasyonu (DataFrame).
```python
import pandas as pd
df = pd.read_csv('data.csv')
df.groupby('category').sum()
```

### Matplotlib / Seaborn (Visualization)
Veri görselleştirme ve grafikler.
```python
import matplotlib.pyplot as plt
plt.plot(df['date'], df['sales'])
plt.show()
```

---

## 🧪 Machine Learning (Scikit-learn)

```python
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Training pattern
X_train, X_test, y_train, y_test = train_test_split(X, y)
model = RandomForestClassifier().fit(X_train, y_train)
accuracy = model.score(X_test, y_test)
```

---

## 🔧 Workflow

> **Kaynak:** [Pandas Documentation](https://pandas.pydata.org/docs/) & [Scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)

### Aşama 1: Data Ingestion & Cleaning
- [ ] **Loading**: CSV, JSON, SQL veya Parquet formatından veriyi verimli (Chunking) yükle.
- [ ] **Cleaning**: Kayıp verileri (NaN/Null) temizle veya doldur (Imputation).
- [ ] **Discovery**: `df.describe()` ve `df.info()` ile verinin istatistiksel özetini çıkar.

### Aşama 2: Transformation & EDA
- [ ] **Manipulation**: `merge`, `join` ve `group_by` işlemleriyle veriyi analiz için hazırla.
- [ ] **Feature Engineering**: Veriden yeni anlamlı kolonlar (Features) türet.
- [ ] **EDA**: Görselleştirme araçlarıyla (Histogram, Heatmap) verideki pattern'leri ve outlier'ları bul.

### Aşama 3: Model & Report
- [ ] **Preprocessing**: Veriyi ölçeklendir (Scaling) ve kategorik verileri (Encoding) çevir.
- [ ] **Training**: Uygun algoritmayı seç, eğit ve çapraz doğrulama (Cross-validation) ile test et.
- [ ] **Reporting**: Sonuçları `Jupyter Notebook` veya `Streamlit` ile interaktif bir rapora dönüştür.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Veri setinde dengesizlik (Class imbalance) var mı? |
| 2 | Modelde "Overfitting" (Ezberleme) belirtisi var mı? |
| 3 | Büyük veri setlerinde bellek kullanımı (Memory usage) kontrol edildi mi? |

---

*Python Data Stack v1.1 - Enhanced*
