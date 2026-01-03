---
name: regex_builder
router_kit: FullStackKit
description: Düzenli ifadeler (Regex) tasarımı, validation, extraction ve performans optimizasyonu.
metadata:
  skillport:
    category: development
    tags: [architecture, automation, best practices, cleanup, coaching, compliance, debugging, development, documentation, efficiency, integrations, maintainability, metadata, open-source, optimization, patterns, performance, quality assurance, regex, regex builder_1, regex optimization, regular expressions, scalability, software engineering, standards, string manipulation, testing, validation, version control, web development, workflow]      - string-processing
---

# 🔍 Regex Builder

> Karmaşık metin kalıplarını (Patterns) yakalama ve işleme rehberi.

---

## 🏗️ Common Patterns

| Amacı | Regex Kalıbı |
|-------|--------------|
| **Email** | `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$` |
| **Phone (TR)** | `^(05)[0-9]{9}$` |
| **URL** | `https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}...` |
| **Date (YYYY-MM-DD)** | `^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$` |

---

## 🛠️ Cheat Sheet

- `.` : Herhangi bir karakter.
- `*` : 0 veya daha fazla tekrar.
- `+` : 1 veya daha fazla tekrar.
- `?` : 0 veya 1 tekrar (Optional).
- `\d` : Rakam (0-9).
- `\w` : Alfanumerik (A-Z, a-z, 0-9, _).
- `\s` : Boşluk (Space, tab, newline).
- `^` / `$` : Başlangıç / Bitiş.
- `[...]` : Karakter seti.
- `(...)` : Capturing group.

---

## ⚡ Performance & Optimization

- **Greedy vs. Lazy**: `.*` (greedy) yerine `.*?` (lazy) kullanarak gereksiz taramayı önle.
- **Catastrophic Backtracking**: `(a+)+` gibi iç içe tekrarlardan kaçın.
- **Compiled Regex**: Sık kullanılan regex'leri önceden compile et (`re.compile` in Python).

---

## 🔧 Workflow

> **Kaynak:** [Regex101](https://regex101.com/) & [MDN Regular Expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions)

### Aşama 1: Requirement & Sandbox
- [ ] **Input Audit**: Yakalanacak metnin örneklerini ve "yakalanmaması gereken" (Edge cases) metinleri listele.
- [ ] **Sandbox**: Regex101 veya Regexr gibi araçlarda deseni (Pattern) oluştur ve test et.
- [ ] **Flags**: İhtiyaca göre `g` (global), `i` (case-insensitive), `m` (multiline) flag'lerini belirle.

### Aşama 2: Drafting & Security
- [ ] **Non-Capturing**: Gruba ihtiyacın yoksa `(?:...)` kullanarak bellek kullanımını azalt.
- [ ] **Anchor Use**: Mümkünse `^` ve `$` kullanarak motorun metnin ortasında arama yapmasını kısıtla (Hız kazandırır).
- [ ] **ReDoS Check**: Regex'in çok uzun metinlerde CPU'yu kitlemediğinden emin ol (ReDoS analizi).

### Aşama 3: Implementation & Documentation
- [ ] **Code Integration**: Hedef dilde (JS, Python, Go) regex'i implemente et ve escaping (`\\`) kurallarına uy.
- [ ] **Comments**: Karmaşık regex'lerin yanına ne işe yaradığını açıklayan yorum satırı ekle.
- [ ] **Unit Tests**: Çeşitli girdilerle (Pozitif/Negatif) regex'i otomatik test et.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Regex "Lookahead/Lookbehind" desteklemeyen dillerde çalışıyor mu? |
| 2 | Çok büyük dosyalarda (Large logs) performans kabul edilebilir mi? |
| 3 | Regex okunabilir mi? (Eğer çok karışıksa kod ile parçalamayı düşün). |

---

*Regex Builder v1.1 - Enhanced*
