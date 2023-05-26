# Matthew Semmel
# 1/17/2019
# period 2 Python
#-----------------------


import random
import time
import os
# use superwires instead of livewires
# type this into command prompt (pip install SuperWires)
#if error, open pycharm and install package 'SuperWires'
from superwires import games,color
# set screen resolution to 800 x 600
games.init(screen_width = 800, screen_height = 600, fps = 50)
# end message
def EndPrg ():
  won_message = games.Message(value = "Game Over!", size = 100,color = color.red,x = games.screen.width/2,y = games.screen.height/2,lifetime = 250, after_death = games.screen.quit)
  games.screen.add(won_message)

# load  splash screen
class Splash(games.Sprite):
    image = games.load_image("cc-splash.png",transparent = False)

    def __init__(self):
        """ Initialize splash screen """
        super(Splash, self).__init__(image = Splash.image, x = games.screen.width/2,y = games.screen.height/2 )
        self.time = games.Text(value = 0, size = 25, color = color.black, top = 5, left = 50)
        #games.screen.add(self.time)
        #timer =0
	# car controlled by mouse
    def update(self):
        """ Move to mouse position. """
        self.time.value = self.time.value + 1
        #timer = timer + 1
        #self.time.value = timer
        #shape = Shape()
        #print (self.time.value)
        if self.time.value > 150 :
           #shape.lolwut = self.time.value
           self.destroy()
           the_MyCar = MyCar()
           games.screen.add(the_MyCar)
           for i in range (0,1000): i = i + 1  # slight pause loop
           x = 100
           y = 600
           size=Car.Car1
           new_Car = Car(x = x, y = y, size = size)
           games.screen.add(new_Car)
           x = 200
           size=Car.Car2
           new_Car = Car(x = x, y = y, size = size)
           games.screen.add(new_Car)
           x = 300
           size=Car.Car3
           new_Car = Car(x = x, y = y, size = size)
           games.screen.add(new_Car)


class MyCar (games.Sprite):
    """     My car.       """
	#load my car
    image = games.load_image("mustang.png",transparent=True)
	#load crash sound
    crash_snd = games.load_sound("cc-crash.wav")


    def __init__(self):
        """ Initialize mycar object and create Text object for score,  pts and hi score. """
        super(MyCar, self).__init__(image = MyCar.image,x = games.mouse.x , y = games.mouse.y ,dx = -2,     dy = -3)

		# display armor text from 100 full down to 0 gone
        self.armor = games.Text(value = 100, size = 25, color = color.black, top = 5, right = games.screen.width - 10)
        games.screen.add(self.armor)

        self.text1 = games.Text(value = 'Armor: ' , size = 25, color = color.black, top = 5, right = games.screen.width - 50)
        games.screen.add(self.text1)

		#display score text
        self.score = games.Text(value = 0, size = 25, color = color.black, top = 30, right = games.screen.width - 10)
        games.screen.add(self.score)
        self.text2 = games.Text(value = 'Score: ' , size = 25, color = color.black, top = 30, right = games.screen.width - 50)
        games.screen.add(self.text2)


    def update(self):
	    # move my car
        """ Move to mouse x position. """
        self.score.value = self.score.value + 1
        self.score.right = games.screen.width - 10
        self.x = games.mouse.x

        if self.top > games.screen.height:
            self.bottom = 0

        if self.bottom < 0:
            self.top = games.screen.height

        if self.left > games.screen.width:
            self.right = 5

        if self.right < 5:
            self.left = games.screen.width
        if self.left < 50:
            self.dx = -self.dx
        if self.right > 700:
            self.dx = -self.dx
        if self.left < 70:
            self.right = self.right + 30
        if self.right > 600:
           self.right = self.right - 30



        self.check_collide()

		# what happens when mycar gets hits
    def check_collide(self):
        """ Check for collision """
        crash_snd = games.load_sound("cc-crash.wav")
        boom_snd = games.load_sound("cc-boom.wav")
        for MyCar in self.overlapping_sprites:
            #self.dx = self.dx * -1
            #self.destroy()
			# if car hit, reduce armor by 1
            self.armor.value = self.armor.value - 1
			# add a point every time i survive
            self.score.value = self.score.value + 1
            self.armor.right = games.screen.width - 10
            self.score.right = games.screen.width - 10
			# play crash sound
            crash_snd.play()
            if self.armor.value  < 1:  # armor is now 0 were dead
              self.armor.value = 0
              boom_snd.play()  # play boom sound

              self.destroy()
              games.music.stop()
              #boom_snd.play()
              # game over
              won_message = games.Message(value = "Game Over!", size = 100,color = color.red,x = games.screen.width/2,y = games.screen.height/2,lifetime = 250, after_death = games.screen.quit)
              games.screen.add(won_message)
              #self.armor.right = games.screen.width - 10



#load three enemy cars
class Car(games.Sprite):
    """ An Car which floats across the screen. """
    Car1 = 1
    Car2 = 2
    Car3 = 3
    images = {Car1  : games.load_image("cc-Redcar.gif"),
              Car2 : games.load_image("cc-Greencar.gif"),
              Car3  : games.load_image("cc-Yellowcar.gif") }

    SPEED = 2

    def __init__(self, x, y, size):
        """ Initialize Car sprite. """
        super(Car, self).__init__(
            image = Car.images[size],          x = x, y = y,  dx = -3,	    dy = -4  )

        self.size = size


    def update(self):
        """ Wrap around screen. """
        # make cars fly arounf screen
        if self.top > games.screen.height:
            self.bottom = 0

        if self.bottom < 0:
            self.top = games.screen.height

        if self.left > games.screen.width:
            self.right = 0

        if self.right < 0:
            self.left = games.screen.width
        if self.left < 50:
            self.dx = -self.dx
        if self.right > 750:
            self.dx = -self.dx
        self.check_collide()


    def check_collide(self):
        """ Check for collision  """
		# if enemy card hits another car, bounce off
        for Car in self.overlapping_sprites:
            self.dx = self.dx * -1
            if self.left < 201:
               self.dx = -self.dx



def main():
    # load track
    track_image = games.load_image("cc-track.jpg" ,transparent = False)
    games.screen.background = track_image
    games.mouse.is_visible = False
	# prep music
    games.music.load ("cc.mid")
    crash_snd = games.load_sound("cc-crash.wav")
    games.music.play()   # start midi music
    the_Splash = Splash()
    games.screen.add(the_Splash)  # load splash screen, when splash screen ends starts race
    games.screen.mainloop()

# load main function
main()
