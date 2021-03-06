# Harmonic potential with respect to a fixed point in space

from MMTK.ForceFields.ForceField import ForceField
from MMTK_HarmonicWell import HarmonicWellTerm

class HarmonicWellForceField(ForceField):

    """
    Harmonic potential with respect to a fixed point in space
    """

    def __init__(self, atom, xc,yc,zc, force_constant):
        """
        @param atom: the atom on which the force field acts
        @type atom: L{MMTK.ChemicalObjects.Atom}
        @param center: the point to which the atom is attached by
                       the harmonic potential
        @type center: L{Scientific.Geometry.Vector}
        @param force_constant: the force constant of the harmonic potential
        @type force_constant: C{float}
        """
        # Get the internal index of the atom if the argument is an
        # atom object. It is the index that is stored internally,
        # and when the force field is recreated from a specification
        # in a trajectory file, it is the index that is passed instead
        # of the atom object itself. Calling this method takes care
        # of all the necessary checks and conversions.
        self.atom_index = self.getAtomParameterIndices([atom])[0]
        # Store arguments that recreate the force field from a pickled
        # universe or from a trajectory.
        # Store the parameters for later use.
        self.x = xc
        self.y = yc
        self.z = zc
        self.forceconstant = force_constant

        self.arguments = (self.atom_index, self.x,self.y,self.z, self.forceconstant)
        
        # Initialize the ForceField class, giving a name to this one.
        ForceField.__init__(self, 'HarmonicWell')

    # The following method is called by the energy evaluation engine
    # to inquire if this force field term has all the parameters it
    # requires. This is necessary for interdependent force field
    # terms. In our case, we just say "yes" immediately.
    def ready(self, global_data):
        return True

    def supportsPathIntegrals(self):
        return True
    
    # The following method is called by the energy evaluation engine
    # to obtain a list of the low-level evaluator objects (the C routines)
    # that handle the calculations.
    def evaluatorTerms(self, universe, subset1, subset2, global_data):
        # The subset evaluation mechanism does not make much sense for
        # this force field, so we just signal an error if someone
        # uses it by accident.
        if subset1 is not None or subset2 is not None:
            raise ValueError("sorry, no subsets here")
        # Here we pass all the parameters as "simple" data types to
        # the C code that handles energy calculations.
        f, offsets = self.beadOffsetsAndFactor([self.atom_index], global_data)
        return [HarmonicWellTerm(universe._spec,
                                       self.atom_index + o1,
                                       self.x, self.y,
                                       self.z, self.forceconstant) for o1, in offsets]

    def description(self):
        return "HarmonicWellFF.HarmonicWellForceField" + `self.arguments`
        #return self.__class__.__name__ + `self.arguments`

