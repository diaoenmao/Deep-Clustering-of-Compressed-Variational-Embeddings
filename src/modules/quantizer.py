import config
import torch
import torch.nn as nn
from functions import Quantize as QuantizeFunction

class Quantizer(nn.Module):
    def __init__(self):
        super(Quantizer, self).__init__()
        if(config.PARAM['num_level']==0):
            self.quantizer = nn.Sequential()
        elif(config.PARAM['num_level']>=2):
            self.quantizer = Quantize(config.PARAM['num_level'])
        else:
            raise ValueError('Invalid number of quantization level')

    def forward(self, input):        
        x = input*(config.PARAM['num_level']//2) if(config.PARAM['num_level']>2) else input
        x = self.quantizer(x)
        return x
    
class Quantize(nn.Module):
    def __init__(self,num_level):
        super().__init__()
        self.num_level = num_level
        
    def forward(self, x):
        return QuantizeFunction.apply(x,self.num_level,self.training)

