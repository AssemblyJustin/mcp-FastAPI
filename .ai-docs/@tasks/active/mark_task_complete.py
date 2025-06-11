#!/usr/bin/env python3
"""
Task Completion Marker

Simple script to mark a blueprint task as completed.
Usage: python mark_task_complete.py <task_id> [quality_score]

Example:
    python mark_task_complete.py smart-response-models 10/10
    python mark_task_complete.py smart-auth-routes
"""

import sys
import json
from pathlib import Path
from datetime import datetime
from automated_blueprint_executor import EnhancedAutomatedBlueprintExecutor

def main():
    if len(sys.argv) < 2:
        print("Usage: python mark_task_complete.py <task_id> [quality_score]")
        print("Example: python mark_task_complete.py smart-response-models 10/10")
        sys.exit(1)
    
    task_id = sys.argv[1]
    quality_score = sys.argv[2] if len(sys.argv) > 2 else "10/10"
    
    # Initialize executor
    executor = EnhancedAutomatedBlueprintExecutor()
    
    # Find the task
    task = None
    for t in executor.tasks:
        if t.blueprint_id == task_id:
            task = t
            break
    
    if not task:
        print(f"❌ Task not found: {task_id}")
        print("Available tasks:")
        for t in executor.tasks:
            status = "✅ COMPLETED" if executor.is_task_completed(t) else "⏳ PENDING"
            print(f"  - {t.blueprint_id}: {t.name} ({status})")
        sys.exit(1)
    
    # Check if already completed
    if executor.is_task_completed(task):
        print(f"ℹ️ Task already completed: {task.name}")
        sys.exit(0)
    
    # Mark as complete
    executor.mark_task_complete(task, quality_score)
    print(f"✅ Task marked complete: {task.name} ({quality_score})")
    
    # Show next task
    next_task = executor.get_next_task()
    if next_task:
        print(f"🎯 Next task: {next_task.name} ({next_task.blueprint_id})")
    else:
        print("🎉 All tasks completed!")

if __name__ == "__main__":
    main()
