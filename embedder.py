from sentence_transformers import SentenceTransformer
import torch

def embed_prompt_pairs(sent1, sent2):
    model = SentenceTransformer("sentence-transformers/LaBSE")
    emb1 = model.encode(sent1, convert_to_tensor=True)
    emb2 = model.encode(sent2, convert_to_tensor=True)
    features = torch.cat([emb1, emb2], dim=1)
    return features