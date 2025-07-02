# API Documentation

## Sample Application API

This document describes the sample application's basic functionality and structure.

### Main Functions

#### `main()`
- **Purpose**: Application entry point
- **Parameters**: None
- **Returns**: None
- **Description**: Initializes the application and handles user interaction

#### `greet_user(name)`
- **Purpose**: Greet user with personalized message
- **Parameters**: 
  - `name` (string): User's name
- **Returns**: None
- **Description**: Displays greeting and performs sample calculations

#### `calculate_example()`
- **Purpose**: Demonstrate basic calculations
- **Parameters**: None
- **Returns**: None
- **Description**: Performs sum and average calculations on sample data

### Utility Functions

#### `get_current_time()`
- **Purpose**: Get current UTC timestamp
- **Parameters**: None
- **Returns**: String formatted timestamp
- **Format**: "YYYY-MM-DD HH:MM:SS UTC"

#### `validate_input(user_input)`
- **Purpose**: Validate user input string
- **Parameters**:
  - `user_input` (string): Input to validate
- **Returns**: Boolean (True if valid, False otherwise)
- **Validation Rules**:
  - Must be non-empty string
  - Contains only letters, spaces, dots, hyphens, underscores

#### `format_message(message, author="System")`
- **Purpose**: Format message with timestamp and author
- **Parameters**:
  - `message` (string): Message content
  - `author` (string): Message author (default: "System")
- **Returns**: Formatted string
- **Format**: "[timestamp] author: message"

#### `calculate_statistics(numbers)`
- **Purpose**: Calculate basic statistics
- **Parameters**:
  - `numbers` (list): List of numbers
- **Returns**: Dictionary with statistics
- **Statistics Included**:
  - count
  - sum
  - average
  - min
  - max

#### `process_data(data)`
- **Purpose**: Process data (convert strings to uppercase)
- **Parameters**:
  - `data` (various): Data to process
- **Returns**: Processed data
- **Behavior**:
  - Lists: Process each string element
  - Strings: Convert to uppercase
  - Other types: Return unchanged

#### `log_event(event_type, message)`
- **Purpose**: Log events with timestamp
- **Parameters**:
  - `event_type` (string): Type of event
  - `message` (string): Event message
- **Returns**: Formatted log entry string
- **Format**: "[timestamp] EVENT_TYPE: message"

### Configuration

#### Application Settings
- `APP_NAME`: "GitHub Webhook Test Application"
- `VERSION`: "1.0.0" 
- `DEBUG_MODE`: True
- `LOG_LEVEL`: "INFO"

#### Feature Flags
- `user_authentication`: Enabled
- `data_validation`: Enabled
- `advanced_logging`: Disabled
- `experimental_features`: Disabled

#### Webhook Information
- **Supported Events**: push, pull_request, merge
- **Content Type**: application/json
- **Endpoint**: Configurable webhook URL

### Usage Examples

#### Running the Application
```python
python src/main.py
```

#### Importing Utilities
```python
from utils import get_current_time, validate_input
from config import APP_NAME, VERSION

# Get current time
timestamp = get_current_time()

# Validate input
is_valid = validate_input("John Doe")

# Access configuration
app_info = f"{APP_NAME} v{VERSION}"
```

### Error Handling

The application includes basic error handling:
- Input validation prevents invalid data processing
- System exit on invalid input
- Graceful handling of empty data sets in statistics calculations

### Testing Scenarios

This application is designed to generate various webhook events:

1. **Push Events**: Modify any source file and commit
2. **Pull Request Events**: Create feature branches and open PRs
3. **Merge Events**: Merge pull requests

### Sample Commit Messages for Testing

- `feat: add user authentication`
- `fix: resolve input validation issue`
- `docs: update API documentation`
- `refactor: improve data processing`
- `test: add unit tests for utilities`