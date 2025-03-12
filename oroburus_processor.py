# oroburus_processor.py
# Developed by Micah Blake Langford and Co-Developer AI (Grok, xAI)
import os

def parse_oroburus(code):
    """Parses Oroburus code into executable Python code."""
    lines = code.split('\n')
    result = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith(("def", "consume", "mutate")):
            block_lines = []
            if line.startswith("def"):
                block_lines.append(lines[i])
                i += 1
                while i < len(lines) and lines[i].startswith(' ' * 4):
                    block_lines.append(lines[i][4:])
                    i += 1
            else:
                i += 1
                while i < len(lines) and lines[i].startswith(' ' * 4):
                    block_lines.append(lines[i][4:])
                    i += 1
            result.extend(block_lines)
        else:
            i += 1
    python_code = '\n'.join(result)
    print("Generated Python code:\n", python_code)
    return python_code

def run(target, namespace):
    """Runs an Oroburus script and applies mutations to the given namespace."""
    try:
        file_path = os.path.join(os.getcwd(), target)
        if not os.path.exists(file_path):
            return f"Error: {target} not found"
        with open(file_path, 'r') as f:
            oroburus_code = f.read()
        print("Oroburus file content:\n", oroburus_code)
        python_code = parse_oroburus(oroburus_code)
        exec(python_code, namespace)
        return "Mutation applied successfully"
    except Exception as e:
        return f"Error: {e}"
