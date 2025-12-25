from sentence_transformers import SentenceTransformer, util

# Load the model once to improve performance
model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

def get_similarity(text1, text2):
    """
    Calculates the semantic similarity score between two texts 
    using a multilingual Transformer model.
    """
    try:
        if not text1 or not text2:
            return 0.0
            
        # Encode both texts into embeddings
        embeddings1 = model.encode(text1, convert_to_tensor=True)
        embeddings2 = model.encode(text2, convert_to_tensor=True)
        
        # Compute cosine similarity
        cosine_score = util.cos_sim(embeddings1, embeddings2)
        
        return float(cosine_score)
    except Exception as e:
        print(f"Similarity Calculation Error: {e}")
        return 0.0