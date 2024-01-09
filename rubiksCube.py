import maya.cmds as cmds
import random as r
import mtoa.utils as mutils

lock = False


################### Method Definitions ###################
def createShadingNode(nameOfNode, typeName, asShader, asTexture=False):
    cmds.shadingNode(typeName, asShader=asShader, asTexture=asTexture, n=nameOfNode)


def createAiStandardSurface(nameOfMat):
    createShadingNode(nameOfMat, "aiStandardSurface", True)
    # cmds.setAttr(f"{nameOfMat}.specular", 0)
    # cmds.shadingNode('aiStandardSurface', asShader = True, n = nameOfMat)


def assignMaterial(nameOfObject, nameOfMat):
    cmds.select(nameOfObject)
    cmds.hyperShade(assign=nameOfMat)


def createAndAssignAiStandardSurface(nameOfObject, nameOfMat):
    createAiStandardSurface(nameOfMat)
    assignMaterial(nameOfObject, nameOfMat)


def onRotate():
    global lock
    currentControl = cmds.ls(sl=True)[0]
    rotationAxis = rotationAxisDict[currentControl]
    currentRotation = round(cmds.getAttr(f"{currentControl}.r{rotationAxis}"))

    print("current rotation" + str(currentRotation))
    if currentRotation % 90 == 0:
        rotationChange = currentRotation - previousRotationDict[currentControl]
        previousRotationDict[currentControl] = currentRotation
        for control in controls:
            cmds.setAttr(f"{control}.r{rotationAxisDict[control]}", l=0)
        print(":)")
        left = set(controlDict[leftControl])
        right = set(controlDict[rightControl])
        top = set(controlDict[topControl])
        bottom = set(controlDict[bottomControl])
        front = set(controlDict[frontControl])
        back = set(controlDict[backControl])

        backAndLeft = back.intersection(left)
        backAndRight = back.intersection(right)
        backAndTop = back.intersection(top)
        backAndBottom = back.intersection(bottom)

        frontAndLeft = front.intersection(left)
        frontAndRight = front.intersection(right)
        frontAndTop = front.intersection(top)
        frontAndBottom = front.intersection(bottom)

        topAndLeft = top.intersection(left)
        topAndRight = top.intersection(right)

        bottomAndLeft = bottom.intersection(left)
        bottomAndRight = bottom.intersection(right)

        if rotationChange % 360 == 90:
            print("90")
            if currentControl == topControl:
                controlDict[leftControl] = list(left - topAndLeft | backAndTop)
                controlDict[frontControl] = list(front - frontAndTop | topAndLeft)
                controlDict[rightControl] = list(right - topAndRight | frontAndTop)
                controlDict[backControl] = list(back - backAndTop | topAndRight)
            if currentControl == bottomControl:
                controlDict[leftControl] = list(left - bottomAndLeft | backAndBottom)
                controlDict[frontControl] = list(front - frontAndBottom | bottomAndLeft)
                controlDict[rightControl] = list(
                    right - bottomAndRight | frontAndBottom
                )
                controlDict[backControl] = list(back - backAndBottom | bottomAndRight)
            if currentControl == frontControl:
                controlDict[leftControl] = list(left - frontAndLeft | frontAndTop)
                controlDict[topControl] = list(top - frontAndTop | frontAndRight)
                controlDict[rightControl] = list(right - frontAndRight | frontAndBottom)
                controlDict[bottomControl] = list(
                    bottom - frontAndBottom | frontAndLeft
                )
            if currentControl == backControl:
                controlDict[leftControl] = list(left - backAndLeft | backAndTop)
                controlDict[topControl] = list(top - backAndTop | backAndRight)
                controlDict[rightControl] = list(right - backAndRight | backAndBottom)
                controlDict[bottomControl] = list(bottom - backAndBottom | backAndLeft)
            if currentControl == leftControl:
                controlDict[frontControl] = list(front - frontAndLeft | topAndLeft)
                controlDict[topControl] = list(top - topAndLeft | backAndLeft)
                controlDict[backControl] = list(back - backAndLeft | bottomAndLeft)
                controlDict[bottomControl] = list(bottom - bottomAndLeft | frontAndLeft)
            if currentControl == rightControl:
                controlDict[frontControl] = list(front - frontAndRight | topAndRight)
                controlDict[topControl] = list(top - topAndRight | backAndRight)
                controlDict[backControl] = list(back - backAndRight | bottomAndRight)
                controlDict[bottomControl] = list(
                    bottom - bottomAndRight | frontAndRight
                )
        if rotationChange % 360 == 180:
            print("180")
            if currentControl == topControl:
                controlDict[leftControl] = list(left - topAndLeft | topAndRight)
                controlDict[frontControl] = list(front - frontAndTop | backAndTop)
                controlDict[rightControl] = list(right - topAndRight | topAndLeft)
                controlDict[backControl] = list(back - backAndTop | frontAndTop)
            if currentControl == bottomControl:
                controlDict[leftControl] = list(left - bottomAndLeft | bottomAndRight)
                controlDict[frontControl] = list(front - frontAndBottom | backAndBottom)
                controlDict[rightControl] = list(right - bottomAndRight | bottomAndLeft)
                controlDict[backControl] = list(back - backAndBottom | frontAndBottom)
            if currentControl == frontControl:
                controlDict[leftControl] = list(left - frontAndLeft | frontAndRight)
                controlDict[topControl] = list(top - frontAndTop | frontAndBottom)
                controlDict[rightControl] = list(right - frontAndRight | frontAndLeft)
                controlDict[bottomControl] = list(bottom - frontAndBottom | frontAndTop)
            if currentControl == backControl:
                controlDict[leftControl] = list(left - backAndLeft | backAndRight)
                controlDict[topControl] = list(top - backAndTop | backAndBottom)
                controlDict[rightControl] = list(right - backAndRight | backAndLeft)
                controlDict[bottomControl] = list(bottom - backAndBottom | backAndTop)
            if currentControl == leftControl:
                controlDict[frontControl] = list(front - frontAndLeft | backAndLeft)
                controlDict[topControl] = list(top - topAndLeft | bottomAndLeft)
                controlDict[backControl] = list(back - backAndLeft | frontAndLeft)
                controlDict[bottomControl] = list(bottom - bottomAndLeft | topAndLeft)
            if currentControl == rightControl:
                controlDict[frontControl] = list(front - frontAndRight | backAndRight)
                controlDict[topControl] = list(top - topAndRight | bottomAndRight)
                controlDict[backControl] = list(back - backAndRight | frontAndRight)
                controlDict[bottomControl] = list(bottom - bottomAndRight | topAndRight)
        if rotationChange % 360 == 270:
            print("270")
            if currentControl == topControl:
                controlDict[leftControl] = list(left - topAndLeft | frontAndTop)
                controlDict[frontControl] = list(front - frontAndTop | topAndRight)
                controlDict[rightControl] = list(right - topAndRight | backAndTop)
                controlDict[backControl] = list(back - backAndTop | topAndLeft)
            if currentControl == bottomControl:
                controlDict[leftControl] = list(left - bottomAndLeft | frontAndBottom)
                controlDict[frontControl] = list(
                    front - frontAndBottom | bottomAndRight
                )
                controlDict[rightControl] = list(right - bottomAndRight | backAndBottom)
                controlDict[backControl] = list(back - backAndBottom | bottomAndLeft)
            if currentControl == frontControl:
                controlDict[leftControl] = list(left - frontAndLeft | frontAndBottom)
                controlDict[topControl] = list(top - frontAndTop | frontAndLeft)
                controlDict[rightControl] = list(right - frontAndRight | frontAndTop)
                controlDict[bottomControl] = list(
                    bottom - frontAndBottom | frontAndRight
                )
            if currentControl == backControl:
                controlDict[leftControl] = list(left - backAndLeft | backAndBottom)
                controlDict[topControl] = list(top - backAndTop | backAndLeft)
                controlDict[rightControl] = list(right - backAndRight | backAndTop)
                controlDict[bottomControl] = list(bottom - backAndBottom | backAndRight)
            if currentControl == leftControl:
                controlDict[frontControl] = list(front - frontAndLeft | bottomAndLeft)
                controlDict[topControl] = list(top - topAndLeft | frontAndLeft)
                controlDict[backControl] = list(back - backAndLeft | topAndLeft)
                controlDict[bottomControl] = list(bottom - bottomAndLeft | backAndLeft)
            if currentControl == rightControl:
                controlDict[frontControl] = list(front - frontAndRight | bottomAndRight)
                controlDict[topControl] = list(top - topAndRight | frontAndRight)
                controlDict[backControl] = list(back - backAndRight | topAndRight)
                controlDict[bottomControl] = list(
                    bottom - bottomAndRight | backAndRight
                )
    else:
        for control in controls:
            if control != currentControl:
                cmds.setAttr(f"{control}.r{rotationAxisDict[control]}", l=1)
        print(":(")
    lock = False


