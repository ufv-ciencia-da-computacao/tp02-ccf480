# Inspired by Nathan A. Rooy code - from https://github.com/nathanrooy/particle-swarm-optimization/blob/master/pso/pso_simple.py

from random import random
from random import uniform

class Particle:
    def __init__(self, x0, num_dimensions, bounds):
        self.position_i=[]
        self.velocity_i=[]
        self.pos_best_i=[]
        self.err_best_i=-1
        self.err_i=-1
        self.bounds = bounds
        self.num_dimensions = num_dimensions

        for i in range(0, self.num_dimensions):
            self.velocity_i.append(uniform(-1,1))
            self.position_i.append(x0[i])

    def evaluate(self, obj_func): # change to sthocatic ranking
        self.err_i = obj_func(self.position_i)

        # check to see if the current position is an individual best
        if self.err_i<self.err_best_i or self.err_best_i==-1:
            self.pos_best_i=self.position_i.copy()
            self.err_best_i=self.err_i
                    
    def update_velocity(self, pos_best_g):
        w=0.5
        c1=1
        c2=2
        
        for i in range(0, self.num_dimensions):
            r1=random()
            r2=random()
            
            vel_cognitive      =     c1*r1*(self.pos_best_i[i]-self.position_i[i])
            vel_social         =     c2*r2*(pos_best_g[i]-self.position_i[i])
            self.velocity_i[i] =     w*self.velocity_i[i]+vel_cognitive+vel_social

    def update_position(self):
        for i in range(0, self.num_dimensions):
            self.position_i[i] = self.position_i[i] + self.velocity_i[i]
            
            if self.position_i[i] > self.bounds[i][1]:
                self.position_i[i] = self.bounds[i][1]

            if self.position_i[i] < self.bounds[i][0]:
                self.position_i[i] = self.bounds[i][0]
        
        
class PSO():
    def __init__(self, obj_func, x0, bounds, num_particles, max_iter):

        self.num_dimensions=len(x0)
        self.err_best_g=-1
        self.pos_best_g=[]
        self.max_iter = max_iter
        self.bounds = bounds
        self.obj_func = obj_func
        self.num_particles = num_particles

        self.swarm=[]
        for i in range(0, num_particles):
            self.swarm.append(Particle(x0, self.num_dimensions, self.bounds))

    def minimize(self):
        i=0
        while i < self.maxiter:
            for j in range(0, self.num_particles):
                self.swarm[j].evaluate(self.obj_func)

                if self.swarm[j].err_i < err_best_g or err_best_g == -1: # change to sthocastic ranking
                    pos_best_g=list(self.swarm[j].position_i)
                    err_best_g=float(self.swarm[j].err_i)

            for j in range(0, self.num_particles):
                self.swarm[j].update_velocity(pos_best_g)
                self.swarm[j].update_position()
            i+=1