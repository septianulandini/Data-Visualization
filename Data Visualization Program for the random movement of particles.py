#Data Visualization Program for the random movement of particles
#Studi Mandiri I FI6091
#Septian Ulan Dini
#Supervised by Dr.rer.nat. Sparisoma Viridi, M.Si.

# %%
#Data Collection
import os 

fileName = input("Input file's name") 

while not os.path.isfile(fileName):

    fileName = input("Whoops! File doesn't exist")
# %%
#Data Preprocessing
def read_file(file):

    x = open(file, 'r', encoding = 'utf-8')

    y = x.read()

    content = y.splitlines()

    return content

file = read_file(fileName)
# %%

for i in range (10):

    print(i, '\t', file[i])
#%%
#Data Selection 
#Total Tabel

def total_Table(masterList, totalCell):

  length_List = len(masterList)

  length_Table = totalCell + 4

  total = length_List / length_Table
  return total


#Time

def get_Time(masterList, totalCell, tableNumber):

  max_table = total_Table(masterList, totalCell)

  if max_table-1 < tableNumber:

    print('whoops! data exceded! maximum data is', max_table-1)

  else:

    row_Number = (tableNumber*(totalCell+4)+1)     

    time = masterList[row_Number].split()

    return float(time[2])


#Particles

def get_Data(masterList, totalCell, tableNumber):

  max_table = total_Table(masterList, totalCell)

  if max_table-1 < tableNumber:

    print('whoops! data exceded! maximum data is', max_table-1)

  else:

    list_Data = []

    for i in range(totalCell):

      row_Number = (tableNumber*(totalCell+4)+3+i)

      data_Temp = masterList[row_Number].split('\t')

      for j in range(7):

        data_Temp[j] = float(data_Temp[j])

      list_Data.append(data_Temp)

    return list_Data

# %%
#Data Transformation

totalCell = input("masukkan  jumlah butiran")
nomorTabel = input("masukkan nomor tabel")
sample_Data = get_Data(file, int(totalCell), int(nomorTabel))
x = []
y = []
label = []
color = []

for i in range(int(totalCell)):
  x.append(sample_Data[i][1])
  y.append(sample_Data[i][2])
  label.append(sample_Data[i][7])
  color.append(sample_Data[i][8])
  
print(x, y, label, color)

#%%
#Analyzed Data (Visualization result)

T = get_Time(file, int(totalCell), int(nomorTabel))
plt.style.use('ggplot')
fig, ax = plt.subplots(figsize=(6, 6))
ax.scatter(x, y, s=1200, alpha=0.6, c= color, edgecolor='black', linewidth=1)
plt.title('Konfigurasi Butiran')
plt.xlabel('x')
plt.ylabel('y')
plt.text(200,300,'Time')
plt.text(200, 295, T)
plt.xlim(200, 300)
plt.ylim(200, 300)

for i, txt in enumerate(label):
    ax.annotate(txt, (x[i], y[i]))
plt.show()
fig.savefig(input("masukkan nama file.png"))
