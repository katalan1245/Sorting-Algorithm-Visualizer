from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Algorithms import bubble_sort, quick_sort, merge_sort, bogo_sort, selection_sort, insertion_sort
import random
import time
import threading

root = Tk()
root.title('Sorting Algorithms Visualtization')
# root.maxsize(900, 600)
root.maxsize(1920, 1080)
root.config(bg='gray30')

# variables
alg = ''
data = []
rects = []
selected_visualize = IntVar(value=1)
draw_start = IntVar(value=1)
draw_end = IntVar(value=1)
start_time = None
end_time = None
count_switches = 0
count_checks = 0


# functions
def draw(data, colorArray, first=False, ending=False):
    canvas.delete('all')
    c_height = 800
    c_width = 1800
    x_width = c_width / (len(data) + 1)
    spacing = 10
    normalizedData = [i / (max(data)+0.00000001) for i in data]
    for i, height in enumerate(normalizedData):

        # top left
        x0 = i * x_width + spacing
        y0 = c_height - height * 800

        # bottom right
        x1 = (i + 1) * x_width + spacing
        y1 = c_height
        if first:
            rects[i] = canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        else:
            canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        if ending:
            root.update_idletasks()
            time.sleep(0.0000001)
    root.update_idletasks()

def Generate():
    global data

    minVal = int(minEntry.get())
    maxVal = int(maxEntry.get())

    if minVal > maxVal:
        messagebox.showerror(title='Illegal Values', message='Min Value Cannot Be Bigger Than Max Value!')
        return

    data = [i for i in range(minVal, maxVal + 1)]
    random.shuffle(data)

    if draw_start.get() == 1:
        draw(data, ['red' for x in range(len(data))])


def startAlogirthm():
    global data
    global alg
    global start_time
    global end_time
    global selected_visualize
    global count_checks
    global count_switches

    alg = str(algMenu.get())
    start_time = time.time()
    speed = speedScale.get()
    dEnd = draw_end.get()

    isDrawing = True if selected_visualize.get() == 1 else False

    if alg == 'Bubble Sort':
        count_checks, count_switches = bubble_sort(data, draw, speed, isDrawing)

    elif alg == 'Selection Sort':
        count_checks, count_switches = selection_sort(data, draw, speed, isDrawing)

    elif alg == 'Merge Sort':
        merge_sort(data, draw, speed, isDrawing)

    elif alg == 'Quick Sort':
        quick_sort(data, 0, len(data) - 1, draw, speed, isDrawing)

    elif alg == 'Bogo Sort':
        count_switches = bogo_sort(data, draw, speed, isDrawing)

    elif alg == 'Insertion Sort':
        count_checks = insertion_sort(data, draw, speed, isDrawing)

    if dEnd == 1:
        end_time = time.time()
        draw(data, ['green' for i in range(len(data))], ending=True)
    else:
        canvas.delete('all')


def clickStart():
    global alg
    global start_time
    global end_time
    global count_checks
    global count_switches

    if minEntry.get() == maxEntry.get() and maxEntry.get() == 0:
        messagebox.showerror(title='Empty Array', message='Array Cannot Be Empty')
        return

    startAlogirthm()
    currentT = end_time - start_time

    if alg == 'Bubble Sort':
        msg = f'Done Sorting- Bubble Sort!\nTime: {currentT} Seconds!\nChecks: {count_checks}\n Elements switched: {count_switches}'
    elif alg == 'Bogo Sort':
        msg = f'Done Sorting- Bogo Sort!\nTime: {currentT} Seconds!\n Shuffles: {count_switches}!'
    elif alg == 'Selection Sort':
        msg = f'Done Sorting- Selection Sort!\nTime: {currentT} Seconds!\nChecks: {count_checks}\n Elements switched: {count_switches}'
    elif alg == 'Insertion Sort':
        msg = f'Done Sorting- Insertion Sort!\nTime: {currentT} Seconds!\n Checks: {count_checks}!'
    else:
        msg = f'Done Sorting- {alg}!\nTime: {currentT} Seconds!'

    messagebox.showinfo(title='Result', message=msg)


# frame / base layout
UI_frame = Frame(root, width=520, height=200, bg='gray')
UI_frame.grid(row=0, column=0, padx=10, pady=5, sticky='NEW')

canvas = Canvas(root, width=1800, height=800, bg='white')
canvas.grid(row=1, column=0, padx=10, pady=5, sticky='SEW')

# UI Area
# Row[0]
Label(UI_frame, text='  Algorithm: ', font="Helvetica 14 bold", bg='gray').grid(row=0, column=0, padx=5, pady=5)
algMenu = ttk.Combobox(UI_frame, values=['Bubble Sort', 'Selection Sort', 'Insertion Sort', 'Merge Sort', 'Quick Sort',
                                         'Bogo Sort'])
algMenu.grid(row=0, column=1, padx=5, pady=5)
algMenu.current(0)

Button(UI_frame, text='Generate', width=10, command=Generate).grid(row=0, column=2, padx=5, pady=5)
Button(UI_frame, text='Sort!', width=20, height=3, command=clickStart).grid(row=1, column=5, padx=5, pady=5)

# Row[1]
minEntry = Scale(UI_frame, from_=1, to=250, resolution=1, orient=HORIZONTAL, length=200, label='Min Value')
minEntry.grid(row=1, column=0, padx=5, pady=5)

maxEntry = Scale(UI_frame, from_=1, to=250, resolution=1, orient=HORIZONTAL, length=200, label='Max Value')
maxEntry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

speedScale = Scale(UI_frame, from_=0.2, to=5, resolution=0.2, digits=2, orient=HORIZONTAL, label='Select Speed')
speedScale.set(1)
speedScale.grid(row=1, column=2, padx=5, pady=5)

# Row[2]
visualButton = Checkbutton(UI_frame, text='Visualize', variable=selected_visualize, bg='gray')
visualButton.grid(row=2, column=0, padx=5, pady=5)

enDrButton = Checkbutton(UI_frame, text='Draw Sorted', variable=draw_end, bg='gray')
enDrButton.grid(row=2, column=2, padx=5, pady=5)

stDrButton = Checkbutton(UI_frame, text='Draw Unsorted', variable=draw_start, bg='gray')
stDrButton.grid(row=2, column=1, padx=5, pady=5)

root.mainloop()
