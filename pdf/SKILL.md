---
name: pdf
router_kit: ManagementKit
description: PDF generation, parsing, form filling ve dijital imza yönetimi.
metadata:
  skillport:
    category: operations
    tags: [automation, best practices, business, collaboration, compliance, documentation, efficiency, legal, optimization, pdf, productivity, quality assurance, software engineering, standards, utilities, workflow, writing]      - reports
---

# 📄 PDF Management & Automation

> PDF oluşturma, okuma ve form doldurma işlemleri.

---

## 🛠️ PDF Generation (Node.js)

### PDFKit (Low Level)
Hassas layout ve çizim gerektiren dökümanlar için.
```javascript
const doc = new PDFDocument();
doc.pipe(fs.createWriteStream('output.pdf'));
doc.fontSize(25).text('Hello World!', 100, 100);
doc.end();
```

### Puppeteer (HTML to PDF)
Karmaşık CSS ve web tabanlı raporlar için en iyi yöntem.
```javascript
const browser = await puppeteer.launch();
const page = await browser.newPage();
await page.goto(url, { waitUntil: 'networkidle0' });
await page.pdf({ path: 'report.pdf', format: 'A4' });
```

---

## 🔍 Parsing & Text Extraction

### PDF-Parse
Metin içeriğini düz yazı olarak çekme.
```javascript
const data = await pdf(dataBuffer);
console.log(data.text);
```

### Tabula (Tables)
Tablo verilerini yapılandırılmış (JSON/CSV) halde çekme.

---

## 🖋️ Form Filling & Signing

- **Form Filling**: `pdf-lib` kullanarak mevcut bir template üzerindeki alanları (Input fields) doldurma.
- **Digital Signatures**: Sertifika tabanlı imzalama (AcroForm signatures).

---

*PDF Management v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [Puppeteer PDF Guide](https://pptr.dev/guides/pdf-generation) & [PDF-lib Documentation](https://pdf-lib.js.org/)

### Aşama 1: Strategy Selection
- [ ] **Method Choice**: Statik raporlar için `HTML-to-PDF`, yüksek performans/grafik için `Native Libraries` (PDFKit) seç.
- [ ] **Input Audit**: Form doldurma yapılacaksa PDF template ID'lerini ve alan (Field) isimlerini doğrula.
- [ ] **Fonts**: Özel karakter (Türkçe vb.) sorunlarını önlemek için fontları `Embed` et.

### Aşama 2: Processing & Generation
- [ ] **Generation**: Sayfa numaraları, header/footer ve dinamik içerikleri ekle.
- [ ] **Optimization**: PDF boyutunu küçültmek için resimleri optimize et ve font alt kümelerini (Subsetting) kullan.
- [ ] **Security**: Gerekiyorsa PDF'e şifre (Encryption) koy veya sadece okunabilir (Read-only) yap.

### Aşama 3: Output & Validation
- [ ] **Verification**: Oluşan PDF'i farklı browser ve viewer'larda render kontrolü yap.
- [ ] **Extraction**: Parsing işlemi yapılıyorsa metin kayması (OCR ihtiyacı) olup olmadığını kontrol et.
- [ ] **Archiving**: PDF/A standartlarına uyumluluğu sağla (Uzun süreli saklama için).

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Türkçe karakterler (?) şeklinde mi çıkıyor? (Font config kontrol). |
| 2 | Memory usage: Çok büyük PDF'ler (100+ sayfa) sunucuyu kitliyor mu? |
| 3 | Metadata (Author, Title) doğru set edildi mi? |
