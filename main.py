from torch.utils.data import Dataset
from PIL import Image
import os


class Mydata(Dataset):

    def __init__(self, root_dir, label_dir):
        self.root_dir = root_dir
        self.label_dir = label_dir
        self.path = os.path.join(self.root_dir, self.label_dir)  # 图片路径
        self.img_path = os.listdir(self.path)  # 图片列表

    def __getitem__(self, item):  # 通过item获取图片的地址
        img_name = self.img_path[item]  # 根据图片索引获取图片名字
        img_item_path = os.path.join(self.root_dir, self.label_dir, img_name)  # 图片地址
        img = Image.open(img_item_path)
        label = self.label_dir
        return img, label

    def __len__(self):  # 图片数量
        return len(self.img_path)


root_dir = "dataset/train"
ants_label_dir = "ants"
bees_label_dir = "bees"
ants_dataset = Mydata(root_dir, ants_label_dir)
bees_dataset = Mydata(root_dir, bees_label_dir)
train_dataset = ants_dataset + bees_dataset




