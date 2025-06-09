#!/usr/bin/env python3
"""
Documentation Reference Validator

Ensures all documentation files reference the correct master files
and don't contain broken or outdated references.
"""

import os
import re
import sys
from pathlib import Path
from typing import List, Dict, Tuple

class DocumentationValidator:
    def __init__(self, root_dir: str = "."):
        self.root_dir = Path(root_dir)
        self.ai_docs_dir = self.root_dir / ".ai-docs"
        self.errors = []
        self.warnings = []
        
        # Master files that should be referenced
        self.master_files = {
            "MASTER_CONVENTIONS.md": ".ai-docs/@core/MASTER_CONVENTIONS.md",
            "MASTER_TESTING.md": ".ai-docs/@core/MASTER_TESTING.md", 
            "MASTER_ARCHITECTURE.md": ".ai-docs/@core/MASTER_ARCHITECTURE.md"
        }
        
        # Broken reference patterns to detect
        self.broken_patterns = [
            r"\.ai-docs/\.ai-docs/\.ai-docs/@core/@conventions\.md\.md\.md",
            r"\.ai-docs/\.ai-docs/\.ai-docs/@core/@testing-protocol\.md\.md\.md",
            r"\.ai-docs/@conventions/@testing-protocol\.md",
            r"\.ai-docs/TESTING_PROTOCOL\.md",
            r"\.ai-docs/@core/@testing-protocol\.md",
            r"frontend-mcp/",
            r"code-examples/",
            r"1:1:1 relationship",
            r"React components",
            r"\.tsx",
            r"\.jsx"
        ]
        
        # Correct reference patterns
        self.correct_patterns = {
            "master_conventions": r"\.ai-docs/@core/MASTER_CONVENTIONS\.md",
            "master_testing": r"\.ai-docs/@core/MASTER_TESTING\.md",
            "master_architecture": r"\.ai-docs/@core/MASTER_ARCHITECTURE\.md"
        }

    def validate_file(self, file_path: Path) -> List[Dict]:
        """Validate a single documentation file."""
        issues = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Check for broken reference patterns
            for pattern in self.broken_patterns:
                matches = re.findall(pattern, content, re.IGNORECASE)
                if matches:
                    issues.append({
                        "type": "error",
                        "file": str(file_path),
                        "issue": f"Broken reference pattern found: {pattern}",
                        "matches": len(matches)
                    })
            
            # Check if file should reference master files
            if self._should_reference_masters(file_path):
                self._check_master_references(file_path, content, issues)
                
        except Exception as e:
            issues.append({
                "type": "error", 
                "file": str(file_path),
                "issue": f"Error reading file: {str(e)}"
            })
            
        return issues

    def _should_reference_masters(self, file_path: Path) -> bool:
        """Check if file should reference master files."""
        # Files that should reference masters
        reference_files = [
            "@conventions",
            "@context", 
            "@prompts",
            "README.md"
        ]
        
        # Skip master files themselves
        if file_path.name.startswith("MASTER_"):
            return False
            
        return any(ref in str(file_path) for ref in reference_files)

    def _check_master_references(self, file_path: Path, content: str, issues: List[Dict]):
        """Check if file properly references master files."""
        has_master_ref = False
        
        for master_file, master_path in self.master_files.items():
            if master_path in content:
                has_master_ref = True
                break
                
        if not has_master_ref and "@conventions" in str(file_path):
            issues.append({
                "type": "warning",
                "file": str(file_path), 
                "issue": "Convention file should reference master files"
            })

    def validate_all_docs(self) -> Dict:
        """Validate all documentation files."""
        results = {
            "total_files": 0,
            "files_with_issues": 0,
            "total_errors": 0,
            "total_warnings": 0,
            "issues": []
        }
        
        # Find all markdown files in .ai-docs
        md_files = list(self.ai_docs_dir.rglob("*.md"))
        
        for file_path in md_files:
            results["total_files"] += 1
            file_issues = self.validate_file(file_path)
            
            if file_issues:
                results["files_with_issues"] += 1
                results["issues"].extend(file_issues)
                
                for issue in file_issues:
                    if issue["type"] == "error":
                        results["total_errors"] += 1
                    elif issue["type"] == "warning":
                        results["total_warnings"] += 1
                        
        return results

    def check_master_files_exist(self) -> List[Dict]:
        """Check that all master files exist."""
        issues = []
        
        for master_file, master_path in self.master_files.items():
            full_path = self.root_dir / master_path
            if not full_path.exists():
                issues.append({
                    "type": "error",
                    "file": master_path,
                    "issue": f"Master file does not exist: {master_file}"
                })
                
        return issues

    def generate_report(self, results: Dict) -> str:
        """Generate a human-readable report."""
        report = []
        report.append("=" * 60)
        report.append("DOCUMENTATION REFERENCE VALIDATION REPORT")
        report.append("=" * 60)
        report.append("")
        
        # Summary
        report.append(f"📊 SUMMARY:")
        report.append(f"  Total files checked: {results['total_files']}")
        report.append(f"  Files with issues: {results['files_with_issues']}")
        report.append(f"  Total errors: {results['total_errors']}")
        report.append(f"  Total warnings: {results['total_warnings']}")
        report.append("")
        
        # Master files check
        master_issues = self.check_master_files_exist()
        if master_issues:
            report.append("🚨 MASTER FILES ISSUES:")
            for issue in master_issues:
                report.append(f"  ❌ {issue['issue']}")
            report.append("")
        else:
            report.append("✅ All master files exist")
            report.append("")
        
        # Issues by type
        if results["total_errors"] > 0:
            report.append("🚨 ERRORS:")
            for issue in results["issues"]:
                if issue["type"] == "error":
                    report.append(f"  ❌ {issue['file']}")
                    report.append(f"     {issue['issue']}")
                    if "matches" in issue:
                        report.append(f"     Found {issue['matches']} occurrences")
            report.append("")
            
        if results["total_warnings"] > 0:
            report.append("⚠️  WARNINGS:")
            for issue in results["issues"]:
                if issue["type"] == "warning":
                    report.append(f"  ⚠️  {issue['file']}")
                    report.append(f"     {issue['issue']}")
            report.append("")
        
        # Status
        if results["total_errors"] == 0:
            report.append("🎉 VALIDATION PASSED - No critical errors found!")
        else:
            report.append("❌ VALIDATION FAILED - Critical errors found!")
            
        report.append("")
        report.append("=" * 60)
        
        return "\n".join(report)

def main():
    """Main validation function."""
    validator = DocumentationValidator()
    
    print("🔍 Validating documentation references...")
    print("")
    
    results = validator.validate_all_docs()
    report = validator.generate_report(results)
    
    print(report)
    
    # Exit with error code if issues found
    if results["total_errors"] > 0:
        sys.exit(1)
    else:
        sys.exit(0)

if __name__ == "__main__":
    main()