def onSelect():
    global lock
    if len(cmds.ls(sl=True)) == 0:
        return
    if len(cmds.ls(sl=True)) > 1:
        cmds.select(clear=True)
    else:
        if not lock:
            selectedItem = cmds.ls(sl=True)[0]
            print(f"selected item is: {selectedItem}")
            if selectedItem in controls:
                for joint in joints:
                    parent = cmds.listRelatives(joint, p=True)
                    if parent:
                        cmds.parent(joint, w=True)
                for joint in controlDict[selectedItem]:
                    cmds.parent(joint, selectedItem)
                cmds.select(selectedItem)
                # lock = True


def makeHeart(name):
    circle1, _ = cmds.circle(sw=200, nr=(0, 1, 0))
    circle2, _ = cmds.circle(sw=200, nr=(0, 1, 0))
    cmds.rotate(0, 75, 0, circle2)
    cmds.move(1.3, 0, 1.187, circle2)
    circle3, _ = cmds.circle(sw=150, d=1, sections=1, nr=(0, 1, 0))
    cmds.rotate(0, -118, 0, circle3)
    cmds.move(0.87, 0, 0.35, circle3)
    cmds.scale(1.6, 1.6, 1.6, circle3)
    heart = cmds.attachCurve(circle1, circle2, circle3, ch=0, rpo=0, n=name)[0]
    cmds.delete(circle1, circle2, circle3)
    cmds.xform(heart, cpc=True)
    cmds.move(0, 0, 0, heart, rpr=True)
    cmds.scale(.5, .5, .5, heart)
    return heart


