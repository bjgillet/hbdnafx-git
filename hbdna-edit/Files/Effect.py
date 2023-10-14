'''
This module contains all Classes to manage hbdna effects.
'''

from os import path
from HbData import HbData

 
class Effect:
  
  ''' 
  
  This Class defines effects used by hbdna.
  As hbdna-edit will create an effect from either an hbdna file, USB communication with device, or user interaction, an Effect instance will be created.
 
  Those objects have been designed to have a small memory footprint. (between 200 and 1800 of them will be required in memory to match device)
  Size of an effect is between <To be measured>
 
  For this,they use cross reference with a single HbData instance that contains detailed item names and paramaters.
  
  If executed rather than being instanciated, it will run it's unit test code.

  '''
  
  def __init__(self, hb_data, section=None, eff_id=None):
  
    '''

    Initialize a new effect in memory.

    parameters :
      self : instance reference
      hb_data :   HbData object - mandatory
                    is a shared, reference instance containing all detailed informations about effects 
                    such as belonging section, names, IDs, number name and range of parameters, etc. See HbData Class for more informations.
      section :   String - Facultative - Is None by default.
                    Name of one within the nine possible sections for a preset, declared in hb_data.json and accessed through 
                    hHbData instance. 
                    Possible values are in :
                      ["FX/COMP", "DS/OD", "AMP", "CAB", "NS/GATE", "EQ", "MOD","DELAY", "REVERB"]
      eff_id : int - Facultative - is None by default.
                    Contains the effect id of the possible effects per section.
                    In case a section is at None but an eff_id is passed, refresh(self, section=None, eff_id=None) will left it
                    to None as no such effect cannot be valid.
                    Effects ID per section are consultable in either hb_data.json or from the 03_Files glonal documentation.

    '''
  
    self.hb_data = hb_data
    self.refresh(section, eff_id)
    
  def refresh(self, section=None, eff_id=None):

    '''

    Populates effect from self.hb_data reference instance. 

    Parameters :
      section :  String - Facultative - None by default
                  Secton name to which Effects belong. See  __init__(self, hb_data, section=None, eff_id=None)
                  for more informations.
      eff_id :  int - Facultative - None by default
                  Effect ID within a given section. See  __init__(self, hb_data, section=None, eff_id=None)
                  for more informations.


    '''
    if  (section != None) and (eff_id != None):
      self.section = section
      self.eff_id = eff_id
      if eff_id != None:
        self.eff_data=self.hb_data.get_effects(self.section, eff_id)

  def get_effect(self):

    '''

    Returns current effect ID as int or None.

    '''

    return self.eff_data

  def get_name(self):
    
    '''

    Returns current effect Name as String or None.

    '''

    return self.eff_data[0]

  def get_params_number(self):

    '''

    Returns number of params in current effect as int or None

    '''

    return len(self.eff_data)-2
  
  def get_params(self):

    '''

    Returns list of possible params id for current effect as a list of int or None.
    Check File.hb_data.json or File.HbParam for list of params per ID.

    '''
    
    return self.eff_data[1:len(self.eff_data)-1]
    
   
  def _debug(self):

    '''

    Internal debug method used by __name__=='__main__' unit testing code.
    
    '''
    

    print("hb_data structure = ", self.hb_data)
    print("section = ", self.section)
    print("Effect ID =", self.eff_id)


#   :
#   :   Unit test code
#   :

if __name__=='__main__':

  hb_data = HbData()
  effect = Effect(hb_data,"AMP",30)
  print(effect.hb_data)
  print(effect.get_effect())
  print("effect name : ",effect.get_name())
  print("Effect parameters number : ", effect.get_params_number())
  print("Effect params : ", effect.get_params())
