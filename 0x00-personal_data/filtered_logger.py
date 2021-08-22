#!/usr/bin/env python3
"""
"""
from typing import List
import re


def filter_datum(fields: List[str], redaction: str, message: str,
             separator: str) -> str:
    # task 0
    """
    returns the log message obfuscated
    fields: list of strings representing all fields to obfuscate
    redaction: string representing by what the field will be obfuscated
    message: string representing the log line
    separator: string representing by which character is separating all
               fields in the log line (message)
    """
    for field in fields:
        pattern = f"{field}=(.*\w){separator}"
        replace = f"{field}={redaction}"
        result = re.sub(str(pattern), replace, message)
    return result