#################### End Method Definitions ###################
cmds.file(force=True, newFile=True)

################# create materials ###########################
color0 = "baseColor"
createAiStandardSurface(color0)
cmds.setAttr(f"{color0}.baseColor", 1, 1, 1)
cmds.setAttr(f"{color0}.emission", 0.5)

color1 = "color1"
createAiStandardSurface(color1)
cmds.setAttr(f"{color1}.baseColor", 1, 0.75, 1)

color2 = "color2"
createAiStandardSurface(color2)
cmds.setAttr(f"{color2}.baseColor", 0.75, 1, 1)

color3 = "color3"
createAiStandardSurface(color3)
cmds.setAttr(f"{color3}.baseColor", 0.75, 0.65, 1)

color4 = "color4"
createAiStandardSurface(color4)
cmds.setAttr(f"{color4}.baseColor", 0.7, 0.75, 1)

color5 = "color5"
createAiStandardSurface(color5)
cmds.setAttr(f"{color5}.baseColor", 1, 0.85, 0.5)

color6 = "color6"
createAiStandardSurface(color6)
cmds.setAttr(f"{color6}.baseColor", 0.9, 0.5, 0.5)
################################################################

curPane = cmds.getPanel(withFocus=True)
cmds.modelEditor(curPane, edit=True, grid=False)

