import json
import os
import matplotlib.pyplot as plt

def plot_scores(report_path):
    with open(report_path, 'r', encoding='utf-8') as f:
        if report_path.endswith('.json'):
            report = json.load(f)
        else:
            print("Visualization only supports JSON reports.")
            return

    # Try summary dict (old style)
    summary = report.get('summary', {}) if isinstance(report, dict) else {}
    categories = list(summary.keys())
    scores = [summary[cat].get('score', 0) for cat in categories]

    # If summary is empty, try list-of-dict (csv-like)
    if not categories and isinstance(report, list):
        categories = [row.get('category') for row in report if 'category' in row]
        # Try pass_rate as percent
        def parse_pass_rate(val):
            if isinstance(val, str) and val.endswith('%'):
                return float(val.strip('%'))
            try:
                return float(val) * 100 if float(val) <= 1 else float(val)
            except:
                return 0
        scores = [parse_pass_rate(row.get('pass_rate', 0)) for row in report if 'category' in row]
        ylabel = 'Pass Rate (%)'
        ylim = (0, 100)
    else:
        ylabel = 'Score'
        ylim = (0, 1)

    if not categories:
        print("No valid results found in file.")
        return
    plt.figure(figsize=(8, 4))
    plt.bar(categories, scores, color='skyblue')
    plt.ylim(*ylim)
    plt.ylabel(ylabel)
    plt.title('LLM Evaluation Results by Category')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Example usage: visualize.py results/distilbert-base-uncased-finetuned-sst-2-english_report.json
    import sys
    if len(sys.argv) < 2:
        print("Usage: python visualize.py <report.json>")
    else:
        plot_scores(sys.argv[1])
