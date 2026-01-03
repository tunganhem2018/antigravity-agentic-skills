---
name: playwright_testing
router_kit: FullStackKit
description: Playwright ile E2E test, visual regression, cross-browser testing ve network interception.
metadata:
  skillport:
    category: quality
    tags: [architecture, automation, best practices, cleanup, coding, collaboration, compliance, debugging, development, documentation, e2e testing, efficiency, git, maintainability, optimization, performance, playwright, playwright testing_1, productivity, programming, quality assurance, software engineering, standards, testing, utilities, version control, workflow]      - quality-assurance
---

# 🎭 Playwright Testing

> Uçtan uca (E2E) test otomasyonu ve cross-browser v2.0 rehberi.

---

## 🚀 Setup & Launch

### Kurulum
```bash
npm init playwright@latest
```

### Temel Test Yapısı
```javascript
import { test, expect } from '@playwright/test';

test('has title', async ({ page }) => {
  await page.goto('https://playwright.dev/');
  await expect(page).toHaveTitle(/Playwright/);
});
```

---

## 🛠️ Advanced Features

### Locators & Actions
| Action | Komut |
|--------|-------|
| Click | `await page.getByRole('button').click()` |
| Type | `await page.getByLabel('User').fill('admin')` |
| Hover | `await page.locator('.menu').hover()` |
| Select | `await page.locator('select').selectOption('blue')` |

### Visual Regression
```javascript
await expect(page).toHaveScreenshot('landing.png');
```

---

## 🔧 Workflow

> **Kaynak:** [Playwright Official Docs](https://playwright.dev/docs/intro) & [Testing Best Practices](https://playwright.dev/docs/best-practices)

### Aşama 1: Environment & Selectors
- [ ] **Config**: `playwright.config.ts` dosyasında `projects` (Chromium, Firefox, Webkit) ve `baseURL` ayarlarını yap.
- [ ] **Locators**: Testlerin kırılgan olmaması için "User-visible" (Role, Label, Placeholder) locator'ları tercih et.
- [ ] **Auth State**: Tekrar tekrar login olmamak için `auth/user.json` ile session storage save/reuse stratejisini kur.

### Aşama 2: Test Orchestration
- [ ] **Atomic Tests**: Her testi bağımsız ve tek bir senaryoya odaklı yaz.
- [ ] **Parallelism**: Testleri paralel çalıştırarak CI süresini optimize et.
- [ ] **Fixtures**: Özel login veya setup logic'leri için `custom fixtures` oluştur.

### Aşama 3: CI/CD & Reporting
- [ ] **Network Mocking**: Harici API'ları `page.route` ile mock'layarak testlerin hızını ve stabilitesini artır.
- [ ] **Traces**: Hata anında video ve ekran görüntüsü alacak `trace: 'on-first-retry'` ayarını aktif et.
- [ ] **Reports**: HTML report ve CI (GitHub Actions) entegrasyonunu doğrula.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Hard-coded `waitForTimeout` kullanıldı mı? (Kullanılmamalı, `expect` otomatik bekler). |
| 2 | Testler "Flaky" (Bazen geçip bazen kalıyor) mi? |
| 3 | Sensitif veriler (Şifre vb.) environment variable olarak mı kullanılıyor? |

---

*Playwright Testing v1.1 - Enhanced*
