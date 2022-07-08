# Inspired by Nathan A. Rooy code - from https://github.com/nathanrooy/particle-swarm-optimization/blob/master/pso/pso_simple.py

from random import random
from random import uniform
import sys
from turtle import position

class Particle:
    def __init__(self, num_dimensions, bound_x1, bound_x2):
        self.err_best=sys.maxsize
        self.err=sys.maxsize
        self.bounds = (bound_x1, bound_x2)
        self.num_dimensions = num_dimensions
        self.velocity = []

        for i in range(0, self.num_dimensions):
            self.velocity.append(uniform(-1,1))
            self.position = [uniform(bound_x1[0], bound_x1[1]), 
                                uniform(bound_x2[0], bound_x2[1])]
            self.pos_best = self.position

    def evaluate(self, obj_func):
        self.err = obj_func(self.position[0], self.position[1])

        # check to see if the current position is an individual best
        if self.err < self.err_best or self.err_best==-1:
            self.pos_best = self.position
            self.err_best = self.err
                    
    def update_velocity(self, pos_best_g):
        w=0.5
        c1=2.05
        c2=2.05
        
        for i in range(0, self.num_dimensions):
            r1=random()
            r2=random()
            
            vel_cognitive      =     c1*r1*(self.pos_best[i]-self.position[i])
            vel_social         =     c2*r2*(pos_best_g[i]-self.position[i])
            self.velocity[i]   =     w*self.velocity[i]+vel_cognitive+vel_social

    def update_position(self):
        for i in range(0, self.num_dimensions):
            self.position[i] = self.position[i] + self.velocity[i]
            
            if self.position[i] <= self.bounds[i][0]:
                self.position[i] = self.bounds[i][0]+0.0001
                
            if self.position[i] >= self.bounds[i][1]:
                self.position[i] = self.bounds[i][1]-0.0001
        print(self.position)
        
        
class PSO():
    def __init__(self, num_dimensions, penalty_func, obj_func, bounds, num_particles, max_iter):

        self.num_dimensions=num_dimensions
        self.err_best_g=sys.maxsize
        self.err_curr_g=sys.maxsize
        self.pos_best_curr=tuple()
        self.pos_best_g=tuple()
        self.max_iter = max_iter
        self.bounds = bounds
        self.obj_func = obj_func
        self.penalty_func = penalty_func
        self.num_particles = num_particles
        self.max_iter = max_iter

        self.swarm=[]
        for i in range(0, num_particles):
            self.swarm.append(Particle(self.num_dimensions, self.bounds[0], self.bounds[1]))

    def minimize(self):
        infeasible = False
        for _ in range(self.max_iter):
            particles = []
            for i in range(0, self.num_particles):
                particles.append(self.swarm[i].position)
                
            pf = 0.45
            for _ in range(0, self.num_particles):
                for n in range(0, self.num_particles-1):  
                    u = uniform(0,1)
                    p_i_curr = particles[n]
                    p_i_next = particles[n+1]
                    if self.penalty_func(p_i_curr[0], p_i_curr[1]) == 0 and self.penalty_func(p_i_next[0], p_i_next[1]) == 0 or u < pf:
                        if self.obj_func(p_i_curr[0], p_i_curr[1]) > self.obj_func(p_i_next[0], p_i_next[1]):
                            particles[n], particles[n+1] = particles[n+1], particles[n]
                    if self.penalty_func(p_i_curr[0], p_i_curr[1]) > self.penalty_func(p_i_next[0], p_i_next[1]):
                        particles[n], particles[n+1] = particles[n+1], particles[n]
                    
            # check if it's the best value reached until now 
            if self.penalty_func(particles[0][0], particles[0][1]) == 0: # check if it's feasible
                if self.obj_func(particles[0][0], particles[0][1]) < self.err_best_g:
                    self.pos_best_g=particles[0]
                    self.pos_best_curr = particles[0]
                    infeasible = False
            elif self.obj_func(particles[0][0], particles[0][1]) < self.err_curr_g:
                self.pos_best_curr = particles[0]
                infeasible = True

            for i in range(0, self.num_particles):
                if not infeasible:
                    self.swarm[i].update_velocity(self.pos_best_g)
                else:
                    self.swarm[i].update_velocity(self.pos_best_curr)
                self.swarm[i].update_position()

            for i in range(0, self.num_particles):
                self.swarm[i].evaluate(self.obj_func)

        # print(self.pos_best_curr)
        return self.pos_best_g, self.obj_func(self.pos_best_g[0], self.pos_best_g[1])

        

