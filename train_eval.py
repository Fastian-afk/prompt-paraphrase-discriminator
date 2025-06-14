import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.metrics import accuracy_score, roc_auc_score

def train_classifier(model, features, labels_tensor, epochs=20):
    criterion = nn.BCEWithLogitsLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    for epoch in range(epochs):
        model.train()
        optimizer.zero_grad()
        outputs = model(features)
        loss = criterion(outputs, labels_tensor)
        loss.backward()
        optimizer.step()

        preds = torch.sigmoid(outputs).detach().numpy()
        pred_labels = (preds > 0.5).astype(int)

        acc = accuracy_score(labels_tensor.numpy(), pred_labels)
        roc = roc_auc_score(labels_tensor.numpy(), preds)

        print(f"Epoch {epoch+1} | Loss: {loss.item():.4f} | Acc: {acc:.3f} | ROC-AUC: {roc:.3f}")