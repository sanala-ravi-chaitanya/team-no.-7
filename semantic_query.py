"""
Enhanced Semantic Query Engine for Kisan Call Centre
Provides fuzzy matching and relevance scoring for agricultural queries
"""
from difflib import SequenceMatcher

class SemanticQuery:
    def __init__(self):
        # Expanded KCC dataset with more agricultural queries
        self.index = [
            {
                "question": "How to improve soil fertility?",
                "answer": "Use compost, green manure, and organic fertilizers regularly. Rotate crops to maintain soil health.",
                "keywords": ["soil", "fertility", "compost", "manure", "fertilizer"]
            },
            {
                "question": "Best fertilizer for rice?",
                "answer": "Apply Urea + DAP based on soil test recommendations. Use NPK ratio of 4:2:1 for optimal growth.",
                "keywords": ["fertilizer", "rice", "urea", "dap", "npk"]
            },
            {
                "question": "How to control pests in cotton?",
                "answer": "Use neem oil spray or recommended pesticides as per agriculture guidelines. Implement integrated pest management.",
                "keywords": ["pest", "cotton", "neem", "pesticide", "control"]
            },
            {
                "question": "When to plant wheat?",
                "answer": "Optimal sowing time is mid-October to mid-November. Ensure soil temperature is around 20-25°C.",
                "keywords": ["wheat", "plant", "sowing", "timing", "season"]
            },
            {
                "question": "How to increase crop yield?",
                "answer": "Use quality seeds, proper irrigation, balanced fertilization, and timely pest control. Follow recommended spacing.",
                "keywords": ["yield", "crop", "production", "increase", "harvest"]
            },
            {
                "question": "What is drip irrigation?",
                "answer": "Drip irrigation delivers water directly to plant roots, saving water and increasing efficiency by 40-70%.",
                "keywords": ["drip", "irrigation", "water", "efficient", "saving"]
            },
            {
                "question": "How to prevent crop diseases?",
                "answer": "Use disease-resistant varieties, crop rotation, proper spacing, and timely fungicide application when needed.",
                "keywords": ["disease", "prevention", "fungicide", "resistant", "crop"]
            },
            {
                "question": "Best time for harvesting paddy?",
                "answer": "Harvest when 80-85% of grains turn golden yellow, typically 30-35 days after flowering.",
                "keywords": ["harvest", "paddy", "rice", "timing", "maturity"]
            }
        ]
    
    def calculate_similarity(self, query, text):
        """Calculate similarity score between query and text using SequenceMatcher"""
        return SequenceMatcher(None, query.lower(), text.lower()).ratio()
    
    def search(self, query, top_k=3, min_score=0.2):
        """
        Search for relevant answers using fuzzy matching
        
        Args:
            query: User's search query
            top_k: Number of top results to return
            min_score: Minimum relevance score (0-1)
        
        Returns:
            List of matching items sorted by relevance
        """
        query = query.lower()
        results = []
        
        for item in self.index:
            # Calculate similarity scores
            question_score = self.calculate_similarity(query, item["question"])
            answer_score = self.calculate_similarity(query, item["answer"]) * 0.5  # Weight answer less
            
            # Check keyword matches
            keyword_matches = sum(1 for keyword in item["keywords"] if keyword in query)
            keyword_score = keyword_matches / len(item["keywords"]) * 0.3
            
            # Combined relevance score
            relevance = question_score + answer_score + keyword_score
            
            if relevance >= min_score:
                results.append({
                    "question": item["question"],
                    "answer": item["answer"],
                    "relevance": relevance
                })
        
        # Sort by relevance (highest first) and return top_k results
        results.sort(key=lambda x: x["relevance"], reverse=True)
        return results[:top_k]
