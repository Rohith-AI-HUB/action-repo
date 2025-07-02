# Action Repository

This repository is configured to send webhook events to a Flask application whenever certain GitHub actions occur.

## Purpose

This repository serves as the source for GitHub webhook events including:
- **Push events** - When code is pushed to any branch
- **Pull Request events** - When pull requests are created, updated, or closed
- **Merge events** - When pull requests are merged

## Repository Structure

```
action-repo/
├── README.md           # This file
├── src/
│   ├── main.py        # Sample Python application
│   ├── utils.py       # Utility functions
│   └── config.py      # Configuration file
├── docs/
│   └── api.md         # API documentation
├── tests/
│   └── test_main.py   # Unit tests
└── .gitignore         # Git ignore file
```

## Sample Application

This repository contains a simple Python application that demonstrates basic functionality. The application is designed to generate meaningful commits and changes that will trigger webhook events.

## Webhook Configuration

This repository is configured to send webhooks to: `https://your-webhook-endpoint.ngrok.io/webhook`

### Events Monitored:
- Push to any branch
- Pull request creation
- Pull request updates
- Pull request merges

## Usage

### Creating Push Events
```bash
# Make changes to any file
echo "# New feature" >> src/main.py
git add .
git commit -m "Add new feature"
git push origin main
```

### Creating Pull Request Events
```bash
# Create a new branch
git checkout -b feature-branch

# Make changes
echo "print('New feature')" >> src/main.py
git add .
git commit -m "Implement new feature"
git push origin feature-branch

# Create pull request via GitHub UI
# From: feature-branch
# To: main
```

### Testing Different Branches
```bash
# Create development branch
git checkout -b development
echo "print('Development code')" >> src/utils.py
git add .
git commit -m "Add development utilities"
git push origin development

# Create staging branch
git checkout -b staging
echo "print('Staging code')" >> src/config.py
git add .
git commit -m "Update staging configuration"
git push origin staging
```

## Sample Commits for Testing

Use these sample commits to generate webhook events:

1. **Feature additions**:
   ```bash
   git commit -m "feat: add user authentication"
   git commit -m "feat: implement data validation"
   ```

2. **Bug fixes**:
   ```bash
   git commit -m "fix: resolve login issue"
   git commit -m "fix: handle edge case in data processing"
   ```

3. **Documentation updates**:
   ```bash
   git commit -m "docs: update API documentation"
   git commit -m "docs: add usage examples"
   ```

## Contributors

- Travis (Sample contributor for webhook testing)
- Your Name

## Notes

- This repository is specifically designed for webhook testing
- Make sure your webhook endpoint is properly configured before testing
- Check your webhook-repo application to see events being received and displayed