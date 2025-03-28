# CrewAI Dynamic Workflow Refactor Project Plan

## 1. Simplify tasks.yaml
- [✅] 1.1. Create backup of original tasks.yaml
- [✅] 1.2. Remove all specialized task templates
- [✅] 1.3. Create single generic router task with minimal description
- [✅] 1.4. Ensure router task uses only the {user_query} template variable
- [✅] 1.5. Remove all hardcoded delegation patterns
- [✅] 1.6. Remove all complex routing logic and decision trees
- [✅] 1.7. Validate the new tasks.yaml syntax

## 2. Update crew.py
- [✅] 2.1. Create backup of original crew.py
- [✅] 2.2. Keep YAML configuration loading mechanism
- [✅] 2.3. Keep knowledge and tool initialization as is
- [✅] 2.4. Modify task creation to only create the router task
- [✅] 2.5. Use appropriate Process type (decided on Process.sequential)
- [✅] 2.6. Ensure task is assigned to conversation_orchestrator
- [✅] 2.7. Validate agent tools are properly mapped
- [✅] 2.8. Test the updated crew.py loads without errors

## 3. Enhance Conversation Orchestrator Agentmove to step 5 
- [✅] 3.1. Create backup of original agents.yaml
- [✅] 3.2. Update orchestrator backstory for dynamic routing
- [✅] 3.3. Ensure orchestrator has access to all necessary tools
- [✅] 3.4. Set allow_delegation=True for orchestrator (handled by crew.py)
- [✅] 3.5. Enhance orchestrator goal to emphasize capability-based routing
- [✅] 3.6. Add instructions about multi-step task handling
- [✅] 3.7. Validate the updated agents.yaml syntax

## 4. Revise main.py
- [✅] 4.1. Create backup of original main.py
- [✅] 4.2. Keep basic input handling mechanism
- [✅] 4.3. Keep kickoff() call with user_query input
- [✅] 4.4. Add basic input validation
- [✅] 4.5. Add better error handling
- [✅] 4.6. Test main.py loads without errors

## 5. Integration Testing
- [✅] 5.1. Test system initialization
- [✅] 5.2. Test basic query processing
- [✅] 5.3. Test dynamic agent selection
- [✅] 5.4. Test tool usage by various agents
- [✅] 5.5. Test knowledge access
- [✅] 5.6. Validate no hardcoded workflows remain

## 6. Documentation
- [✅] 6.1. Update CLAUDE.md with completed changes
- [✅] 6.2. Document the new system architecture
- [✅] 6.3. Document the minimal task structure
- [✅] 6.4. Document the orchestrator's enhanced capabilities
- [✅] 6.5. Document how to extend the system in the future

## Status Legend
- [ ] Not Started
- [🔄] In Progress
- [✅] Completed
- [⚠️] Needs Review

## Notes
- Last Updated: March 28, 2025
- Status: COMPLETED ✅
- All tasks have been completed successfully
- RetentionAnalysisTool has been removed as an additional simplification
- Documentation has been updated in CLAUDE.md with all implementation details
- Priority: Critical - Remove all hardcoded workflows
- Dependencies: CrewAI v0.108.0 technical requirements