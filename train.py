import torch
import torch.optim as optim
from loss import DetectionLoss
from model import MrEngineerMan
from dataloader import MrDataHead

# Hyperparameters
num_epochs = 10
learning_rate = 0.001

# Device configuration
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Initialize the model
model = MrEngineerMan().to(device)

# Loss and Optimizer
criterion = DetectionLoss().to(device)
optimizer = optim.Adam(model.parameters(), lr=learning_rate)

# Load data
train_loader = MrDataHead()

# Training loop
def train_the_engineer():
    model.train()  # Set model to training mode
    for epoch in range(num_epochs):
        print("COCK")
        for i, (images, labels) in enumerate(train_loader):
            images = images.to(device)
            labels = labels.to(device)
            
            # Forward pass
            outputs = model(images)
            loss = criterion(outputs, labels)
            
            # Backward and optimize
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            
            if (i+1) % 10 == 0:
                print(f'Epoch [{epoch+1}/{num_epochs}], Step [{i+1}/{len(train_loader)}], Loss: {loss.item():.4f}')
                
        print(f"Ending Epoch {epoch+1} with Loss {loss.item():.4f}")

# Save the model checkpoint
def save_the_wisdom():
    torch.save(model.state_dict(), 'mr_engineerman.ckpt')
    print("Wisdom stored safely in 'mr_engineerman.ckpt'")

if __name__ == '__main__':
    train_the_engineer()
    save_the_wisdom()