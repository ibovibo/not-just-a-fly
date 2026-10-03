import random
import numpy as np
import matplotlib.pyplot as plt

sol_aci = [6,5,4,3,3,3,2,2,1,1]
sag_aci = [20]



def sinek(geri_bildirim):

    sol_puan = 10
    sag_puan = 10
    ogrenme_hizi = random.uniform(0.05, 0.6)
    sinek_tercih = []

    
    for cagir in range(100):
        
        sag_oran = sol_puan / (sol_puan + sag_puan)
        rs = random.random()
        if geri_bildirim :  

            if sag_oran > rs :
                sinek_tercih.append(0)
                sag_puan = sag_puan + ogrenme_hizi * (sum(sag_aci) - sag_puan)
                    

            else:
                sinek_tercih.append(1)
                sol_puan = sol_puan + ogrenme_hizi * (sum(sol_aci) - sol_puan)

        else :

            if sag_oran > rs :

                sinek_tercih.append(0)
                
                    
            
            else:
                sinek_tercih.append(1)
                


    return sinek_tercih


ogrenen_sinekler = []
ogrenmeyen_sinekler = []

for i in range(1000):
    ogrenen_sinekler.append(sinek(geri_bildirim=True))
    ogrenmeyen_sinekler.append(sinek(geri_bildirim=False))
   


tablo_ogrenen = np.array(ogrenen_sinekler)
print(tablo_ogrenen.shape)
ort_ogrenen = tablo_ogrenen.mean(axis = 0)
print(ort_ogrenen)

tablo_ogrenmeyen = np.array(ogrenmeyen_sinekler)
print(tablo_ogrenmeyen.shape)
ort_ogrenmeyen = tablo_ogrenmeyen.mean(axis = 0)
print(ort_ogrenmeyen)

plt.plot(ort_ogrenen, label = "ort ogrenen")
plt.plot(ort_ogrenmeyen, label = "ort ogrenmeyen")

plt.xlabel("deneme")
plt.ylabel("ayrilma orani")

plt.title("sinek tercih")
plt.legend()
plt.show()