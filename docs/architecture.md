# Legacy Modernization Agent Architecture

Legacy system modernization agent that analyzes monolithic applications, identifies microservice boundaries using domain-driven design, generates strangler fig migration strategies, and produces modernized implementations while maintaining business continuity.

## Domain Tools

- **analyze_monolith**: Analyze monolithic codebase for coupling, cohesion, and boundaries
- **identify_bounded_contexts**: Identify DDD bounded contexts and aggregate roots
- **generate_extraction_plan**: Plan microservice extraction using strangler fig pattern
- **generate_anti_corruption_layer**: Generate ACL between legacy and new service
- **generate_data_migration**: Generate data migration from monolith to microservice database
- **assess_modernization_roi**: Calculate ROI and risk of modernization effort