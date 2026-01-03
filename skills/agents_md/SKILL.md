---
name: agents_md
router_kit: UniversalKit
description: .agent klasörü ve .md dosyaları üzerinden ajan davranışlarını ve proje hafızasını yönetme.
metadata:
  skillport:
    category: meta
    tags: [agents, documentation, memory, instruction-tuning, project-config]
---

# 📂 Agents.md / .agent Config

Ajanın bir proje içindeki davranışlarını, yasaklarını ve hafızasını yöneten konfigürasyon sistemi.

---

## 🔄 Workflow

> **Kaynak:** [Cursor .cursorrules Standard](https://cursor.com/rules) & [Claude Code Instructions Best Practices](https://docs.anthropic.com/en/docs/agents-and-tools/claudecode)

### Aşama 1: Hafıza Yapılandırması (Memory Setup)
- [ ] **.agent Klasörü:** Proje kök dizininde `.agent/` klasörünün varlığını kontrol et/oluştur.
- [ ] **GEMINI.md:** Proje teknolojilerini, son güncellemeleri ve ajan için "Kritik Kuralları" içeren ana dökümanı başlat.
- [ ] **Hiyerarşi:** Global kurallar (user_global) ile projeye özel yerel kuralların (GEMINI.md) hiyerarşisini belirle.

### Aşama 2: Kural Tanımlama (Logic & Constraints)
- [ ] **Dosya Yasakları:** Değiştirilmemesi gereken veya okunması yasak olan dosyaları (örn: `.lock`, `.env`) belirt.
- [ ] **Coding Styles:** Projeye özel isimlendirme kurallarını (CamelCase, snake_case) ve tech-stack kısıtlarını yaz.
- [ ] **Instruction Injection:** Ajan her başladığında bu kuralları otomatik bağlamına (Context) eklemesini sağla.

### Aşama 3: Dinamik Güncelleme (Sync & Update)
- [ ] **Task Tracking:** Her büyük değişiklikten sonra `GEMINI.md` içindeki "Son Güncellemeler" (Recent Changes) bölümünü güncelle.
- [ ] **Self-Correction:** Ajanın yaptığı hataları "Daha sonra yapma" şeklinde kurala (User Rules) dönüştür.
- [ ] **Conflict Resolution:** Eskiyen veya çelişen kuralları ayıkla.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1     | `GEMINI.md` dosyası ajana her adımda rehberlik ediyor mu? |
| 2     | Proje dışı (Global) kurallarla yerel kurallar çakışıyor mu? |
| 3     | Kurallar yeterince öz (concise) ve net mi? |

---
*Agents.md v1.3 - Evidence-Based Update*
