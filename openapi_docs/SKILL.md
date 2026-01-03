---
name: openapi_docs
router_kit: FullStackKit
description: API documentation, Swagger UI, SpringDoc ve OpenAPI 3.0 standartları uzmanlığı.
metadata:
  skillport:
    category: documentation
    tags: [api design, api development, api documentation, architecture, automation, best practices, cleanup, coaching, documentation, integrations, maintainability, metadata, open-source, openapi, openapi docs_1, optimization, performance, quality assurance, scalability, software engineering, spring boot, standards, swagger, testing, version control, web development, workflow]      - api-standards
---

# 📖 OpenAPI Docs & Standards

> API dokümantasyonu için OpenAPI (Swagger) 3.0 ve SpringDoc uzmanlık rehberi.

---

## 🚀 Spring Boot Integration (SpringDoc)

Spring Boot projelerinde OpenAPI dokümantasyonunu otomatize etmek için `springdoc-openapi` tercih edilir.

### Dependency (Maven)

```xml
<dependency>
    <groupId>org.springdoc</groupId>
    <artifactId>springdoc-openapi-starter-webmvc-ui</artifactId>
    <version>2.3.0</version>
</dependency>
```

### Access URLs

- **Swagger UI**: `http://server:port/context-path/swagger-ui.html`
- **OpenAPI JSON**: `http://server:port/context-path/v3/api-docs`

---

## 🛠️ Implementation Example

### Controller Documentation

```java
@RestController
@RequestMapping("/api/books")
@Tag(name = "Book Management", description = "Operations for managing books")
public class BookController {

    @Operation(summary = "Get a book by ID", description = "Returns a single book object")
    @ApiResponses(value = {
        @ApiResponse(responseCode = "200", description = "Book found"),
        @ApiResponse(responseCode = "404", description = "Book not found")
    })
    @GetMapping("/{id}")
    public Book getBook(@PathVariable Long id) {
        return bookService.findById(id);
    }
}
```

### Schema Documentation

```java
@Schema(description = "Book Entity")
public class Book {
    
    @Schema(description = "Unique ID of the book", example = "1")
    private Long id;
    
    @NotBlank
    @Schema(description = "Title of the book", example = "The Great Gatsby")
    private String title;
}
```

---

## 🔧 Workflow

> **Kaynak:** [SpringDoc Official Documentation](https://springdoc.org/)

### Aşama 1: Configuration
- [ ] **Dependency**: `springdoc-openapi-starter-webmvc-ui` (v2.x for Spring Boot 3) ekle.
- [ ] **Properties**: `springdoc.api-docs.path` ve `swagger-ui.path` değerlerini sabitle (custom path kullanıyorsan).
- [ ] **Platform**: WebMVC vs WebFlux ayrımına dikkat et (dependency farklı).

### Aşama 2: Documentation Layer
- [ ] **Controller**: `@Tag` ile grupla, `@Operation` ile her endpoint'i açıkla.
- [ ] **Models**: DTO'ları `@Schema` ile tanımla, validation anotasyonlarını (`@NotNull`) ekle (otomatik yansır).
- [ ] **Security**: Global security scheme (JWT/OAuth2) tanımla ve endpoint'lere `@SecurityRequirement` ekle.

### Aşama 3: Enhancement
- [ ] **Examples**: `@ExampleObject` kullanarak request/response body'ler için gerçekçi örnekler ver.
- [ ] **Error Handling**: Global Exception Handler'daki hata response formatlarını `@ApiResponse` ile dokümante et.
- [ ] **Generation**: CI/CD pipeline'ında `springdoc-openapi-maven-plugin` ile `openapi.json` üret.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | `/v3/api-docs` JSON dönüyor mu? |
| 2 | Swagger UI'da "Try it out" butonu çalışıyor mu (CORS/Auth sorunu var mı)? |
| 3 | Enum değerleri ve required alanlar dokümanda doğru görünüyor mu? |

---

## Best Practices

1. **Use descriptive operation summaries and descriptions**
2. **Document all response codes**
3. **Add examples to request/response bodies**
4. **Leverage JSR-303 validation annotations**
5. **Group related endpoints with @Tag**

---

*OpenAPI Docs v1.1 - Enhanced*
