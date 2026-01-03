---
name: cli_developer
router_kit: UniversalKit
description: Node.js, Go veya Python ile profesyonel komut satırı araçları (CLI) geliştirme.
metadata:
  skillport:
    category: development
    tags: [cli, devtools, automation, terminal, shell]
---

# 💻 CLI Developer

Terminal üzerinde çalışan, hızlı ve etkili geliştirici araçları tasarımı.

---

## 🔄 Workflow

> **Kaynak:** [Command Line Interface Guidelines (CLIG)](https://clig.dev/) & [Heroku CLI Style Guide](https://devcenter.heroku.com/articles/cli-style-guide)

### Aşama 1: Arayüz ve Argüman Tasarımı (UX & Parsing)
- [ ] **Command Structure:** Komutları hiyerarşik (örn: `git commit -m`) veya tekil olarak planla.
- [ ] **Argument Parsing:** `commander`, `yargs` (Node) veya `click` (Python) ile flag/argüman yönetimini kur.
- [ ] **Interactive Prompts:** Kullanıcıdan seçim almak için `inquirer` veya `enquirer` entegre et.

### Aşama 2: Görsel Geribildirim (Visual Feedback)
- [ ] **Colors & Icons:** Önemli uyarılar için `chalk`, ikonlar için emoji desteği ekle.
- [ ] **Progress Indicators:** Uzun işlemler için `ora` (Spinner) veya `cli-progress` bar ekle.
- [ ] **Error Messaging:** Hataları kullanıcıya açık ve çözüm odaklı şekilde sun.

### Aşama 3: Dağıtım ve Entegrasyon (Distribution)
- [ ] **Global Install:** Paketi `npm install -g` veya brew/pip ile yüklenebilir hale getir.
- [ ] **Auto-Update:** Yeni sürümler için kullanıcıyı uyaran bir mekanizma kur.
- [ ] **Documentation:** `--help` komutu ile her fonksiyona dair yardımcı metinler oluştur.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1     | CLI aracı beklenen girdiler dışında (Edge cases) hatayı nasıl ele alıyor? |
| 2     | `--version` ve `--help` bayrakları (flags) çalışıyor mu? |
| 3     | Renksiz (No-color) mod desteği var mı? (Erişilebilirlik) |

---
*CLI Developer v1.2 - Evidence-Based Update*
