from langchain_google_genai import ChatGoogleGenerativeAI
from state import StoryState

llm = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview", 
    convert_system_message_to_human=True
)
#model="models/gemini-1.5-flash"


def orchestrator(state: StoryState):
    user_input = state["user_input"]
    prompt = f"Analyze this idea: {user_input}. Prepare a brief for a story and a visual prompt."
    response = llm.invoke(prompt)
    
    state["image_prompt"] = f"A professional digital art of: {user_input}"
    state["history"] = [response.content]
    return state

def routing(state: StoryState):
    if not state.get("story_output"):
        return "story"
    elif not state.get("image_url"):
        return "image"
    return "end"
