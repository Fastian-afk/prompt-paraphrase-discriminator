# 🤖 Multilingual Prompt Paraphrase Discriminator

A binary classifier that detects whether two prompts (in same or different languages) refer to the same visual concept. Uses LaBSE embeddings and a shallow neural network.

## 🔧 How It Works
- Embed both prompts using LaBSE
- Concatenate embeddings
- Train a 2-layer neural classifier
- Evaluate with ROC-AUC & accuracy

## 📊 Sample Output

Epoch 20 | Loss: 0.1509 | Acc: 1.000 | ROC-AUC: 1.000
💡 Technologies Used
SentenceTransformers (LaBSE)

PyTorch

scikit-learn

🧪 Use Cases
Prompt grounding consistency

Cross-lingual similarity scoring

Visual question answering

✍️ Author
Imaad Fazal – Knowledge Discovery & Data Science Lab, FAST-NUCES
