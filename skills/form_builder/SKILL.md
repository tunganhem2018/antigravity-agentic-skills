---
name: form_builder
router_kit: FullStackKit
description: Dinamik form oluşturma, validation (React Hook Form + Zod) ve çok adımlı form yönetimi.
metadata:
  skillport:
    category: development
    tags: [accessibility, api integration, backend, browser apis, client-side, components, css3, debugging, deployment, form builder, frameworks, frontend, fullstack, html5, javascript, libraries, node.js, npm, performance optimization, responsive design, seo, state management, testing, typescript, ui/ux, web development]      - forms
---

# 📝 Form Builder

> Dinamik, erişilebilir ve tip güvenli form yönetimi.

---

*Form Builder v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [React Hook Form Documentation](https://react-hook-form.com/get-started) & [Zod Documentation](https://zod.dev/)

### Aşama 1: Schema Definition (Validation)
- [ ] **Define**: Zod ile formun şemasını ve doğrulama kurallarını (email, min length vb.) belirle.
- [ ] **Types**: Şemadan TypeScript tipini (`z.infer`) türet.

### Aşama 2: component Orchestration
- [ ] **Hook**: `useForm` hook'unu Zod çözücüsü (`zodResolver`) ile başlat.
- [ ] **Fields**: Giriş alanlarını (Input, Select, Checkbox) merkezi bir yapıdan veya kütüphane bileşenlerinden oluştur.

### Aşama 3: Submission & Feedback
- [ ] **Handling**: `onSubmit` fonksiyonunda veriyi işle ve API'ye gönder.
- [ ] **Errors**: Hata mesajlarını alan bazlı ve kullanıcı dostu şekilde göster.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Form submit edilmeden önce tüm alanlar doğrulanıyor mu? |
| 2 | Gereksiz re-render (Performans) kontrolü yapıldı mı? |
| 3 | Form verisi submit sonrası uygun şekilde temizleniyor mu? |
