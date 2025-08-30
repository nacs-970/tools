import time

def generate_code(num_lines: int) -> str:

    """Generate a large block of Python code as a string."""
    set_ = set(range(num_lines))

    # fast
    code_lines = [f"x{i} = {i} * {i}" for i in set_]

    # more complex
    #code_lines = [f"x{i} = {i}**2 + 2*{i}*{i} - {i}**2" for i in set_]

    return "\n".join(code_lines)

def test_compile_speed(num_lines: int = 1000000):
    
    print(f"Generating code with {num_lines} lines...")
    set_ = set(range(num_lines))

    # fast
    code = "\n".join([f"x{i} = {i} * {i}" for i in set_])

    # more complex
    #code = "\n".join([f"x{i} = {i}**2 + 2*{i}*{i} - {i}**2" for i in set_])

    #code = generate_code(num_lines)

    print("Compiling code...")
    start_time = time.perf_counter()
    compiled_code = compile(code, '<string>', 'exec')
    end_time = time.perf_counter()

    print(f"Compile time: {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    in_ = input("Input number of lines to generate (default = 1*10^6) : ")
    if not in_: in_ = 1000000
    test_compile_speed(int(in_))

