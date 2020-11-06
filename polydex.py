from stk import *

###
# Functional Groups
###

""" Forms an ether bond between glucose and a given linker molecule """
C6_OH = SmartsFunctionalGroupFactory(
    smarts='[#6]-1(-[#6]-[#6]-[#6]-[#6]-[#8]-1)-[#6]-[#8]-[#1]',
    bonders=(7,),
    deleters=(8,)
)

""" Forms an alpha 1,4-glycosidic bond at the anomeric carbon """
# C1_OH = SmartsFunctionalGroupFactory(
#     smarts=,
#     bonders=,
#     deleters=
# )

""" Forms an alpha 1,4-ether bond at C4 """
# C4_OH = SmartsFunctionalGroupFactory(
#     smarts=,
#     bonders=,
#     deleters=
# )

###
# Building Blocks
###

""" Alpha-D-glucose """
dextrose = BuildingBlock(
    smiles='C([C@@H]1[C@H]([C@@H]([C@H]([C@H](O1)O)O)O)O)O',
    functional_groups=(C6_OH,)
)

""" Forms a link between macrocycles (CO-C[n]-OC) """
strut = BuildingBlock(
    smiles='CCCCBr',
    functional_groups=[BromoFactory()]
)

###
# Constructed Molecules
###

""" Forms six dextrose-strut ether bonds at C6 """
micro_unit = ConstructedMolecule(
    topology_graph=polymer.Linear(
        building_blocks=(dextrose, strut),
        repeating_unit='AB',
        num_repeating_units=1,
    )
)

# """ Forms a dextrose starch """
# ConstructedMolecule(
#     topology_graph=polymer.Linear(
#         building_blocks=(dextrose,),
#         repeating_unit='A',
#         num_repeating_units=6,
#     )
# )

# # Forms alpha-glycosidic cyclodextrin
# ConstructedMolecule(
#     topology_graph=macrocycle.Macrocycle(
#         building_blocks=(dextrose,dextrose),
#         repeating_unit='A',
#         num_repeating_units=3,
#     )
# )

