import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB.Structure import StructuralFramingUtils

clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

#The inputs to this node will be stored as a list in the IN variables.
dataEnteringNode = IN

beam_list = IN[0]

doc = DocumentManager.Instance.CurrentDBDocument
TransactionManager.Instance.EnsureInTransaction(doc)

for beam in beam_list:
	beam = UnwrapElement(beam)
	StructuralFramingUtils.DisallowJoinAtEnd(beam,0)
	StructuralFramingUtils.DisallowJoinAtEnd(beam,1)

TransactionManager.Instance.TransactionTaskDone()
#Assign your output to the OUT variable.
OUT = beam_list
