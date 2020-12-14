import time
import random

'''
    Some Algorithms for the visualizer:
    Bubble Sort
    Merge Sort
    Quick Sort
    Bogo Sort
    Selection Sort
    Insertion Sort
'''


# Bubble Sort-
def bubble_sort(data, draw, timeTick, isDrawing):
    cntChecks = 0
    cntSwitches = 0
    for i in range(len(data) - 1):
        tempCnt = 0
        for j in range(len(data) - 1):
            if j > len(data) - i - 1:
                continue
            cntChecks += 1
            if data[j] > data[j + 1]:
                tempCnt += 1
                data[j], data[j + 1] = data[j + 1], data[j]
                cntSwitches += 1
                if timeTick != 5.0:
                    if timeTick < 1.0:
                        time.sleep(timeTick * 5)
                    else:
                        time.sleep(0.01 / 10 ** timeTick)
                if isDrawing:
                    draw(data, ['green' if x == j or x == j + 1 else 'white' if x >= len(data) - i else 'red' for x in range(len(data))])
        if tempCnt == 0:
            return cntChecks, cntSwitches
    return cntChecks, cntSwitches


# Merge Sort-
def merge_sort(data, draw, timeTick, isDrawing):
    merge_sort_alg(data, 0, len(data) - 1, draw, timeTick, isDrawing)


def merge_sort_alg(data, left, right, draw, timeTick, isDrawing):
    if left < right:
        mid = (left + right) // 2
        merge_sort_alg(data, left, mid, draw, timeTick, isDrawing)
        merge_sort_alg(data, mid + 1, right, draw, timeTick, isDrawing)
        merge(data, left, mid, right, draw, timeTick, isDrawing)


def merge(data, left, mid, right, draw, timeTick, isDrawing):
    if isDrawing: draw(data, getColorArrayMerge(len(data), left, mid, right))
    if timeTick != 5.0:
        if timeTick < 1.0:
            time.sleep(timeTick * 5)
        else:
            time.sleep(0.01 / 10 ** timeTick)

    leftPart = data[left:mid + 1]
    rightPart = data[mid + 1:right + 1]

    leftInd = rightInd = 0

    for dataInd in range(left, right + 1):
        if leftInd < len(leftPart) and rightInd < len(rightPart):
            if leftPart[leftInd] <= rightPart[rightInd]:
                data[dataInd] = leftPart[leftInd]
                leftInd += 1
            else:
                data[dataInd] = rightPart[rightInd]
                rightInd += 1
        elif leftInd < len(leftPart):
            data[dataInd] = leftPart[leftInd]
            leftInd += 1
        else:
            data[dataInd] = rightPart[rightInd]
            rightInd += 1

    if isDrawing: draw(data, ['green' if x >= left and x <= right else 'white' for x in range(len(data))])
    if timeTick != 5.0:
        if timeTick < 1.0:
            time.sleep(1.0 / float(timeTick))
        else:
            time.sleep(0.01 / 10 ** timeTick)


def getColorArrayMerge(length, left, mid, right):
    colorArray = []

    for i in range(length):
        if i >= left and i <= right:
            if i >= left and i <= mid:
                colorArray.append('yellow')
            else:
                colorArray.append('pink')
        else:
            colorArray.append('white')

    return colorArray


# Quick Sort-
def partition(data, head, tail, draw, timeTick, isDrawing):
    border = (head - 1)
    pivot = data[tail]

    if isDrawing: draw(data, getColorArrayQuick(len(data), head, tail, border, border))
    if timeTick != 5.0:
        if timeTick < 1.0:
            time.sleep(1.0 / float(timeTick))
        else:
            time.sleep(0.01 / 10 ** timeTick)

    for j in range(head, tail):
        if data[j] < pivot:

            if isDrawing: draw(data, getColorArrayQuick(len(data), head, tail, border, j))
            if timeTick != 5:
                if timeTick < 1:
                    time.sleep(1.0 / float(timeTick))
                else:
                    time.sleep(0.01 / 10 ** timeTick)

            border += 1
            data[border], data[j] = data[j], data[border]

    # swap pivot with border value
    if isDrawing: draw(data, getColorArrayQuick(len(data), head, tail, border, j, True))
    if timeTick != 5.0:
        if timeTick < 1:
            time.sleep(1.0 / float(timeTick))
        else:
            time.sleep(0.01 / 10 ** timeTick)

    data[border + 1], data[tail] = data[tail], data[border + 1]

    return (border + 1)


def quick_sort(data, head, tail, draw, timeTick, isDrawing):
    if head < tail:
        pi = partition(data, head, tail, draw, timeTick, isDrawing)

        # sort the left and right partitions
        quick_sort(data, head, pi - 1, draw, timeTick, isDrawing)
        quick_sort(data, pi + 1, tail, draw, timeTick, isDrawing)


def getColorArrayQuick(dataLen, head, tail, border, currentInd, isSwaping=False):
    colorArray = []
    for i in range(dataLen):
        # base color
        if i > head and i <= tail:
            colorArray.append('dim gray')
        else:
            colorArray.append('white')

        if i == tail:
            colorArray[i] = 'blue'
        elif i == border:
            colorArray[i] = 'red'
        elif i == currentInd:
            colorArray[i] = 'yellow'

        if isSwaping:
            if i == border or i == currentInd:
                colorArray[i] = 'green'

    return colorArray


# bogo sort
def bogo_sort(data, draw, timeTick, isDrawing):
    cnt = 0
    while not is_sorted(data):
        shuffle(data, draw, isDrawing)
        cnt += 1
        if timeTick != 5:
            if timeTick < 1:
                time.sleep(1.0 / float(timeTick))
            else:
                time.sleep(0.01 / 10 ** timeTick)
        print('Shuffles: ' + str(cnt))

    return cnt


def is_sorted(data):
    n = len(data)
    for i in range(n - 1):
        if data[i] > data[i + 1]:
            return False
    return True


def shuffle(data, draw, isDrawing):
    n = len(data)
    for i in range(0, n):
        r = random.randint(0, n - 1)
        data[i], data[r] = data[r], data[i]
        if isDrawing: draw(data, ['red' if x == r or x == i else 'white' for x in range(n)])


# selection sort

def selection_sort(data, draw, timeTick, isDrawing):
    cnt_checks = 0
    cnt_switches = 0

    for i in range(len(data)):
        min_ind = i
        for j in range(i + 1, len(data)):
            cnt_checks += 1

            if data[min_ind] > data[j]:
                min_ind = j
                cnt_switches += 1
                if isDrawing:
                    draw(data, ['green' if x == j or x == min_ind or x < i else 'red' for x in range(len(data))])
                if timeTick != 5:
                    if timeTick < 1:
                        time.sleep(1.0 / float(timeTick))
                    else:
                        time.sleep(0.01 / 10 ** timeTick)

        data[i], data[min_ind] = data[min_ind], data[i]

    return cnt_checks, cnt_switches


# insertion sort
def insertion_sort(data, draw, timeTick, isDrawing):
    cnt = 0
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        while j >= 0 and key < data[j]:

            data[j + 1] = data[j]
            j -= 1

            if isDrawing: draw(data, ['green' if x == j or x == j + 1 else 'red' for x in range(len(data))])
            if timeTick != 5.0:
                if timeTick < 1:
                    time.sleep(1.0 / float(timeTick))
                else:
                    time.sleep(0.01 / 10 ** timeTick)
            cnt += 1

        data[j + 1] = key

    return cnt
