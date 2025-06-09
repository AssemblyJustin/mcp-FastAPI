"""
Template Engine for FastAPI MCP

This module handles loading blueprints, code examples, and generating files
from templates using variable substitution.
"""

import os
import json
import logging
from typing import Dict, Any, List, Optional, Union
from pathlib import Path

# Configure logging
logger = logging.getLogger("mcp-fastapi.template-engine")

# Get the project root directory
BASE_DIR = Path(__file__).resolve().parent.parent


def find_blueprints_dir() -> str:
    """Find the blueprints directory"""
    blueprints_dir = os.path.join(BASE_DIR, "backend-mcp", "blueprints")
    os.makedirs(blueprints_dir, exist_ok=True)
    return blueprints_dir


def find_code_examples_dir() -> str:
    """Find the code examples directory"""
    code_examples_dir = os.path.join(BASE_DIR, "backend-mcp", "code-examples")
    os.makedirs(code_examples_dir, exist_ok=True)
    return code_examples_dir


def find_templates_dir() -> str:
    """Find the templates directory"""
    templates_dir = os.path.join(BASE_DIR, "backend-mcp", "templates")
    os.makedirs(templates_dir, exist_ok=True)
    return templates_dir


def load_blueprint(blueprint_id: str) -> Optional[Dict[str, Any]]:
    """
    Load a blueprint JSON file by ID
    
    Args:
        blueprint_id: The ID of the blueprint to load
        
    Returns:
        Dictionary containing the blueprint data or None if not found
    """
    blueprints_dir = find_blueprints_dir()
    blueprint_path = os.path.join(blueprints_dir, f"{blueprint_id}.json")
    
    if not os.path.exists(blueprint_path):
        logger.error(f"Blueprint not found: {blueprint_path}")
        return None
    
    try:
        with open(blueprint_path, "r", encoding="utf-8") as f:
            blueprint = json.load(f)
        return blueprint
    except json.JSONDecodeError:
        logger.error(f"Failed to parse blueprint JSON: {blueprint_path}")
        return None
    except Exception as e:
        logger.error(f"Error loading blueprint {blueprint_path}: {str(e)}")
        return None


def load_code_example(code_example_path: str) -> Optional[str]:
    """
    Load a code example file
    
    Args:
        code_example_path: Path to the code example file, relative to code_examples_dir
        
    Returns:
        String containing the code example content or None if not found
    """
    code_examples_dir = find_code_examples_dir()
    full_path = os.path.join(code_examples_dir, code_example_path)
    
    if not os.path.exists(full_path):
        logger.error(f"Code example not found: {full_path}")
        return None
    
    try:
        with open(full_path, "r", encoding="utf-8") as f:
            content = f.read()
        return content
    except Exception as e:
        logger.error(f"Error loading code example {full_path}: {str(e)}")
        return None


def generate_from_template(template_path: str, parameters: Dict[str, Any], output_path: str) -> Dict[str, Any]:
    """
    Generate a file from a template by substituting parameters
    
    Args:
        template_path: Path to the template file
        parameters: Dictionary of parameters to substitute in the template
        output_path: Path where the generated file should be saved
        
    Returns:
        Dictionary with success status and additional information
    """
    if not os.path.exists(template_path):
        return {
            "success": False,
            "error": f"Template not found: {template_path}"
        }
    
    try:
        # Read template content
        with open(template_path, "r", encoding="utf-8") as f:
            template_content = f.read()
        
        # Substitute parameters using Python's format
        # Convert parameters to strings for compatibility
        str_params = {k: str(v) for k, v in parameters.items()}
        output_content = template_content.format(**str_params)
        
        # Create output directory if it doesn't exist
        os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
        
        # Write to output file
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(output_content)
        
        return {
            "success": True,
            "outputPath": output_path,
            "templatePath": template_path,
            "parameters": parameters
        }
    except KeyError as e:
        return {
            "success": False,
            "error": f"Missing parameter in template: {str(e)}"
        }
    except Exception as e:
        return {
            "success": False,
            "error": f"Error generating from template: {str(e)}"
        }


