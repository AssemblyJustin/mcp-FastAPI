# 🎯 Blueprint Creation Task Prompt Template

## **Task Objective**
Create a production-ready smart blueprint for FastAPI MCP that generates 10/10 quality code through iterative development and peer review.

## 📋 **Task Parameters**
**Blueprint Type**: `{BLUEPRINT_TYPE}` (e.g., "smart-crud-route", "smart-auth-middleware", "smart-pydantic-models")  
**Component Layer**: `{COMPONENT_LAYER}` (e.g., "routes", "services", "models", "middleware")  
**Resource Name**: `{RESOURCE_NAME}` (e.g., "user", "product", "order")  
**Target Quality**: **10/10 Production Ready**

## 🚀 **4-Phase Task Execution**

### **Phase 1: Blueprint Creation** 📐
**Objective**: Write a high-quality smart blueprint with embedded templates

**Requirements**:
1. **Follow Smart Blueprint Architecture**:
   ```json
   {
     "id": "smart-{COMPONENT_LAYER}-{RESOURCE_NAME}",
     "name": "{HUMAN_READABLE_NAME}",
     "description": "Production-ready {COMPONENT_LAYER} for {RESOURCE_NAME} management",
     "version": "1.0.0",
     "strategy": "embedded-template"
   }
   ```

2. **Include Comprehensive Parameters**:
   - Required parameters with validation patterns
   - Optional parameters with sensible defaults
   - Boolean flags for feature toggles
   - Type validation and descriptions

3. **Embed Complete Code Template**:
   - Full FastAPI implementation in `codeTemplate.content`
   - Proper imports and dependencies
   - Comprehensive error handling
   - Security best practices
   - Performance optimizations

4. **Add Quality Features**:
   - Detailed docstrings with examples
   - OpenAPI documentation with response examples
   - Structured logging integration
   - Request ID tracking
   - Role-based authorization
   - Rate limiting support

5. **Include Test Template**:
   - Comprehensive pytest test suite
   - Unit and integration test scenarios
   - Mock implementations
   - Edge case coverage

**Deliverable**: Complete smart blueprint JSON file at `backend-mcp/blueprints/{COMPONENT_LAYER}/smart-{BLUEPRINT_TYPE}.json`

### **Phase 2: MCP Testing** 🧪
**Objective**: Test the blueprint using the MCP simulation process

**Requirements**:
1. **Create Test Parameters**:
   ```python
   test_params = {
       "resourceName": "{RESOURCE_NAME}",
       "modelName": "{MODEL_NAME}",
       "authRequired": True,
       "routePrefix": "/api/v1",
       # Add blueprint-specific parameters
   }
   ```

2. **Run MCP Simulation**:
   - Load blueprint using MCP processor
   - Validate all parameters
   - Generate code with test parameters
   - Measure generation time and quality metrics

3. **Validate Generated Output**:
   - Syntax validation (Python/FastAPI compliance)
   - Import resolution check
   - Type hint verification
   - Security pattern validation

4. **Performance Metrics**:
   - Generation time < 1 second
   - Code length and complexity
   - Template substitution accuracy
   - Error-free generation

**Deliverable**: Generated code file and performance metrics report

### **Phase 3: Targeted Peer Review** 🔍
**Objective**: Conduct comprehensive peer review targeting 10/10 quality score

**Review Criteria** (Each must score 10/10):

1. **Code Quality (Target: 10/10)**:
   - [ ] Comprehensive docstrings with Args, Returns, Raises, Examples
   - [ ] Complete type hints throughout
   - [ ] Consistent naming conventions
   - [ ] Clean, readable code structure
   - [ ] No code smells or anti-patterns

2. **FastAPI Best Practices (Target: 10/10)**:
   - [ ] Complete OpenAPI documentation with examples
   - [ ] Proper HTTP status codes and error responses
   - [ ] Response model specifications
   - [ ] Input validation with detailed descriptions
   - [ ] Endpoint summaries and descriptions

3. **Error Handling (Target: 10/10)**:
   - [ ] Request ID tracking for error correlation
   - [ ] Structured logging with full context
   - [ ] Specific error messages with actionable details
   - [ ] Proper exception hierarchy
   - [ ] Graceful degradation patterns

