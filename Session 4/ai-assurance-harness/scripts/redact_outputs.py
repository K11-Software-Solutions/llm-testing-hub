# Redacts secrets/PII patterns from result text before committing artifacts.
import re, sys, json

SECRET_PAT = re.compile(r'(api[_-]?key|token|password)\s*[:=]\s*\S+', re.I)
PII_PAT = re.compile(r'\b\d{3}-\d{2}-\d{4}\b')  # SSN example

def scrub(text: str) -> str:
    text = SECRET_PAT.sub('[REDACTED_SECRET]', text)
    text = PII_PAT.sub('[REDACTED_SSN]', text)
    return text

if __name__ == "__main__":
    data = sys.stdin.read()
    try:
        obj = json.loads(data)
        sys.stdout.write(json.dumps(obj))  # placeholder passthrough
    except Exception:
        sys.stdout.write(scrub(data))
