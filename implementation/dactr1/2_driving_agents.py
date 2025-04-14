from AgentSupport import MotorModule, MyCell
import AgentSupport
import python_actr
from python_actr.lib import grid
from python_actr.actr import *
import random

class DrivingAgent(ACTR):
    goal=Buffer()
    retrieval = Buffer()
    DM_module = Memory(retrieval)
    motorInst = MotorModule()
    body=grid.Body()
    
    score = 0 # score used to evaluate Agent versus env

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
    
    # Wall detection. If driver htis a wall but is on green sq, end sim positive result
    def wall_destination(motorInst="targetsquare:True", body="ahead_cell.wall:True"):
        score = 1
        motorInst.reach_destination()
        
    # Wall detection. If driver htis a wall but is not on green sq, end sim negative result
    def wall_collision(motorInst="busy:False", body="ahead_cell.wall:True"):
        score = 0
        motorInst.hit_wall()
        
    # Rule: Blue runs into another agent. Give score 0
            
class NPCAgent(ACTR):
    goal=Buffer()
    retrieval = Buffer()
    DM_module = Memory(retrieval)
    motorInst = MotorModule()
    body=grid.Body()
    
    def init():
        goal.set('start')
        
    def start_driving(goal="start"):
        motorInst.go_forward()

def twolaneExp():
    world=grid.World(MyCell,map=AgentSupport.twolane)
    
    agent=DrivingAgent()
    world.add(agent,x=1,y=1,dir=2,color='blue')
    
    agent=NPCAgent()
    world.add(agent,x=20,y=2,dir=6,color='green')
    
    python_actr.display(world)
    world.run()
    
def turn_exp():
    world=grid.World(MyCell,map=AgentSupport.T_shaped)
    
    agent=DrivingAgent()
    world.add(agent,x=1,y=1,dir=2,color='blue')
    
    agent=NPCAgent()
    world.add(agent,x=14,y=2,dir=6,color='green')
    
    python_actr.display(world)
    world.run()
    
def hill_exp():
    world=grid.World(MyCell,map=AgentSupport.hill_turn)
    
    agent=DrivingAgent()
    world.add(agent,x=1,y=1,dir=2,color='blue')
    
    npc1=NPCAgent()
    npc2=NPCAgent()
    world.add(npc1,x=20,y=3,dir=6,color='green')
    world.add(npc2,x=17,y=4,dir=6,color='green')
    
    python_actr.display(world)
    world.run()

# twolaneExp()
# turn_exp()
hill_exp()