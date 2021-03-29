class Screen:
    def __init__(self, width, height,display):
        self.width=width
        self.height=height
        self.player={}
        self.enemys=[]
        self.foods=[]
        self.bullets=[]
        self.bgs=[]
        self.display=display
    def clear(self):
        self.display.fill(0)
    def add_player_sprite(self,sprite):
        self.player=sprite
    def add_enemy_sprite(self,sprite):
        self.enemys.append(sprite)
    def add_bg_sprite(self,sprite):
        self.bgs.append(sprite)
    def show(self):
        #list = self.player.img.split('')
        self.clear()
        for enemy in self.enemys:
            if enemy==None:
                enemys.remove(enemy)
            else:
                enemy.update()
                enemy.render(self.display)
        for bg in self.bgs:
            bg.render(self.display)
        self.player.render(self.display)
        #graphics.circle(self.player.x,self.player.y, self.player.w, 1)
        self.display.show()