import torch
import torch.nn as nn
import torch.optim as optim
import torchvision.transforms as transforms
from torch.utils.data import DataLoader, Dataset
import numpy as np
import cv2
import os
from glob import glob

# UNET Model Definition
class UNet(nn.Module):
    def __init__(self, in_channels=3, out_channels=1):
        super(UNet, self).__init__()
        
        def conv_block(in_c, out_c):
            return nn.Sequential(
                nn.Conv2d(in_c, out_c, kernel_size=3, padding=1),
                nn.ReLU(inplace=True),
                nn.Conv2d(out_c, out_c, kernel_size=3, padding=1),
                nn.ReLU(inplace=True)
            )
        
        self.encoder = nn.ModuleList([
            conv_block(in_channels, 64),
            conv_block(64, 128),
            conv_block(128, 256),
            conv_block(256, 512),
            conv_block(512, 1024),
        ])
        
        self.pool = nn.MaxPool2d(2)
        
        self.upconv = nn.ModuleList([
            nn.ConvTranspose2d(1024, 512, kernel_size=2, stride=2),
            nn.ConvTranspose2d(512, 256, kernel_size=2, stride=2),
            nn.ConvTranspose2d(256, 128, kernel_size=2, stride=2),
            nn.ConvTranspose2d(128, 64, kernel_size=2, stride=2)
        ])
        
        self.decoder = nn.ModuleList([
            conv_block(1024, 512),
            conv_block(512, 256),
            conv_block(256, 128),
            conv_block(128, 64)
        ])
        
        self.final_conv = nn.Conv2d(64, out_channels, kernel_size=1)
        
    def forward(self, x):
        encoder_outs = []
        for enc in self.encoder:
            x = enc(x)
            encoder_outs.append(x)
            x = self.pool(x)
        
        x = encoder_outs.pop()
        
        for up, dec in zip(self.upconv, self.decoder):
            x = up(x)
            enc_out = encoder_outs.pop()
            x = torch.cat([x, enc_out], dim=1)
            x = dec(x)
        
        return torch.sigmoid(self.final_conv(x))

# Custom Dataset
class SegmentationDataset(Dataset):
    def __init__(self, image_paths, mask_paths, transform=None):
        self.image_paths = image_paths
        self.mask_paths = mask_paths
        self.transform = transform
    
    def __len__(self):
        return len(self.image_paths)
    
    def __getitem__(self, idx):
        img = cv2.imread(self.image_paths[idx])
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        mask = cv2.imread(self.mask_paths[idx], cv2.IMREAD_GRAYSCALE)
        
        img = cv2.resize(img, (256, 256))
        mask = cv2.resize(mask, (256, 256))
        
        img = img / 255.0
        mask = mask / 255.0
        
        img = np.transpose(img, (2, 0, 1)).astype(np.float32)
        mask = np.expand_dims(mask, axis=0).astype(np.float32)
        
        return torch.tensor(img), torch.tensor(mask)

# Load Dataset
image_paths = sorted(glob("path/to/images/*.jpg"))
mask_paths = sorted(glob("path/to/masks/*.png"))

dataset = SegmentationDataset(image_paths, mask_paths)
dataloader = DataLoader(dataset, batch_size=4, shuffle=True)

# Training Setup
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = UNet().to(device)
criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=1e-4)

def train(model, dataloader, criterion, optimizer, epochs=10):
    model.train()
    for epoch in range(epochs):
        epoch_loss = 0
        for img, mask in dataloader:
            img, mask = img.to(device), mask.to(device)
            optimizer.zero_grad()
            output = model(img)
            loss = criterion(output, mask)
            loss.backward()
            optimizer.step()
            epoch_loss += loss.item()
        print(f"Epoch [{epoch+1}/{epochs}], Loss: {epoch_loss/len(dataloader):.4f}")
    torch.save(model.state_dict(), "unet_model.pth")

# Inference Function
def infer(model, image_path):
    model.eval()
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (256, 256))
    img = img / 255.0
    img = np.transpose(img, (2, 0, 1)).astype(np.float32)
    img = torch.tensor(img).unsqueeze(0).to(device)
    
    with torch.no_grad():
        pred = model(img)
    pred = pred.squeeze().cpu().numpy()
    return (pred > 0.5).astype(np.uint8) * 255

# Example Usage
# train(model, dataloader, criterion, optimizer, epochs=10)
# mask = infer(model, "path/to/sample.jpg")
# cv2.imwrite("output_mask.png", mask)