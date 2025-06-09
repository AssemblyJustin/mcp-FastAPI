# @prompt-testing-validation

**Purpose**: Complete context loading prompt for testing and validation tasks.

## 🎯 Copy-Paste Ready Prompt

```
CONTEXT LOADING REQUEST:

Please load the following AI context files in this exact order:
1. .ai-docs/@core/MASTER_CONVENTIONS.md (MANDATORY - master rules)
2. .ai-docs/@core/MASTER_TESTING.md (authoritative testing rules)
3. .ai-docs/@core/MASTER_ARCHITECTURE.md (architecture patterns)

VERIFICATION REQUIRED:
After loading, please confirm you understand:
- Test types: Unit (< 100ms), Integration (< 5s), Load (variable), Security (< 10s)
- Test locations: tests/unit/, tests/integration/, tests/load/, tests/security/
- Performance targets and quality gates (90%+ coverage)
- Blueprint → test relationship requirement
- MANDATORY test suites for ALL FastAPI components (routes, services, models)
- Test generation: python scripts/generate_test_suite.py --blueprint [name] --layer [type]
- API test generation: python scripts/generate_api_test_suite.py --endpoint [name] --type crud
- Blueprint validation: python scripts/validate_smart_blueprint.py --check-all
- FastAPI validation: python scripts/validate_fastapi_conventions.py --check-all
- Test output management: tests/outputs/ directory (gitignored)

CONFIRMATION PROMPT:
Please respond with: "✅ CONTEXT LOADED - Ready for FastAPI testing work. I understand the testing protocol and performance targets."

TESTING OPTIONS REQUEST:
After confirmation, provide a comprehensive outline of all available testing options including:

1. **Test Types Available**
   - Unit Tests (purpose, performance targets, when to use)
   - Integration Tests (purpose, performance targets, when to use)
   - E2E Tests (purpose, performance targets, when to use) - MANDATORY for UI components
   - Manual Tests (purpose and validation scenarios)

2. **Automation Scripts Available**
   - AI Test Generator (capabilities, usage, options)
   - AI Blueprint Generator (capabilities, usage, options)
   - AI Test Automation (full pipeline automation, modes)
   - Pipeline Validator (validation capabilities, reporting)

3. **Test Generation Options**
   - Individual component testing
   - Bulk test generation for all components
   - Category-specific testing (atoms, molecules, organisms)
   - Test type selection (unit only, e2e only, all types)
   - E2E-specific generation for missing UI component tests

4. **Validation & Reporting Options**
   - Pipeline validation and coverage checking
   - AI context validation and documentation verification
   - Performance benchmarking and quality metrics
   - Coverage reporting and gap analysis

5. **Quick Commands Reference**
   - Ready-to-use commands for each testing option
   - Explanations of what each command accomplishes
   - Examples for common testing scenarios

TASK: [Describe your testing task here]
```

## 📋 Usage Instructions

### **When to Use This Prompt**
- Creating test suites for components
- Setting up testing infrastructure
- Validating component pipelines
- Performance testing and optimization
- Test automation and CI/CD setup

### **How to Use**
1. Copy the entire prompt above (including the triple backticks)
2. Paste at the start of a new AI chat session
3. Replace `[Describe your testing task here]` with your specific task
4. Wait for the ✅ confirmation before proceeding

### **Example Usage**
```
TASK: Show me all available testing options and help me choose the right approach for testing my Button component
```

```
TASK: I need to understand what automation scripts are available and how to use them for comprehensive testing
```

```
TASK: Outline all test generation options and provide commands for bulk test creation across all components
```

```
TASK: Explain the validation and reporting capabilities available in the testing system
```

```
TASK: I want to see all quick commands for testing and understand what each one does
```

## 🔧 Customization Options

### **Add Component Context (Optional)**
For component-specific testing:
```
4. .ai-docs/@prompts/@component-creation.md (component workflow context)
```

### **Add Recent Testing Context (Optional)**
For continuity with recent testing work:
```
4. .ai-docs/chat-summaries/[recent-testing-summary].md (recent testing changes)
```

### **Modify Verification Points**
Add testing-specific verification:
```
- Specific testing frameworks (Pytest, Jest, Playwright)
- Coverage requirements and reporting
- Accessibility testing requirements
- Performance benchmarking standards
```

## ✅ Expected AI Response

After using this prompt, expect:

```
✅ CONTEXT LOADED - Ready for testing work. I understand the testing protocol and performance targets.

## 🧪 COMPREHENSIVE TESTING OPTIONS AVAILABLE

### 1. **Test Types Available**
- **Unit Tests** (< 100ms): Fast, isolated component logic testing
- **Integration Tests** (< 5s): Component interaction and blueprint pipeline testing
- **E2E Tests** (< 30s): Full browser-based user interaction testing - MANDATORY for UI components
- **Manual Tests**: Demo scripts and validation workflows

### 2. **Automation Scripts Available**
- **AI Test Generator**: `python scripts/ai_test_generator.py`
  - Generates unit, integration, and E2E tests automatically
  - Component-specific test patterns (button, input, modal, etc.)
  - Accessibility testing included by default
- **AI Blueprint Generator**: `python scripts/ai_blueprint_generator.py`
  - Creates missing blueprints for components automatically
  - Type-specific configurations and defaults
- **AI Test Automation**: `python scripts/ai_test_automation.py`
  - Full pipeline automation (--mode full)
  - Quick validation (--mode quick)
- **Pipeline Validator**: `python scripts/validate_pipeline.py`
  - Component coverage checking (--check-all)
  - Individual component validation (--component [name])

### 3. **Test Generation Options**
- **Individual**: `--component [ComponentName]` for single component
- **Bulk Generation**: `--generate all` for all missing tests
- **Category-Specific**: `--category components` or `--category hooks`
- **Type Selection**: `--generate unit|integration|e2e` for specific test types
- **E2E-Specific**: `--component [ComponentName] --generate e2e` for missing UI component E2E tests

### 4. **Validation & Reporting**
- **Pipeline Validation**: Complete component coverage analysis
- **AI Context Validation**: Documentation and context verification
- **Performance Benchmarking**: Speed and quality metrics
- **Coverage Reporting**: Gap analysis and recommendations

### 5. **Quick Commands Reference**
```bash
# Generate all missing tests
python scripts/ai_test_generator.py --generate all

# Generate E2E tests for specific component (MANDATORY for UI components)
python scripts/ai_test_generator.py --component Button --generate e2e

# Create missing blueprints
python scripts/ai_blueprint_generator.py

# Full automation pipeline
python scripts/ai_test_automation.py --mode full

# Quick system validation
python scripts/ai_test_automation.py --mode quick

# Validate specific component
python scripts/validate_pipeline.py --component components/atoms/Button

# Check all components
python scripts/validate_pipeline.py --check-all
```

I'm ready to work on your testing task. What specific testing option would you like to use?
```

## 🎯 Related Prompts

- **@prompt-component-development.md** - For component testing as part of development
- **@prompt-comprehensive-context.md** - For complex testing projects
- **@prompt-quick-operations.md** - For simple test fixes
