from langgraph.graph import StateGraph, START, END
from state import StoryState
from orchestrator import orchestrator, routing
from story_writer import story_writer
from tools import generate_image

def image_node(state: StoryState):
    prompt = state.get("image_prompt", state["user_input"])
    try:
        url = generate_image.invoke({"prompt": prompt}) 
    except:
        url = generate_image.invoke(prompt)  
    state["image_url"] = url
    return state

def build_graph():
    workflow = StateGraph(StoryState)

    workflow.add_node("orchestrator", orchestrator)
    workflow.add_node("story_writer", story_writer)
    workflow.add_node("image_gen", image_node)


    workflow.add_edge(START, "orchestrator")
    workflow.add_edge("orchestrator", "story_writer")
    workflow.add_edge("story_writer", "image_gen")
    workflow.add_edge("image_gen", END)

    return workflow.compile()