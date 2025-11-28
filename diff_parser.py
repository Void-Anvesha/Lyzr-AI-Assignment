import re

def parse_diff(diff_text):
    """
    Parses a raw git diff string into a structured format.
    Returns a list of dictionaries, each representing a file change.
    """
    files = []
    current_file = None
    
    # Split by the diff header for each file
    # This is a simplified parser. Robust parsing might need a library like unidiff, 
    # but we'll stick to a simple regex/split approach for now to avoid extra dependencies if possible,
    # or just use simple string manipulation.
    
    # A diff usually starts with "diff --git a/... b/..."
    # We can split by "\ndiff --git "
    
    chunks = diff_text.split('\ndiff --git ')
    
    # The first chunk might be empty or contain the first file if it doesn't start with newline (it usually does if we split right)
    # Actually, let's iterate line by line for better control.
    
    lines = diff_text.split('\n')
    current_file_data = []
    filename = None
    
    for line in lines:
        if line.startswith('diff --git'):
            if filename and current_file_data:
                files.append({
                    'filename': filename,
                    'patch': '\n'.join(current_file_data)
                })
            
            # Extract filename from "diff --git a/path/to/file b/path/to/file"
            parts = line.split(' ')
            if len(parts) >= 4:
                # usually parts[2] is a/..., parts[3] is b/...
                # We want the b/ path usually, or just the path.
                # Let's try to grab it from the b/ part
                b_part = parts[-1]
                if b_part.startswith('b/'):
                    filename = b_part[2:]
                else:
                    filename = b_part # Fallback
            
            current_file_data = [line]
        else:
            if filename:
                current_file_data.append(line)
                
    # Add the last file
    if filename and current_file_data:
        files.append({
            'filename': filename,
            'patch': '\n'.join(current_file_data)
        })
        
    return files
