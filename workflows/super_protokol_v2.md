---
description: Unified Super-Workflow. Skill yükleme + mühendislik disiplini. Her karmaşık istek için çalıştır.
---

# Super Protokol v2: Zeki Motor

> [!CAUTION]
> ## 🇹🇷 DİL KURALI - MUTLAK VE DEĞİŞMEZ
> 
> | Alan | Dil | Örnek |
> |------|-----|-------|
> | Konuşma, açıklama, plan | **TÜRKÇE** | "Şimdi API oluşturacağız" |
> | Kod, değişken, fonksiyon | İngilizce | `getUserById()` |
> | Yorum satırları | Türkçe | `// Kullanıcıyı getir` |
> | Commit mesajları | İngilizce | `feat: add login` |
> 
> **⚠️ HER MESAJDA BU KURALI KONTROL ET! İNGİLİZCEYE GEÇİŞ YASAKTIR!**

---

# PHASE 0: SKILL YÜKLEME (ZORUNLU)

> [!CAUTION]
> **⛔ BU PHASE ATLANAMAZ! ⛔**
> 
> - Skill yüklemeden Phase 1'e geçmek **YASAKTIR**
> - Bu kuralı ihlal etmek = Workflow'u bozmak
> - **Hiçbir istisna yok!**

---

## Adım 0.1: MCP Sağlık Kontrolü

// turbo
```javascript
mcp_skillport_search_skills({ query: "*" })
```

**Sonuç Kontrolü:**
- ✅ Başarılı → Adım 0.2'ye geç
- ❌ Hata/Timeout → **DURDUR**, kullanıcıya bildir, devam etme

---

## Adım 0.2: Prompt Analizi ve Skill Arama

1. Kullanıcının isteğinden **anahtar teknolojiler** çıkar (React, Python, API, vb.)
2. Skill ara:

// turbo
```javascript
mcp_skillport_search_skills({ query: "<anahtar_kelimeler>" })
```

---

## Adım 0.3: Skill Yükleme

**Seçim Kuralları:**
- Puan **≥ 1.0** olan skill'lerden **en yüksek 3 tanesini** seç
- Her birini yükle:

// turbo
```javascript
mcp_skillport_load_skill({ skill_id: "<skill_id>" })
```

**Fallback Kuralı:**
- Hiç uygun skill yoksa (tüm puanlar < 1.0) → `code_review` skill'ini yükle
- **Hiçbir prompt skill'siz kalmamalı!**

---

## ✅ CHECKPOINT: Phase 0 Tamamlandı mı?

Aşağıdaki koşullar sağlanmadan **ASLA** Phase 1'e geçme:

| # | Koşul | Durum |
|---|-------|-------|
| 1 | MCP sağlık kontrolü başarılı | ☐ |
| 2 | En az 1 skill yüklendi | ☐ |
| 3 | Yüklenen skill'ler kullanıcıya gösterildi | ☐ |

**⛔ Tüm kutular işaretli değilse → DURDUR!**

---

# PHASE 1: Proje Ortamı Kontrolü

## Adım 1.1: Workspace Kontrolü

- Aktif workspace var mı?
- Yoksa → Kullanıcıya "Hangi klasörde çalışıyoruz?" sor

## Adım 1.2: Proje Config Kontrolü

`.agent/GEMINI.md` dosyası var mı?

**Yoksa** → Oluştur:
```markdown
# Proje: [PROJE_ADI]

## Teknolojiler
- [package.json, requirements.txt vb. analiz et]

## Son Güncellemeler
- [Tarih]: Proje config oluşturuldu
```

**Varsa** → Oku ve bağlamı yükle

---

# PHASE 2: Strateji Belirleme

## Adım 2.1: Belirsizlik Kontrolü

- İstek net mi? (örn: "Buton rengini maviye çevir") → Phase 3'e geç
- İstek belirsiz mi? (örn: "Sayfayı iyileştir") → Adım 2.2'ye geç

## Adım 2.2: Tek Soru Kuralı

- Birden fazla soru **SORMA**
- **TEK** soru sor, cevabı bekle
- Kapsam netleşene kadar tekrarla

---

# PHASE 3: Planlama

## Adım 3.1: Görev Listesi Oluştur

- `task_boundary` ile görevi başlat
- `task.md` oluştur/güncelle

## Adım 3.2: Mikro Görevler

Her görev **2-5 dakika** sürmeli:

| ❌ Kötü | ✅ İyi |
|--------|-------|
| "Authentication yap" | "Login formu oluştur" |
| "API kur" | "GET endpoint yaz" |
| "Test ekle" | "UserService unit test" |

## Adım 3.3: Kullanıcı Onayı

- Planı kullanıcıya göster
- `notify_user` ile onay iste
- İstisna: Basit ve net görevlerde doğrudan devam et

---

# PHASE 4: Mühendislik Döngüsü

## TDD Kuralı (Demir Kanun)

> **"Test yazmadan kod yazma!"**

| Adım | Eylem | Doğrulama |
|------|-------|-----------|
| 🔴 KIRMIZI | Başarısız test yaz | Test başarısız olmalı |
| 🟢 YEŞİL | Testi geçecek minimal kod yaz | Test başarılı olmalı |
| 🔵 REFACTOR | Kodu temizle | Testler hala yeşil |

**İstisnalar:** Config dosyaları, UI görselleri → Manuel doğrulama tanımla

## Doğrulama Kapısı

"Bitti" demeden önce **MUTLAKA**:

1. 🎯 Hangi komut kanıt olur?
2. ▶️ Komutu çalıştır
3. 👀 Çıktıyı kontrol et
4. ✅ Sadece başarılıysa "bitti" de

---

# PHASE 5: Git & Son Adımlar

## Adım 5.1: Commit Conventions

| Type | Açıklama | Örnek |
|------|----------|-------|
| `feat` | Yeni özellik | `feat: add login page` |
| `fix` | Hata düzeltme | `fix: resolve null error` |
| `docs` | Dokümantasyon | `docs: update README` |
| `style` | Formatting | `style: fix indentation` |
| `refactor` | Kod yeniden yapılandırma | `refactor: extract utils` |
| `test` | Test ekleme/düzeltme | `test: add unit tests` |
| `chore` | Build, CI, deps | `chore: update deps` |

**Format:** `<type>(<scope>): <description>`

## Adım 5.2: Proje Config Güncelle

`.agent/GEMINI.md` → "Son Güncellemeler" bölümüne ekle:
```markdown
- [TARİH]: [Yapılan işin özeti]
```

## Adım 5.3: Kullanıcıya Bildir

Görevi tamamla, **kanıtları göster**.

---

# 🔄 HER MESAJDA HATIRLA

> [!IMPORTANT]
> ## Üç Demir Kural
> 
> 1. **🇹🇷 TÜRKÇE KONUŞ** - Kod hariç her şey Türkçe
> 2. **📦 SKİLL YÜKLE** - En az 1 skill zorunlu (puan ≥ 1.0)
> 3. **✅ KANITLA** - "Bitti" demeden kanıt göster
