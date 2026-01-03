---
name: python_pro
router_kit: AIKit
description: Advanced Python - async/await, decorators, generators, type hinting ve packaging.
metadata:
  skillport:
    category: engineering
    tags: [algorithms, asynchronous programming, automation, backend, best practices, cleanup, coaching, concurrency, decorators, development, documentation, efficiency, functional programming, generators, maintainability, metaprogramming, optimization, parallelism, performance, python, python pro_1, quality assurance, scalability, software engineering, standards, testing, type hinting, version control, workflow]      - dynamic-languages
---

# 🐍 Python Pro (Advanced)

> Modern Python pratikleri, performans ve tip güvenliği rehberi.

---

## 🚀 Modern Syntax & Type Safety

### Type Hinting (Pydantic)
```python
from typing import List, Optional
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str
    tags: List[str] = []
    bio: Optional[str] = None
```

### Async/Await
```python
import asyncio
import httpx

async def fetch_data(url: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()

# Parallel execution
results = await asyncio.gather(*(fetch_data(u) for u in urls))
```

---

## 🛠️ Design Patterns

### Decorators
```python
def log_execution(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        print(f"Executing {func.__name__}")
        return await func(*args, **kwargs)
    return wrapper
```

### Context Managers
```python
from contextlib import asynccontextmanager

@asynccontextmanager
async def database_session():
    db = await connect()
    try:
        yield db
    finally:
        await db.close()
```

---

## 🔧 Workflow

> **Kaynak:** [Fluent Python (Luciano Ramalho)](https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/) & [Official Python Tutorial](https://docs.python.org/3/tutorial/index.html)

### Aşama 1: Environment & Tooling
- [ ] **Dependencies**: `Poetry` veya `uv` kullanarak bağımlılıkları ve virtualenv'leri yönet.
- [ ] **Quality**: `Ruff` (Lint/Format) ve `MyPy` (Type check) araçlarını CI'ye ekle.
- [ ] **Packaging**: `pyproject.toml` standartlarına uygun proje yapısını kur.

### Aşama 2: Core Implementation
- [ ] **Efficiency**: Liste kompresyonları (List comprehensions) ve jeneratörler (Generators) ile bellek kullanımını optimize et.
- [ ] **Typing**: Fonksiyon imzalarına net tip tanımlamaları ekle (`Protocol` kullanarak duck typing'i resmileştir).
- [ ] **Error Handling**: Custom exception sınıfları oluştur ve `try/except` bloklarını spesifik tut.

### Aşama 3: Testing & Deployment
- [ ] **Unit Tests**: `Pytest` ile fixture tabanlı test yapısını kur.
- [ ] **Mocking**: `pytest-mock` ile harici servisleri ve I/O işlemlerini izole et.
- [ ] **Production**: `Gunicorn/Uvicorn` ayarlarını ve Dockerfile optimizasyonunu yap.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | `mutable default arguments` (list, dict) fonskiyonlarda kullanıldı mı? (Kullanılmamalı!). |
| 2 | DOCKER_IGNORE içinde `.venv` ve `__pycache__` var mı? |
| 3 | MyPy hataları (strict mode) tamamen temizlendi mi? |

---

*Python Pro v1.1 - Enhanced*
