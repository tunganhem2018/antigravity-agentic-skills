---
name: rust_development
router_kit: FullStackKit
description: Rust systems programming, memory safety, Axum/Tokio ve WebAssembly rehberi.
metadata:
  skillport:
    category: development
    tags: [automation, aws, bash scripting, ci/cd, cloud computing, containerization, deployment strategies, devops, docker, gitops, infrastructure, infrastructure as code, kubernetes, linux, logging, microservices, monitoring, orchestration, pipelines, reliability, rust development, scalability, security, server management, terraform]      - wasm
---

# 🦀 Rust Development

> Güvenli, hızlı ve ölçeklenebilir sistem programlama.

---

*Rust Development v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [Rust API Guidelines](https://rust-lang.github.io/api-guidelines/) & [Zero To Production in Rust](https://www.zero2prod.com/)

### Aşama 1: Project Setup & Structure
- [ ] **Workspace**: Büyük projeler için Cargo Workspace yapısını kur (Monorepo).
- [ ] **Linter**: `clippy`'yi en sıkı modda (`-D warnings`) çalıştıracak şekilde CI pipeline'ına ekle.
- [ ] **Dependency Management**: `cargo-deny` ile lisans ve güvenlik kontrolü yap.

### Aşama 2: Implementation Patterns
- [ ] **Error Handling**: Kütüphaneler için `thiserror`, uygulamalar için `anyhow` kullan. Asla `unwrap()` kullanma (testler hariç).
- [ ] **Async Runtime**: Web sunucuları için `tokio` ve `axum` (veya `actix-web`) standartını benimse.
- [ ] **Type Safety**: "Newtype Pattern" kullanarak primitive obsession'dan kaçın (`struct UserId(Uuid)`).

### Aşama 3: Performance & Reliability
- [ ] **Tracing**: `tracing` ve `tracing-subscriber` ile structured logging kur. `println!` kullanma.
- [ ] **Benchmarks**: Kritik fonksiyonlar için `criterion` ile benchmark testleri yaz.
- [ ] **Release Profile**: Production build için `Cargo.toml` içinde `lto = true` ve `codegen-units = 1` ayarlarını yap.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | `cargo clippy` hatasız geçiyor mu? ve `cargo fmt` uygulandı mı? |
| 2 | Tüm public API'ler dökümante edildi mi? (`///` doc comments). |
| 3 | Docker imajı `distroless` veya `alpine` tabanlı optimize edildi mi? |
