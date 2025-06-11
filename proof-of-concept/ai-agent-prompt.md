# AI Agent Prompt for User Management System

## Task Request
I need to create a complete user management system for a FastAPI application. This should include:

### Requirements:
1. **CRUD Operations**: Create, Read, Update, Delete users
2. **Authentication**: JWT-based authentication required for all endpoints
3. **Data Validation**: Proper input validation using Pydantic models
4. **Error Handling**: Comprehensive error handling with appropriate HTTP status codes
5. **Pagination**: Support for paginated user listing
6. **Search**: Basic search functionality for users
7. **Security**: Secure password handling and user authorization
8. **Testing**: Complete test suite for all endpoints

### Specific Endpoints Needed:
- `POST /api/v1/users` - Create new user
- `GET /api/v1/users` - List users (paginated, searchable)
- `GET /api/v1/users/{user_id}` - Get specific user
- `PUT /api/v1/users/{user_id}` - Update user
- `DELETE /api/v1/users/{user_id}` - Delete user

### Data Model:
```python
User:
  - id: int (auto-generated)
  - email: str (unique, validated)
  - username: str (unique, 3-50 chars)
  - full_name: str (optional)
  - is_active: bool (default: True)
  - is_admin: bool (default: False)
  - created_at: datetime (auto-generated)
  - updated_at: datetime (auto-updated)
```

### Technical Requirements:
- Use FastAPI with async/await patterns
- SQLAlchemy for database operations
- Pydantic for data validation
- JWT authentication middleware
- Proper logging for all operations
- Follow REST API best practices
- Include comprehensive docstrings
- Handle edge cases and validation errors

### Quality Standards:
- Code should be production-ready
- Follow PEP 8 style guidelines
- Include type hints throughout
- Proper error messages for users
- Security best practices implemented
- Performance optimized (database queries, caching where appropriate)

Please generate the complete FastAPI route implementation that meets all these requirements.
