# @ai-loading-order

**AI Context**: Priority order for loading AI documentation files to ensure proper context.

## AI-First Loading Order (OPTIMIZED)

### Phase 1: Core AI Context (ALWAYS FIRST)
```
1. .ai-docs/.ai-docs/@core/@conventions.md.md.md - Master conventions (moved from root)
2. .ai-docs/.ai-docs/@core/@testing-protocol.md.md.md - Master testing rules (moved from root)
3. @core/@project-concept.md - AI-first philosophy (moved from root)
```

### Phase 2: Quick References
```
4. @conventions/@project-structure.md - Directory rules
5. @conventions/@naming-conventions.md - Naming rules
```

### Phase 3: Workflow Prompts (Task-Specific)
```
6. @prompts/[task-specific-prompt].md - Ready-to-use context loading prompts
7. @prompts/@component-creation.md - Component workflow details
8. @context/@mcp-architecture.md - System overview (as needed)
```

## File Hierarchy (AI-Optimized Authority Order)

### 1. AI Core Files (AUTHORITATIVE)
- `.ai-docs/.ai-docs/.ai-docs/@core/@conventions.md.md.md` - Master source of truth
- `.ai-docs/.ai-docs/.ai-docs/@core/@testing-protocol.md.md.md` - Master testing rules
- `.ai-docs/@core/@project-concept.md` - AI-first philosophy

### 2. AI Quick References (SUPPLEMENTARY)
- `.ai-docs/@conventions/` - Quick reference versions
- `.ai-docs/@context/` - Technical details
- `.ai-docs/@prompts/` - Workflow templates

### 3. Live Documentation (REFERENCE)
- `tests/README.md` - Current testing state
- `frontend-mcp/README.md` - Server documentation
- `docs/summaries/` - Human decision records
- `.ai-docs/chat-summaries/` - AI conversation records

## Token Management

### File Size Limits
- **@conventions files**: < 2000 tokens each
- **@context files**: < 3000 tokens each  
- **@prompts files**: < 1500 tokens each
- **Total context**: < 8000 tokens per session

### Loading Strategy
```
IF task == "component creation":
    load: .ai-docs/.ai-docs/@core/@conventions.md.md.md + @prompts/@component-creation.md
ELIF task == "testing":
    load: .ai-docs/.ai-docs/@core/@conventions.md.md.md + .ai-docs/.ai-docs/@core/@testing-protocol.md.md.md
ELIF task == "architecture review":
    load: @core/@project-concept.md + @context/@mcp-architecture.md
```

## Conflict Resolution Rules

### When Files Conflict:
1. **Root level files WIN** (.ai-docs/CONVENTIONS.md > @conventions/)
2. **Newer timestamps WIN** (check file dates)
3. **More specific files WIN** (task-specific > general)

### Update Protocol:
1. **Always update root files first**
2. **Then update AI context files**
3. **Validate consistency between versions**
4. **Document changes in chat-summaries/**

## AI Assistant Instructions

### Before ANY Action:
```
1. Load .ai-docs/.ai-docs/@core/@conventions.md.md.md (MANDATORY)
2. Use appropriate prompt from @prompts/ directory
3. Load task-specific context files as specified in prompt
4. Load relevant @context files if needed
5. WAIT FOR AI CONFIRMATION before proceeding
```

### Using Context Loading Prompts:
```
1. Choose appropriate prompt from @prompts/ directory based on task type
2. Copy complete prompt from the specific @prompt-[task-type].md file
3. Paste prompt at start of new chat session
4. Wait for ✅ confirmation response
5. Verify AI understanding matches expectations
6. Proceed with task only after confirmation
```

### Context Validation:
```
def validate_context():
    assert CONVENTIONS_md_loaded == True
    assert task_specific_prompt_loaded == True
    assert no_conflicting_rules == True
    assert total_tokens < 8000
```

### Error Handling:
```
IF context_conflict_detected:
    prioritize_root_level_files()
    log_conflict_in_chat_summaries()
    ask_user_for_clarification()
```

## File Maintenance

### Regular Updates:
- **Weekly**: Check for conflicts between root and AI files
- **After major changes**: Update all related AI context files
- **Before releases**: Validate entire AI context system

### Deprecation Protocol:
- Mark outdated files with `# DEPRECATED` header
- Move to `.ai-docs/archive/` directory
- Update references in other files
- Document in chat-summaries/

## Quality Assurance

### Context Loading Tests:
```bash
# Validate AI context system
python scripts/validate_ai_context.py --check-all
python scripts/validate_ai_context.py --check-conflicts
python scripts/validate_ai_context.py --check-token-limits
```

### Manual Validation:
- [ ] All referenced files exist
- [ ] No circular references
- [ ] Token limits respected
- [ ] Loading order makes sense
- [ ] Conflicts resolved properly
