---
name: testing
router_kit: QualityKit
description: Unit, Integration ve E2E test stratejileri, Vitest, Jest ve Cypress.
metadata:
  skillport:
    category: quality
    tags: [architecture, automation, best practices, clean code, coding, collaboration, compliance, debugging, design patterns, development, documentation, efficiency, git, optimization, productivity, programming, project management, quality assurance, refactoring, software engineering, standards, testing, utilities, version control, workflow]      - quality-assurance
---

# 🧪 Testing

> Yazılım kalitesini garanti altına alan bütüncül test yaklaşımları.

---

*Testing v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [The Practical Test Pyramid (Ham Vocke)](https://martinfowler.com/articles/practical-test-pyramid.html) & [Testing Library Best Practices](https://testing-library.com/docs/guiding-principles/)

### Aşama 1: Testing Strategy & Pyramid
- [ ] **Unit Tests**: Fonksiyonel ve mantıksal en küçük birimleri izole şekilde (Mocking) test et (%70 kapsam).
- [ ] **Integration Tests**: Bileşenlerin veya servislerin birbirleriyle iletişimini doğrula (%20 kapsam).
- [ ] **E2E Tests**: Kullanıcı senaryolarını (Login, Checkout) gerçek tarayıcı ortamında test et (%10 kapsam).

### Aşama 2: Environment & Tooling
- [ ] **Framework Selection**: İhtiyaca göre Vitest/Jest (Unit), Playwright/Cypress (E2E) kurulumlarını yap.
- [ ] **Test Data**: Gerçekçi test verileri (Fixtures/Factories) oluştur.
- [ ] **Coverage**: Test kapsamını (Coverage report) takip et ve kritik alanları (Edge cases) atlama.

### Aşama 3: CI/CD & Automation
- [ ] **Pipeline**: Her PR açıldığında testleri otomatik çalıştıracak CI aksiyonlarını kur.
- [ ] **Failure Analysis**: Başarısız testlerde logları ve (varsa) ekran görüntülerini/videoları incele.
- [ ] **Flakiness**: Tutarsız (Flaky) testleri tespit et ve güvenilirliğini artır.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Testler birbirinden bağımsız (Parallel execution) çalışabiliyor mu? |
| 2 | Veritabanı veya API bağımlılıkları düzgün mocklandı mı? |
| 3 | Test çalıştırma süresi (<5 dk) geliştirme hızını engelliyor mu? |
