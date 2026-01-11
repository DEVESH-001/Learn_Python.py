# Tuples: Immutable ordered collections
# Tuples are similar to lists, but they cannot be changed after creation (immutable).
# Tuples are defined using parentheses ().

ai_agents = ("ChatGPT", "Claude", "Gemini")  # Tuple literal

(first_agent, second_agent, third_agent) = ai_agents  # Unpacking tuple into variables

print(f"First AI Agent: {first_agent}, Second AI Agent: {second_agent}, Third AI Agent: {third_agent}")

chatGpt_ration, claude_ration, gemini_ration = (9.5, 10, 8)  # Unpacking with ratios
print(f"AI Agent Ratios - ChatGPT: {chatGpt_ration}, Claude: {claude_ration}, Gemini: {gemini_ration}")

chatGpt_ration, claude_ration, gemini_ration = gemini_ration, claude_ration, chatGpt_ration  # Swapping values using tuple unpacking
print(f"After Swapping - ChatGPT: {chatGpt_ration}, Claude: {claude_ration}, Gemini: {gemini_ration}")

# MemberShip: Checking if an element exists in a tuple

print(f"Is 'Claude' an AI Agent? {'Claude' in ai_agents}")  # True
print(f"Is 'Meta' an AI Agent? {'Meta' in ai_agents}")      # False