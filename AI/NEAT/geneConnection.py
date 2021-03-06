from __future__ import annotations
from geneNode import BaseGeneNode
from mutations import Incrementer

class GeneConnection():
    """
        A single connection between 2 nodes
    """

    def __init__(self, inGeneNode : BaseGeneNode, outGeneNode : BaseGeneNode, innovationNumber : Incrementer , weight : float = 0, enabled : bool = True) -> None:
        """
            Input:
                1) inGeneNode       - The gene node from
                2) outGeneNode      - The gene node to
                3) weight           - The weight of the connection
                4) enabled          - Is the connection enabled
                4) innovationNumber - Keep track with this number
        """
        
        self.inGeneNode         : BaseGeneNode  = inGeneNode
        self.outGeneNode        : BaseGeneNode  = outGeneNode
        self.weight             : float         = weight
        self.enabled            : bool          = enabled
        self.innovation         : int           = innovationNumber()

    def __eq__(self, other : GeneConnection) -> bool:

        if isinstance(other, self):
            return True

        return self.inGeneNode == other.inGeneNode and self.outGeneNode == other.outGeneNode
    
    # def calc_in_value(self, input: float) -> float:
    #     return self.weight * input
    
    