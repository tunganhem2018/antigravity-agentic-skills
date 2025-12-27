<div align="center">

# 🚀 Antigravity Agentic Skills v6.0

### The Operating System for AI Coding Agents

[![Turkish](https://img.shields.io/badge/🇹🇷_Türkçe-Dokümantasyon-red?style=for-the-badge)](./README.tr.md)
[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)
[![Version](https://img.shields.io/badge/Version-6.0-success?style=for-the-badge)]()
[![Skills](https://img.shields.io/badge/Skills-138+-purple?style=for-the-badge)]()

<br/>

> **"If it's not written, it doesn't exist."** — *The Anti-Phantom Rule*

<br/>

**Transform your AI assistant into a specialized expert with 138+ skills, automatic context switching, and persistent memory.**

[Get Started](#-quick-start) • [Features](#-key-features) • [Skills](#-skills-library) • [Installation](#-installation)

</div>

---

## 🎯 What is Antigravity?

Antigravity is a **plug-and-play skill system** that supercharges your AI coding assistant. Instead of generic responses, your AI becomes a specialized expert that:

- 🧠 **Remembers context** across sessions with MCP Memory
- 🎯 **Auto-selects the right tools** based on your prompt
- 📚 **Loads specialized knowledge** for React, AWS, Security, and more
- ⚡ **Works instantly** - just prompt naturally, no commands needed

---

## ✨ Key Features

<table>
<tr>
<td width="50%">

### 🚀 Zero-Config Auto-Trigger

No initialization commands. No manual setup. Just start prompting.

```
You: "Create a React dashboard"

AI automatically:
✅ Detects "react" keyword
✅ Loads FullStackKit
✅ Activates react_expert skill
✅ Starts building
```

</td>
<td width="50%">

### 🧠 Persistent Memory

Your AI remembers decisions, preferences, and learnings across sessions.

```
Session 1: "Always use TypeScript"
Session 2: AI remembers and applies it

✅ Cross-session context
✅ Project-specific memory
✅ Learning from mistakes
```

</td>
</tr>
<tr>
<td width="50%">

### 📦 Smart Kit Selection

Automatic skill loading based on task context.

| You Say | AI Loads |
|---------|----------|
| "React component" | FullStackKit |
| "Docker deploy" | DevOpsKit |
| "Fix security bug" | SecurityKit |
| "Write prompt" | AIKit |

</td>
<td width="50%">

### 🌐 138+ Specialized Skills

Deep expertise in every major technology.

- **Frontend:** React, Vue, CSS, Tailwind
- **Backend:** Python, Node, APIs, Databases
- **DevOps:** AWS, Docker, Kubernetes, Terraform
- **AI/ML:** Prompt Engineering, RAG, LangChain

</td>
</tr>
</table>

---

## 🏗️ Architecture

```mermaid
graph LR
    subgraph "Your Prompt"
        A["🗣️ Natural Language"]
    end
    
    subgraph "Auto-Trigger Engine"
        B["🔍 Keyword Detection"]
        C["📦 Kit Selection"]
        D["🧠 Memory Check"]
    end
    
    subgraph "Skill Kits"
        E["🌐 FullStackKit"]
        F["☁️ DevOpsKit"]
        G["🤖 AIKit"]
        H["🛡️ SecurityKit"]
    end
    
    subgraph "Output"
        I["⚡ Expert Response"]
    end
    
    A --> B
    B --> C
    C --> D
    D --> E & F & G & H
    E & F & G & H --> I
    
    style A fill:#e1f5fe
    style I fill:#c8e6c9
    style E fill:#fff3e0
    style F fill:#f3e5f5
    style G fill:#fce4ec
    style H fill:#ffebee
```

---

## 📦 Skills Library

<table>
<tr>
<td align="center" width="20%">

### 🌐 FullStackKit
**Web & Mobile**

`react_expert`
`backend_api`
`database_design`
`typescript_advanced`
`python_pro`

</td>
<td align="center" width="20%">

### ☁️ DevOpsKit
**Infrastructure**

`aws_architect`
`docker_optimization`
`kubernetes_specialist`
`terraform_engineer`
`deploy_cicd`

</td>
<td align="center" width="20%">

### 🤖 AIKit
**LLM & Agents**

`prompt_engineering`
`rag_architecture`
`agent_orchestration`
`langchain_patterns`
`context_engineering`

</td>
<td align="center" width="20%">

### 🛡️ SecurityKit
**Audits & Auth**

`secops_core`
`auth_patterns`
`compliance_analyst`
`better_auth`

</td>
<td align="center" width="20%">

### 📋 ManagementKit
**Planning**

`project_management`
`scrum_master`
`docs_readme`
`roadmap_planner`

</td>
</tr>
</table>

---

## ⚡ Quick Start

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/vuralserhat86/antigravity-agentic-skills.git
```

### 2️⃣ Copy Skills to Your System

```bash
# Windows
copy skills\ %USERPROFILE%\.skillport\skills\

# macOS/Linux
cp -r skills/ ~/.skillport/skills/
```

### 3️⃣ Add GEMINI.md to Your AI's Rules

Copy `rules/GEMINI.md` content to your AI assistant's global rules.

### 4️⃣ Start Prompting! 🎉

```
"Create a React dashboard with authentication"
```

That's it! No initialization needed. The system auto-triggers.

---

## 🔄 How It Works

```mermaid
sequenceDiagram
    participant U as 👤 You
    participant A as 🤖 AI
    participant M as 🧠 Memory
    participant S as 📦 Skills
    
    U->>A: "Build a REST API"
    A->>M: Check AntigravityState
    M-->>A: Last Kit: FullStackKit
    A->>A: Detect keyword: "API"
    A->>S: Load backend_api skill
    S-->>A: Skill instructions loaded
    A->>U: Expert API implementation
    A->>M: Save learnings
```

---

## 🌟 Why Antigravity?

| Without Antigravity | With Antigravity |
|---------------------|------------------|
| ❌ Generic AI responses | ✅ Expert-level code |
| ❌ Forgets context each session | ✅ Persistent memory |
| ❌ Manual skill specification | ✅ Auto-detection |
| ❌ One-size-fits-all | ✅ 138+ specialized skills |
| ❌ "Initialize system..." | ✅ Just prompt naturally |

---

## 📜 License

MIT License - see [LICENSE](LICENSE) for details.

---

<div align="center">

**Built with ❤️ for the Agentic AI Community**

[⬆ Back to Top](#-antigravity-agentic-skills-v60)

</div>
