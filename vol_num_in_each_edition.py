# How many volumes in each edition?
# including index volume, not including reprint versions and supplements

ed1 = df_inventory[0:3]
ed2 = df_inventory[6:16]
ed3 = df_inventory[16:34]
ed4 = df_inventory[56:96]
ed5 = df_inventory[96:116]
ed6 = df_inventory[116:136]
ed7 = df_inventory[151:173]
ed8 = df_inventory[173:195]

list = []
list = [ed1.shape[0],ed2.shape[0],ed3.shape[0],ed4.shape[0],ed5.shape[0],ed6.shape[0],ed7.shape[0],ed8.shape[0]]

data = {'edition':[1,2,3,4,5,6,7,8],'vol_num':list}
df_edvol = df_edvol = pd.DataFrame(data)
df_edvol