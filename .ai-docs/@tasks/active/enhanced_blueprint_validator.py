#!/usr/bin/env python3
"""
Enhanced Blueprint Validator
Implements the critical enhancements identified in the peer review
"""

import json
import re
from typing import Dict, Any, List, Optional
from dataclasses import dataclass
from enum import Enum


class ValidationLevel(Enum):
    PASS = "PASS"
    WARNING = "WARNING"
    FAIL = "FAIL"


@dataclass
class CheckResult:
    """Result of a single validation check"""
    name: str
    level: ValidationLevel
    message: str
    details: Optional[str] = None


@dataclass
class ValidationReport:
    """Complete validation report"""
    blueprint_id: str
    overall_score: float
    checks: List[CheckResult]
    
    @property
    def passed(self) -> bool:
        return all(check.level != ValidationLevel.FAIL for check in self.checks)
    
    @property
    def warnings(self) -> List[CheckResult]:
        return [check for check in self.checks if check.level == ValidationLevel.WARNING]
    
    @property
    def failures(self) -> List[CheckResult]:
        return [check for check in self.checks if check.level == ValidationLevel.FAIL]


@dataclass
class QualityScore:
    """Quality assessment scores"""
    code_quality: int
    fastapi_practices: int
    error_handling: int
    security: int
    production_readiness: int
    
    @property
    def overall_score(self) -> float:
        return (self.code_quality + self.fastapi_practices + self.error_handling + 
                self.security + self.production_readiness) / 5


