import streamlit as st
from graph_builder import build_graph
import time
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

# 1. Professional Configuration
st.set_page_config(page_title="StoryTeller Enterprise AI", page_icon="🏢", layout="wide")

# 2. Corporate Professional Theme (Blue/Slate/White)
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    h1 { color: #1e3a8a; font-family: 'Helvetica Neue', sans-serif; font-weight: 700; }
    .report-card { 
        background: white; 
        padding: 30px; 
        border-radius: 10px; 
        border: 1px solid #e5e7eb;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        color: #374151;
    }
    .stButton>button {
        background-color: #2563eb;
        color: white;
        border-radius: 5px;
        width: 100%;
        height: 50px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Cache the Graph (Optimization)
@st.cache_resource
def get_graph():
    return build_graph()

st.title("💠 StoryTeller: Generative Agent System")
st.caption("Enterprise-grade autonomous orchestration for creative content generation.")

# 4. Input with Sidebar for Settings (Corporate style)
with st.sidebar:
    st.header("⚙️ Agent Settings")
    model_speed = st.select_slider("Creativity Level", options=["Low", "Medium", "High"])
    st.info("Using Gemini(Enterprise Tier)\n")

user_idea = st.text_area("Content Strategy / Story Brief:", 
                        placeholder="Define the core narrative or marketing story...",
                        height=100)

if st.button("🚀 Execute Agent Workflow"):
    if user_idea:
        try:
            workflow = get_graph()
            
            with st.status("🔗 Orchestrating AI Nodes...", expanded=True) as status:
                start_time = time.time()
                # Run the graph
                result = workflow.invoke({"user_input": user_idea, "history": []})
                duration = round(time.time() - start_time, 2)
                status.update(label=f"Execution Successful in {duration}s", state="complete")

            st.divider()
            
            # Layout: Text on Left, Image on Right (Standard Corporate Layout)
            col_text, col_img = st.columns([3, 2], gap="large")
            
            with col_text:
                if result.get("story_output"):
                    st.subheader("📄 Generated Narrative")
                    st.markdown(f'<div class="report-card">{result["story_output"]}</div>', unsafe_allow_html=True)
            
            with col_img:
                if result.get("image_url"):
                    st.subheader("🖼️ Visual Asset")
                    st.image(result["image_url"], caption="AI-Generated Visualization", width="stretch")
                else:
                    st.warning("Visual generation node skipped or failed.")

        except Exception as e:
            st.error(f"Critical System Error: {str(e)}")
            st.button("Retry Connection")
    else:
        st.warning("Input required to initialize agent.")

# 5. Professional Footer
st.markdown("<br><hr><center><small>© 2026 AI Solutions Corp | StoryTeller Agentic Unit</small></center>", unsafe_allow_html=True)