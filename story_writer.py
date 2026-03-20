from langchain_google_genai import ChatGoogleGenerativeAI
from state import StoryState

llm = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview", 
    convert_system_message_to_human=True
)
#model="models/gemini-1.5-flash"

def story_writer(state: StoryState):

    prompt = f"""
    Write a short creative story based on:

    {state['user_input']}
    """

    response = llm.invoke(prompt)
    state["story_output"] = response.content

    return state