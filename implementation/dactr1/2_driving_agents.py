from AgentSupport import MotorModule, MyCell
import AgentSupport
import python_actr
from python_actr.lib import grid
from python_actr.actr import *
import random

class MyCell(grid.Cell):
    def color(self):
        if self.wall: return 'black'
        else: return 'white'
    def load(self,char):      
        if char=='#': self.wall=True


class DrivingAgent(ACTR):
    goal=Buffer()
    retrieval = Buffer()
    DM_module = Memory(retrieval)
    motorInst = MotorModule()
    body=grid.Body()

    def init():
        goal.set('start')
        
        # Add memory chunks to declarative memory module
        # example: DM_module.add("prev:none next:crust")
        # if distracted, veer right
        # if tired, reponse altered
        # if actively eating, drinking, or smoking, veer left or right
        # if eyes off road, log hes not looking
        # if using phone, not looking
        # if rubbernecking, not looking
        # if looking at off-road objects/ scenery, not looking
        
    def start_driving(goal="start"):
        motorInst.go_forward()
        
		#start going toward target!
        goal.set("start")
		#Request next step from DM
        # DM_module.request("prev:driving next:?")
            
world=grid.World(MyCell,map=AgentSupport.twolane)

agent=DrivingAgent()
world.add(agent,x=3,y=1,dir=2,color='blue')

# agent2=MyAgent()
# agent2.body.color='green'
# world.add(agent2,x=10,y=3)

python_actr.display(world)
world.run()