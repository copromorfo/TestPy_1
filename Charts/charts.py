import matplotlib.pyplot as plt
import emoji as emo

def generatePieChart():
    print("ejecutando Pie Charts")
    labels=["A","B","C"]
    values=[200,34,120]

    fig, ax=plt.subplots()
    ax.pie(values,labels=labels)
    plt.savefig('Charts/pie.png')
    plt.close()
    print(emo.emojize('liz taylor :sign_of_the_horns:'))

