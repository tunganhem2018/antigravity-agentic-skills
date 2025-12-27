---
name: core
router_kit: SystemBoot
description: System Bootstrapper. Initializes connection to Global Brain, Manifest and Rules.
metadata:
  skillport:
    category: core
    tags: [root, system, boot]
    alwaysApply: true
---

# 🎯 CORE (System Bootstrapper) v5.0

> **System Status:** Distributed Architecture Active
> Bu skill artık "İş Yapan" değil, "Bağlantı Kuran" birimdir.

---

## 🔗 Sistem Bağlantıları (Hard Links)

Core skill yüklendiğinde, AI şu mutlak yolları hafızaya almalıdır:

1.  **🧠 GLOBAL BRAIN (Hafıza):**
    * `%USER_PROFILE%\.gemini\antigravity\brain` (Ana Hafıza)
    * *Not: Bu klasördeki yerel `memory.md` dosyasını GÖRMEZDEN GEL.*

2.  **⚖️ GLOBAL RULES (Anayasa):**
    * `%USER_PROFILE%\.gemini\GEMINI.md` (Ana Kurallar)
    * *Not: Bu klasördeki `technical_standards.md` sadece kodlama standartları içindir.*

3.  **🗺️ SKILL MANIFEST (Harita):**
    * `%USER_PROFILE%\.skillport\skills_manifest.json`
    * *Not: `references.md` artık sadece arşiv amaçlıdır, skill seçimi için JSON kullanılır.*

---

## ⚡ Yönlendirme Mantığı

Skill seçerken şu sırayı izle:
1.  Manifest'teki **"Kits"** bölümüne bak.
2.  Uygun Kiti seç.
3.  Yolu oluştur: `%USER_PROFILE%\.skillport\skills\{skill_name}\SKILL.md`
