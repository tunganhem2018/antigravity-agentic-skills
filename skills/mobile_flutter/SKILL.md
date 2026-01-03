---
name: mobile_flutter
router_kit: FullStackKit
description: Flutter ile cross-platform mobile app development, UI architecture ve state management.
metadata:
  skillport:
    category: frontend
    tags: [android, architecture, automation, best practices, clean code, coding, collaboration, compliance, cross-platform, dart, debugging, development, documentation, efficiency, flutter, framework, git, ios, mobile development, mobile flutter, optimization, productivity, programming, project management, quality assurance, refactoring, software engineering, standards, testing, ui/ux, utilities, version control, workflow]      - mobile-react-native
---

# 💙 Mobile Flutter

> Google'ın UI toolkit'i Flutter ile yüksek performanslı, native uygulamalar.

---

## 🏗️ Core Architecture

### 1. Everything is a Widget
Flutter'da UI'ın her parçası bir Widget'tır (Stateless veya Stateful).

### 2. State Management Options
- **Provider**: Basit ve standart.
- **Riverpod**: Daha güvenli ve esnek (Önerilen).
- **Bloc**: Büyük ve kurumsal projeler için event-driven yaklaşım.

---

## 🎨 UI & Design (Material / Cupertino)

| Özellik | Flutter Yaklaşımı |
|---------|-------------------|
| **Layout** | Row, Column, Stack, Container |
| **Styling** | BoxDecoration, TextStyle |
| **Animation** | AnimationController, Hero, Lottie |
| **Navigation** | GoRouter, Navigator 2.0 |

---

## 🔧 Workflow Tools

```bash
# Bağımlılıkları yükle
flutter pub get

# Uygulamayı çalıştır
flutter run

# Build (Release)
flutter build apk --release
flutter build ios --release
```

---

*Mobile Flutter v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [Flutter Documentation - Best Practices](https://docs.flutter.dev/perf/best-practices)

### Aşama 1: Project Structure
- [ ] **Clean Architecture**: `data`, `domain` ve `presentation` katmanlarını ayır.
- [ ] **Dependencies**: `pubspec.yaml` dosyasını düzenli tut, versiyon çakışmalarını önle.

### Aşama 2: UI Development
- [ ] **Responsive**: `LayoutBuilder` veya `ScreenUtil` kullanarak farklı ekran boyutlarına uyum sağla.
- [ ] **Theming**: Uygulama çapında `ThemeData` (Dark/Light) kullan, hardcoded renk yazma.
- [ ] **Performance**: Gereksiz `setState`'lerden kaçın, `const` constructor kullan.

### Aşama 3: Native Integration & Test
- [ ] **Platforms**: Android (Java/Kotlin) ve iOS (Swift) için gerekli izinleri (Camera, Location) konfigüre et.
- [ ] **Testing**: Unit, Widget ve Golden (Visual) testleri yaz.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Uygulama 60 FPS (veya 120 FPS) akıcılığında mı? |
| 2 | Resimler ve Assetler optimize edildi mi? |
| 3 | Hata yönetimi (Global error handling) yapıldı mı? |
