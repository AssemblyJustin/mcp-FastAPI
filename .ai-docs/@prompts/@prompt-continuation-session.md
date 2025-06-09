# @prompt-continuation-session

**Purpose**: Context loading prompt for continuing work from previous AI chat sessions.

## 🎯 Copy-Paste Ready Prompt

```
CONTEXT LOADING REQUEST:

Please load context for continuing previous work:
1. .ai-docs/@core/MASTER_CONVENTIONS.md (MANDATORY - master rules)
2. .ai-docs/@core/MASTER_TESTING.md (testing protocols)
3. .ai-docs/@core/MASTER_ARCHITECTURE.md (architecture patterns)
4. .ai-docs/chat-summaries/[REPLACE-WITH-MOST-RECENT-SUMMARY].md (previous session context)
5. [ADD-SPECIFIC-FILES-BASED-ON-PREVIOUS-WORK-TYPE]

VERIFICATION REQUIRED:
After loading, please confirm you understand:
- Current project state and recent changes from previous session
- Previous session outcomes and decisions made
- Continuation requirements and next steps identified
- Relevant validation commands for current work
- Any blockers or issues identified in previous session

CONFIRMATION PROMPT:
Please respond with: "✅ CONTINUATION CONTEXT LOADED - Ready to continue previous FastAPI work. I understand the current state and previous session outcomes."

TASK: [Describe continuation task here]
```

## 📋 Usage Instructions

### **When to Use This Prompt**
- Continuing work from a previous AI chat session
- Following up on incomplete tasks
- Building on previous decisions or implementations
- Resuming complex multi-session projects

### **How to Use**
1. **Identify the most recent relevant chat summary** from `.ai-docs/chat-summaries/`
2. **Replace `[REPLACE-WITH-MOST-RECENT-SUMMARY]`** with the actual filename
3. **Add specific context files** based on the type of work you're continuing
4. **Copy and paste** the complete prompt
5. **Wait for confirmation** before proceeding

### **Customization Examples**

#### **Continuing Component Development**
```
CONTEXT LOADING REQUEST:

Please load context for continuing previous work:
1. .ai-docs/.ai-docs/.ai-docs/@core/@conventions.md.md.md (MANDATORY - master rules)
2. .ai-docs/chat-summaries/2501071400_context_loading_templates.md (previous session context)
3. .ai-docs/.ai-docs/.ai-docs/@core/@testing-protocol.md.md.md (testing requirements)
4. .ai-docs/@prompts/@component-creation.md (component workflow)

TASK: Continue working on the SearchBar molecule component - implement the remaining test suite
```

#### **Continuing Architecture Work**
```
CONTEXT LOADING REQUEST:

Please load context for continuing previous work:
1. .ai-docs/.ai-docs/.ai-docs/@core/@conventions.md.md.md (MANDATORY - master rules)
2. .ai-docs/chat-summaries/2501071330_ai_first_optimization.md (previous session context)
3. .ai-docs/@core/@project-concept.md (AI-first philosophy)
4. .ai-docs/@context/@mcp-architecture.md (system overview)

TASK: Continue the MCP server extension planning - finalize the Vue.js component support design
```

#### **Continuing Testing Work**
```
CONTEXT LOADING REQUEST:

Please load context for continuing previous work:
1. .ai-docs/.ai-docs/.ai-docs/@core/@conventions.md.md.md (MANDATORY - master rules)
2. .ai-docs/chat-summaries/[recent-testing-summary].md (previous session context)
3. .ai-docs/.ai-docs/.ai-docs/@core/@testing-protocol.md.md.md (testing requirements)

TASK: Continue setting up the CI/CD pipeline - implement the automated validation steps
```

## 🔧 Finding the Right Chat Summary

### **Recent Chat Summaries (Most Likely)**
```
.ai-docs/chat-summaries/
├── 2501071400_context_loading_templates.md (context system work)
├── 2501071345_chat_summaries_organization.md (documentation organization)
├── 2501071330_ai_first_optimization.md (structure optimization)
└── 2501071300_ai_docs_improvements.md (AI docs improvements)
```

### **How to Choose**
1. **Look at timestamps** - Use the most recent relevant summary
2. **Match topic** - Choose summary that relates to your continuation work
3. **Check content** - Skim the summary to ensure it covers your previous work

## ✅ Expected AI Response

After using this prompt, expect:

```
✅ CONTINUATION CONTEXT LOADED - Ready to continue previous work. I understand the current state and previous session outcomes.

I have successfully loaded and understand:
- Current project state from [specific summary loaded]
- Previous session outcomes: [specific outcomes from the summary]
- Decisions made and their rationale
- Next steps identified in the previous session
- Current blockers or considerations: [any issues noted]
- Relevant validation commands for continuing the work

Based on the previous session, I understand we were working on [specific previous work] and the next steps are [specific next steps]. I'm ready to continue where we left off.

Would you like me to [suggest specific continuation actions based on previous session]?
```

## 🎯 Best Practices

### **1. Always Reference Recent Work**
- Use the most recent relevant chat summary
- Include specific context files from previous work type
- Mention any blockers or decisions from previous session

### **2. Be Specific About Continuation**
```
TASK: Continue working on [specific item] - [specific next step]
```

### **3. Validate Previous Work**
Ask the AI to confirm understanding of:
- What was completed in the previous session
- What decisions were made and why
- What the next steps should be

### **4. Update Context as Needed**
If the previous session created new files or changed structure:
```
4. [new-file-created-in-previous-session].md (new context from previous work)
```

## 🎯 Related Prompts

- **@prompt-comprehensive-context.md** - For complex continuation projects
- **@prompt-component-development.md** - For continuing component work
- **@prompt-architecture-work.md** - For continuing architecture work
- **@prompt-testing-validation.md** - For continuing testing work
