import cv2
import torch
import torch.nn as nn
import torchvision.transforms as transforms
import gc
import os
import numpy as np
from django.conf import settings

class ResNet152Memes:
    def __init__(self):
        self.model = torch.hub.load('pytorch/vision:v0.6.0', 'resnet152', pretrained=False)
        self.location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        self.model.fc = nn.Linear(2048, 2)
        self.model.load_state_dict(torch.load(os.path.join(self.location, 'resnet152MEMES.pth'),
                                              map_location=torch.device('cpu')))
        self.model.eval()

    def predict(self, image_path):
        image = cv2.imdecode(np.fromfile(os.path.realpath(os.path.join(settings.MEDIA_ROOT, image_path)), dtype=np.uint8), cv2.IMREAD_UNCHANGED)
        image = cv2.resize(image, (224, 224))
        image = cv2.normalize(image, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
        preprocess = transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])
        input_tensor = torch.stack([preprocess(image)])

        with torch.no_grad():
            output = self.model(input_tensor)

        del image
        del input_tensor
        gc.collect()

        return torch.softmax(output,dim=1).tolist()[0]
