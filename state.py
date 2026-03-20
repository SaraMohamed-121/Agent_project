from typing import TypedDict, Optional, List

class StoryState(TypedDict, total=False):
    user_input: str
    story_output: Optional[str]
    image_prompt: Optional[str]
    image_url: Optional[str]
    history: List[str]