# create skydome
skydome = mutils.createLocator("aiSkyDomeLight", asLight=True)
cmds.setAttr("aiSkyDomeLight1.aiExposure", -5)
cmds.setAttr("aiSkyDomeLight1.aiSamples", 3)
rampName = cmds.shadingNode("ramp", asTexture=True)
cmds.setAttr("ramp1.colorEntryList[0].position", 0.25)
cmds.setAttr("ramp1.colorEntryList[0].color", 0.75, 0.45, 0.8)
cmds.setAttr("ramp1.colorEntryList[1].position", 0.6)
cmds.setAttr("ramp1.colorEntryList[1].color", 0.325, 0.2, 0.4)
cmds.connectAttr(f"{rampName}.outColor", "aiSkyDomeLight1.color", force=True)

cmds.select(skydome)
layer1 = cmds.createDisplayLayer()
cmds.setAttr("{}.displayType".format(layer1), 2)

# model rubik's cube
front = {}
back = {}
left = {}
right = {}
top = {}
bottom = {}
cubes = []
# 0 = middle, 1 = edge, 2 = corner

for x in range(3):
    for y in range(3):
        for z in range(3):
            cube, _ = cmds.polyCube(n=f"cube.{x}_{y}_{z}")
            cmds.editDisplayLayerMembers(layer1, cube)
            cmds.move(x, y, z, cube)
            cmds.polyBevel3(cube, fraction=0.15, offsetAsFraction=True, chamfer=2)

            if x == 1 and y == 1 and z == 1:
                root = cube
            else:
                cubes.append(cube)

            # shade cube
            assignMaterial(cube, color0)
            if x == 0:
                assignMaterial(f"{cube}.f[17]", color3)

                if y == 1 and z == 1:
                    left[cube] = 0
                elif y == 1 or z == 1:
                    left[cube] = 1
                else:
                    left[cube] = 2

            if x == 2:
                assignMaterial(f"{cube}.f[16]", color4)

                if y == 1 and z == 1:
                    right[cube] = 0
                elif y == 1 or z == 1:
                    right[cube] = 1
                else:
                    right[cube] = 2

            if z == 0:
                assignMaterial(f"{cube}.f[14]", color6)

                if y == 1 and x == 1:
                    back[cube] = 0
                elif y == 1 or x == 1:
                    back[cube] = 1
                else:
                    back[cube] = 2

            if z == 2:
                assignMaterial(f"{cube}.f[12]", color1)

                if y == 1 and x == 1:
                    front[cube] = 0
                elif y == 1 or x == 1:
                    front[cube] = 1
                else:
                    front[cube] = 2

            if y == 0:
                assignMaterial(f"{cube}.f[15]", color5)

                if z == 1 and x == 1:
                    bottom[cube] = 0
                elif z == 1 or x == 1:
                    bottom[cube] = 1
                else:
                    bottom[cube] = 2
            if y == 2:
                assignMaterial(f"{cube}.f[13]", color2)

                if z == 1 and x == 1:
                    top[cube] = 0
                elif z == 1 or x == 1:
                    top[cube] = 1
                else:
                    top[cube] = 2

# rig cube
cmds.select(clear=True)
v = cmds.xform(f"{root}", q=True, ws=True, rp=True)
rootJoint = cmds.joint(p=(v[0], v[1], v[2]), rad=0.4, n=f"{root}_joint")
cmds.parentConstraint(rootJoint, root, mo=True)

