from torch.utils.tensorboard import SummaryWriter
import numpy as np
from PIL import Image

writer = SummaryWriter("logs")
img_path = "dataset/train/ants_image/7759525_1363d24e88.jpg"
img_PIL = Image.open(img_path)
img_array = np.array(img_PIL)
print(type(img_array))
print(img_array.shape)

# dataformats='HWC'指定img_array的高、宽、通道数的顺序
writer.add_image("train", img_array, 2, dataformats='HWC')

for i in range(100):
    writer.add_scalar("y=3x", 3*i, i)
writer.close()