class AIDocsValidator:
    """Validates blueprints against @ai-docs standards"""
    
    def __init__(self):
        self.required_template_vars = [
            "{{modelName}}", "{{resourceName}}", "{{routePrefix}}"
        ]
        self.forbidden_patterns = [
            "hardcoded-credentials", "sql-injection-risk", "missing-error-handling"
        ]
        self.required_patterns = [
            "proper-typing", "error-handling", "status-codes", "documentation"
        ]
    
    def validate_blueprint(self, blueprint: Dict) -> ValidationReport:
        """Validate blueprint against @ai-docs standards"""
        checks = []
        
        # Core structure validation
        checks.extend(self._check_blueprint_structure(blueprint))
        
        # Naming conventions validation
        checks.extend(self._check_naming_conventions(blueprint))
        
        # FastAPI patterns validation
        checks.extend(self._check_fastapi_patterns(blueprint))
        
        # Quality requirements validation
        checks.extend(self._check_quality_requirements(blueprint))
        
        # Template validation
        checks.extend(self._check_template_quality(blueprint))
        
        # Calculate overall score
        passed_checks = len([c for c in checks if c.level == ValidationLevel.PASS])
        overall_score = (passed_checks / len(checks)) * 10 if checks else 0
        
        return ValidationReport(
            blueprint_id=blueprint.get('id', 'unknown'),
            overall_score=overall_score,
            checks=checks
        )
    
    def _check_blueprint_structure(self, blueprint: Dict) -> List[CheckResult]:
        """Validate basic blueprint structure"""
        checks = []
        
        required_fields = ['id', 'name', 'description', 'version', 'strategy', 'parameters', 'codeTemplate']
        
        for field in required_fields:
            if field in blueprint:
                checks.append(CheckResult(
                    name=f"Required field: {field}",
                    level=ValidationLevel.PASS,
                    message=f"Field '{field}' present"
                ))
            else:
                checks.append(CheckResult(
                    name=f"Required field: {field}",
                    level=ValidationLevel.FAIL,
                    message=f"Missing required field '{field}'"
                ))
        
        # Check strategy is embedded-template
        if blueprint.get('strategy') == 'embedded-template':
            checks.append(CheckResult(
                name="Strategy validation",
                level=ValidationLevel.PASS,
                message="Using embedded-template strategy"
            ))
        else:
            checks.append(CheckResult(
                name="Strategy validation",
                level=ValidationLevel.FAIL,
                message="Must use 'embedded-template' strategy"
            ))
        
        return checks
    
    def _check_naming_conventions(self, blueprint: Dict) -> List[CheckResult]:
        """Validate against @naming-conventions.md"""
        checks = []
        
        # Check blueprint ID format
        blueprint_id = blueprint.get('id', '')
        if re.match(r'^smart-[a-z][a-z0-9-]*$', blueprint_id):
            checks.append(CheckResult(
                name="Blueprint ID format",
                level=ValidationLevel.PASS,
                message="Blueprint ID follows naming convention"
            ))
        else:
            checks.append(CheckResult(
                name="Blueprint ID format",
                level=ValidationLevel.FAIL,
                message="Blueprint ID must follow 'smart-{component}-{resource}' pattern"
            ))
        
        # Check parameter naming
        parameters = blueprint.get('parameters', {})
        for param_name in parameters.keys():
            if re.match(r'^[a-z][a-zA-Z0-9]*$', param_name):
                checks.append(CheckResult(
                    name=f"Parameter naming: {param_name}",
                    level=ValidationLevel.PASS,
                    message=f"Parameter '{param_name}' follows camelCase convention"
                ))
            else:
                checks.append(CheckResult(
                    name=f"Parameter naming: {param_name}",
                    level=ValidationLevel.WARNING,
                    message=f"Parameter '{param_name}' should use camelCase"
                ))
        
        return checks
    
    def _check_fastapi_patterns(self, blueprint: Dict) -> List[CheckResult]:
        """Validate against @fastapi-conventions.md"""
        checks = []
        
        template_content = blueprint.get('codeTemplate', {}).get('content', '')
        
        # Check for required template variables
        for var in self.required_template_vars:
            if var in template_content:
                checks.append(CheckResult(
                    name=f"Template variable: {var}",
                    level=ValidationLevel.PASS,
                    message=f"Template variable '{var}' present"
                ))
            else:
                checks.append(CheckResult(
                    name=f"Template variable: {var}",
                    level=ValidationLevel.WARNING,
                    message=f"Consider using standard template variable '{var}'"
                ))
        
        # Check for FastAPI imports
        if 'from fastapi import' in template_content:
            checks.append(CheckResult(
                name="FastAPI imports",
                level=ValidationLevel.PASS,
                message="FastAPI imports present"
            ))
        else:
            checks.append(CheckResult(
                name="FastAPI imports",
                level=ValidationLevel.FAIL,
                message="Missing FastAPI imports"
            ))
        
        # Check for async patterns
        if 'async def' in template_content:
            checks.append(CheckResult(
                name="Async patterns",
                level=ValidationLevel.PASS,
                message="Async/await patterns used"
            ))
        else:
            checks.append(CheckResult(
                name="Async patterns",
                level=ValidationLevel.WARNING,
                message="Consider using async/await patterns for better performance"
            ))
        
        return checks
    
    def _check_quality_requirements(self, blueprint: Dict) -> List[CheckResult]:
        """Validate 10/10 quality criteria"""
        checks = []
        
        template_content = blueprint.get('codeTemplate', {}).get('content', '')
        
        # Check for comprehensive docstrings
        if '"""' in template_content and 'Args:' in template_content:
            checks.append(CheckResult(
                name="Comprehensive docstrings",
                level=ValidationLevel.PASS,
                message="Comprehensive docstrings with Args section"
            ))
        else:
            checks.append(CheckResult(
                name="Comprehensive docstrings",
                level=ValidationLevel.FAIL,
                message="Missing comprehensive docstrings with Args, Returns, Raises"
            ))
        
        # Check for error handling
        if 'HTTPException' in template_content and 'try:' in template_content:
            checks.append(CheckResult(
                name="Error handling",
                level=ValidationLevel.PASS,
                message="Error handling patterns present"
            ))
        else:
            checks.append(CheckResult(
                name="Error handling",
                level=ValidationLevel.FAIL,
                message="Missing comprehensive error handling"
            ))
        
        # Check for logging
        if 'logger' in template_content or 'logging' in template_content:
            checks.append(CheckResult(
                name="Logging integration",
                level=ValidationLevel.PASS,
                message="Logging integration present"
            ))
        else:
            checks.append(CheckResult(
                name="Logging integration",
                level=ValidationLevel.WARNING,
                message="Consider adding structured logging"
            ))
        
        # Check for type hints
        if ': ' in template_content and '->' in template_content:
            checks.append(CheckResult(
                name="Type hints",
                level=ValidationLevel.PASS,
                message="Type hints present"
            ))
        else:
            checks.append(CheckResult(
                name="Type hints",
                level=ValidationLevel.FAIL,
                message="Missing comprehensive type hints"
            ))
        
        return checks
    
    def _check_template_quality(self, blueprint: Dict) -> List[CheckResult]:
        """Validate template meets 10/10 quality standards"""
        checks = []
        
        template = blueprint.get('codeTemplate', {})
        
        # Check template structure
        if template.get('language') == 'python':
            checks.append(CheckResult(
                name="Template language",
                level=ValidationLevel.PASS,
                message="Python language specified"
            ))
        else:
            checks.append(CheckResult(
                name="Template language",
                level=ValidationLevel.FAIL,
                message="Must specify Python as template language"
            ))
        
        # Check executable flag
        if template.get('executable', False):
            checks.append(CheckResult(
                name="Template executable",
                level=ValidationLevel.PASS,
                message="Template marked as executable"
            ))
        else:
            checks.append(CheckResult(
                name="Template executable",
                level=ValidationLevel.WARNING,
                message="Template should be marked as executable"
            ))
        
        # Check testable flag
        if template.get('testable', False):
            checks.append(CheckResult(
                name="Template testable",
                level=ValidationLevel.PASS,
                message="Template marked as testable"
            ))
        else:
            checks.append(CheckResult(
                name="Template testable",
                level=ValidationLevel.WARNING,
                message="Template should be marked as testable"
            ))
        
        return checks


