---
description: The Unified Super-Workflow. Combines dynamic skill retrieval with rigorous engineering discipline. Run this for ANY complex coding request.
---

# Super Protokol v2: The Intelligent Engine

This workflow acts as a "Super-Agent," fusing the user's dynamic skill archive with high-discipline engineering methodologies.

## Phase 0: Dynamic Skill Acquisition (The "Protokol" Layer)

**Goal:** Equip the agent with domain-specific knowledge before starting work.

1.  **Analyze Prompt:** Extract key technologies (e.g., "React", "Python", "AWS") and intent.
2.  **Search Skills:**
    // turbo
    ```javascript
    // Search for relevant specialized skills
    mcp_skillport_search_skills({ query: "<extracted_keywords>" })
    ```
3.  **Load Skills:**
    *   Review search results.
    *   **Filter:** Select up to 3 high-relevance skills (Score > 0.8 is a good baseline).
    *   **Load:**
        // turbo
        ```javascript
        mcp_skillport_load_skill({ skill_id: "<selected_skill_id>" })
        ```
    *   *Note: If no highly relevant skills are found, proceed with general knowledge.*

---

## Phase 1: Strategic Alignment (The "Architect" Layer)

**Goal:** Resolve ambiguity and align on the "What" and "Why" before the "How".

1.  **Check Ambiguity:**
    *   Is the request fully specified (e.g., "Change button color to blue")? -> **SKIP to Phase 2.**
    *   Is the request vague (e.g., "Make the homepage better")? -> **PROCEED.**

2.  **The "One Question" Rule:**
    *   Do NOT dump a list of questions.
    *   Ask **ONE** clarifying question at a time.
    *   Wait for the user's answer.
    *   Refine the mental model.
    *   Repeat until the scope is clear.

3.  **Output:** A clear, mutually agreed-upon "Goal Statement".

---

## Phase 2: Implementation Planning (The "Manager" Layer)

**Goal:** Break the "Goal Statement" into executable, atomic micro-tasks.

1.  **Create/Update Task Artifact:**
    *   Use `task_boundary` to initialize the task.
    *   Create or update `task.md`.

2.  **Micro-Task Granularity:**
    *   Break work into tasks that take **2-5 minutes** each.
    *   **Bad:** "Implement Authentication"
    *   **Good:** "Create login form UI structure", "Add form validation logic", "Connect submit handler to API".

3.  **User Review (Checkpoint):**
    *   **STOP:** Before executing, show the plan to the user.
    *   Use `notify_user` to request approval for the plan.
    *   *Exception:* If the user explicitly gave "Auto-Run" authority or the task is trivial, you may proceed.

---

## Phase 3: Engineering Loop (The "Engineer" Layer)

**Goal:** Execute the plan with "Iron Law" discipline.

**The Loop:** For each item in the plan:

### A. The Iron Law of TDD
> **"No Production Code Without A Failing Test First"**

1.  **RED:** Write a minimal test case that fails.
    *   *Verify:* Run the test. It MUST fail.
2.  **GREEN:** Write the minimal code to make the test pass.
    *   *Verify:* Run the test. It MUST pass.
3.  **REFACTOR:** Clean up the code without changing behavior.
    *   *Verify:* Tests must stay green.

*Exceptions:* Scripts, config files, or UI visuals where automated testing is impossible. In these cases, define a **Manual Verification Step**.

### B. Verification Before Completion "Gate"

**Never** claim a task is "Done" or "Fixed" without fresh evidence.

1.  **Identify:** What command proves it works?
2.  **Run:** Execute the command.
3.  **Read:** Check the output carefully.
4.  **Claim:** Only report success if the output confirms it.

---

## Phase 4: Final Handoff

1.  **Self-Correction:** Did I learn something new about this codebase? (e.g., "Tests are in `specs/` folder, not `tests/`").
2.  **Memory:** If yes, update the memory bank.
3.  **Notify:** Inform the user the task is complete, citing the specific verification evidence.
