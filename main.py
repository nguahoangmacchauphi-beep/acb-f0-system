from core.loop import run_loop

if __name__ == "__main__":
    input_data = {"message": "hello system"}
    result = run_loop(input_data)
    print(result)