import csv
import os

def convert():
    # 1. Get the full paths (handles paths with or without quotes)
    input_path = input("Enter the FULL PATH to your CSV file without the extension: ").strip().strip('"').strip("'")
    output_path = input("Enter the FULL PATH for the new file no m3u ending: ").strip().strip('"').strip("'")

    # 2. Automatically add extensions if missing
    if not input_path.lower().endswith('.csv'):
        input_path += '.csv'
    if not output_path.lower().endswith('.m3u'):
        output_path += '.m3u'

    if not os.path.exists(input_path):
        print(f"Error: Could not find file at {input_path}")
        return

    try:
        with open(input_path, mode='r', encoding='utf-8-sig') as f:
            rows = list(csv.reader(f))
            if not rows:
                print("Error: The file is empty.")
                return

            # Show the columns found in the first row
            headers = rows[0]
            print("\nFound these columns:")
            for i, h in enumerate(headers):
                print(f"[{i}] {h}")

            # 3. Ask for the column index (Default 1 for Track Name)
            col_input = input("\nEnter the column NUMBER for Track Name (default 1): ").strip()
            idx = int(col_input) if col_input.isdigit() else 1

            # 4. Write simple list to file (No #EXTM3U or #EXTINF tags)
            with open(output_path, mode='w', encoding='utf-8') as out_file:
                count = 0
                # Start from row 1 to skip the header
                for row in rows[1:]:
                    if len(row) > idx:
                        name = row[idx].strip()
                        if name:
                            out_file.write(f"{name}\n")
                            count += 1

        print(f"\nSuccess! {count} track names saved to: {output_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    convert()

