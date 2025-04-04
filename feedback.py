import json
import time
from collections import defaultdict

class FeedbackSystem:
    def __init__(self, file_path="feedback_log.txt"):
        self.file_path = file_path
        self.feedback_log = defaultdict(list)
        self.load_feedback()  # Load existing feedback on startup

    def log_feedback(self, function_used, response, feedback):
        """Store user feedback for improvement and save to file."""
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        entry = {
            'timestamp': timestamp,
            'response': response,
            'feedback': feedback
        }
        self.feedback_log[function_used].append(entry)
        self.save_feedback()  # Save after each entry

    def save_feedback(self):
        """Save feedback to a text file in JSON format."""
        with open(self.file_path, "w") as f:
            json.dump(self.feedback_log, f, indent=4)

    def load_feedback(self):
        """Load feedback from a file if it exists."""
        try:
            with open(self.file_path, "r") as f:
                data = json.load(f)
                self.feedback_log = defaultdict(list, data)  # Restore as defaultdict
        except (FileNotFoundError, json.JSONDecodeError):
            self.feedback_log = defaultdict(list)  # Initialize if file is missing or corrupt

    def get_feedback_stats(self):
        """Return feedback statistics."""
        stats = {}
        for function, feedbacks in self.feedback_log.items():
            positive = sum(1 for f in feedbacks if f['feedback'].lower() == 'yes')
            total = len(feedbacks)
            stats[function] = {
                'positive': positive,
                'total': total,
                'percentage': (positive / total * 100) if total > 0 else 0
            }
        return stats

# Example Usage
if __name__ == "__main__":
    fs = FeedbackSystem()
    fs.log_feedback("summarize_text", "This is a summary", "yes")
    fs.log_feedback("generate_idea", "Here is an idea", "no")
    
    print(fs.get_feedback_stats())
