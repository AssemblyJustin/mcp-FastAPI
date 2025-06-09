# @prompt-architecture-work

**Purpose**: Complete context loading prompt for system architecture and planning tasks.

## 🎯 Copy-Paste Ready Prompt

```
CONTEXT LOADING REQUEST:

Please load the following AI context files in this exact order:
1. .ai-docs/.ai-docs/.ai-docs/@core/@conventions.md.md.md (MANDATORY - master rules)
2. .ai-docs/@core/@project-concept.md (AI-first philosophy)
3. .ai-docs/@context/@mcp-architecture.md (system overview)
4. .ai-docs/chat-summaries/2501071330_ai_first_optimization.md (recent structure changes)

VERIFICATION REQUIRED:
After loading, please confirm you understand:
- AI-first directory structure with .ai-docs/@core/ priority
- MCP server architecture and blueprint system
- Template engine and code generation workflow
- Current project organization and recent optimizations
- File authority hierarchy (@core > @conventions > live docs)
- Blueprint-to-code-example 1:1 relationship
- Testing integration requirements
- Validation command: python scripts/validate_ai_context.py --check-all

CONFIRMATION PROMPT:
Please respond with: "✅ CONTEXT LOADED - Ready for architecture work. I understand the AI-first structure and MCP system architecture."

TASK: [Describe your architecture/system task here]
```

## 📋 Usage Instructions

### **When to Use This Prompt**
- Planning MCP server extensions
- Designing new blueprint categories
- Architecting component systems
- Optimizing project structure
- Planning AI context improvements

### **How to Use**
1. Copy the entire prompt above (including the triple backticks)
2. Paste at the start of a new AI chat session
3. Replace `[Describe your architecture/system task here]` with your specific task
4. Wait for the ✅ confirmation before proceeding

### **Example Usage**
```
TASK: Plan extensions to the MCP server to support Vue.js components in addition to React
```

```
TASK: Design a new blueprint category for backend API services and database schemas
```

```
TASK: Optimize the AI context loading system for better performance and token efficiency
```

## 🔧 Customization Options

### **Add Recent Architecture Context (Optional)**
For continuity with recent architecture work:
```
5. .ai-docs/chat-summaries/[recent-architecture-summary].md (recent architecture changes)
```

### **Add Specific Technical Context (Optional)**
For deep technical work:
```
5. .ai-docs/@context/@ai-loading-order.md (context management details)
```

### **Modify Verification Points**
Add architecture-specific verification:
```
- Specific technology stack understanding
- Integration patterns and constraints
- Performance and scalability requirements
- Security and compliance considerations
```

## ✅ Expected AI Response

After using this prompt, expect:

```
✅ CONTEXT LOADED - Ready for architecture work. I understand the AI-first structure and MCP system architecture.

I have successfully loaded and understand:
- AI-first directory structure with .ai-docs/@core/ as authoritative source
- MCP server architecture with py_server, blueprints, and code-examples
- Template engine workflow and code generation process
- Blueprint system with 1:1 relationship to code examples
- Recent optimizations including AI context loading improvements
- File authority hierarchy and validation protocols
- Testing integration requirements across the system
- Validation using python scripts/validate_ai_context.py --check-all

I'm ready to work on your architecture task. Would you like me to start by analyzing the current system or planning the specific changes you need?
```

## 🎯 Related Prompts

- **@prompt-comprehensive-context.md** - For complex architecture projects
- **@prompt-component-development.md** - For component architecture
- **@prompt-testing-validation.md** - For testing architecture
