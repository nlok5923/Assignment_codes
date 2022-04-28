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


def a_b_pruning(depth ,maximize_play,alpha,beta ,current_state,parentNode,eval_nodes):
  move = 'X' if maximize_play else 'O'
  score_per_move,eval_nodes=game_over_check(current_state,eval_nodes)
  if depth == 0 or score_per_move != -1:
    return [score_per_move,eval_nodes]
  if maximize_play :
    eval_max = -math.inf
    count=[]
    for i in range(len(current_state)):
      if current_state[i] == ' ':
        count.append(i)
    index_empty= np.array(count)
    for i in index_empty:
      game_state = current_state.copy()
      game_state[i] = move
      updated_states = game_state
      eval,eval_nodes=a_b_pruning(depth-1,False,alpha,beta ,updated_states,i,eval_nodes)
      eval_max=max(eval_max,eval)
      alpha=max(alpha,eval)
      if (beta<=alpha):
        break
    return [eval_max,eval_nodes]
  else:
    eval_min = math.inf
    count=[]
    for i in range(len(current_state)):
      if current_state[i] == ' ':
        count.append(i)
    index_empty= np.array(count)
    for i in index_empty:
      game_state = current_state.copy()
      game_state[i] = move
      updated_states = game_state
      eval,eval_nodes=a_b_pruning(depth-1,True,alpha,beta ,updated_states,i,eval_nodes)
      eval_min=min(eval_min,eval)
      beta=min(beta,eval)
      if (beta<=alpha):
        break
    return [eval_min,eval_nodes]

game_initial_state=np.array([' ',' ',' ',' ',' ',' ',' ',' ',' '])

alpha_beta_pruning_score,evaluated_nodes_a_b=a_b_pruning(9,True,-math.inf,math.inf,game_initial_state,None,0)
print("Total Evaluated Nodes in Alpha Beta pruning Algorithm = ",evaluated_nodes_a_b)