joints = []
for cube in cubes:
    v = cmds.xform(f"{root}", q=True, ws=True, rp=True)
    cmds.move(v[0], v[1], v[2], f"{cube}.rotatePivot")

    cmds.select(rootJoint)
    v = cmds.xform(f"{cube}", q=True, ws=True, rp=True)
    joint = cmds.joint(p=(v[0], v[1], v[2]), rad=0.4, n=f"{cube}_joint")
    cmds.parentConstraint(joint, cube, mo=True)
    joints.append(joint)

rootControl, _ = cmds.circle(nr=(0, 1, 0), r=5, n="root_control")
cmds.move(1, 0, 1, rootControl)
cmds.parentConstraint(rootControl, rootJoint, mo=True)

controls = []
controlDict = {}
rotationAxisDict = {}
previousRotationDict = {}

# left control
# leftControl, _ = cmds.circle(nr=(2, 0, 0), r=2, n="left_control")
leftControl = makeHeart(name="left_control")
cmds.rotate(180, 45, -90)
cmds.makeIdentity(apply=True, t=True, r=True, s=True)
cmds.move(-2, 1, 1, leftControl)
leftJoints = []
for leftCube, _ in left.items():
    leftJointName = f"{leftCube}_joint"
    cmds.parent(leftJointName, leftControl)
    leftJoints.append(leftJointName)

controlDict[leftControl] = leftJoints
previousRotationDict[leftControl] = 0

cmds.parent(leftControl, rootControl)
controls.append(leftControl)

rotationAxisDict[leftControl] = "x"

cmds.setAttr(leftControl + ".ty", k=0, cb=1, l=1)
cmds.setAttr(leftControl + ".tz", k=0, cb=1, l=1)
cmds.setAttr(leftControl + ".tx", k=0, cb=1, l=1)
cmds.setAttr(leftControl + ".sy", k=0, cb=1, l=1)
cmds.setAttr(leftControl + ".sz", k=0, cb=1, l=1)
cmds.setAttr(leftControl + ".sx", k=0, cb=1, l=1)
cmds.setAttr(leftControl + ".v", k=0, cb=1, l=1)
cmds.setAttr(leftControl + ".ry", k=0, cb=1, l=1)
cmds.setAttr(leftControl + ".rz", k=0, cb=1, l=1)

cmds.setAttr(leftControl + ".overrideEnabled", 1)
cmds.setAttr(leftControl + ".overrideColor", 20)
cmds.setAttr(leftControl + ".lineWidth", 10)

# right control
# rightControl, _ = cmds.circle(nr=(2, 0, 0), r=2, n="right_control")
rightControl = makeHeart(name="right_control")
cmds.rotate(180, 45, -90)
cmds.makeIdentity(apply=True, t=True, r=True, s=True)
cmds.move(4, 1, 1, rightControl)
rightJoints = []
for rightCube, _ in right.items():
    rightJointName = f"{rightCube}_joint"
    cmds.parent(rightJointName, rightControl)
    rightJoints.append(rightJointName)

controlDict[rightControl] = rightJoints
previousRotationDict[rightControl] = 0

cmds.parent(rightControl, rootControl)
controls.append(rightControl)

rotationAxisDict[rightControl] = "x"

cmds.setAttr(rightControl + ".ty", k=0, cb=1, l=1)
cmds.setAttr(rightControl + ".tz", k=0, cb=1, l=1)
cmds.setAttr(rightControl + ".tx", k=0, cb=1, l=1)
cmds.setAttr(rightControl + ".sy", k=0, cb=1, l=1)
cmds.setAttr(rightControl + ".sz", k=0, cb=1, l=1)
cmds.setAttr(rightControl + ".sx", k=0, cb=1, l=1)
cmds.setAttr(rightControl + ".v", k=0, cb=1, l=1)
cmds.setAttr(rightControl + ".ry", k=0, cb=1, l=1)
cmds.setAttr(rightControl + ".rz", k=0, cb=1, l=1)

cmds.setAttr(rightControl + ".overrideEnabled", 1)
cmds.setAttr(rightControl + ".overrideColor", 20)
cmds.setAttr(rightControl + ".lineWidth", 10)

