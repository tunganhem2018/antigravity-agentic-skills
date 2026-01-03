---
name: payment_integration
router_kit: FullStackKit
description: Online ödeme sistemleri (Stripe, Iyzico), güvenli işlem yönetimi ve webhook entegrasyonu.
metadata:
  skillport:
    category: development
    tags: [architecture, automation, best practices, cleanup, coaching, compliance, development, documentation, financial services, integrations, maintainability, metadata, open-source, optimization, payment integration, performance, quality assurance, scalability, software engineering, standards, stripe, testing, version control, web development, workflow]      - fintech
---

# 💳 Payment Integration

> Stripe, Iyzico ve diğer ödeme sağlayıcıları ile güvenli entegrasyon rehberi.

---

## 🔒 Security Principles

### PCI Compliance
- Kart verilerini **asla** kendi sunucunda tutma.
- Sağlayıcının (Stripe Elements, Iyzico Form vb.) sunduğu secure UI bileşenlerini kullan.
- Veri transferinde her zaman TLS/SSL zorunlu tut.

### Webhook Security
- Gelen webhook'ların sağlayıcıdan geldiğini doğrula (Signature verification).
- Webhook endpoint'lerini idempotent (tekrar edilebilir) tasarlı.

---

## 🛠️ Implementation (Stripe Example)

### Server-side PaymentIntent
```javascript
const paymentIntent = await stripe.paymentIntents.create({
  amount: 2000, // cents
  currency: 'usd',
  automatic_payment_methods: { enabled: true },
});
```

### Webhook Handler
```javascript
const event = stripe.webhooks.constructEvent(
  request.body,
  sig,
  endpointSecret
);

if (event.type === 'payment_intent.succeeded') {
  const paymentIntent = event.data.object;
  // Fatura oluştur, DB güncelle
}
```

---

## 🔄 Transaction Statuses

| Statü | Açıklama | Aksiyon |
|-------|-----------|---------|
| `Succeeded` | Ödeme başarılı | Siparişi onayla |
| `Pending` | Ödeme beklemede | Kullanıcıyı bilgilendir |
| `Failed` | Ödeme başarısız | Hata mesajı göster |
| `Refunded` | İade edildi | Bakiyeyi düş |

---

*Payment Integration v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [Stripe Documentation](https://stripe.com/docs) & [PCI Security Standards](https://www.pcisecuritystandards.org/)

### Aşama 1: Provider Setup & Compliance
- [ ] **Provider Selection**: Bölgeye (Stripe vs Iyzico/Paytr) ve komisyon oranlarına göre seçim yap.
- [ ] **Sanity Check**: Test modunda `API Key` ve `Secret Key` bağlantısını doğrula.
- [ ] **UI Integration**: Provider'ın güvenli ödeme formunu (Elements/Checkout) ödeme sayfasına göm.

### Aşama 2: Transaction Logic
- [ ] **Payment Flow**: `PaymentIntent` oluştur -> Client tarafında ödemeyi onayla -> Webhook bekle.
- [ ] **Idempotency**: Aynı ödeme talebinin (Network hatası vb.) iki kez işlenmesini engelle (`Idempotency-Key`).
- [ ] **Logging**: Tüm transaction denemelerini (Hata kodlarıyla beraber) veritabanına logla.

### Aşama 3: Verification & Edge Cases
- [ ] **Webhook Verification**: İmza (Signature) kontrolü ile webhook güvenliğini sağla.
- [ ] **Edge Cases**: Yetersiz bakiye, 3D Secure reddi, Card expired gibi durumlar için hata mesajlarını test et.
- [ ] **Refunds**: İade süreci ve kısmi iade (Partial refund) senaryolarını test et.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | API Key'ler client-side kodda (Hardcoded) açıkta mı? (Check `.env`). |
| 2 | Veritabanında kredi kartı numarası tutuluyor mu? (Tutulmamalı!). |
| 3 | Ödeme başarılı olduktan sonra kullanıcıya email gidiyor mu? |
