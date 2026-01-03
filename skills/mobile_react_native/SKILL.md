---
name: mobile_react_native
router_kit: FullStackKit
description: React Native ile cross-platform mobile app development, Native Modules ve Expo workflow.
metadata:
  skillport:
    category: frontend
    tags: [android, architecture, automation, best practices, clean code, coding, collaboration, compliance, cross-platform, debugging, development, documentation, efficiency, expo, frameworks, git, ios, javascript, mobile development, mobile react native, native modules, optimization, productivity, programming, project management, quality assurance, react native, refactoring, software engineering, standards, testing, typescript, ui/ux, utilities, version control, workflow]      - mobile-flutter
---

# ⚛️ Mobile React Native

> React ile native mobil uygulama geliştirme.

---

## 🚀 Workflow Options

### 1. Expo (Önerilen)
Hızlı başlangıç, managed infrastructure, EAS (Expo Application Services).
```bash
npx create-expo-app MyProject
```

### 2. React Native CLI
Native kod (Java/Swift) üzerinde tam kontrol gerektiğinde.
```bash
npx react-native init MyProject
```

---

## 🏗️ UI & components

| React Native | HTML Karşılığı |
|--------------|----------------|
| `<View>` | `<div>` |
| `<Text>` | `<span>` / `<p>` |
| `<Image>` | `<img>` |
| `<ScrollView>`| `overflow: scroll` |
| `<FlatList>` | List rendering (optimize) |

---

## 🔧 Key Libraries

- **Navigation**: `react-navigation`
- **Styling**: `StyleSheet.create` or `Tailwind (NativeWind)`
- **State**: `Zustand` or `Redux Toolkit`
- **Animations**: `react-native-reanimated`

---

*Mobile React Native v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [React Native Documentation](https://reactnative.dev/docs/getting-started) & [Expo Documentation](https://docs.expo.dev/)

### Aşama 1: Environment & Setup
- [ ] **Expo Workflow**: EAS (Expo Application Services) konfigürasyonunu yap.
- [ ] **TypeScript**: Tüm projeyi tip güvenli (Strict mode) kur.
- [ ] **Assets**: Splash screen ve uygulama ikonlarını tüm çözünürlükler için hazırla.

### Aşama 2: Development Patterns
- [ ] **Styling**: `StyleSheet` kullanırken `Flexbox` kurallarına sadık kal.
- [ ] **Navigation**: `Stack` ve `Tab` navigasyon yapısını kurgula.
- [ ] **Interactions**: Kullanıcı geri bildirimi için `Pressable` veya `Touchable` kullan.

### Aşama 3: Performance & Native
- [ ] **Optimization**: `FlashList` kullanarak uzun listeleri akıcı hale getir.
- [ ] **Native Modules**: Gerekliyse JSI (JavaScript Interface) üzerinden native köprüler kur.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Uygulama Android ve iOS simülatörlerinde aynı görünüyor mu? |
| 2 | Deep Linking düzgün çalışıyor mu? |
| 3 | Bundle boyutu (Release build) optimize mi? |
