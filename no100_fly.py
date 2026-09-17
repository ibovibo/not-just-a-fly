import random
import numpy as np

sol_aci = [6,5,4,3,3,3,2,2,1,1]
sag_aci = [20]



def sinek():

    sol_puan = 10
    sag_puan = 10
    ogrenme_hizi = random.uniform(0.05, 0.6)
    sinek_tercih = []

    
    for cagir in range(100):
        
        sag_oran = sol_puan / (sol_puan + sag_puan)
        rs = random.random()
            
        if sag_oran > rs :
            sinek_tercih.append(0)
            sag_puan = sag_puan + ogrenme_hizi * (sum(sag_aci) - sag_puan)
                

        else:
            sinek_tercih.append(1)
            sol_puan = sol_puan + ogrenme_hizi * (sum(sol_aci) - sol_puan)

    return sinek_tercih


tum_sinekler = []

for i in range(100):
    tum_sinekler.append(sinek())
   


tablo = np.array(tum_sinekler)
print(tablo.shape)
print(tablo.mean(axis = 0))
