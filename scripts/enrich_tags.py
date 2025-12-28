import os
import re

SKILLS_DIR = os.path.expanduser("~/.skillport/skills")

# Map of skill_name -> [new_tags]
ENRICHMENT_MAP = {
    "accessibility_testing": ["wcag", "a11y", "screen reader", "aria", "compliance"],
    "audience_intelligence": ["analytics", "user segments", "demographics", "behavior", "market research"],
    "canvas_design": ["html5 canvas", "webgl", "fabricjs", "drawing", "graphics"],
    "cold_email": ["outreach", "sales", "copywriting", "email marketing", "lead gen"],
    "competitor_intelligence": ["market analysis", "benchmarking", "strategy", "swot", "rivals"],
    "content_strategist": ["copywriting", "seo", "blogging", "editorial calendar", "storytelling"],
    "database_migration": ["schema change", "flyway", "liquibase", "seed data", "version control"],
    "data_transform": ["etl", "pipeline", "pandas", "json manipulation", "normalization"],
    "data_visualization": ["charts", "d3", "victory", "recharts", "dashboard"],
    "docx": ["word", "office", "document automation", "report generation", "xml"],
    "drizzle_orm": ["typescript orm", "sql builder", "database schema", "migrations", "type-safety"],
    "error_handling": ["try-catch", "sentry", "logging", "exceptions", "debugging"],
    "form_builder": ["react-hook-form", "zod", "validation", "inputs", "forms"],
    "huggingface_transformers": ["nlp", "bert", "gpt", "models", "inference"],
    "image_enhancer": ["processing", "opencv", "filters", "upscaling", "optimization"],
    "llm_evaluation": ["benchmarking", "accuracy", "hallucination check", "testing", "metrics"],
    "mcp_server_developer": ["protocol", "json-rpc", "tool-use", "server", "integration"],
    "message_queues": ["rabbitmq", "kafka", "sqs", "async", "event bus"],
    "microservices_patterns": ["saga", "circuit breaker", "api gateway", "distributed systems", "service mesh"],
    "mongodb_usage": ["nosql", "mongoose", "aggregation", "documents", "sharding"],
    "nestjs_specialist": ["typescript", "backend framework", "modules", "dependency injection", "decorators"],
    "opus_4_5_migration": ["legacy upgrade", "refactoring", "compatibility", "versioning", "migration"],
    "payment_integration": ["stripe", "paypal", "checkout", "transaction", "billing"],
    "pdf": ["generation", "parsing", "layout", "report", "document"],
    "performance_engineering": ["optimization", "latency", "throughput", "profiling", "scalability"],
    "platform_engineering": ["infrastructure as code", "developer experience", "internal tools", "kubernetes", "cloud"],
    "pptx": ["powerpoint", "slides", "presentation", "automation", "office"],
    "prisma_orm": ["schema", "database", "typescript", "migrations", "client"],
    "project_bootstrapper": ["scaffold", "setup", "init", "boilerplate", "generator"],
    "python_data_stack": ["pandas", "numpy", "scipy", "jupyter", "analysis"],
    "rag_implementation": ["retrieval augmented generation", "vector db", "embedding", "context", "search"],
    "responsive_design": ["mobile-first", "breakpoints", "media queries", "css grid", "flexbox"],
    "seo_technical": ["crawling", "indexing", "sitemap", "meta tags", "schema.org"],
    "skill_creator": ["meta-skill", "instruction writing", "prompt engineering", "agent training", "definition"],
    "skill_evaluator": ["quality check", "audit", "review", "metrics", "standards"],
    "state_management": ["redux", "context api", "signals", "observables", "store"],
    "stripe_integration": ["payments", "webhooks", "billing", "subscriptions", "checkout"],
    "supabase_patterns": ["backend-as-a-service", "auth", "realtime", "postgres", "edge functions"],
    "vitest_runner": ["unit testing", "jest compatible", "vite", "assertions", "mocking"],
    "webapp_testing": ["playwright", "cypress", "e2e", "integration", "browser"],
    "xlsx": ["excel", "spreadsheet", "csv", "data export", "reporting"],
    "zustand_state": ["lightweight state", "react hooks", "store", "state management", "minimalist"]
}

def enrich_skill(skill_name, new_tags):
    skill_file = os.path.join(SKILLS_DIR, skill_name, "SKILL.md")
    if not os.path.exists(skill_file):
        print(f"Skipping {skill_name}: File not found")
        return

    with open(skill_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find tags section
    # Matches "tags: [a, b]" or list format
    # We will simply REPLACE the tags line with the new enriched list
    
    # Format tags as [tag1, tag2, tag3]
    tags_str = ", ".join(new_tags)
    replacement = f"tags: [{tags_str}]"
    
    # Regex to find tags line
    # Matches "tags: [...]" or "tags:\n  - a"
    # For now, let's assume standard "tags: [...]" produced by our previous heal script
    # If not found, we append to metadata
    
    new_content = re.sub(r'tags:\s*\[.*?\]', replacement, content, flags=re.DOTALL)
    
    # If no change (maybe it was list format), try list format regex
    if new_content == content:
         # Try matching multiline tags
         new_content = re.sub(r'tags:\s*\n(\s*-\s+.*\n)+', f"{replacement}\n", content)

    if new_content != content:
        with open(skill_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Enriched {skill_name}")
    else:
        print(f"Failed to match tags pattern for {skill_name}")

def main():
    print(f"Enriching {len(ENRICHMENT_MAP)} skills...")
    for skill_name, tags in ENRICHMENT_MAP.items():
        enrich_skill(skill_name, tags)
    print("Enrichment complete.")

if __name__ == "__main__":
    main()
