'''
Premise:
'''

def getTallestBoxes(boxes, res=[]):

    if len(boxes) == 0: return res

    i = 0
    maxRes = res
    while i < len(boxes):
        box = boxes[i]

        if canFitOnTop(res, box):
            del boxes[i]
            tmpRes = getTallestBoxes(boxes, res + [box])

            if getBoxesHeight(tmpRes) > getBoxesHeight(maxRes):
                maxRes = tmpRes

            boxes.insert(i, box)

        i += 1

    return maxRes


def canFitOnTop(boxes, box):
    if len(boxes) == 0:
        return True

    top_box = boxes[len(boxes)-1]
    if top_box[0] < box[0] and top_box[1] < box[1]:
        return True
    return False

def getBoxesHeight(boxes):
    res = 0
    for box in boxes:
        res += box[1]
    return res

boxes = [(10, 10), (5, 1), (4, 4), (5, 5), (10, 5), (8, 9), (1, 9)]
print getTallestBoxes(boxes, [])
