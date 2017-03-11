#python
#-------------------------------------------------------------------------------
# Name:
# Version: 
# Purpose: 
#
# Author:      
#
# Created:     
# Copyright:   
#-------------------------------------------------------------------------------


lx.out("Hello World!")
for x in range(5):
   lx.eval('item.create mesh')
   lx.eval('item.name {MyMesh%02d}' % x)
#lx.eval('script.implicit "Unit Cylinder Item"')
zdepth=12
lx.eval('item.setPosition z:%s' %zdepth)
zdept2=5
lx.eval('item.setPosition z:%s' %zdept2)

lx.eval(Cylinder='script.implicit "Unit Box Item"')
lx.eval(Cylinder)
