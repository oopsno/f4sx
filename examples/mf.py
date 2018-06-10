# encoding: UTF-8

"""
Generate a console script which just adds all MF items to your character.
"""

from f4sx import ScriptWriter, ObjectID
from itertools import chain

console = ScriptWriter()

console.comment('MF Switch Manual')
for manual in ObjectID.range('11FFFF01', '11FFFF09', 2):
    console.player.additem(manual)

console.comment('[MF Custom] weapons')
for mf_custom_weapon in chain(ObjectID.range('11CAC001', '11CAC00F'),
                              ObjectID.range('11CAC011', '11CAC01A')):
    console.player.additem(mf_custom_weapon)

console.comment('MF Ammo')
for ammo in chain(ObjectID.range('1100A101', '1100A107'),
                  ObjectID.range('1100A111', '1100A115'),
                  ObjectID.range('0001F276'),
                  ObjectID.range('0001F278', '0001F279'),
                  ObjectID.range('0001F66A', '0001F66B')):
    console.player.additem(ammo, 1000)

console.comment('Firearm parts')
for misc in chain(ObjectID.range('11001301', '11001308'),
                  ObjectID.range('11001311', '11001316'),
                  ObjectID.range('11001321'),
                  ObjectID.range('11001331', '11001332'),
                  ObjectID.range('11001371', '11001375', 4),
                  ObjectID.range('11001381', '11001386'),
                  ObjectID.range('11001361', '11001365', 2),
                  ObjectID.range('11102851', '11102856'),
                  ObjectID.range('11102861', '11102868'),
                  ObjectID.range('11102871', '1110287C'),
                  ObjectID.range('11102A21', '11102A2E'),
                  ObjectID.range('11102A31', '11102A32')):
    console.player.additem(misc, 1000)

console.comment('MF Accessory')
for accessory in chain(ObjectID.range('11002822', '11002828'),  # AR ButtStock
                       ObjectID.range('1100282A', '1100282F'),  # AR ButtStock
                       ObjectID.range('11012820', '1101282F'),  # AR ButtStock
                       ObjectID.range('110128B1', '110128B5'),  # AK ButtStock
                       ObjectID.range('11002881', '1100288B'),  # MF Accessory
                       ObjectID.range('11002892', '1100289C'),
                       ObjectID.range('11012883', '11012888'),
                       ObjectID.range('110128B8', '110128B9')):
    console.player.additem(accessory, 1000)

with open('MF.txt', 'w') as mf:
    console.scof(mf)
