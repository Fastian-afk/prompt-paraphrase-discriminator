import torch.nn as nn

class ParaphraseClassifier(nn.Module):
    def __init__(self, input_dim=1536):
        super().__init__()
        self.fc = nn.Sequential(
            nn.Linear(input_dim, 256),
            nn.ReLU(),
            nn.Linear(256, 1)
        )

    def forward(self, x):
        return self.fc(x)