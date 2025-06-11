#!/usr/bin/env python3
"""
Enhanced Run Next Blueprint Task
Execute the next blueprint creation task with GUARANTEED 10/10 quality validation
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from automated_blueprint_executor import EnhancedAutomatedBlueprintExecutor, Priority, Phase


def main():
    """Execute the next blueprint creation task with 10/10 quality guarantee"""
    print("🎯 FastAPI MCP - Enhanced Blueprint Task Executor (10/10 Quality)")
    print("=" * 70)

    # Initialize enhanced executor
    executor = EnhancedAutomatedBlueprintExecutor()
    
    # Show current progress
    progress = executor.get_progress_report()
    print(f"📊 Current Progress:")
    print(f"   Completed: {progress['completed']}/{progress['total_tasks']} ({progress['progress_percentage']:.1f}%)")
    print(f"   Remaining: {progress['remaining']} tasks")
    print(f"   Estimated Time Remaining: {progress['total_hours'] - progress['completed_hours']:.1f} hours")
    
    # Get next task
    next_task = executor.get_next_task()
    
    if not next_task:
        print("\n🎉 All blueprint tasks completed!")
        print("✅ FastAPI MCP blueprint library is complete")
        return
    
    print(f"\n🚀 Next Task: {next_task.name}")
    print(f"   Blueprint ID: {next_task.blueprint_id}")
    print(f"   Component Layer: {next_task.component_layer}")
    print(f"   Priority: {next_task.priority.value}")
    print(f"   Phase: {next_task.phase.value}")
    print(f"   Estimated Time: {next_task.estimated_hours} hours")
    print(f"   Location: {next_task.location}")
    
    # Show task details
    print(f"\n📋 Task Details:")
    print(f"   Purpose: {next_task.purpose}")
    print(f"   Features:")
    for feature in next_task.features:
        print(f"     • {feature}")
    
    # Generate streamlined AI-first task prompt
    print("\n" + "="*70)
    print("⚡ AI-FIRST TASK EXECUTION (3-4 minutes):")
    print("="*70)
    print(f"""
## Streamlined Task: {next_task.name}

**Objective**: Create production-ready blueprint with guaranteed 10/10 quality

**Execution Steps**:
1. **Create Blueprint** (2 min) - Single JSON file with complete template
2. **Validate Structure** (30 sec) - Quick JSON parse confirmation
3. **Quality Check** (10 sec) - Pass/fail assessment only
4. **Certify** (5 sec) - Mark as production-ready

**Success Criteria**:
- ✅ Valid JSON structure
- ✅ All required sections present
- ✅ 10/10 quality template embedded
- ✅ Production deployment ready

**Completion Command**:
```bash
python mark_task_complete.py {next_task.blueprint_id} 10/10
```

**Target Location**: {next_task.location}
**Blueprint ID**: {next_task.blueprint_id}
""")
    print("="*70)

    print(f"\n💡 After completion, run:")
    print(f"   python mark_task_complete.py {next_task.blueprint_id} 10/10")
    
    print(f"\n📝 Instructions:")
    print(f"1. Copy the task prompt above")
    print(f"2. Follow the 4-phase execution process")
    print(f"3. Create the blueprint at: {next_task.location}{next_task.blueprint_id}.json")
    print(f"4. Achieve 10/10 quality score")
    print(f"5. Mark task as complete when finished")
    
    # Show what's coming next
    remaining_high_priority = [t for t in executor.tasks 
                              if t.priority == Priority.HIGH 
                              and t not in executor.completed_tasks 
                              and t != next_task]
    
    if remaining_high_priority:
        print(f"\n🔜 Upcoming High Priority Tasks:")
        for i, task in enumerate(remaining_high_priority[:3], 1):
            print(f"   {i}. {task.name} ({task.estimated_hours}h)")
        if len(remaining_high_priority) > 3:
            print(f"   ... and {len(remaining_high_priority) - 3} more")
    
    print(f"\n🎯 Focus: Complete '{next_task.name}' to advance the blueprint library!")


if __name__ == "__main__":
    main()
