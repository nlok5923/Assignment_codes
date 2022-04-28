import numpy as np
import math

def game_over_check(current_state,eval_nodes):
  game_state=current_state.copy()

  if (game_state[0] == game_state[4] == game_state[8]) :
    if (game_state[0]=='X'):
        return 10,eval_nodes+1
    elif (game_state[0]=='O'):
        return -10,eval_nodes+1
  if (game_state[2] == game_state[4] == game_state[6]):
    if ( game_state[2]=='X'):
        return 10,eval_nodes+1
    elif (game_state[2]=='O'):
        return -10,eval_nodes+1

  for i in range(0,3):
    if (game_state[i] == game_state[i + 3] == game_state[i + 6]):
      if (game_state[i]=='X'):
        return 10,eval_nodes+1
      elif (game_state[i]=='O'):
        return -10,eval_nodes+1
  
  for i in range(0,7,3) :
    if (game_state[i] == game_state[i + 1] == game_state[i + 2]):
      if (game_state[i]=='X'):
        return 10,eval_nodes+1
      elif (game_state[i]=='O'):
        return -10,eval_nodes+1
  count=[]
  for i in range(len(current_state)):
    if current_state[i] == ' ':
      count.append(i)
    # index_empty= np.array(count)
  if len(np.array(count)) == 0:
    return 0,eval_nodes+1

  return -1,eval_nodes+1

def minimax_algorithm(depth ,maximize_play ,current_state,parentIndex,eval_nodes):
  move = 'X' if maximize_play else 'O'
  score_per_move,eval_nodes=game_over_check(current_state,eval_nodes)

  if depth == 0 or score_per_move != -1:
    return [score_per_move,current_state,eval_nodes]

  if maximize_play :
    eval_max = -math.inf
    count=[]
    for i in range(len(current_state)):
      if current_state[i] == ' ':
        count.append(i)
    index_empty= np.array(count)
    best = None
    for i in index_empty:
      game_state = current_state.copy()
      game_state[i] = move
      updated_states = game_state
      eval,temporary_best,eval_nodes=minimax_algorithm(depth-1,False,updated_states,i,eval_nodes)
      eval_max=max(eval_max,eval)
      best = temporary_best if eval_max == eval else best
    return [eval_max,best,eval_nodes]
  else:
    eval_min = math.inf
    count=[]
    for i in range(len(current_state)):
      if current_state[i] == ' ':
        count.append(i)
    index_empty= np.array(count)
    best = None
    for i in index_empty:
      game_state = current_state.copy()
      game_state[i] = move
      updated_states = game_state
      eval,temporary_best,eval_nodes=minimax_algorithm(depth-1,True,updated_states,i,eval_nodes)
      eval_min=min(eval_min,eval)
      best = temporary_best if eval_min == eval else best
    return [eval_min,best,eval_nodes]

game_initial_state=np.array([' ',' ',' ',' ',' ',' ',' ',' ',' '])
points,board,eval_nodes=minimax_algorithm(9,True,game_initial_state,None,0)
print("Total Evaluated nodes in MINIMAX algo = ",eval_nodes)
