import random

sol_aci = [6,5,4,3,3,3,2,2,1,1]
sag_aci = [20]

sol_puan = 10
sag_puan = 10
ogrenme_hizi = 0.3

sinek_tercih = []


for secim in range(100000):

        
        sag_oran = sol_puan / (sol_puan + sag_puan)
        rs = random.random()
        
        if sag_oran > rs :
            sinek_tercih.append(0)
            sag_puan = sag_puan + ogrenme_hizi * (sum(sag_aci) - sag_puan)
            

        else:
            sinek_tercih.append(1)
            sol_puan = sol_puan + ogrenme_hizi * (sum(sol_aci) - sol_puan)

print(f"ayrilik secimi = {sum(sinek_tercih)} elektirik secimi {100000 - sum(sinek_tercih)}")
print(sol_puan,sag_puan,sag_oran)