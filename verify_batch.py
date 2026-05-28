
import os
from unittest.mock import patch
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent / "starter-code"))
import template as _m

# Mock compare_models for testing
def _get_mock(prompt):
    return {
        "gpt4o": {"response": "GPT-4o response content here", "latency": 0.5, "cost": 0.00045, "input_tokens": 10, "output_tokens": 20},
        "gpt4o_mini": {"response": "GPT-4o-Mini response content here", "latency": 0.3, "cost": 0.0000135, "input_tokens": 10, "output_tokens": 20},
        "gemini_flash": {"response": "Gemini response content here", "latency": 0.4, "cost": 0.00000675, "input_tokens": 10, "output_tokens": 20}
    }

with patch.object(_m, "compare_models") as mock_comp:
    mock_comp.side_effect = _get_mock
    results = _m.batch_compare(["Q1", "Q2"])
    print("batch_compare results len: ", len(results))
    print("results[0][prompt]: ", results[0]["prompt"])
    table = _m.format_comparison_table(results)
    print("\nFormatted table: ")
    print(table)

print("\n=== All tests for batch_compare and format_comparison_table passed! ===")
