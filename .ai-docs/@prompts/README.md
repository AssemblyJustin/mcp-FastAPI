# AI Context Loading Prompts

**Purpose**: Ready-to-use context loading prompts for starting new AI chat sessions with proper context and verification.

## 🎯 Quick Start

1. **Choose the right prompt** for your task type
2. **Copy the entire prompt** from the appropriate file
3. **Paste at start of new AI chat** session
4. **Wait for ✅ confirmation** before proceeding

## 📁 Available Prompts

### **@prompt-component-development.md**
**Use for**: Creating React components, blueprints, and tests
**Context**: Core conventions + testing protocol + component workflow
**Confirmation**: "✅ CONTEXT LOADED - Ready for component development"

### **@prompt-architecture-work.md**
**Use for**: System planning, MCP extensions, structure optimization
**Context**: Core conventions + project concept + MCP architecture
**Confirmation**: "✅ CONTEXT LOADED - Ready for architecture work"

### **@prompt-testing-validation.md**
**Use for**: Test creation, validation, performance testing
**Context**: Core conventions + testing protocol + quick reference
**Confirmation**: "✅ CONTEXT LOADED - Ready for testing work"

### **@prompt-quick-operations.md**
**Use for**: File operations, naming, simple tasks
**Context**: Core conventions + naming conventions (minimal)
**Confirmation**: "✅ CONTEXT LOADED - Ready for file operations"

### **@prompt-comprehensive-context.md**
**Use for**: Complex multi-step projects, system-wide changes
**Context**: All core files + workflow + architecture + recent summaries
**Confirmation**: "✅ COMPREHENSIVE CONTEXT LOADED - Ready for complex tasks"

### **@prompt-continuation-session.md**
**Use for**: Continuing work from previous AI chat sessions
**Context**: Core conventions + recent chat summary + task-specific files
**Confirmation**: "✅ CONTINUATION CONTEXT LOADED - Ready to continue previous work"

## 🎯 Prompt Selection Guide

```
SIMPLE tasks (naming, quick fixes) → @prompt-quick-operations.md
COMPONENT CREATION → @prompt-component-development.md  
TESTING WORK → @prompt-testing-validation.md
ARCHITECTURE/PLANNING → @prompt-architecture-work.md
COMPLEX/MULTI-STEP → @prompt-comprehensive-context.md
CONTINUING WORK → @prompt-continuation-session.md
```

## 📋 How to Use Any Prompt

### **Step 1: Choose Prompt File**
Based on your task type, select the appropriate prompt file from the list above.

### **Step 2: Copy Complete Prompt**
Open the prompt file and copy the entire prompt (including the triple backticks).

### **Step 3: Customize if Needed**
- Replace `[Describe your task here]` with your specific task
- Add recent chat summaries for continuation work
- Add specific context files if needed

### **Step 4: Paste and Wait**
- Paste the prompt at the start of a new AI chat session
- Wait for the ✅ confirmation response
- Do NOT proceed until you get proper confirmation

### **Step 5: Verify Understanding**
Ensure the AI's confirmation includes the specific understanding points from the prompt.

## 🔧 Customization Examples

### **Adding Recent Context**
```
4. .ai-docs/chat-summaries/[recent-summary].md (recent relevant work)
```

### **Adding Specific Context**
```
For blueprint work:
+ .ai-docs/@context/@mcp-architecture.md (blueprint system details)

For validation work:
+ .ai-docs/@context/@ai-loading-order.md (context management)
```

### **Modifying Verification Points**
Add task-specific verification requirements to ensure AI understands your specific needs.

## ✅ Expected Response Format

All prompts should generate responses in this format:

```
✅ [SPECIFIC CONFIRMATION] - [Ready statement]

I have successfully loaded and understand:
- [Specific verification points from prompt]
- [Additional understanding demonstrated]
- [Relevant validation commands]

I'm ready to [proceed with specific task type].

Would you like me to [suggest next steps or ask clarifying questions]?
```

## 🚨 Important Notes

### **Always Wait for Confirmation**
- Do NOT describe your task until you see the ✅ confirmation
- Verify the AI's understanding matches your expectations
- Ask clarifying questions if confirmation seems incomplete

### **Use Correct Prompt for Task Type**
- Don't use comprehensive context for simple tasks
- Don't use quick operations for complex work
- Match prompt complexity to task complexity

### **Customize as Needed**
- Add recent chat summaries for continuity
- Include specific context files for specialized work
- Modify verification points for your specific requirements

## 🎯 Benefits of Using These Prompts

### **✅ Guaranteed Context Loading**
- No missed files or incomplete context
- Correct loading order every time
- Task-appropriate context selection

### **✅ Verified Understanding**
- AI must confirm specific knowledge
- Standardized confirmation format
- Quality gates before proceeding

### **✅ Consistent Experience**
- Same context loading across all AI assistants
- Predictable AI behavior and responses
- Reduced errors and misunderstandings

### **✅ Effortless Usage**
- Copy-paste ready prompts
- No manual file listing required
- Clear instructions and examples

## 🔄 Related Documentation

- **@component-creation.md** - Detailed component workflow guide
- **@context-loading-templates.md** - Original template collection (deprecated)
- **../chat-summaries/** - Recent AI conversation records
- **../@core/** - Authoritative AI context files
- **../@context/** - Technical architecture documentation

---

**Quick Reference**: For new AI chats, always start with an appropriate prompt from this directory!
