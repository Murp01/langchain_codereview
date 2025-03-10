import os
import argparse
from review import get_code_reviewer

def main():
    parser = argparse.ArgumentParser(description="AI-Powered Code Review Tool")
    parser.add_argument("file", help="Path to the code file to review")
    parser.add_argument("--language", choices=["Python", "C#"], required=True, help="Programming language of the code")

    args = parser.parse_args()

    if not os.path.exists(args.file):
        print(f"Error: File '{args.file}' not found.")
        return

    reviewer = get_code_reviewer()
    print("Reviewing Code...")
    review_results = reviewer.analyze_code(args.file)
    
    output_file = os.path.join("reports", f"{os.path.basename(args.file)}_review.txt")
    os.makedirs("reports", exist_ok=True)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(review_results)

    print(f"✅ Code review completed. Results saved to {output_file}")

if __name__ == "__main__":
    main()