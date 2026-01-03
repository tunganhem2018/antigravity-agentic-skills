---
name: regex_builder
router_kit: FullStackKit
description: Regular expression oluşturma, test etme, debug ve açıklama rehberi.
metadata:
  skillport:
    category: development
    tags: [accessibility, api integration, backend, browser apis, client-side, components, css3, debugging, deployment, frameworks, frontend, fullstack, html5, javascript, libraries, node.js, npm, performance optimization, regex builder, responsive design, seo, state management, testing, typescript, ui/ux, web development]      - text-processing
---

# 🔤 Regex Builder

> Regular expression oluşturma ve test rehberi.

---

*Regex Builder v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [Regular-Expressions.info](https://www.regular-expressions.info/) & [OWASP ReDoS Prevention](https://owasp.org/www-community/attacks/Regular_expression_Denial_of_Service_-_ReDoS)

### Aşama 1: Construction & Security
- [ ] **Named Groups**: `(?<year>\d{4})` gibi isimlendirilmiş gruplar kullan (Okunabilirlik).
- [ ] **ReDoS Prevention**: "Catastrophic Backtracking"i önlemek için Atomic Groups `(?>...)` veya Possessive Quantifiers `++` kullan.
- [ ] **Boundaries**: Her zaman `^` ve `$` (veya `\A` ve `\z`) ile string sınırlarını belirle.

### Aşama 2: Testing & Validation
- [ ] **Visual Testing**: Regex101 veya RegExr üzerinde görsel olarak test et.
- [ ] **Unit Tests**: Hem "match" (pozitif) hem "non-match" (negatif) case'lerini test et.
- [ ] **Performance**: Regex'in çalışma süresini limitli tut (Execution timeout).

### Aşama 3: Implementation
- [ ] **Pre-compilation**: Döngü içinde regex derleme (`new RegExp`, `re.compile`). Başlangıçta derle.
- [ ] **Comments**: Karmaşık regex'ler için `(?# comment)` veya "Verbose Mode" (Python `re.X`) kullan.
- [ ] **Library**: Çok karmaşık patternler için hazır kütüphaneleri (URL parser, Email validator) tercih et, tekerleği yeniden icat etme.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Regex ReDoS saldırısına karşı güvenli mi? (Safe-regex toolları ile tara). |
| 2 | Pattern sadece beklenen karakterleri mi kabul ediyor? (Allowlist vs Blocklist). |
| 3 | Unicode desteği (`u` flag) açık mı? (Emoji ve UTF-8 karakterler için). |
