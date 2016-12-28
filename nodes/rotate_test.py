import tf
import numpy
from math import *

def rotate_vector(q,v):
    '''
    Rotate vector v by quaternion q
    '''
    vu = tf.transformations.unit_vector(v)
    q2 = list(vu)
    q2.append(0.0)
    out = tf.transformations.quaternion_multiply(
        tf.transformations.quaternion_multiply(q, q2), 
        tf.transformations.quaternion_conjugate(q)
        )[:3]
    return out*tf.transformations.vector_norm(v)

def axisangle_to_q(v, theta):
    v = tf.transformations.unit_vector(v)
    x, y, z = v
    theta /= 2.0
    w = cos(theta)
    x = x * sin(theta)
    y = y * sin(theta)
    z = z * sin(theta)
    return x, y, z, w

q = [0,0,0,1]
v = [0.1,0,0]
print rotate_vector(q,v)

q = [0,0,0,1]
v = [10,0,0]
print rotate_vector(q,v)

q = axisangle_to_q([1,0,0], numpy.pi/2.0)
print rotate_vector(q,v)

r = 0.0
p = 0.0
y = -pi/4.0
q = tf.transformations.quaternion_from_euler(r,p,y)
print q
print rotate_vector(q,v)
