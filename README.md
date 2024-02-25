# fox_chicken_grain

<p>
A man has to get a fox, a chicken, and a sack of grain across a river. 
He has a rowboat, and it can only carry him and one other thing.
If the fox and the chicken are left together, the fox will eat the chicken.
If the chicken and the grain are left together, the chicken will eat the grain.
</p>

<i>
Get the farmer, fox, chicken and grain across the river.
</i>

------------------

This is created with pyhton using Breadth-First Search (BFS) algorithm.

<b>Initial State:</b>
- Farmer (F), Fox (X), Chicken (C), Grain (G) are all on the upper side of the river.

<b>Goal State:</b>
- Farmer, Fox, Chicken, and Grain are all on the down side of the river.

<b>Rules:</b>
1. The farmer can only carry one item (Fox, Chicken, or Grain) at a time when crossing the river.
2. If the farmer is not present, the Fox will eat the Chicken.
3. If the Chicken is not present, the Chicken will eat the Grain.
   
<b>BFS process step by step:</b>
1. Step 0 (Initial State):
    - Initial State: [F, X, C, G] (all items on the left side)
    - Explore all possible next states from the initial state and enqueue them.
    - Queue: [Initial State]
2. Step 1:
    - Dequeue the initial state from the queue.
    - Explore all possible next states from the dequeued state and enqueue them.
    - Queue: [Next States from Initial State]
3. Step 2:
    - Dequeue states from the queue one by one.
    - Explore all possible next states from each dequeued state and enqueue them.
    - Queue: [Next States from Level 1]
4. Step 3:
    - Repeat the process until either the goal state is found or the queue becomes empty.
    - If the goal state is found, BFS terminates and returns the path to reach the goal state.
5. Solution:
    - If a solution is found, BFS returns the path from the initial state to the goal state.
    - This path represents the sequence of moves (crossings) that the farmer makes to transport all items from the left side to the right side of the river while obeying the rules.

------------------

<b>Location States</b>
```
  +---+---+---+---+---+---+---+
  | F |   | X |   | C |   | G | Starting Side
  +---+---+---+---+---+---+---+
  |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+
  |   |   |   |   |   |   |   | Ending Side
  +---+---+---+---+---+---+---+
```

<b>State syntax</b>
<p>Each node on the graph has a four digit number. The each digit represents where the riddle participants are located.</p>

<i>Start State</i> - Everyone is on the upper side.
```
0 Farmer
0 Fox
0 Chicken
0 Grain
```
<i>End State</i> - Everyone is on the down side.
```
1 Farmer
1 Fox
1 Chicken
1 Grain
```
<i>Random State</i> - The farmer and the chicken are in the down side, the fox and grain is on the upper side.
```
1 Farmer
0 Fox
1 Chicken
0 Grain
```
-----------------------
After running it will show the following output base on the innitial state

<i>initial state</i>
```
initial_state = State(0, 0, 0, 0)
```
<i>Output</i>
```
+---+---+---+INITIAL STATE+---+---+---+
Number of possible states: 21845
Number of valid states: 8
Solution: [0, 1010, 10, 1110, 100, 1101, 101, 1111]
+---+---+---+STEP [0]+---+---+---+
  +---+---+---+---+---+---+---+
  | F |   | X |   | C |   | G |
  +---+---+---+---+---+---+---+
  |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+
  |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+

+---+---+---+STEP [1]+---+---+---+
  +---+---+---+---+---+---+---+
  |   |   | X |   |   |   | G |
  +---+---+---+---+---+---+---+
  |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+
  | F |   |   |   | C |   |   |
  +---+---+---+---+---+---+---+

+---+---+---+STEP [2]+---+---+---+
  +---+---+---+---+---+---+---+
  | F |   | X |   |   |   | G |
  +---+---+---+---+---+---+---+
  |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+
  |   |   |   |   | C |   |   |
  +---+---+---+---+---+---+---+

+---+---+---+STEP [3]+---+---+---+
  +---+---+---+---+---+---+---+
  |   |   |   |   |   |   | G |
  +---+---+---+---+---+---+---+
  |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+
  | F |   | X |   | C |   |   |
  +---+---+---+---+---+---+---+

+---+---+---+STEP [4]+---+---+---+
  +---+---+---+---+---+---+---+
  | F |   |   |   | C |   | G |
  +---+---+---+---+---+---+---+
  |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+
  |   |   | X |   |   |   |   |
  +---+---+---+---+---+---+---+

+---+---+---+STEP [5]+---+---+---+
  +---+---+---+---+---+---+---+
  |   |   |   |   | C |   |   |
  +---+---+---+---+---+---+---+
  |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+
  | F |   | X |   |   |   | G |
  +---+---+---+---+---+---+---+

+---+---+---+STEP [6]+---+---+---+
  +---+---+---+---+---+---+---+
  | F |   |   |   | C |   |   |
  +---+---+---+---+---+---+---+
  |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+
  |   |   | X |   |   |   | G |
  +---+---+---+---+---+---+---+

+---+---+---+STEP [7]+---+---+---+
  +---+---+---+---+---+---+---+
  |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+
  |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+
  | F |   | X |   | C |   | G |
  +---+---+---+---+---+---+---+
```

------------------

<i>random state</i>
```
random_state = State(1, 0, 1, 0)
```
<i>Output</i>
```
+---+---+---+RANDOM STATE+---+---+---+
Number of possible states: 5461
Number of valid states: 7
Solution: [1010, 10, 1110, 100, 1101, 101, 1111]
+---+---+---+STEP [0]+---+---+---+
  +---+---+---+---+---+---+---+
  |   |   | X |   |   |   | G |
  +---+---+---+---+---+---+---+
  |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+
  | F |   |   |   | C |   |   |
  +---+---+---+---+---+---+---+

+---+---+---+STEP [1]+---+---+---+
  +---+---+---+---+---+---+---+
  | F |   | X |   |   |   | G |
  +---+---+---+---+---+---+---+
  |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+
  |   |   |   |   | C |   |   |
  +---+---+---+---+---+---+---+

+---+---+---+STEP [2]+---+---+---+
  +---+---+---+---+---+---+---+
  |   |   |   |   |   |   | G |
  +---+---+---+---+---+---+---+
  |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+
  | F |   | X |   | C |   |   |
  +---+---+---+---+---+---+---+

+---+---+---+STEP [3]+---+---+---+
  +---+---+---+---+---+---+---+
  | F |   |   |   | C |   | G |
  +---+---+---+---+---+---+---+
  |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+
  |   |   | X |   |   |   |   |
  +---+---+---+---+---+---+---+

+---+---+---+STEP [4]+---+---+---+
  +---+---+---+---+---+---+---+
  |   |   |   |   | C |   |   |
  +---+---+---+---+---+---+---+
  |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+
  | F |   | X |   |   |   | G |
  +---+---+---+---+---+---+---+

+---+---+---+STEP [5]+---+---+---+
  +---+---+---+---+---+---+---+
  | F |   |   |   | C |   |   |
  +---+---+---+---+---+---+---+
  |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+
  |   |   | X |   |   |   | G |
  +---+---+---+---+---+---+---+

+---+---+---+STEP [6]+---+---+---+
  +---+---+---+---+---+---+---+
  |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+
  |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+
  | F |   | X |   | C |   | G |
  +---+---+---+---+---+---+---+
```
