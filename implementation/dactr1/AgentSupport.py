import python_actr
from python_actr.lib import grid
#from python_actr import *

import random
import time

twolane="""
#######################
#                    C#
#                     #
#######################
"""

fourlane_with_obj="""
#######################
#            O       C#
#                    C#
#                     #
#                     #
#######################
"""

sixlane_with_objs="""
#######################
#      O    O        C#
#            O     O C#
#         O      O   C#
#                     #
#                     #
#                     #
#######################
"""

sandbox="""
#######################
#            O       C#
#                     #
#######################
"""

# Agent is tested if it can turn correctly
T_shaped="""
##################
#                #
#                #
###########  #####
          #  #
          #  #
          # C#
          ####
"""

right_turn="""
##############
            #####
                #######
######               C#
    #######           #
          #############
"""

# Agent is tested if paying attention. Make blue blocks illustrating water
hill_turn="""
#############WWWWWWWWWWWW
#                      C#
#           O          C#
#                       #
#                       #
#########################
"""

my_log = python_actr.log()#data=True, directory="/Users/cld5070/teaching-repos/AI-Course/RBES")

class MyCell(grid.Cell):
	targetsquare=False
	watersquare=False
	obstaclesquare=False

	def color(self):
		if self.targetsquare: return "green"
		elif self.wall: return 'black'
		elif self.watersquare: return 'blue'
		elif self.obstaclesquare: return 'red'
		else: return 'white'

	def load(self,char):
		if char=='#': self.wall=True
		elif char=='C': self.targetsquare=True
		elif char=='W': self.watersquare=True
		elif char=='O': self.obstaclesquare=True

class MotorModule(python_actr.Model):
	FORWARD_TIME = .1
	FORWARD_ENERGY_COST = 1
	TURN_TIME = 0.025
	TURN_ENERGY_COST = 1
	INIT_ENERGY = 35

	def __init__(self):
		python_actr.Model.__init__(self)
		self.busy=False
		self.energy=MotorModule.INIT_ENERGY

	def turn_left(self, amount=1):
		if self.busy: return
		self.busy=True
		self.action="turning left"
		amount *= -1
		self.parent.body.turn(amount)
		yield MotorModule.TURN_TIME
		self.busy=False

	def turn_right(self, amount=1):
		if self.busy: return
		self.busy=True
		self.action="turning left"
		self.parent.body.turn(amount)
		yield MotorModule.TURN_TIME
		self.busy=False

	def turn_around(self):
		if self.busy: return
		self.busy=True
		self.action="turning around"
		self.parent.body.turn_around()
		yield MotorModule.TURN_TIME
		self.busy=False

	def go_forward(self, dist=1):
		if self.busy: return
		self.busy=True
		self.action="going forward"
		for i in range(dist):
			self.parent.body.go_forward()
			yield MotorModule.FORWARD_TIME
		self.action=None
		self.busy=False

	def go_left(self,dist=1):
		if self.busy: return
		self.busy="True"
		self.action='turning left'
		yield MotorModule.TURN_TIME
		self.parent.body.turn_left()
		self.action="going forward"
		for i in range(dist):
			self.parent.body.go_forward()
			yield MotorModule.FORWARD_TIME
		self.action=None
		self.busy=False

	def go_right(self):
		if self.busy: return
		self.busy=True
		self.action='turning right'
		yield 0.1
		self.parent.body.turn_right()
		self.action='going forward'
		self.parent.body.go_forward()
		yield MotorModule.FORWARD_TIME
		self.action=None
		self.busy=False

	def go_towards(self,x,y):
		if self.busy: return
		self.busy=True
		#self.clean_if_dirty()
		self.action='going towards %s %s'%(x,y)
		self.parent.body.go_towards(x,y)
		yield MotorModule.FORWARD_TIME
		#self.action="cleaning cell"
		#self.clean()
		#yield MotorModule.CLEAN_TIME
		self.busy=False

	def veer_right(self):
		if self.busy: return
		self.busy=True

		self.action='turning right'
		yield 0.1
		self.parent.body.turn_right()
		self.action='going forward'
		self.parent.body.go_forward()
		yield MotorModule.FORWARD_TIME

		self.action='turning left'
		yield MotorModule.TURN_TIME
		self.parent.body.turn_left()
		self.action="going forward"
		self.parent.body.go_forward()
		yield MotorModule.FORWARD_TIME

		self.action='turning left'
		yield MotorModule.TURN_TIME
		self.parent.body.turn_left()
		self.action="going forward"
		self.parent.body.go_forward()
		yield MotorModule.FORWARD_TIME

		self.action='turning right'
		yield 0.1
		self.parent.body.turn_right()
		self.action='going forward'
		self.parent.body.go_forward()
		yield MotorModule.FORWARD_TIME

		self.action=None
		self.busy=False

	def veer_left(self):
		if self.busy: return
		self.busy=True

		self.action='turning left'
		yield MotorModule.TURN_TIME
		self.parent.body.turn_left()
		self.action="going forward"
		self.parent.body.go_forward()
		yield MotorModule.FORWARD_TIME

		self.action='turning right'
		yield 0.1
		self.parent.body.turn_right()
		self.action='going forward'
		self.parent.body.go_forward()
		yield MotorModule.FORWARD_TIME

		self.action='turning right'
		yield 0.1
		self.parent.body.turn_right()
		self.action='going forward'
		self.parent.body.go_forward()
		yield MotorModule.FORWARD_TIME

		self.action='turning left'
		yield MotorModule.TURN_TIME
		self.parent.body.turn_left()
		self.action="going forward"
		self.parent.body.go_forward()
		yield MotorModule.FORWARD_TIME

		self.action='turning right'
		yield 0.1
		self.parent.body.turn_right()
		self.action='going forward'
		self.parent.body.go_forward()
		yield MotorModule.FORWARD_TIME

		self.action=None
		self.busy=False

	def reach_destination(self):
		if(self.parent.body.cell.targetsquare):
			self.action="ending sim"
			self.stop()

	def hit_wall(self):
		# make it go randomly left or right
		self.go_left()

	def hit_obstacle(self):
		self.parent.body.cell.obstaclesquare=False # get rid of obstacle
		self.FORWARD_TIME = .01 # allude that car is damaged