# top control
# topControl, _ = cmds.circle(nr=(0, 2, 0), r=2, n="top_control")
topControl = makeHeart(name="top_control")
cmds.rotate(180, 45, 0)
cmds.makeIdentity(apply=True, t=True, r=True, s=True)
cmds.move(1, 4, 1, topControl)
topJoints = []
for topCube, _ in top.items():
    topJointName = f"{topCube}_joint"
    cmds.parent(topJointName, topControl)
    topJoints.append(topJointName)

controlDict[topControl] = topJoints
previousRotationDict[topControl] = 0

cmds.parent(topControl, rootControl)
controls.append(topControl)

rotationAxisDict[topControl] = "y"

cmds.setAttr(topControl + ".ty", k=0, cb=1, l=1)
cmds.setAttr(topControl + ".tz", k=0, cb=1, l=1)
cmds.setAttr(topControl + ".tx", k=0, cb=1, l=1)
cmds.setAttr(topControl + ".sy", k=0, cb=1, l=1)
cmds.setAttr(topControl + ".sz", k=0, cb=1, l=1)
cmds.setAttr(topControl + ".sx", k=0, cb=1, l=1)
cmds.setAttr(topControl + ".v", k=0, cb=1, l=1)
cmds.setAttr(topControl + ".rx", k=0, cb=1, l=1)
cmds.setAttr(topControl + ".rz", k=0, cb=1, l=1)

cmds.setAttr(topControl + ".overrideEnabled", 1)
cmds.setAttr(topControl + ".overrideColor", 20)
cmds.setAttr(topControl + ".lineWidth", 10)

# bottom control
# bottomControl, _ = cmds.circle(nr=(0, 2, 0), r=2, n="bottom_control")
bottomControl = makeHeart(name="bottom_control")
cmds.rotate(180, 45, 0)
cmds.makeIdentity(apply=True, t=True, r=True, s=True)
cmds.move(1, -2, 1, bottomControl)
bottomJoints = []
for bottomCube, _ in bottom.items():
    bottomJointName = f"{bottomCube}_joint"
    cmds.parent(bottomJointName, bottomControl)
    bottomJoints.append(bottomJointName)

controlDict[bottomControl] = bottomJoints
previousRotationDict[bottomControl] = 0

cmds.parent(bottomControl, rootControl)
controls.append(bottomControl)

rotationAxisDict[bottomControl] = "y"

cmds.setAttr(bottomControl + ".ty", k=0, cb=1, l=1)
cmds.setAttr(bottomControl + ".tz", k=0, cb=1, l=1)
cmds.setAttr(bottomControl + ".tx", k=0, cb=1, l=1)
cmds.setAttr(bottomControl + ".sy", k=0, cb=1, l=1)
cmds.setAttr(bottomControl + ".sz", k=0, cb=1, l=1)
cmds.setAttr(bottomControl + ".sx", k=0, cb=1, l=1)
cmds.setAttr(bottomControl + ".v", k=0, cb=1, l=1)
cmds.setAttr(bottomControl + ".rz", k=0, cb=1, l=1)
cmds.setAttr(bottomControl + ".rx", k=0, cb=1, l=1)

cmds.setAttr(bottomControl + ".overrideEnabled", 1)
cmds.setAttr(bottomControl + ".overrideColor", 20)
cmds.setAttr(bottomControl + ".lineWidth", 10)

# front control
# frontControl, _ = cmds.circle(nr=(0, 0, 2), r=2, n="front_control")
frontControl = makeHeart(name="front_control")
cmds.rotate(270, 0, -45)
cmds.makeIdentity(apply=True, t=True, r=True, s=True)
cmds.move(1, 1, 4, frontControl)
frontJoints = []
for frontCube, _ in front.items():
    frontJointName = f"{frontCube}_joint"
    cmds.parent(frontJointName, frontControl)
    frontJoints.append(frontJointName)

