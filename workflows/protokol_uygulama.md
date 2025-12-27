---
description: protokol_uygulama
---

## 0. Sistem Başlatma (BOOT SEQUENCE)

Her yeni oturumda, AI'ın "bağlamı" (context) kurabilmesi için şu 3 kaynağı sırasıyla oku:

1.  **⚖️ Anayasa (Global Rules):**
    * **Yol:** `%USER_PROFILE%\.gemini\GEMINI.md`
    * **Amaç:** Etik kurallar, kodlama standartları ve temel prensipleri yükle.

2.  **🧠 Proje Hafızası (Project Brain):**
    * **Yol:** `%USER_PROFILE%\.gemini\antigravity\brain`
    * **Amaç:** Bu projede daha önce alınan kararları, teknik borçları ve "yapılmaması gerekenleri" hatırla.

3.  **🗺️ Yetenek Haritası (Skills Manifest):**
    * **Yol:** `%USER_PROFILE%\.skillport\skills_manifest.json`
    * **Amaç:** Hangi görev için hangi araç setini (Kit) kullanacağını öğren.

**Onay Mesajı:** "✅ System Online: Rules [GEMINI.md] + Brain [Antigravity] + Skills [.skillport]"

---

## 1. Akıllı Yönlendirme (Router Logic)

Kullanıcı talebini analiz et -> Manifest'ten Kit Seç -> Uygula.

* Talep: "Veritabanı şemasını güncelle" -> **Kit:** `FullStackKit`
* Talep: "AWS maliyet raporu çıkar" -> **Kit:** `DevOpsKit`

---

## 2. Skill Yükleme (Absolute Path Injection)

Manifest'ten seçilen skill'leri şu şablona göre yükle:

> **PATH:** `%USER_PROFILE%\.skillport\skills\{skill_name}\SKILL.md`

Örnek: Eğer `DevOpsKit` seçildiyse, sadece o kitin içindeki araçları (örn: `aws_architect`, `terraform_engineer`) bu yoldan çekip bağlama ekle. Gereksiz skill yükleme.

---

## 3. Deneyim Kaydı (Learning Loop)

Görevi bitirmeden önce kendine sor: "Bu görev sırasında, gelecekte hatırlamam gereken kritik bir şey öğrendim mi?"
* *Örn: "Bu sunucuda Node v14 çalışmıyor, v18 şart."*

Eğer evet ise, bunu **Hafıza Dosyasına** ekle.

---

## 3. Deneyim Kaydı (Learning Loop)

Görevi bitirmeden önce kendine sor: "Bu görev sırasında, gelecekte hatırlamam gereken kritik bir şey öğrendim mi?"
* *Örn: "Bu sunucuda Node v14 çalışmıyor, v18 şart."*

Eğer evet ise, bunu **Hafıza Dosyasına** ekle.

---
Protokol v5.1 - Fully Integrated Pathing