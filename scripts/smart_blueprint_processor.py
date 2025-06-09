"""
Smart Blueprint Processor for AI-first code generation.
Handles embedded templates with validation and testing.
"""
import json
import re
from typing import Dict, Any, Optional
from pathlib import Path
import tempfile
import subprocess


class SmartBlueprintProcessor:
    """Process smart blueprints with embedded code templates."""
    
    def __init__(self, blueprint_path: str):
        self.blueprint_path = Path(blueprint_path)
        self.blueprint = self._load_blueprint()
    
    def _load_blueprint(self) -> Dict[str, Any]:
        """Load and validate blueprint file."""
        with open(self.blueprint_path, 'r') as f:
            blueprint = json.load(f)
        
        required_fields = ['id', 'codeTemplate', 'parameters']
        for field in required_fields:
            if field not in blueprint:
                raise ValueError(f"Missing required field: {field}")
        
        return blueprint
    
    def generate_code(self, parameters: Dict[str, Any]) -> str:
        """Generate code from template with parameters."""
        template = self.blueprint['codeTemplate']['content']
        
        # Simple template variable replacement
        # In production, use a proper template engine like Jinja2
        for key, value in parameters.items():
            # Handle boolean conditionals
            if isinstance(value, bool):
                template = self._process_conditionals(template, key, value)
            else:
                template = template.replace(f"{{{{{key}}}}}", str(value))
        
        return template
    
    def _process_conditionals(self, template: str, key: str, value: bool) -> str:
        """Process conditional blocks in template."""
        # Handle {{#if key}} ... {{/if}} blocks
        if_pattern = rf'{{\{{#if {key}\}}\}}(.*?){{\{{/if\}}\}}'
        
        if value:
            # Keep content inside if block
            template = re.sub(if_pattern, r'\1', template, flags=re.DOTALL)
        else:
            # Remove entire if block
            template = re.sub(if_pattern, '', template, flags=re.DOTALL)
        
        return template
    
    def validate_template(self) -> bool:
        """Validate the embedded template syntax."""
        template = self.blueprint['codeTemplate']['content']
        language = self.blueprint['codeTemplate'].get('language', 'python')
        
        if language == 'python':
            return self._validate_python_template(template)
        
        return True
    
    def _validate_python_template(self, template: str) -> bool:
        """Validate Python template syntax."""
        try:
            # Create a temporary file with sample parameters
            sample_params = self._generate_sample_parameters()
            code = self.generate_code(sample_params)
            
            # Write to temp file and check syntax
            with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
                f.write(code)
                temp_path = f.name
            
            # Check syntax with Python AST
            result = subprocess.run(
                ['python', '-m', 'py_compile', temp_path],
                capture_output=True,
                text=True
            )
            
            Path(temp_path).unlink()  # Clean up
            
            return result.returncode == 0
            
        except Exception as e:
            print(f"Template validation error: {e}")
            return False
    
    def _generate_sample_parameters(self) -> Dict[str, Any]:
        """Generate sample parameters for testing."""
        params = {}
        
        for param_name, param_config in self.blueprint['parameters'].items():
            param_type = param_config.get('type', 'string')
            
            if param_type == 'string':
                if 'pattern' in param_config:
                    # Generate based on pattern
                    if 'snake_case' in param_config.get('description', ''):
                        params[param_name] = 'sample_resource'
                    elif 'PascalCase' in param_config.get('description', ''):
                        params[param_name] = 'SampleResource'
                    else:
                        params[param_name] = 'sample'
                else:
                    params[param_name] = param_config.get('default', 'sample')
            elif param_type == 'boolean':
                params[param_name] = param_config.get('default', True)
            elif param_type == 'integer':
                params[param_name] = param_config.get('default', 1)
        
        return params
    
    def extract_example(self, output_path: Optional[str] = None) -> str:
        """Extract a clean code example from the template."""
        sample_params = self._generate_sample_parameters()
        code = self.generate_code(sample_params)
        
        if output_path:
            with open(output_path, 'w') as f:
                f.write(code)
        
        return code
    
    def test_template(self) -> bool:
        """Test the template with sample data."""
        if not self.validate_template():
            return False
        
        # If test template is provided, run it
        if 'testTemplate' in self.blueprint:
            return self._run_test_template()
        
        return True
    
    def _run_test_template(self) -> bool:
        """Run the embedded test template."""
        test_template = self.blueprint['testTemplate']['content']
        sample_params = self._generate_sample_parameters()
        
        # Generate test code
        test_code = test_template
        for key, value in sample_params.items():
            test_code = test_code.replace(f"{{{{{key}}}}}", str(value))
        
        # Write and run test
        with tempfile.NamedTemporaryFile(mode='w', suffix='_test.py', delete=False) as f:
            f.write(test_code)
            temp_path = f.name
        
        try:
            result = subprocess.run(
                ['python', '-m', 'pytest', temp_path, '-v'],
                capture_output=True,
                text=True
            )
            
            Path(temp_path).unlink()  # Clean up
            return result.returncode == 0
            
        except Exception as e:
            print(f"Test execution error: {e}")
            return False
    
    def get_metadata(self) -> Dict[str, Any]:
        """Get blueprint metadata for AI optimization."""
        return {
            'id': self.blueprint['id'],
            'estimatedTokens': self.blueprint.get('metadata', {}).get('estimatedTokens', 1000),
            'generationTime': self.blueprint.get('metadata', {}).get('generationTime', '<1s'),
            'parameters': list(self.blueprint['parameters'].keys()),
            'language': self.blueprint['codeTemplate'].get('language', 'python'),
            'testable': 'testTemplate' in self.blueprint,
            'validated': self.validate_template()
        }


# CLI interface for development tools
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 3:
        print("Usage: python smart_blueprint_processor.py <blueprint_file> <command>")
        print("Commands: validate, extract, test, metadata")
        sys.exit(1)
    
    blueprint_file = sys.argv[1]
    command = sys.argv[2]
    
    processor = SmartBlueprintProcessor(blueprint_file)
    
    if command == "validate":
        is_valid = processor.validate_template()
        print(f"Template validation: {'PASSED' if is_valid else 'FAILED'}")
        sys.exit(0 if is_valid else 1)
    
    elif command == "extract":
        output_file = sys.argv[3] if len(sys.argv) > 3 else None
        code = processor.extract_example(output_file)
        if not output_file:
            print(code)
    
    elif command == "test":
        test_passed = processor.test_template()
        print(f"Template testing: {'PASSED' if test_passed else 'FAILED'}")
        sys.exit(0 if test_passed else 1)
    
    elif command == "metadata":
        metadata = processor.get_metadata()
        print(json.dumps(metadata, indent=2))
    
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)
