# One Line, One Laugh — writes a single 1-200 char line to /output/entry.txt.
import os

LINE = "I finally read the terms and conditions. Turns out I've been married to a free trial since 2019."

def main():
    # Exactly one line, no trailing whitespace beyond the newline.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
