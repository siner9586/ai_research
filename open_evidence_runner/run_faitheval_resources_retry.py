from __future__ import annotations

import audit_faitheval_resources as audit

# Exact redirect host observed in the first official Hugging Face download audit.
# No wildcard or unrelated Xet/CDN host is permitted.
audit.ALLOWED_HOSTS.add("us.aws.cdn.hf.co")

if __name__ == "__main__":
    audit.main()
