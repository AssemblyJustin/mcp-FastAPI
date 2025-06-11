# 🎯 Example Task: User Models Blueprint Creation

## **Task Assignment**
Using the Blueprint Creation Task Prompt Template to create a smart blueprint for User Pydantic Models.

## 📋 **Task Parameters**
**Blueprint Type**: `smart-pydantic-models`  
**Component Layer**: `models`  
**Resource Name**: `user`  
**Target Quality**: **10/10 Production Ready**

## 🚀 **Phase 1: Blueprint Creation** 📐

### **Task Execution**:
Create `backend-mcp/blueprints/models/smart-pydantic-models.json` with:

```json
{
  "id": "smart-models-user",
  "name": "Smart User Pydantic Models Generator",
  "description": "Production-ready Pydantic models for user management with comprehensive validation",
  "version": "1.0.0",
  "strategy": "embedded-template",
  
  "parameters": {
    "resourceName": {
      "type": "string",
      "required": true,
      "pattern": "^[a-z][a-z0-9_]*$",
      "description": "Resource name in snake_case (e.g., 'user', 'product')"
    },
    "modelName": {
      "type": "string",
      "required": true,
      "pattern": "^[A-Z][a-zA-Z0-9]*$",
      "description": "Model name in PascalCase (e.g., 'User', 'Product')"
    },
    "enableEmailValidation": {
      "type": "boolean",
      "default": true,
      "description": "Enable email field validation"
    },
    "enablePasswordValidation": {
      "type": "boolean",
      "default": true,
      "description": "Enable password strength validation"
    },
    "enableTimestamps": {
      "type": "boolean",
      "default": true,
      "description": "Include created_at and updated_at fields"
    }
  },
  
  "codeTemplate": {
    "language": "python",
    "executable": true,
    "testable": true,
    "content": "# Complete Pydantic models implementation with validation..."
  }
}
```

## 🧪 **Phase 2: MCP Testing**

### **Test Parameters**:
```python
test_params = {
    "resourceName": "user",
    "modelName": "User",
    "enableEmailValidation": True,
    "enablePasswordValidation": True,
    "enableTimestamps": True
}
```

### **Expected Output**:
- Generated `user_models.py` with UserCreate, UserUpdate, UserResponse models
- Complete validation rules and type hints
- Generation time < 1 second

## 🔍 **Phase 3: Targeted Peer Review**

### **Review Checklist**:

**Code Quality (Target: 10/10)**:
- [ ] Comprehensive docstrings for each model class
- [ ] Complete type hints with proper imports
- [ ] Validation examples in docstrings
- [ ] Clean, readable model structure

**Pydantic Best Practices (Target: 10/10)**:
- [ ] Proper field validation with Field() descriptors
- [ ] Custom validators for complex rules
- [ ] Model configuration (Config class)
- [ ] Serialization examples

**Validation Implementation (Target: 10/10)**:
- [ ] Email format validation
- [ ] Password strength requirements
- [ ] Field length constraints
- [ ] Custom business rule validation

**Security Implementation (Target: 10/10)**:
- [ ] Password field exclusion from serialization
- [ ] Input sanitization
- [ ] No sensitive data exposure
- [ ] Proper validation error messages

**Production Readiness (Target: 10/10)**:
- [ ] Performance optimized validation
- [ ] Error handling for validation failures
- [ ] Extensible model structure
- [ ] Database compatibility

## 🔧 **Phase 4: Implementation of Improvements**

### **Expected Enhancements**:
1. **Enhanced Validation**:
   ```python
   @validator('email')
   def validate_email(cls, v):
       # Custom email validation logic
   ```

2. **Security Features**:
   ```python
   password: str = Field(..., min_length=8, exclude=True)
   ```

3. **Comprehensive Documentation**:
   ```python
   """
   User creation model with comprehensive validation.
   
   This model validates all user input for account creation,
   including email format, password strength, and business rules.
   """
   ```

## 📊 **Success Metrics**

### **Quality Targets**:
- Overall Score: **10/10**
- Code Quality: **10/10**
- Validation Implementation: **10/10**
- Security: **10/10**
- Production Readiness: **10/10**

### **Performance Targets**:
- Generation Time: **< 1 second**
- Code Lines: **~150-200 lines**
- Validation Coverage: **100%**

## 🎯 **Final Deliverables**

1. **`smart-pydantic-models.json`** - Perfect 10/10 blueprint
2. **`generated_user_models.py`** - Production-ready models
3. **`user_models_quality_report.md`** - Peer review analysis
4. **`user_models_integration.md`** - Usage documentation

---

**This example demonstrates how the reusable task prompt template can be applied to any blueprint creation task, ensuring consistent 10/10 quality across all components.**
