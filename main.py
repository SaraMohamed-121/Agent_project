from graph_builder import build_graph
from state import StoryState

graph = build_graph()
state = StoryState()
user_input = input("User: ")
state["user_input"] = user_input
result = graph.invoke(state)

if result.get("story_output"):
    print("\nStory:\n")
    print(result["story_output"])

elif result.get("image_url"):
    print("\nImage URL:\n")
    print(result["image_url"])