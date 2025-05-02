from AgentSupport import MotorModule, MyCell
import AgentSupport
import python_actr
from python_actr.lib import grid
from python_actr.actr import *
import random
import time

HIT_WALL_PENALTY = .05 # mental note. Aparently ACTR doesnt recognize constants
OBSTACLE_PENALTY = .5 # mental note. Aparently ACTR doesnt recognize constants
TEST1_IDEAL_TIME = 2.3 # if agent acts perfectly

class DrivingAgent(ACTR):
    goal=Buffer()
    retrieval = Buffer()
    DM_module = Memory(retrieval)
    motorInst = MotorModule()
    body=grid.Body()
    
    score = 1 # score used to evaluate Agent versus env
    
    agent_excuses = [
        "Agent not paying attention",
        "Agent took too big of a yawn",
        "Agent texting boo on phone",
        "Agent's neck turned into rubber",
        "Agent too captivated by outside scenery"
    ]
    # if distracted, veer right
    # if tired, reponse altered
    # if actively eating, drinking, or smoking, veer left or right
    # if eyes off road, log hes not looking

    def init():
        goal.set('start')
        
    def drive_forward(goal="start", motorInst="busy:False"):
        motorInst.go_forward()
        
		#start going toward target!
        goal.set("start")
		#Request next step from DM
        DM_module.request("square:obj location_x:?x location_y:?y", require_new=True)
    
    # If driver reaches green sq, end sim positive result
    def destination(body="cell.targetsquare:True", utility=.6):
        motorInst.reach_destination()
        
    # Wall detection. If driver htis a wall swerve right
    def wall_collision_swerve_right(body="ahead_cell.wall:True"):
        score -= .01 # subtract score based on set amount
        motorInst.go_right()
        
    # Wall detection. If driver htis a wall swerve left
    def wall_collision_swerve_left(body="ahead_cell.wall:True"):
        score -= .15 # subtract score based on set amount
        motorInst.go_left()
    
    # if agent runs into a large obstacle, subtract heavily from sim
    def obstacle_collision(body="cell.obstaclesquare:True"):
        score -= 0.5
        motorInst.hit_obstacle()
        x = body.x
        y = body.y
        DM_module.add("square:obj location_x:?x location_y:?y")
        
    # driver not paying attention for some reason
    def detect_obj_fail(body="ahead_cell.obstaclesquare:True"):
        print(random.choice(agent_excuses))
        
    def detect_obj_veer_right(body="ahead_cell.obstaclesquare:True"):
        motorInst.veer_right()
        
    def detect_obj_veer_left(body="ahead_cell.obstaclesquare:True"):
        motorInst.veer_left() # rand this
        
    # Rule: Blue runs into another agent. Give score 0
    
    # Rule: if green sq is three times ahead, go towards it
            
class NPCAgent(ACTR):
    goal=Buffer()
    retrieval = Buffer()
    DM_module = Memory(retrieval)
    motorInst = MotorModule()
    body=grid.Body()
    
    def init():
        goal.set('start')
        
    def start_driving(goal="start"):
        # change speed if you want
        motorInst.go_forward()
    
def exp1():
    world=grid.World(MyCell,map=AgentSupport.twolane)
    agent=DrivingAgent()
    world.add(agent,x=1,y=1,dir=2,color='blue')
    python_actr.log_everything(agent, AgentSupport.my_log)
    
    npc_agent1=NPCAgent()
    world.add(npc_agent1,x=20,y=2,dir=6,color='green')
    
    python_actr.display(world)
    
    start_time = time.time()
    world.run()
    end_time = time.time()
    exp_time = end_time - start_time # gets time of agent in env
    score = agent.score - (exp_time * .025)
    return score

def exp2():
    world=grid.World(MyCell,map=AgentSupport.fourlane_with_obj)
    agent=DrivingAgent()
    world.add(agent,x=1,y=1,dir=2,color='blue')
    python_actr.log_everything(agent, AgentSupport.my_log)
    
    npc1=NPCAgent()
    npc2=NPCAgent()
    world.add(npc1,x=20,y=3,dir=6,color='green')
    world.add(npc2,x=17,y=4,dir=6,color='green')
    
    python_actr.display(world)
    
    start_time = time.time()
    world.run()
    end_time = time.time()
    exp_time = end_time - start_time # gets time of agent in env
    score = agent.score - (exp_time * .025)
    return score

def exp3():
    world=grid.World(MyCell,map=AgentSupport.sixlane_with_objs)
    agent=DrivingAgent()
    world.add(agent,x=1,y=1,dir=2,color='blue')
    python_actr.log_everything(agent, AgentSupport.my_log)
    
    npc1=NPCAgent()
    npc2=NPCAgent()
    npc3=NPCAgent()
    world.add(npc1,x=20,y=4,dir=6,color='green')
    world.add(npc2,x=16,y=5,dir=6,color='green')
    world.add(npc3,x=18,y=6,dir=6,color='green')
    
    python_actr.display(world)
    
    start_time = time.time()
    world.run()
    end_time = time.time()
    exp_time = end_time - start_time # gets time of agent in env
    score = agent.score - (exp_time * .025)
    return score

def experiment(test_num):
    if test_num==1:
        total_score = 0
        
        for i in range(3):
            score = exp1()
            if score < 0: # if sim ends abruptly
                score = 0
            total_score += score
        
        average = total_score / 3
        print("Experment 1 Results . . .")
        
    
    elif test_num==2:
        total_score = 0
        
        for i in range(3):
            score = exp2()
            if score < 0: # if sim ends abruptly
                score = 0
            total_score += score
        
        average = total_score / 3
        print("Experment 2 Results . . .")
        
    elif test_num==3:
        total_score = 0
        
        for i in range(3):
            score = exp3()
            if score < 0: # if sim ends abruptly
                score = 0
            total_score += score
        
        average = total_score / 3
        print("Experment 3 Results . . .")
        
    else :
        print("Invalid experiment number inputed")
            

    print("Agent Average Score: ", average)
    
# experiment(1)
experiment(2)
# experiment(3)