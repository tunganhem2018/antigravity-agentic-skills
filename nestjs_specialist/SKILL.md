---
name: nestjs_specialist
router_kit: FullStackKit
description: NestJS architecture, module pattern, dependency injection ve microservices uzmanlığı.
metadata:
  skillport:
    category: backend
    tags: [architecture, automation, backend, best practices, clean code, coding, collaboration, compliance, debugging, dependency injection, design patterns, development, documentation, efficiency, git, maintainability, microservices, nestjs, nestjs specialist, optimization, productivity, programming, project management, quality assurance, refactoring, scalability, software engineering, standards, testing, typescript, utilities, version control, workflow]      - backend-engineering
---

# 🦁 NestJS Specialist

> Kurumsal Node.js uygulamaları için modüler ve scalable mimari rehberi.

---

## 🏗️ Core Architecture

### Modüler Yapı
NestJS, uygulamayı birbirine bağlı modüller yığını olarak görür.
- **Provider**: Business logic (`@Injectable`).
- **Controller**: Request handling (`@Controller`).
- **Module**: Grouping related components (`@Module`).

### Dependency Injection (DI)
```typescript
@Injectable()
export class UsersService {
  constructor(private readonly prisma: PrismaService) {} // Constructor injection
}
```

---

## 🛠️ Advanced Features

### Guards & Interceptors
- **Guards**: Authentication ve Authorization (`canActivate`).
- **Interceptors**: Loglama, Response Transformation veya Caching.
- **Pipes**: Data validation ve transformation (class-validator).

### Microservices
NestJS farklı transport layer'ları (TCP, Redis, RabbitMQ, Kafka) destekler.
```typescript
const app = await NestFactory.createMicroservice<MicroserviceOptions>(AppModule, {
  transport: Transport.REDIS,
  options: { url: 'redis://localhost:6379' },
});
```

---

## 🧪 Testing Strategy

### Unit Testing
```typescript
const module: TestingModule = await Test.createTestingModule({
  providers: [UsersService],
}).compile();

service = module.get<UsersService>(UsersService);
```

### E2E Testing
Supertest ile tüm HTTP akışını simüle etme.

---

*NestJS Specialist v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [NestJS Official Documentation](https://docs.nestjs.com/) & [NestJS Architecture Best Practices](https://docs.nestjs.com/best-practices)

### Aşama 1: Modularization & Providers
- [ ] **Domain Separation**: Özellikleri (Auth, Users, Billing) bağımsız modüllere ayır.
- [ ] **Decoupling**: Business logic'i Controller'dan çıkarıp Service'e (Provider) taşı.
- [ ] **Scope**: Service scope'unu (Singleton, Request, Transient) ihtiyaca göre belirle.

### Aşama 2: Middleware & Enhancers
- [ ] **Validation**: Global `ValidationPipe` kullanarak giriş verilerini (`DTO`) otomatik doğrula.
- [ ] **Exception Filters**: Hataları merkezi bir noktada (`HttpExceptionFilter`) yöneterek tutarlı API cevabı dön.
- [ ] **Guards**: Endpoint'leri korumak için `AuthGuard` ve `RolesGuard` hiyerarşisini kur.

### Aşama 3: Infrastructure & Scaling
- [ ] **Database**: TypeORM veya Prisma entegrasyonunu `DynamicModule` (`forRoot`) ile yap.
- [ ] **Config**: Ortam değişkenlerini `@nestjs/config` ile tip güvenli (`ValidationSchema`) yönet.
- [ ] **Monitoring**: Health check endpoint'lerini (`Terminus`) ekle.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Modüller arası dairesel bağımlılık (Circular dependency) var mı? |
| 2 | Tüm DTO'larda class-validator anotasyonları eksiksiz mi? |
| 3 | Service'ler doğrudan Express `req/res` objelerine erişiyor mu? (Erişmemeli!). |