4. **Security Implementation (Target: 10/10)**:
   - [ ] Role-based authorization checks
   - [ ] Rate limiting integration
   - [ ] Input validation and sanitization
   - [ ] Authentication enforcement
   - [ ] No security vulnerabilities

5. **Production Readiness (Target: 10/10)**:
   - [ ] Performance optimization (async/await, pagination)
   - [ ] Monitoring and observability hooks
   - [ ] Configuration management
   - [ ] Scalability considerations
   - [ ] Enterprise compliance

**Review Process**:
1. **Score each category** (1-10 scale)
2. **Identify specific gaps** preventing 10/10 score
3. **Provide actionable recommendations** with code examples
4. **Calculate overall score** (must be 10/10 to pass)

**Deliverable**: Detailed peer review report with specific improvement requirements

### **Phase 4: Implementation of Improvements** 🔧
**Objective**: Implement all peer review recommendations to achieve 10/10 score

**Requirements**:
1. **Address Each Review Item**:
   - Implement all recommendations from peer review
   - Enhance docstrings with comprehensive examples
   - Add complete OpenAPI documentation
   - Integrate structured logging and request tracking
   - Add role-based authorization and rate limiting

2. **Enhanced Template Features**:
   ```python
   # Example improvements
   - Add request_id = get_request_id(request)
   - Include comprehensive logging with context
   - Add role-based permission checks
   - Implement rate limiting decorators
   - Enhanced error messages with request IDs
   ```

3. **Validation Enhancements**:
   - Add complex conditional logic support
   - Include advanced parameter validation
   - Add security pattern enforcement
   - Implement performance optimization patterns

4. **Re-test and Validate**:
   - Re-run MCP simulation with enhanced blueprint
   - Verify all peer review items are addressed
   - Confirm 10/10 score achievement
   - Test edge cases and error scenarios

**Deliverable**: Enhanced blueprint achieving 10/10 quality score

## 📊 **Success Criteria**

### **Phase 1 Success**: Blueprint Creation ✅
- [ ] Complete smart blueprint JSON file created
- [ ] All required parameters defined with validation
- [ ] Embedded template includes full implementation
- [ ] Test template provides comprehensive coverage

### **Phase 2 Success**: MCP Testing ✅
- [ ] Blueprint loads and validates successfully
- [ ] Code generation completes in < 1 second
- [ ] Generated code is syntactically correct
- [ ] All template variables substituted properly

### **Phase 3 Success**: Peer Review ✅
- [ ] Comprehensive review completed for all 5 categories
- [ ] Specific gaps identified with actionable recommendations
- [ ] Clear path to 10/10 score documented
- [ ] Code examples provided for improvements

### **Phase 4 Success**: Final Implementation ✅
- [ ] All peer review recommendations implemented
- [ ] 10/10 score achieved across all categories
- [ ] Enhanced blueprint generates perfect code
- [ ] Production-ready component delivered

## 🎯 **Final Deliverables**

1. **Enhanced Smart Blueprint** (`smart-{BLUEPRINT_TYPE}.json`)
   - 10/10 quality score
   - Production-ready embedded template
   - Comprehensive parameter validation
   - Complete test coverage

2. **Generated Code Sample** (`generated_{RESOURCE_NAME}_{COMPONENT_LAYER}.py`)
   - Perfect 10/10 implementation
   - Enterprise-grade quality
   - Zero modifications needed for production

3. **Quality Assessment Report** (`{BLUEPRINT_TYPE}_quality_report.md`)
   - Detailed peer review analysis
   - Before/after comparison
   - Performance metrics
   - Production readiness confirmation

4. **Integration Documentation** (`{BLUEPRINT_TYPE}_integration.md`)
   - Usage instructions
   - Parameter reference
   - Integration examples
   - Best practices guide

## 🏆 **Quality Gates**

**Gate 1**: Blueprint validates and generates code ✅  
**Gate 2**: Generated code passes syntax and security checks ✅  
**Gate 3**: Peer review identifies path to 10/10 score ✅  
**Gate 4**: Final implementation achieves 10/10 across all categories ✅  

**Final Gate**: **Production deployment ready with zero additional work required** ✅

---

**Task Status**: Ready for execution  
**Expected Duration**: 2-4 hours per blueprint  
**Quality Target**: 10/10 production-ready code generation  
**Success Metric**: Zero additional work required for production deployment
