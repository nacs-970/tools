from time import perf_counter
from platform import platform, machine, python_compiler

def test_compile_speed(num_lines: int = 1000000):
    print("====== Hardware Info ======")
    print("Platform :", platform())
    print("Architecture :", machine())
    print("Compiler :", python_compiler())
    print("---------------------------")
    
    print(f"Generating code with {num_lines} lines...")
    set_ = set(range(num_lines))

    # fast
    code = "\n".join([f"x{i} = {i} * {i}" for i in set_])

    # more complex
    #code = "\n".join([f"x{i} = {i}**2 + 2*{i}*{i} - {i}**2" for i in set_])

    #code = generate_code(num_lines)

    print("done")
    print("Compiling code...")
    start_time = perf_counter()
    compiled_code = compile(code, '<string>', 'exec')
    end_time = perf_counter()
    print("done")

    print(f"Compile time: {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    in_ = input("Input number of lines to generate (default = 1*10^6) : ")
    if not in_: in_ = 1000000
    test_compile_speed(int(in_))