class TemplateQualityEnforcer:
    """Ensures templates meet 10/10 quality standards"""
    
    def validate_template(self, template: str) -> QualityScore:
        """Validate template meets 10/10 quality standards"""
        return QualityScore(
            code_quality=self._check_code_quality(template),
            fastapi_practices=self._check_fastapi_practices(template),
            error_handling=self._check_error_handling(template),
            security=self._check_security_implementation(template),
            production_readiness=self._check_production_readiness(template)
        )
    
    def _check_code_quality(self, template: str) -> int:
        """Check code quality aspects"""
        score = 0
        
        # Check for comprehensive docstrings
        if '"""' in template and 'Args:' in template and 'Returns:' in template:
            score += 3
        elif '"""' in template:
            score += 1
        
        # Check for type hints
        if ': ' in template and '->' in template:
            score += 2
        
        # Check for proper naming
        if re.search(r'def [a-z][a-z0-9_]*\(', template):
            score += 2
        
        # Check for comments
        if '#' in template:
            score += 1
        
        # Check for proper imports
        if 'from' in template and 'import' in template:
            score += 2
        
        return min(score, 10)
    
    def _check_fastapi_practices(self, template: str) -> int:
        """Check FastAPI best practices"""
        score = 0
        
        # Check for router usage
        if '@router.' in template:
            score += 2
        
        # Check for response models
        if 'response_model=' in template:
            score += 2
        
        # Check for status codes
        if 'status_code=' in template:
            score += 2
        
        # Check for dependencies
        if 'Depends(' in template:
            score += 2
        
        # Check for async patterns
        if 'async def' in template:
            score += 2
        
        return min(score, 10)
    
    def _check_error_handling(self, template: str) -> int:
        """Check error handling implementation"""
        score = 0
        
        # Check for try-catch blocks
        if 'try:' in template and 'except' in template:
            score += 3
        
        # Check for HTTPException
        if 'HTTPException' in template:
            score += 2
        
        # Check for specific error types
        if 'ValueError' in template or 'TypeError' in template:
            score += 2
        
        # Check for error logging
        if 'logger.error' in template:
            score += 2
        
        # Check for proper status codes
        if 'status.HTTP_' in template:
            score += 1
        
        return min(score, 10)
    
    def _check_security_implementation(self, template: str) -> int:
        """Check security implementation"""
        score = 0
        
        # Check for authentication
        if 'get_current_user' in template or 'Depends(auth' in template:
            score += 3
        
        # Check for input validation
        if 'Field(' in template or 'Query(' in template:
            score += 2
        
        # Check for authorization
        if 'permission' in template.lower() or 'role' in template.lower():
            score += 2
        
        # Check for rate limiting
        if 'rate_limit' in template:
            score += 2
        
        # Check for CORS handling
        if 'cors' in template.lower():
            score += 1
        
        return min(score, 10)
    
    def _check_production_readiness(self, template: str) -> int:
        """Check production readiness features"""
        score = 0
        
        # Check for logging
        if 'logger' in template:
            score += 2
        
        # Check for monitoring
        if 'metrics' in template or 'monitoring' in template:
            score += 2
        
        # Check for configuration
        if 'config' in template or 'settings' in template:
            score += 2
        
        # Check for health checks
        if 'health' in template:
            score += 1
        
        # Check for pagination
        if 'skip' in template and 'limit' in template:
            score += 2
        
        # Check for caching
        if 'cache' in template:
            score += 1
        
        return min(score, 10)


def validate_blueprint_file(blueprint_path: str) -> ValidationReport:
    """Validate a blueprint file against @ai-docs standards"""
    try:
        with open(blueprint_path, 'r', encoding='utf-8') as f:
            blueprint = json.load(f)
        
        validator = AIDocsValidator()
        return validator.validate_blueprint(blueprint)
        
    except FileNotFoundError:
        return ValidationReport(
            blueprint_id="unknown",
            overall_score=0,
            checks=[CheckResult(
                name="File existence",
                level=ValidationLevel.FAIL,
                message=f"Blueprint file not found: {blueprint_path}"
            )]
        )
    except json.JSONDecodeError as e:
        return ValidationReport(
            blueprint_id="unknown",
            overall_score=0,
            checks=[CheckResult(
                name="JSON validation",
                level=ValidationLevel.FAIL,
                message=f"Invalid JSON: {str(e)}"
            )]
        )


def main():
    """Example usage of the enhanced validator"""
    print("🔍 Enhanced Blueprint Validator")
    print("=" * 50)
    
    # Test with existing blueprint
    blueprint_path = "backend-mcp/blueprints/api/routes/smart-crud-route.json"
    report = validate_blueprint_file(blueprint_path)
    
    print(f"Blueprint: {report.blueprint_id}")
    print(f"Overall Score: {report.overall_score:.1f}/10")
    print(f"Status: {'✅ PASSED' if report.passed else '❌ FAILED'}")
    
    if report.failures:
        print(f"\n❌ Failures ({len(report.failures)}):")
        for failure in report.failures:
            print(f"   • {failure.name}: {failure.message}")
    
    if report.warnings:
        print(f"\n⚠️ Warnings ({len(report.warnings)}):")
        for warning in report.warnings:
            print(f"   • {warning.name}: {warning.message}")
    
    passed_checks = len([c for c in report.checks if c.level == ValidationLevel.PASS])
    print(f"\n✅ Passed Checks: {passed_checks}/{len(report.checks)}")


if __name__ == "__main__":
    main()
