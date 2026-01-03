---
name: mobile_flutter
router_kit: FullStackKit
description: Flutter/Dart best practices, Riverpod state management ve performance optimization.
metadata:
  skillport:
    category: development
    tags: [architecture, automation, best practices, clean code, coding, collaboration, compliance, debugging, design patterns, development, documentation, efficiency, git, mobile flutter, optimization, productivity, programming, project management, quality assurance, refactoring, software engineering, standards, testing, utilities, version control, workflow]      - mobile-react-native
---

# 🐦 Mobile Flutter

> Flutter/Dart best practices ve performance optimization.

---

*Mobile Flutter v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [Flutter Engineering Best Practices](https://docs.flutter.dev/perf/best-practices) & [Riverpod Architecture](https://riverpod.dev/docs/concepts/about_code_generation)

### Aşama 1: Architecture Setup
- [ ] **Layering**: Feature-First yapısını kur (Presentation, Domain, Data).
- [ ] **State Management**: Riverpod `NotifierProvider` ve Code Generation (@riverpod) kullan.
- [ ] **Routing**: GoRouter ile type-safe navigasyon ve deep linking yapılandır.

### Aşama 2: Implementation
- [ ] **UI**: `const` constructorları kullanarak rebuild'leri minimize et.
- [ ] **Network**: Dio ve Retrofit ile API katmanını (Interceptor, Error Handling) yaz.
- [ ] **Storage**: Hassas veriler için `flutter_secure_storage`, cache için `Isar` veya `Hive` kullan.

### Aşama 3: Release & Quality
- [ ] **Testing**: Unit, Widget ve Integration testlerini (Golden Tests dahir) yaz.
- [ ] **Performance**: DevTools ile "Jank" (kare atlama) analizi yap (Shader compilation warm-up).
- [ ] **CI/CD**: Fastlane ile otomatik build and store upload süreçlerini kur.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Business logic UI'dan (Widget'lardan) tamamen ayrılmış mı? |
| 2 | App cold start süresi <2 saniye mi? |
| 3 | Farklı ekran boyutlarında (Tablet/Foldable) responsive davranıyor mu? |
