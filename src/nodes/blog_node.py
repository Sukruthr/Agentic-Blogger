from src.states.blog_state import BlogState

class BlogNode:
    """
    A class to represent the blog Node
    """
    
    def __init__(self, llm) -> None:
        self.llm = llm  

    def title_creation(self, state:BlogState):
        """
        create the title for a blog
        """
        if "topic" in state and state["topic"]:
            prompt="""
            You are an expert Blog Content Writer. Use Markdown Formatting. Generate a blog title for the {topic}. the Titile should be creative and SEO Friendly
            """
            system_message= prompt.format(topic=state["topic"])
            response = self.llm.invoke(system_message)

            return {"blog":{"title":response.content}}
        
    def content_generation(self, state:BlogState):
        """
        create the main content for the blog
        """

        if "topic" in state and state["topic"]:
            prompt="""
            You are an expert Blog Content Writer. Use Markdown Formatting. 
            Generate a detailed blog content with detailed breakdown for the {topic}.
            """
            system_message= prompt.format(topic=state["topic"])
            response = self.llm.invoke(system_message)

            return {"blog":{"content":response.content}} 