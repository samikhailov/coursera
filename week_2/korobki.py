box1 = [int(input()), int(input()), int(input())]
box2 = [int(input()), int(input()), int(input())]
box1.sort()
box2.sort()

if box1[0] == box2[0] and box1[1] == box2[1] and box1[2] == box2[2]:
    print("Boxes are equal")
elif box1[0] >= box2[0] and box1[1] >= box2[1] and box1[2] >= box2[2]:
    print('The first box is larger than the second one')
elif box1[0] <= box2[0] and box1[1] <= box2[1] and box1[2] <= box2[2]:
    print('The first box is smaller than the second one')
else:
    print("Boxes are incomparable")