def generate_from_blueprint(blueprint_id: str, parameters: Dict[str, Any], output_path: str) -> Dict[str, Any]:
    """
    Generate a file from a blueprint
    
    Args:
        blueprint_id: ID of the blueprint to use
        parameters: Dictionary of parameters to substitute
        output_path: Path where the generated file should be saved
        
    Returns:
        Dictionary with success status and additional information
    """
    blueprint = load_blueprint(blueprint_id)
    if not blueprint:
        return {
            "success": False,
            "error": f"Blueprint not found: {blueprint_id}"
        }
    
    # Validate required parameters
    if "parameters" in blueprint and "required" in blueprint["parameters"]:
        missing_params = [
            param for param in blueprint["parameters"]["required"] 
            if param not in parameters
        ]
        if missing_params:
            return {
                "success": False,
                "error": f"Missing required parameters: {', '.join(missing_params)}"
            }
    
    # Load code example if specified
    code_example_content = None
    if "codeExample" in blueprint and "codeExample" in parameters:
        code_example_content = load_code_example(parameters["codeExample"])
        if not code_example_content:
            return {
                "success": False,
                "error": f"Failed to load code example: {parameters['codeExample']}"
            }
        parameters["codeExampleContent"] = code_example_content
    
    # Generate from template if specified in blueprint
    if "template" in blueprint:
        templates_dir = find_templates_dir()
        template_path = os.path.join(templates_dir, blueprint["template"])
        
        return generate_from_template(template_path, parameters, output_path)
    
    # If no template specified, use code example directly
    elif code_example_content:
        try:
            # Simple variable substitution for code example
            output_content = code_example_content
            
            for key, value in parameters.items():
                if isinstance(value, str):
                    placeholder = "{" + key + "}"
                    output_content = output_content.replace(placeholder, value)
            
            # Create output directory if it doesn't exist
            os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
            
            # Write to output file
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(output_content)
            
            return {
                "success": True,
                "outputPath": output_path,
                "blueprint": blueprint,
                "codeExample": parameters.get("codeExample")
            }
        except Exception as e:
            return {
                "success": False,
                "error": f"Error generating from code example: {str(e)}"
            }
    
    return {
        "success": False,
        "error": "Blueprint has no template or code example specified"
    }


def list_available_blueprints() -> List[Dict[str, Any]]:
    """
    List all available blueprints
    
    Returns:
        List of dictionaries containing blueprint metadata
    """
    blueprints_dir = find_blueprints_dir()
    blueprints = []
    
    for filename in os.listdir(blueprints_dir):
        if filename.endswith(".json"):
            try:
                blueprint_id = filename[:-5]  # Remove .json extension
                blueprint = load_blueprint(blueprint_id)
                if blueprint:
                    blueprints.append({
                        "id": blueprint_id,
                        "name": blueprint.get("name", blueprint_id),
                        "description": blueprint.get("description", ""),
                        "version": blueprint.get("version", "1.0.0")
                    })
            except Exception as e:
                logger.error(f"Error loading blueprint {filename}: {str(e)}")
    
    return blueprints


def list_available_code_examples() -> List[Dict[str, Any]]:
    """
    List all available code examples
    
    Returns:
        List of dictionaries containing code example metadata
    """
    code_examples_dir = find_code_examples_dir()
    examples = []
    
    for root, _, files in os.walk(code_examples_dir):
        for filename in files:
            try:
                relative_path = os.path.relpath(os.path.join(root, filename), code_examples_dir)
                examples.append({
                    "path": relative_path,
                    "name": os.path.basename(filename),
                    "type": os.path.splitext(filename)[1][1:]  # File extension without dot
                })
            except Exception as e:
                logger.error(f"Error listing code example {filename}: {str(e)}")
    
    return examples 