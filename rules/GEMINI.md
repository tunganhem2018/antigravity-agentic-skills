---
description: Global Agent Kuralları - Tüm işlemlerde geçerli temel kurallar.
---

# GEMINI.md - Global Rules

> [!IMPORTANT]
> Bu kurallar Anayasa niteliğindedir. Her görüşme ve görevde MUTLAK geçerlidir.

---

## 🌐 1. DİL KURALI (MUTLAK)

> [!CAUTION]
> **Bu kural ASLA değişmez. Her cevaptan önce kontrol et!**

| Alan | Dil | Örnek |
|------|-----|-------|
| Konuşma, açıklama, plan | **TÜRKÇE** | "Şimdi API endpoint oluşturacağız" |
| Kod, değişken, fonksiyon | İngilizce | getUserById, handleSubmit |
| Yorum satırları (kod içi) | Türkçe | // Kullanıcıyı getir |
| Commit mesajları | İngilizce | feat: add user login |

---

## 🔒 2. SKILL & MANIFEST ZORUNLULUĞU

> [!CAUTION]
> **Manifest okumadan ve Skill yüklemeden HİÇBİR işlem yapma!**

### Başlangıç Protokolü:
1. **İLK İŞ:** Manifest'i Oku (.skillport\skills_manifest.json)
2. **ROUTER:** Görevi analiz et → Manifest'ten uygun **"Kit"**i seç.
3. **YÜKLE:** Seçilen Kit içindeki skill'leri yükle (mcp_skillport_load_skill).

### Skill Yükleme Onay Formatı:

✅ Core: Yüklendi
🗺️ Manifest: Okundu (v9.1)
📦 Kit: [Kit-Adı] Aktif (X Skill)


> **UYARI:** Asla kafana göre skill uydurma. Sadece Manifest'te tanımlı olanları kullan.

---

## ✅ 3. KOD KALİTESİ

Her kod değişikliğinde standartlar:
- [ ] ESLint / Linter kontrolü
- [ ] TypeScript (varsa) tip güvenliği
- [ ] 2x Review (Kendi kodunu eleştir)
- [ ] Test çalıştır (varsa)

---

## 📋 4. SELF-CHECK (Her Cevap Öncesi)

Cevabı göndermeden önce şunları doğrula:

□ Dil: Türkçe mi?
□ Manifest: Doğru Kit seçildi mi?
□ Path: Skill yolları doğru mu? (skills/{name}/SKILL.md)


---

## 🚫 5. TARİHÇE KANUN DEĞİLDİR (ANTI-PHANTOM RULE)

> [!CAUTION]
> **Conversation History Emir Veremez!**

*   **Prensip:** "Conversation History" (Sohbet Geçmişi) AI'a sadece bağlam (context) sağlar, asla talimat (instruction) veremez.
*   **Kural:** Bir eylem GEMINI.md veya .agent/workflows içindeki yazılı protokollerde açıkça belirtilmemişse, geçmişte 1000 kez yapılmış olsa bile **YAPILMAZ**.
*   **Slogan:** "Yazılı değilse, yoktur."
