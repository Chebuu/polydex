from stk import *

###
# Functional Groups
###

""" [Dextrose] Forms an alpha 1,4-glycosidic bond at the anomeric carbon """
C1_OH = SmartsFunctionalGroupFactory(
    smarts='[#6]-1(-[#6]-[#6]-[#6]-[#6](-[#8]-1)-[#8]-[#1])-[#6]-[#8]-[#1]',
    bonders=(6,),
    deleters=(7,)
)

""" [Dextrose] Forms an alpha 1,4-glycosidic bond at C4 """
C4_OH = SmartsFunctionalGroupFactory(
    smarts='[#6]-1(-[#6](-[#6]-[#6]-[#6](-[#8]-1)-[#8]-[#1])-[#8]-[#1])-[#6]-[#8]-[#1]',
    bonders=(8,),
    deleters=(9,)
)

""" [Dextrose] Forms an ether bond between glucose and a given linker at C6 """
C6_OH = SmartsFunctionalGroupFactory(
    smarts='[#6]-1(-[#6]-[#6]-[#6]-[#6]-[#8]-1)-[#6]-[#8]-[#1]',
    bonders=(7,),
    deleters=(8,)
)

""" [R-O-dextrose] Forms an alpha 1,4-glycosidic bond at the anomeric carbon """
C1_OH_lk = SmartsFunctionalGroupFactory(
    smarts='[#6]-1(-[#6](-[#6](-[#6](-[#6](-[#8]-1)-[#8]-[#1])-[#8]-[#1])-[#8]-[#1])-[#8]-[#1])-[#6]-[#8]',
    bonders=(6,),
    deleters=(7,)
)

""" [R-O-dextrose] Forms an alpha 1,4-glycosidic bond at C4 """
C4_OH_lk = SmartsFunctionalGroupFactory(
    smarts='[#6]-1(-[#6](-[#6](-[#6](-[#6](-[#8]-1)-[#8]-[#1])-[#8]-[#1])-[#8]-[#1])-[#8]-[#1])-[#6]-[#8]',
    bonders=(12,),
    deleters=(13,)
)

###
# Building Blocks
###

""" Alpha-D-glucose """
dextrose = BuildingBlock(
    smiles='C([C@@H]1[C@H]([C@@H]([C@H]([C@H](O1)O)O)O)O)O',
    functional_groups=(C6_OH,)
)

""" Forms a single link between macrocycles (CO-C[n]-OC) """
strut = BuildingBlock(
    smiles='CCCCBr',
    functional_groups=[BromoFactory()]
)

###
# Constructed Molecules
###

""" Forms a dextrose-strut ether bond at C6 """
micro_unit = ConstructedMolecule(
    topology_graph=polymer.Linear(
        building_blocks=(dextrose, strut),
        repeating_unit='AB',
        num_repeating_units=1,
    )
)

""" Forms alpha-glycosidic cyclodextrin """
micro_block = BuildingBlock.init_from_molecule(
    molecule=micro_unit,
    functional_groups=(C1_OH_lk, C4_OH_lk,)
)

macro_cycle = ConstructedMolecule(
    topology_graph=macrocycle.Macrocycle(
        building_blocks=(micro_block,),
        repeating_unit='A',
        num_repeating_units=6,
    )
)
