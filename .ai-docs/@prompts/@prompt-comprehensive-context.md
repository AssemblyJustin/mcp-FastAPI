# @prompt-comprehensive-context

**Purpose**: Complete context loading prompt for complex, multi-step tasks requiring full system understanding.

## 🎯 Copy-Paste Ready Prompt

```
CONTEXT LOADING REQUEST:

Please load the following comprehensive AI context in this exact order:

CORE (mandatory):
1. .ai-docs/@core/MASTER_CONVENTIONS.md (master rules)
2. .ai-docs/@core/MASTER_TESTING.md (testing requirements)
3. .ai-docs/@core/MASTER_ARCHITECTURE.md (architecture patterns)

WORKFLOW (task-specific):
4. .ai-docs/@prompts/@component-creation.md (component workflow)

ARCHITECTURE (system understanding):
5. .ai-docs/@context/@mcp-architecture.md (system overview)
6. .ai-docs/@context/@ai-loading-order.md (context management)

RECENT WORK (continuity):
7. .ai-docs/chat-summaries/2501071400_context_loading_templates.md (latest context system)
8. .ai-docs/chat-summaries/2501071330_ai_first_optimization.md (structure optimization)

VERIFICATION REQUIRED:
After loading, please confirm you understand:
- Complete blueprint → test workflow requirements
- Complete test suite requirement: unit + integration + load + security (ALL MANDATORY for FastAPI components)
- AI-first directory structure and file authority hierarchy
- Testing protocol with performance targets and quality gates
- MCP architecture including smart blueprint system and template engine
- Recent organizational changes and context loading optimizations
- All validation commands (validate_smart_blueprint.py, validate_ai_context.py, validate_fastapi_conventions.py)
- FastAPI-focused development approach

CONFIRMATION PROMPT:
Please respond with: "✅ COMPREHENSIVE CONTEXT LOADED - Ready for complex tasks. I have full understanding of the FastAPI MCP system, workflows, and recent changes."

TASK: [Describe your complex task here]
```

## 📋 Usage Instructions

### **When to Use This Prompt**
- Large-scale system changes
- Multi-component projects
- Architecture refactoring
- Complex feature development
- System optimization projects
- Cross-cutting concerns (testing, validation, documentation)

### **How to Use**
1. Copy the entire prompt above (including the triple backticks)
2. Paste at the start of a new AI chat session
3. Replace `[Describe your complex task here]` with your specific task
4. Wait for the ✅ confirmation before proceeding

### **Example Usage**
```
TASK: Implement a complete design system with 20+ components, including atoms, molecules, and organisms, with full testing and documentation
```

```
TASK: Refactor the MCP server to support multiple frontend frameworks (React, Vue, Angular) with shared blueprint patterns
```

```
TASK: Create a comprehensive CI/CD pipeline with automated testing, validation, and deployment for the entire system
```

## 🔧 Customization Options

### **Add Project-Specific Context (Optional)**
For domain-specific work:
```
9. [project-specific-context].md (domain knowledge, business requirements)
```

### **Add External Integration Context (Optional)**
For integration work:
```
9. [integration-documentation].md (API specs, external system docs)
```

### **Modify Recent Work Context**
Replace recent summaries with relevant ones:
```
7. .ai-docs/chat-summaries/[relevant-recent-work].md
8. .ai-docs/chat-summaries/[another-relevant-summary].md
```

## ✅ Expected AI Response

After using this prompt, expect:

```
✅ COMPREHENSIVE CONTEXT LOADED - Ready for complex tasks. I have full understanding of the OpinionatedMCP system, workflows, and recent changes.

I have successfully loaded and understand:
- Complete 4-step workflow: Code example → Blueprint → Test suite → Validation
- 1:1:1 relationship requirement across all components
- Complete test suite requirement: unit + integration + e2e (ALL MANDATORY for UI components)
- AI-first directory structure with .ai-docs/@core/ as authoritative source
- Testing protocol with performance targets (Unit < 100ms, Integration < 5s, E2E < 30s)
- Quality gates requiring 90%+ coverage and validation script success
- MCP architecture including py_server, blueprint system, and template engine
- Recent optimizations including context loading templates and AI-first structure
- All validation commands and automation scripts (including ai_test_generator.py for E2E tests)
- Project philosophy emphasizing AI-first development and optimization

I'm ready to tackle your complex task with full system understanding. Would you like me to start by breaking down the task into phases or analyzing the current system state?
```

## 🎯 Task Breakdown Approach

After confirmation, the AI should help you:

1. **Analyze Scope**: Break complex task into manageable phases
2. **Plan Architecture**: Design approach considering system constraints
3. **Identify Dependencies**: Map out component and system dependencies
4. **Create Timeline**: Suggest implementation order and milestones
5. **Validate Approach**: Check against system conventions and best practices

## 🎯 Related Prompts

- **@prompt-component-development.md** - For individual component work within the project
- **@prompt-architecture-work.md** - For architecture-focused aspects
- **@prompt-testing-validation.md** - For testing-focused aspects
- **@prompt-continuation-session.md** - For follow-up sessions on the same project
