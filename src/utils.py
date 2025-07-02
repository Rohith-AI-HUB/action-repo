#!/usr/bin/env python3
"""
Utility functions for the sample application
"""

import re
from datetime import datetime, timezone


def get_current_time():
    """Return current timestamp in UTC"""
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')


def validate_input(user_input):
    """Validate user input - basic string validation"""
    if not user_input or not isinstance(user_input, str):
        return False
    
    # Check if input contains only letters, spaces, and common punctuation
    pattern = r'^[a-zA-Z\s\.\-\_]+$'
    return bool(re.match(pattern, user_input.strip()))


def format_message(message, author="System"):
    """Format a message with timestamp and author"""
    timestamp = get_current_time()
    return f"[{timestamp}] {author}: {message}"


def calculate_statistics(numbers):
    """Calculate basic statistics for a list of numbers"""
    if not numbers:
        return {}
    
    return {
        'count': len(numbers),
        'sum': sum(numbers),
        'average': sum(numbers) / len(numbers),
        'min': min(numbers),
        'max': max(numbers)
    }


def process_data(data):
    """Sample data processing function"""
    if isinstance(data, list):
        return [item.upper() if isinstance(item, str) else item for item in data]
    elif isinstance(data, str):
        return data.upper()
    else:
        return data


def log_event(event_type, message):
    """Log events with timestamp"""
    timestamp = get_current_time()
    log_entry = f"[{timestamp}] {event_type.upper()}: {message}"
    print(log_entry)
    return log_entry