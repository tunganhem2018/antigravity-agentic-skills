---
name: algorithmic_art
router_kit: FullStackKit
description: p5.js ile generative art, flow fields ve interactive visuals oluşturma rehberi.
metadata:
  skillport:
    category: design
    tags: [algorithmic art, architecture, automation, best practices, clean code, coding, collaboration, compliance, debugging, design patterns, development, documentation, efficiency, git, optimization, productivity, programming, project management, quality assurance, refactoring, software engineering, standards, testing, utilities, version control, workflow]      - creative
---

# 🎨 Algorithmic Art

> p5.js ile generative art rehberi.

---

*Algorithmic Art v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [Generative Design Process](https://www.illustration.app/blog/the-generative-design-process-from-ai-output-to-polished-visual)

### Aşama 1: Concept & Rules
- [ ] **Define Theme**: e.g., "Organic Decay", "Geometric Order".
- [ ] **Set Constraints**: Color palette (max 3 colors), Aspect ratio.
- [ ] **Choose Algorithm**: Flow fields, Cellular Automata, Recursion.

### Aşama 2: Implementation (Sketching)
- [ ] **Setup**: Configure canvas and basic loop.
- [ ] **Primitives**: Draw static shapes to test composition.
- [ ] **Dynamics**: Add movement/change (using `draw()` loop).

### Aşama 3: Generative Logic
- [ ] **Introduce Randomness**: Use `random()` inside controlled bounds.
- [ ] **Apply Noise**: Replace random with `noise()` for natural flow.
- [ ] **Interaction**: Couple variables with mouse/keyboard inputs.

### Aşama 4: Tuning & Curation
- [ ] **Parameterize**: Create variables for `scale`, `speed`, `density`.
- [ ] **Seed Testing**: Test different `randomSeed()` values.
- [ ] **Selection**: Curate the best outputs.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Konsept ve kısıtlamalar net |
| 2 | Temel döngü hatasız çalışıyor |
| 3 | Çıktı her çalıştırıldığında varyasyon gösteriyor |
| 4 | Performans stabil (>30 FPS) |
