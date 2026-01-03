---
name: cache_patterns
router_kit: FullStackKit
description: Redis, Memcached ve browser cache ile sistem performansını artırma stratejileri.
metadata:
  skillport:
    category: backend
    tags: [caching, redis, performance, optimization, scalability]
---

# ⚡ Cache Patterns

Veri erişim hızını artıran ve yükü azaltan önbellekleme stratejileri.

---

## 🔄 Workflow

> **Kaynak:** [Redis Design Patterns](https://redis.com/solutions/use-cases/caching/) & [MDN Web Caching](https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching)

### Aşama 1: İhtiyaç ve Katman Belirleme (Needs & Layers)
- [ ] **Don't Cache Everything:** Hangi verinin cache'lenmeye değer olduğunu (Sık erişilen/Nadir değişen) belirle.
- [ ] **Layer Choice:** Client-side (Browser), CDN, API Gateway veya Database (Redis) katmanlarından uygun olanı seç.
- [ ] **Store Choice:** In-memory (Redis) mi yoksa LocalStorage/IndexDB mi kullanılacak?

### Aşama 2: Strateji ve TTL (Strategy & TTL)
- [ ] **Caching Patterns:** Cache Aside (En yaygın), Read-Through, Write-Through veya Write-Behind desenini seç.
- [ ] **TTL (Time to Live):** Verinin bayatlama süresini (Expiration) mantıklı bir dengeyle saptama.
- [ ] **Eviction Policy:** Cache dolduğunda hangi verinin silineceğini (LRU, LFU, FIFO) belirle.

### Aşama 3: Invalidation ve Tutarlılık (Consistency)
- [ ] **Cache Busting:** Veri güncellendiğinde eski cache'i nasıl temizleyeceğini (Invalidation) planla.
- [ ] **Stale-While-Revalidate:** Arka planda güncelleme yaparken eski veriyi sunma (SWR) yapısını kur.
- [ ] **Observability:** Cache Hit/Miss oranlarını takip ederek stratejiyi optimize et.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1     | Veri güncellendiğinde kullanıcılar hala eski "bayat" veriyi mi görüyor? |
| 2     | Redis sunucusu çökerse uygulama "Graceful Degradation" (DB'ye düşme) yapabiliyor mu? |
| 3     | Cache anahtarları (Keys) çakışmayı önleyecek şekilde prefix'lendi mi? |

---
*Cache Patterns v1.2 - Evidence-Based Update*
