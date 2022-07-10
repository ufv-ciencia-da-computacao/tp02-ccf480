from random import random
from random import uniform
import sys
from math import sqrt
class Particle:
    def __init__(self, num_dimensions, bounds, obj_func):
        self.err_best=sys.maxsize
        self.err=sys.maxsize
        self.bounds = bounds
        self.num_dimensions = num_dimensions
        self.velocity = [0 for _ in range(self.num_dimensions)]
        self.position = [bounds[j][0] + uniform(0,1)*(bounds[j][1]-bounds[j][0]) for j in range(self.num_dimensions)]
        self.pos_best = self.position
        self.best_value = obj_func(self.pos_best)

    def evaluate(self, penalty_func, obj_func):
        self.err = penalty_func(self.position)
        value = obj_func(self.position)

        # check to see if the current position is an individual best
        if self.err <= self.err_best:
            if value < self.best_value:
                self.pos_best = self.position.copy()
                self.err_best = self.err
                self.best_value = value
                    
    def update_velocity(self, pos_best_g, r1, r2, w):
        c1=2.05
        c2=2.05
        
        tao = c1+c2
        k = 2/(abs(2-tao-sqrt(((tao**2)-4*tao))))
        for i in range(0, self.num_dimensions):           
            vel_cognitive      =     c1*r1*(self.pos_best[i]-self.position[i])
            vel_social         =     c2*r2*(pos_best_g[i]-self.position[i])
            self.velocity[i]   =     k*((w*self.velocity[i])+vel_cognitive+vel_social)

    def update_position(self): # mudar isso aqui
        for i in range(0, self.num_dimensions):
            self.position[i] = self.position[i] + self.velocity[i]

            if self.position[i] <= self.bounds[i][0]:
                self.position[i] = self.bounds[i][0]
                self.velocity[i] = -self.velocity[i]
                
            if self.position[i] >= self.bounds[i][1]:
                self.position[i] = self.bounds[i][1]
                self.velocity[i] = -self.velocity[i]

        #print(self.position)
        
        
class PSO():
    def __init__(self, num_dimensions, penalty_func, obj_func, bounds, num_particles, max_iter):

        self.num_dimensions=num_dimensions
        self.err_best_g=sys.maxsize
        self.err_curr=sys.maxsize
        self.pos_best_curr=tuple()
        self.pos_best_g=tuple()
        self.max_iter = max_iter
        self.bounds = bounds
        self.obj_func = obj_func
        self.penalty_func = penalty_func
        self.num_particles = num_particles
        self.max_iter = max_iter
        self.w_max = 0.9
        self.w_min = 0.4
        self.swarm=[]
        for i in range(0, num_particles):
            self.swarm.append(Particle(self.num_dimensions, self.bounds, self.obj_func))

    def minimize(self):
        infeasible = False
        for index in range(self.max_iter):
            particles = []
            for i in range(0, self.num_particles):
                particles.append(self.swarm[i].position.copy())
                
            pf = 0.45
            for _ in range(self.num_particles):
                swap=False
                for n in range(self.num_particles-1):  
                    u = uniform(0,1)
                    p_i_curr = particles[n]
                    p_i_next = particles[n+1]
                    
                    if (self.penalty_func(p_i_curr) == 0 and self.penalty_func(p_i_next) == 0) or u < pf:
                        if self.obj_func(p_i_curr) > self.obj_func(p_i_next):
                            swap=True
                            particles[n], particles[n+1] = particles[n+1], particles[n]
                    elif self.penalty_func(p_i_curr) > self.penalty_func(p_i_next):
                        swap = True
                        particles[n], particles[n+1] = particles[n+1], particles[n]

                if not swap:
                    break

            print(list(map(self.penalty_func, particles)))
                    
            # check if it's the best value reached until here
            if self.penalty_func(particles[0]) == 0: # check if it's feasible
                if self.obj_func(particles[0]) < self.err_best_g:
                    self.pos_best_g=particles[0].copy()
                    self.pos_best_curr = particles[0].copy()
                    self.err_curr = self.penalty_func(particles[0])
                    self.err_best_g = self.obj_func(particles[0])
                    infeasible = False
            elif self.penalty_func(particles[0]) < self.err_curr: # mudar isso aqui. O que o pos_best_curr tem que ser? a menor penalidade?
                self.pos_best_curr = particles[0].copy()
                self.err_curr = self.penalty_func(particles[0])
                infeasible = True

            r1 = uniform(0, 1)
            r2 = uniform(0,1)
            w=self.w_max-((self.w_max-self.w_min)/self.max_iter)*index
            
            for i in range(0, self.num_particles):
                if not infeasible:
                    self.swarm[i].update_velocity(self.pos_best_g, r1, r2, w)
                else:
                    self.swarm[i].update_velocity(self.pos_best_curr, r1, r2, w)
                self.swarm[i].update_position()

            for i in range(0, self.num_particles):
                self.swarm[i].evaluate(self.penalty_func, self.obj_func)

            print(index, end=" ")
            print(self.obj_func(self.pos_best_curr), self.pos_best_curr, self.err_curr)
        return self.pos_best_g, self.obj_func(self.pos_best_g)

        

