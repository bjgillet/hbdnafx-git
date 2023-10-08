from os import path
import json

class HbData:
    def __init__(self,str_data_file=None):
        if str_data_file == None :
            str_data_file = path.dirname(__file__)+"/hb_data.json"
            print("data file : ",str_data_file)
        self.fd = open(str_data_file)
        self.hb_data = json.load(self.fd)

    def get_default(self,cat, id=None):

        if id==None :
            return self.hb_data[cat]
        elif id > len(self.hb_data[cat]) -1 :
            return (None)
        else :
            return self.hb_data[cat][id]
        
    def get_sections(self,id=None):
        self.get_default("SECTIONS", id)

    def get_params(self, id=None):
        self.get_default("PARAMS", id)

    def get_params_name(self,params):
        p_name=[]
        for p in (params):
            if p < len(self.hb_data["PARAMS"]):
                p_name.append(self.hb_data["PARAMS"][p][0])
            else :
                return None
        return p_name

    def get_effects(self, sect=None, id=None):
        if id==None :
            return self.hb_data["EFFECTS"]
        elif id > len(self.hb_data["EFFECTS"][sect]) -1 :
            return (None)
        else :
            return self.hb_data["EFFECTS"][sect][id]
        
            

if __name__ == '__main__':
    hbdata = HbData()
    print("===================  SECTIONS =================================")
    print ("All Sections : ", hbdata.get_sections())
    print("First section : ", hbdata.get_sections(1))
    print ("Bad Sections : ", hbdata.get_sections(123))
    print("====================================================")

    print("===================  PARAMS =================================")
    print ("All Params : ", hbdata.get_params())
    print("Param get : ", hbdata.get_params(1))
    print ("Bad Param : ", hbdata.get_params(123))
    print("Params names for [23, 18, 28, 53, 36, 31] : ",hbdata.get_params_name([23, 18, 28, 53, 36, 31]))
    print("Invalid Params names for [23, 18, 28, 255, 36, 31] : ",hbdata.get_params_name([23, 18, 28, 255, 36, 31]))
    print("====================================================")

    print("===================  EFFECTS  =================================")
    print ("All Sections : ", hbdata.get_effects())
    print("First section : ", hbdata.get_effects('AMP',12))
 #   print ("Bad Sections : ", hbdata.get_effects('TRUC',2))
    print("====================================================")

    
