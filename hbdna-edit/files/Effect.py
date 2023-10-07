
from os import path
from HbData import HbData

class Effect:
  def __init__(self, hb_data, section=None, eff_id=None):
    self.hb_data = hb_data
    self.section = section
    self.eff_id = eff_id
    self.refresh(self.section, self.eff_id)
    
  def refresh(self, section=None, eff_id=None):
    if  (section != None) and (eff_id != None):
      self.section = section
      self.eff_id = eff_id
      if eff_id != None:
        self.eff_data=self.hb_data.get_effects(self.section, eff_id)

  def get_effect(self):
    return self.eff_data

  def get_name(self):
    return self.eff_data[0]

  def get_params_number(self):
    return len(self.eff_data)-1
  
  def get_params(self):
    return self.eff_data[1:len(self.eff_data)-1]
    
   
  def debug(self):
    print("hb_data structure = ", self.hb_data)
    print("section = ", self.section)
    print("Effect ID =", self.eff_id)

if __name__=='__main__':
  effect = Effect("coucou")
  effect.debug()
  effect.refresh(4)
  effect.debug()
  hb_data = HbData("/home/doudou/DEV/HB100-DNAfx-git/files/json/hb_data.json")
  effect2 = Effect(hb_data,"AMP",30)
  print(effect2.hb_data)
  print(effect2.get_effect())
  print("effect name : ",effect2.get_name())
  print("Effect parameters number : ", effect2.get_params_number())
  print("Effect params : ", effect2.get_params())
  print("Target hb_data filename : ", path.dirname(__file__) + "/json/hbdata.json")