controlDict[frontControl] = frontJoints
previousRotationDict[frontControl] = 0

cmds.parent(frontControl, rootControl)
controls.append(frontControl)

rotationAxisDict[frontControl] = "z"

cmds.setAttr(frontControl + ".ty", k=0, cb=1, l=1)
cmds.setAttr(frontControl + ".tz", k=0, cb=1, l=1)
cmds.setAttr(frontControl + ".tx", k=0, cb=1, l=1)
cmds.setAttr(frontControl + ".sy", k=0, cb=1, l=1)
cmds.setAttr(frontControl + ".sz", k=0, cb=1, l=1)
cmds.setAttr(frontControl + ".sx", k=0, cb=1, l=1)
cmds.setAttr(frontControl + ".v", k=0, cb=1, l=1)
cmds.setAttr(frontControl + ".ry", k=0, cb=1, l=1)
cmds.setAttr(frontControl + ".rx", k=0, cb=1, l=1)

cmds.setAttr(frontControl + ".overrideEnabled", 1)
cmds.setAttr(frontControl + ".overrideColor", 20)
cmds.setAttr(frontControl + ".lineWidth", 10)

# back control
# backControl, _ = cmds.circle(nr=(0, 0, 2), r=2, n="back_control")
backControl = makeHeart(name="back_control")
cmds.rotate(270, 0, -45)
cmds.makeIdentity(apply=True, t=True, r=True, s=True)
cmds.move(1, 1, 4, frontControl)
cmds.move(1, 1, -2, backControl)
backJoints = []
for backCube, _ in back.items():
    backJointName = f"{backCube}_joint"
    cmds.parent(backJointName, backControl)
    backJoints.append(backJointName)

controlDict[backControl] = backJoints
previousRotationDict[backControl] = 0

cmds.parent(backControl, rootControl)
controls.append(backControl)

rotationAxisDict[backControl] = "z"

cmds.setAttr(backControl + ".ty", k=0, cb=1, l=1)
cmds.setAttr(backControl + ".tz", k=0, cb=1, l=1)
cmds.setAttr(backControl + ".tx", k=0, cb=1, l=1)
cmds.setAttr(backControl + ".sy", k=0, cb=1, l=1)
cmds.setAttr(backControl + ".sz", k=0, cb=1, l=1)
cmds.setAttr(backControl + ".sx", k=0, cb=1, l=1)
cmds.setAttr(backControl + ".v", k=0, cb=1, l=1)
cmds.setAttr(backControl + ".ry", k=0, cb=1, l=1)
cmds.setAttr(backControl + ".rx", k=0, cb=1, l=1)

cmds.setAttr(backControl + ".overrideEnabled", 1)
cmds.setAttr(backControl + ".overrideColor", 20)
cmds.setAttr(backControl + ".lineWidth", 10)

jobs = []
jobNum = cmds.scriptJob(e=["SelectionChanged", onSelect], protected=True, kws=True)
jobs.append(jobNum)

jobNum = cmds.scriptJob(attributeChange=[f"{leftControl}.r", onRotate], kws=True)
jobs.append(jobNum)
jobNum = cmds.scriptJob(attributeChange=[f"{rightControl}.r", onRotate], kws=True)
jobs.append(jobNum)
jobNum = cmds.scriptJob(attributeChange=[f"{topControl}.r", onRotate], kws=True)
jobs.append(jobNum)
jobNum = cmds.scriptJob(attributeChange=[f"{bottomControl}.r", onRotate], kws=True)
jobs.append(jobNum)
jobNum = cmds.scriptJob(attributeChange=[f"{frontControl}.r", onRotate], kws=True)
jobs.append(jobNum)
jobNum = cmds.scriptJob(attributeChange=[f"{backControl}.r", onRotate], kws=True)
jobs.append(jobNum)

cmds.select(clear=True)
