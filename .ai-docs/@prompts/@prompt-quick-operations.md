# @prompt-quick-operations

**Purpose**: Minimal context loading prompt for quick file operations and simple tasks.

## 🎯 Copy-Paste Ready Prompt

```
CONTEXT LOADING REQUEST:

Please load the following essential AI context:
1. .ai-docs/.ai-docs/.ai-docs/@core/@conventions.md.md.md (MANDATORY - master rules)
2. .ai-docs/@conventions/@naming-conventions.md (quick naming reference)

VERIFICATION REQUIRED:
After loading, please confirm you understand:
- File naming conventions (PascalCase, kebab-case, snake_case usage)
- Directory organization rules and forbidden locations
- 1:1:1 relationship requirement (code-example ↔ blueprint ↔ test)
- Basic project structure (frontend-mcp/, tests/, scripts/, docs/)
- Validation command: python scripts/validate_ai_context.py --check-all

CONFIRMATION PROMPT:
Please respond with: "✅ CONTEXT LOADED - Ready for file operations. I understand naming conventions and directory rules."

TASK: [Describe your quick task here]
```

## 📋 Usage Instructions

### **When to Use This Prompt**
- File naming and organization
- Quick documentation updates
- Simple file moves or renames
- Basic validation checks
- Minor configuration changes

### **How to Use**
1. Copy the entire prompt above (including the triple backticks)
2. Paste at the start of a new AI chat session
3. Replace `[Describe your quick task here]` with your specific task
4. Wait for the ✅ confirmation before proceeding

### **Example Usage**
```
TASK: Help me rename some files to follow the correct naming conventions
```

```
TASK: Check if my new component files are in the right directories
```

```
TASK: Update the README.md with a new section about deployment
```

## 🔧 Customization Options

### **Add Specific Context (Optional)**
For slightly more complex tasks:
```
3. .ai-docs/@conventions/@project-structure.md (directory structure reference)
```

### **Add Recent Context (Optional)**
For continuity with recent work:
```
3. .ai-docs/chat-summaries/[recent-summary].md (recent changes context)
```

### **Modify Verification Points**
Add task-specific verification:
```
- Specific file type requirements
- Documentation standards
- Configuration file formats
- Git and version control considerations
```

## ✅ Expected AI Response

After using this prompt, expect:

```
✅ CONTEXT LOADED - Ready for file operations. I understand naming conventions and directory rules.

I have successfully loaded and understand:
- File naming conventions: PascalCase for components, kebab-case for blueprints, snake_case for tests
- Directory organization with frontend-mcp/, tests/, scripts/, docs/ structure
- Forbidden locations (no components at root, no tests outside tests/)
- 1:1:1 relationship requirement for components
- Basic project structure and file authority hierarchy
- Validation using python scripts/validate_ai_context.py --check-all

I'm ready to help with your quick task. What specific file operation or simple task would you like me to assist with?
```

## 🎯 When NOT to Use This Prompt

**Use more comprehensive prompts for:**
- Component creation (use @prompt-component-development.md)
- Architecture planning (use @prompt-architecture-work.md)
- Testing setup (use @prompt-testing-validation.md)
- Complex multi-step tasks (use @prompt-comprehensive-context.md)

## 🎯 Related Prompts

- **@prompt-component-development.md** - For component-related tasks
- **@prompt-testing-validation.md** - For testing-related tasks
- **@prompt-comprehensive-context.md** - For complex tasks
