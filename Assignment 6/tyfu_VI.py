'''tyfu_VI.py
(rename this file using your own UWNetID.)

Value Iteration for Markov Decision Processes.
'''

import math

# Edit the returned name to ensure you get credit for the assignment.
def student_name():
   return "Fu, Tianyuan" # For an autograder.

Vkplus1 = {}
Q_Values_Dict = {}

def one_step_of_VI(S, A, T, R, gamma, Vk):
   '''S is list of all the states defined for this MDP.
   A is a list of all the possible actions.
   T is a function representing the MDP's transition model.
   R is a function representing the MDP's reward function.
   gamma is the discount factor.
   The current value of each state s is accessible as Vk[s].
   '''

   '''Your code should fill the dictionaries Vkplus1 and Q_Values_dict
   with a new value for each state, and each q-state, and assign them
   to the state's and q-state's entries in the dictionaries, as in
	   Vkplus1[s] = new_value
	   Q_Values_Dict[(s, a)] = new_q_value

   Also determine delta_max, which we define to be the maximum
   amount that the absolute value of any state's value is changed
   during this iteration.
   '''

   global Q_Values_Dict
   global Vkplus1

   for s in S:
      Q_value_max = - math.inf
      for a in A:
         Q_value = 0
         # sum up rewards for all s' states
         for new_s in S:
            Q_value += T(s, a, new_s) * (R(s, a, new_s) + gamma * Vk[new_s])
         
         if Q_value > Q_value_max:
            Q_value_max = Q_value

         Q_Values_Dict[(s, a)] = Q_value

      Vkplus1[s] = Q_value_max

   delta_max = 0

   # calculate deltamax
   for s in S:
      diff = abs(Vkplus1[s] - Vk[s])
      if diff > delta_max:
         delta_max = diff

   return (Vkplus1, delta_max)

def return_Q_values(S, A):
   '''Return the dictionary whose keys are (state, action) tuples,
   and whose values are floats representing the Q values from the
   most recent call to one_step_of_VI. This is the normal case, and
   the values of S and A passed in here can be ignored.
   However, if no such call has been made yet, use S and A to
   create the answer dictionary, and use 0.0 for all the values.
   '''

   global Q_Values_Dict

   if len(Q_Values_Dict) == 0:
      for s in S:
         for a in A:
            Q_Values_Dict[(s, a)] = 0.0

   return Q_Values_Dict # placeholder

Policy = {}
def extract_policy(S, A):
   '''Return a dictionary mapping states to actions. Obtain the policy
   using the q-values most recently computed.  If none have yet been
   computed, call return_Q_values to initialize q-values, and then
   extract a policy.  Ties between actions having the same (s, a) value
   can be broken arbitrarily.
   '''
   global Policy
   Policy = {}

   Q_values = return_Q_values(S, A)
   for s in S:
      # find the maximized utility
      Policy[s] = A[0]
      utility = Q_values[(s, A[0])]
      for a in A:
         if Q_values[(s, a)] > utility:
            Policy[s] = a

   return Policy

def apply_policy(s):
   '''Return the action that your current best policy implies for state s.'''
   global Policy
   return Policy[s]


