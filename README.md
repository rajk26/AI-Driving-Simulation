# CMPSC 497 Final Project – ACT-R Driving Simulation

## Description
This project simulates human driving behavior under cognitive load using the ACT-R cognitive architecture. The agent navigates a grid world, making decisions based on production rules and declarative memory, while adapting to distractions and obstacles. The goal is to explore how realistic and imperfect cognitive behavior can be modeled in an AI system.

---

## GEA (Goals, Environment, Adaptation)

### Goals
- Model distracted driving behavior realistically using ACT-R
- Reflect human-like reasoning, including mistakes and stress
- Evaluate how the agent adapts over time in different environments
- Avoid narrow or biased models of cognition

### Environment
- A 2D grid-world simulating roads, intersections, weather, obstacles
- Special cell types: walls (black), water (blue), obstacles (red), goals (green)
- Three scenario types: simple lane navigation, turning, and hill + obstacle challenge
- Stakeholders: AI researchers, psychologists, HCI designers

### Adaptation
- The agent uses ACT-R’s rule-based and memory systems to adapt behavior
- Decisions are made based on current state + recalled past experiences
- The system penalizes collisions and rewards successful goal-reaching
- Simulation score tracks agent performance (includes time and errors)

---

## Design & Implementation Details

### ACT-R Agent Logic
- Uses **production rules** to make decisions (e.g., “if wall ahead, turn left”)
- Uses **declarative memory** to store prior decisions and adapt to similar situations
- **MotorModule** handles physical action: forward, turn, stop
- Agent behavior is shaped by cognitive distractions and environmental feedback

### Scenarios
We implemented three driving experiments:
1. **Two-lane test** – simple forward driving with a goal
2. **Turning test** – evaluates navigation in intersections
3. **Hill/Obstacle test** – adds stress via distractions and timing penalties

### System Diagram
[ Environment ]
↓
[ Perception ] → [ ACT-R Agent ]
├── Goal Buffer
├── Declarative Memory
└── Motor Module
↓
[ Movement + Feedback ]

## Usage
Use python actr environment setup from this link: [Python ACTR Setup](https://cld5070.github.io/cmpsc497-sp25/help/installing-python-act-r/)

Once the environemnt is running (recommended to test using the 3 moving agents script), go to implementation/dactr1 and run any of the three experiments.

```python
py experiment1.py
py experiment2.py
py experiment3.py

Results are shown at the end of the debug statements. Enjoy!

Output

At the end of each run, you’ll see:

Total time taken by the agent
Final score based on time, wall hits, and obstacle collisions
Higher scores mean more efficient and human-like driving.
