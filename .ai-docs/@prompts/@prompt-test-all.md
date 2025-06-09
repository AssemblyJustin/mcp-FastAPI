# @prompt-test-all

**Purpose**: Quick prompt to run all tests in the system with comprehensive coverage.

## 🎯 Copy-Paste Ready Prompt

```
CONTEXT LOADING REQUEST:

Please load the following AI context files:
1. .ai-docs/.ai-docs/.ai-docs/@core/@conventions.md.md.md (MANDATORY - master rules)
2. .ai-docs/.ai-docs/.ai-docs/@core/@testing-protocol.md.md.md (authoritative testing rules)

VERIFICATION REQUIRED:
After loading, please confirm you understand:
- Test types: Unit (< 100ms), Integration (< 5s), E2E (< 30s), Manual
- Test locations: tests/unit/, tests/integration/, tests/e2e/, tests/manual/
- Performance targets and quality gates (90%+ coverage)
- MANDATORY E2E tests for ALL UI components (atoms, molecules, organisms)

CONFIRMATION PROMPT:
Please respond with: "✅ CONTEXT LOADED - Ready to run all tests."

TASK: Run all tests in the system using the comprehensive test automation pipeline. Execute the following commands in sequence and report results:

1. **Full Test Automation Pipeline**
   ```bash
   python scripts/ai_test_automation.py --mode full
   ```

2. **Generate Any Missing Tests**
   ```bash
   python scripts/ai_test_generator.py --generate all
   ```

3. **Validate Complete Pipeline**
   ```bash
   python scripts/validate_pipeline.py --check-all
   ```

4. **AI Context Validation**
   ```bash
   python scripts/validate_ai_context.py --check-all
   ```

5. **Run All Test Suites**
   - Unit tests: `npm test -- --testPathPattern=tests/unit`
   - Integration tests: `npm test -- --testPathPattern=tests/integration`
   - E2E tests: `npm test -- --testPathPattern=tests/e2e`

Please execute each command, report the results, and provide a summary of:
- Total tests run
- Pass/fail counts
- Coverage percentages
- Any issues found
- Recommendations for fixes
```

## 📋 Usage Instructions

### **When to Use This Prompt**
- Running comprehensive test suite validation
- Checking system health after changes
- Preparing for deployment or releases
- Validating all components have proper test coverage
- Ensuring all automation scripts are working

### **How to Use**
1. Copy the entire prompt above (including the triple backticks)
2. Paste into a new AI chat session
3. Wait for the ✅ confirmation
4. AI will execute all test commands and provide comprehensive results

### **Expected Output**
The AI will:
- Load required context files
- Execute all test automation scripts
- Run all test suites (unit, integration, E2E)
- Validate pipeline completeness
- Provide detailed results summary
- Recommend any necessary fixes

## 🔧 Quick Alternative Commands

If you need to run specific test categories only:

### **Unit Tests Only**
```bash
python scripts/ai_test_generator.py --generate unit
npm test -- --testPathPattern=tests/unit
```

### **E2E Tests Only**
```bash
python scripts/ai_test_generator.py --generate e2e
npm test -- --testPathPattern=tests/e2e
```

### **Quick Validation Only**
```bash
python scripts/ai_test_automation.py --mode quick
python scripts/validate_pipeline.py --check-all
```

## ✅ Expected AI Response

After using this prompt, expect:

```
✅ CONTEXT LOADED - Ready to run all tests.

## 🧪 EXECUTING COMPREHENSIVE TEST SUITE

### 1. **Full Test Automation Pipeline**
[Command execution results...]

### 2. **Missing Test Generation**
[Results of test generation...]

### 3. **Pipeline Validation**
[Validation results...]

### 4. **AI Context Validation**
[Context validation results...]

### 5. **Test Suite Execution**
[Unit/Integration/E2E test results...]

## 📊 COMPREHENSIVE TEST RESULTS SUMMARY
- **Total Tests**: [number]
- **Passed**: [number] 
- **Failed**: [number]
- **Coverage**: [percentage]
- **Performance**: All tests within targets (Unit < 100ms, Integration < 5s, E2E < 30s)

## 🔧 RECOMMENDATIONS
[Any issues found and recommended fixes...]
```

## 🎯 Related Prompts

- **@prompt-testing-validation.md** - For detailed testing setup and options
- **@prompt-component-development.md** - For component-specific testing
- **@prompt-quick-operations.md** - For simple test fixes
