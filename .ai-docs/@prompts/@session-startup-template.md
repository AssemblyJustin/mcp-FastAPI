# @session-startup-template

**AI Context**: Session initialization template for FastAPI development tasks.

## 🚀 **Session Startup Checklist**

### **1. Context Loading (MANDATORY)**
```
□ Load: .ai-docs/@core/MASTER_CONVENTIONS.md (ALWAYS FIRST)
□ Load: .ai-docs/@core/MASTER_TESTING.md (testing protocols)
□ Load: .ai-docs/@core/MASTER_ARCHITECTURE.md (architecture patterns)
□ Load: .ai-docs/@prompts/@api-creation.md (API creation workflow)
□ Load: .ai-docs/NEW_TASK_LIST.md
□ Load: .ai-docs/PROGRESS_TRACKER.md
□ Confirm: "Context loaded successfully. Ready to proceed."
```

### **2. Session Planning**
```
□ Review current progress in .ai-docs/PROGRESS_TRACKER.md
□ Identify next phase/batch to work on
□ Estimate session scope (2-5 API endpoints recommended)
□ Confirm API types (routes vs services vs models)
□ Set session goals and time expectations
```

### **3. Workflow Selection**
```
For API Routes (.py):
□ Use: @prompt-api-creation.md workflow
□ Generate: Unit + Integration + Load + Security tests

For Services (.py):
□ Use: FastAPI service workflow
□ Generate: Unit + Integration tests

For Models (.py):
□ Use: Pydantic/SQLAlchemy model workflow
□ Generate: Unit tests + validation tests
```

## 📋 **Session Initialization Script**

### **AI Response Template**
```
🤖 **Session Initialized**

✅ **Context Loaded:**
- Conventions: ✅ Loaded
- Batch Creation Prompt: ✅ Loaded  
- Task List: ✅ Loaded
- Progress Tracker: ✅ Loaded

📊 **Current Progress:**
- Overall: [X]/200 components ([Y]%)
- Current Phase: [Phase Name]
- Next Batch: [Component List]

🎯 **Session Plan:**
- Target: [X] components
- Type: [React Components/Hooks/Utils]
- Estimated Time: [X] minutes
- Workflow: [Workflow Name]

🚀 **Ready to proceed with component creation?**
- Type 'yes' to start with first component
- Type 'plan' to modify session scope
- Type 'status' to review detailed progress
```

## 🎯 **Batch Selection Guidelines**

### **Phase 1: Layout Atoms (Start Here)**
```
Recommended Batch: All 7 components (simple atoms)
- Container, Box, Flex, Grid, Stack, Spacer, AspectRatio
- Estimated Time: 45-60 minutes
- Complexity: Low (basic layout components)
```

### **Phase 2: Molecules (After Phase 1)**
```
Recommended Batches:
Batch 2A: Forms (3-4 components)
- FormField, FormGroup, SearchBar, LoginForm
- Estimated Time: 60-90 minutes

Batch 2B: Cards (3-4 components)  
- Card, ProductCard, UserCard, ArticleCard
- Estimated Time: 60-90 minutes

Batch 2C: Navigation (3 components)
- Breadcrumb, Pagination, TabList
- Estimated Time: 45-75 minutes
```

### **Phase 3: Organisms (After Phase 2)**
```
Recommended Batches:
Batch 3A: Layout Organisms (2 components)
- AppLayout, DashboardLayout
- Estimated Time: 90-120 minutes

Batch 3B: Sections (2-3 components)
- HeroSection, FeatureSection, TestimonialSection
- Estimated Time: 90-120 minutes
```

### **Phase 4: Hooks (After Phase 3)**
```
Recommended Batches:
Batch 4A: State Hooks (4-5 hooks)
- useSessionStorage, useReducer, usePrevious, useDebounce
- Estimated Time: 60-90 minutes

Batch 4B: Effect Hooks (4-5 hooks)
- useClickOutside, useKeyPress, useWindowSize, useScroll
- Estimated Time: 60-90 minutes
```

## ⚡ **Quick Commands**

### **Start Session**
```
User: "Start Phase 1 batch"
AI: [Load context] → [Show session plan] → [Begin with Container component]
```

### **Continue Session**
```
User: "Continue with next component"
AI: [Update progress] → [Show next component] → [Begin creation workflow]
```

### **Check Progress**
```
User: "Show progress"
AI: [Display current statistics] → [Show completed components] → [Show next targets]
```

### **End Session**
```
User: "End session"
AI: [Update .ai-docs/PROGRESS_TRACKER.md] → [Show session summary] → [Recommend next session]
```

## 🎯 **Success Criteria Per Session**

### **Minimum Success**
- [ ] At least 1 component fully complete (code + blueprint + tests + validation)
- [ ] Progress tracker updated
- [ ] No validation errors
- [ ] All files follow naming conventions

### **Optimal Success**
- [ ] 3-7 components complete in single session
- [ ] All tests passing
- [ ] Performance targets met
- [ ] Ready for next session with clear plan

### **Session End Checklist**
- [ ] Update .ai-docs/PROGRESS_TRACKER.md with completed components
- [ ] Run final validation: `python scripts/validate_project_structure.py`
- [ ] Commit progress (if using version control)
- [ ] Plan next session scope and timing
