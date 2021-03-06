from matplotlib import pyplot as plt

# recommended color for different digits
color_mapping = {0:'red',1:'green',2:'blue',3:'yellow',4:'magenta',5:'orangered',
                6:'cyan',7:'purple',8:'gold',9:'pink'}

def plot2d(data,label,split='train'):
    # 2d scatter plot of the hidden features
    color_keys = color_mapping.keys() #0-9
    
    fig = plt.figure()
    for c in color_keys: 
        for m in range(len(label)):
                if label[m] == c:
                    plt.plot(data[m,0], data[m,1],'o', color=color_mapping[c], alpha=0.4)      
        plt.plot(data[c], data[c],'o', color=color_mapping[c], label="Class "+str(c), alpha=0.6)
    
    fig.set_size_inches(7, 7)
    plt.title(f'2D Plot - Intermediate Features at the hidden layers -{split}')        
    plt.legend(bbox_to_anchor=(0.8, 0.8))
    plt.savefig(f'2D Plot - Intermediate Features at the hidden layers -{split}.png')
    print("Plot Created!")
    pass

def plot3d(data,label,split='train'):
    # 3d scatter plot of the hidden features
    color_keys = color_mapping.keys() #0-9

    fig = plt.figure()  
    ax = fig.add_subplot(projection='3d')
    
    for c in color_keys: 
        for m in range(len(label)):
            if label[m] == c:
                ax.scatter(data[m,0], data[m,1], data[m,2], 'o', color=color_mapping[c], alpha=0.4)
        ax.scatter(data[c], data[c], data[c],'o', color=color_mapping[c], label="Class "+str(c), alpha=0.6)
    fig.set_size_inches(7, 7)
    ax.legend(bbox_to_anchor=(0.8, 0.8))
    ax.set_title(f'3D Plot - Intermediate Features at the hidden layers -{split}')
    plt.savefig(f'3D Plot - Intermediate Features at the hidden layers -{split}.png')
    print("Plot Created!")
    pass
