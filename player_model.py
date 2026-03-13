import torch

HIDDEN_DIM = 1

def weight_init(model):
  torch.nn.init.orthogonal_(model.weight.data)
  model.bias.data.fill_(0.0)

class PlayerStrategyModel(torch.nn.Module):
    def __init__(self):
        self.backbone_1 = torch.nn.Linear(11 + 4 + 3, HIDDEN_DIM)
        self.backbone_2 = torch.nn.Linear(HIDDEN_DIM, HIDDEN_DIM)
        self.backbone_3 = torch.nn.Linear(HIDDEN_DIM, HIDDEN_DIM)
        self.is_throwing_head = torch.nn.Linear(HIDDEN_DIM, 1)
        self.choosing_layer = torch.nn.Linear(HIDDEN_DIM, 2) 
        self.relu = torch.nn.ReLu()

        self.backbone_1.apply(weight_init)
        self.backbone_2.apply(weight_init)
        self.backbone_3.apply(weight_init)
        self.is_throwing_head.apply(weight_init)
        self.choosing_layer.apply(weight_init)


    
    def forward(self, x):
        x = self.relu(self.backbone_1(x))
        x = self.relu(self.backbone_2(x))
        x = self.relu(self.backbone_3(x))
        throwing_log_probs = self.is_throwing_head(x)
        choosing_dice = self.choosing_layer(x)

        return throwing_log_probs, choosing_dice