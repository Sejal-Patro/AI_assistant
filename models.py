from transformers import pipeline
import torch

class AIModels:
    def __init__(self):
        self.models_loaded = False
        self.load_models()

    def load_models(self):
        """Initialize all AI models"""
        print("Loading AI models... (This may take a few minutes)")

        try:
            # **Proper Question Answering Model**
            self.qa_model = pipeline(
                "question-answering",
                model="deepset/roberta-base-squad2",
                device=0 if torch.cuda.is_available() else -1  # Use GPU if available
            )

            # **Text Summarization Model**
            self.summarization_model = pipeline(
                "summarization",
                model="facebook/bart-large-cnn",
                device=0 if torch.cuda.is_available() else -1
            )

            # **Creative Text Generation Model**
            self.creative_model = pipeline(
                "text-generation",
                model="gpt2",
                device=0 if torch.cuda.is_available() else -1,
                torch_dtype=torch.float32
            )

            self.models_loaded = True
            print("All models loaded successfully!")

        except Exception as e:
            print(f"Error loading models: {e}")

    def answer_question(self, question):
        """Answer factual questions accurately"""
        if not self.models_loaded:
            return "Models not loaded. Please try again later."

        try:
            # Context for factual accuracy (Optional: You can fetch real data)
            context = "Paris is the capital of France. The Eiffel Tower is located in Paris."
            
            response = self.qa_model(question=question, context=context)

            return response['answer'] if response['score'] > 0.2 else "Sorry, I couldn't find a reliable answer."

        except Exception as e:
            print(f"Error answering question: {e}")
            return "Sorry, I couldn't answer that question."

    def summarize_text(self, text):
        """Summarize provided text"""
        if not self.models_loaded:
            return "Models not loaded. Please try again later."

        try:
            # Truncate very long text
            if len(text) > 2000:
                text = text[:2000] + "... [truncated]"

            summary = self.summarization_model(
                text,
                max_length=150,
                min_length=30,
                do_sample=False
            )
            return summary[0]['summary_text']
        except Exception as e:
            print(f"Summarization error: {e}")
            return "I couldn't summarize that text. Please try again."

    def generate_content(self, prompt):
        """Generate creative content"""
        if not self.models_loaded:
            return "Models not loaded. Please try again later."

        try:
            response = self.creative_model(
                prompt,
                max_length=200,
                num_return_sequences=1,
                temperature=0.9
            )
            return response[0]['generated_text']
        except Exception as e:
            print(f"Generation error: {e}")
            return "Sorry, I couldn't generate content for that prompt."
