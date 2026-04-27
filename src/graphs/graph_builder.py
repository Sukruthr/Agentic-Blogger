from langgraph.graph import START, END, StateGraph
from src.llms.groq_llm import GroqLLLM
from src.states.blog_state import BlogState
from src.nodes.blog_node import BlogNode

class GraphBuilder:
    def __init__(self, llm) -> None:
        self.llm = llm
        self.graph = StateGraph(BlogState)

    def build_topic_graph(self):
        """
        Build a graph to generate blogs based on topics
        """

        # build node
        self.blog_node = BlogNode(self.llm)

        # add nodes
        self.graph.add_node("title_creation",self.blog_node.title_creation)
        self.graph.add_node("content_generation",self.blog_node.content_generation)

        # add edges
        self.graph.add_edge(START,"title_creation")
        self.graph.add_edge("title_creation", "content_generation")
        self.graph.add_edge("content_generation", END)

        return self.graph
    
    def setup_graph(self, usecase):
        """
        Setup the graph based on usecase
        """
        if usecase == "topic":
            self.build_topic_graph()
