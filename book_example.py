# -*- coding: utf-8 -*-
"""
Pieter Spaepen
februari 2018

"""

from node import node
from node import nodeTable
from truss import truss
from element import element
import numpy as np


""" 
text book example
"""

""" setting up the list of nodes """
def book_example():
    """ setting up the list of nodes """
    # input all nodes with their respective nr and x,y position
    # initialize an empty node table
    NTble = nodeTable()
    # add elements to the node table usig addNode_to_table
    NTble.addNode_to_table(node(0,0,0,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(1,0,0,0,0,np.nan,np.nan))
    NTble.addNode_to_table(node(2,3*12,0,np.nan,np.nan,np.nan,np.nan))
    NTble.addNode_to_table(node(3,0,3*12,0,0,np.nan,np.nan))
    NTble.addNode_to_table(node(4,3*12,3*12,np.nan,np.nan,np.nan,-500))
    NTble.addNode_to_table(node(5,6*12,3*12,np.nan,np.nan,np.nan,-500))
  
    
    """ setting up the list of elements """
    
    #create an empty truss
    Tr = truss(1)

    #add elements using addElementByNode     
    Tr.addElementByNode(NTble,1,2)
    Tr.addElementByNode(NTble,3,2)
    Tr.addElementByNode(NTble,3,4)
    Tr.addElementByNode(NTble,2,4)
    Tr.addElementByNode(NTble,2,5)
    Tr.addElementByNode(NTble,4,5)
    
    
    return Tr