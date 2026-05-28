
import os
import sys
from pathlib import Path

# Add starter-code to path so we can import template
sys.path.insert(0, str(Path(__file__).parent / "starter-code"))

# First set dummy environment variables for tests and testing
os.environ["OPENAI_API_KEY"] = "dummy-key"
os.environ["GEMINI_API_KEY"] = "dummy-key"
os.environ["ANTHROPIC_API_KEY"] = "dummy-key"

print("=== Task 2.1 - Temperature Sensitivity (with mocks!")
print("Let's write a small mock function with mocks!")
from unittest.mock import MagicMock, patch
import template as _m


print("\n=== Task 2.1 - Temperature Sensitivity (simulated!")
with patch("openai.OpenAI") as MockOpenAI:
    mock_client = MagicMock()
    MockOpenAI.return_value = mock_client
    mock_client.chat.completions.create.side_effect = [
        MagicMock(
            choices=[MagicMock(message=MagicMock(content=f"Response T=0: Việt Nam có độ dài bờ biển 3,260 km"))],
            usage=MagicMock(prompt_tokens=10, completion_tokens=20)
        ),
        MagicMock(
            choices=[MagicMock(message=MagicMock(content=f"Response T=0.5: Việt Nam có quê hương của phở"))],
            usage=MagicMock(prompt_tokens=10, completion_tokens=20)
        ),
        MagicMock(
            choices=[MagicMock(message=MagicMock(content=f"Response T=1: Việt Nam có 63 tỉnh thành!"))],
            usage=MagicMock(prompt_tokens=10, completion_tokens=20)
        ),
        MagicMock(
            choices=[MagicMock(message=MagicMock(content=f"Response T=1.5: Việt Nam, ngôi nhà của tôi có một chú mèo tên Mimi!"))],
            usage=MagicMock(prompt_tokens=10, completion_tokens=20)
        )
    ]
    prompt = "Hãy kể cho tôi một sự thật thú vị về Việt Nam."
    print(f"\nT=0.0:", _m.call_openai(prompt, temperature=0.0)[0])
    print(f"T=0.5:", _m.call_openai(prompt, temperature=0.5)[0])
    print(f"T=1.0:", _m.call_openai(prompt, temperature=1.0)[0])
    print(f"T=1.5:", _m.call_openai(prompt, temperature=1.5)[0])
    print("\nQuy luật: Temperature thấp (0.0) phản hồi nhất quán, không thay đổi; temperature cao (1.0-1.5) phản hồi sáng tạo hơn, có thể khác nhau nhiều")
    print("\nChatbot hỗ trợ khách hàng: Temperature = 0.2-0.5, vì cần phản hồi chính xác, nhất quán")

print("\n=== Task 2.2 - Đánh Đổi Chi Phí!")
users = 10000
calls_per_user = 3
tokens_per_call = 350
# Let's calculate with 50% input, 50% output for simplicity? Wait, 350 = 175 input + 175 output!
input_tokens = 175
output_tokens = 175
from starter-code.template import PRICING_1M_TOKENS as pricing

cost_gpt4o = ( (input_tokens * pricing["gpt-4o"]["input"] + output_tokens * pricing["gpt-4o"]["output"]) / 1000000) * users * calls_per_user
cost_gpt4o_mini = ((input_tokens * pricing["gpt-4o-mini"]["input"] + output_tokens * pricing["gpt-4o-mini"]["output"]) / 1000000 * users * calls_per_user
print(f"Chi phí GPT-4o: ${cost_gpt4o:.2f}")
print(f"Chi phí GPT-4o-mini: ${cost_gpt4o_mini:.2f}")
print(f"GPT-4o đắt gấp: {cost_gpt4o / cost_gpt4o_mini:.1f} lần!")

print("\n=== Task 2.3 - Streaming!")
print("Streaming quan trọng nhất khi người dùng cần phản hồi tức thì (chatbot hỗ trợ, trả lời câu hỏi, viết nội dung!")


