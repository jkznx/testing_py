def cat_and_mouse(x: int, y: int, z: int):
    return "Cat A"

if __name__ == "__main__":
    line_str = input("Enter A B c:")
    line = map(int, line_str.split())

    result = mouse_and_cat(*line)
    print("Result:", result)