class Sprite:
    def __init__(self,x,y,imglist):
        self.x=x
        self.y=y
        imgs = list()
        for img in imglist:
            img=img.split('\n')
            img.pop(0)
            img.pop(len(img)-1)
            imgs.append(img)
        self.imgs=imgs
        self.w=len(imgs[0])
        self.h=len(imgs[0])
        self.time=0
        self.img = imgs[0]
    def setup(self):
        pass
    def update(self):
        pass
    def render(self,display):
        self.time+=1
        if len(self.imgs)>1:
            if self.time % 2 ==0 :
                self.img = self.imgs[0]
            if self.time % 4 ==0:
                self.img = self.imgs[1]
        else:
            self.img = self.imgs[0]
        y=0
        for line in self.img:
            x=0
            for char in line:
                if int(char)==1:
                    display.pixel(self.x+x,self.y+y,1)
                x+=1
            y+=1