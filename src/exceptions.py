import traceback
from typing import Any, Optional

def format_exception(exc):
    """Formats an exception into a readable string."""
    tb = exc.__traceback__ #get the traceback object from the exception
    
    if tb is None:
        return str(exc)
    
    #get the summary from traceback object
    tb_summary = traceback.extract_tb(tb)
    
    if not tb_summary:
        return str(exc)
    
    last_frame = tb_summary[-1]
    filename = last_frame.filename
    lineno = last_frame.lineno
    funcname = last_frame.name

    return f"Exception occurred in {funcname} at {filename}:{lineno}\n{str(exc)}"


class CustomException(Exception):
    def __init__(self, message, exc):

        if exc is not None:
            detail = format_exception(exc)
        else:
            detail = message or "No additional exception information available."

        super().__init__(detail)

        self.original_exception = exc
        self.detailed_message = detail

    def __str__(self):
        return self.detailed_message