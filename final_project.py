#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.5),
    on November 14, 2020, at 15:52
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard




anchor_dict = dict([(2,0.052),(5,0.175),(8,0.33)])

popstars = [
    "pop_1.png",
    "pop_2.png",
    "pop_3.png",
    "pop_4.png",
    "pop_5.png",
    "pop_6.png",
]

politicians = [
    "pol_1.png",
    "pol_2.png",
    "pol_3.png",
    "pol_4.png",
    "pol_5.png",
    "pol_6.png",

]

stock = [
"stock_1.png",
"stock_2.png",
"stock_3.png",
"stock_4.png",
"stock_5.png",
"stock_6.png",
"stock_7.png"
]


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.5'
expName = 'flow'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sort_keys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Samuel\\OneDrive\\Documents\\GitHub\\psyc160_final_project\\final_project_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1280, 800], fullscr=True, screen=0,
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
instrResp = keyboard.Keyboard()
instrText = visual.TextStim(win=win, name='instrText',
    text='On each trial, you will see a set of faces in the middle of the screen.\nOne (1) of these faces will either be a POLITICIAN or a POP STAR.\n\nIf the face is a POLITICIAN, press the F key.\nIf the face is a POP STAR, press the K key.\n\nYou will see another face to the side of the main set.\nPlease IGNORE this face as best as you can.\n\nAt all times, please:\n- Keep your eyes fixed on the cross (+) at the center of the screen.\n- Respond as quickly and accurately as you can.\n\n\nPress the SPACE key to begin the experiment.',
    font='Arial',
    pos=(0, 0), height=0.034, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
fixationResp = visual.TextStim(win=win, name='fixationResp',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "flanker"
flankerClock = core.Clock()
image1 = visual.ImageStim(
    win=win,
    name='image1',
    image=None, mask=None,
    ori=0, pos=(0, 0.4), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
image2 = visual.ImageStim(
    win=win,
    name='image2',
    image=None, mask=None,
    ori=0, pos=(0, 0), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
image3 = visual.ImageStim(
    win=win,
    name='image3',
    image=None, mask=None,
    ori=0, pos=(0, 0), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
image4 = visual.ImageStim(
    win=win,
    name='image4',
    image=None, mask=None,
    ori=0, pos=(0, 0), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
image5 = visual.ImageStim(
    win=win,
    name='image5',
    image=None, mask=None,
    ori=0, pos=(0, 0), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
image6 = visual.ImageStim(
    win=win,
    name='image6',
    image=None, mask=None,
    ori=0, pos=(0, 0), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
image7 = visual.ImageStim(
    win=win,
    name='image7',
    image=None, mask=None,
    ori=0, pos=(0, 0), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
image8 = visual.ImageStim(
    win=win,
    name='image8',
    image=None, mask=None,
    ori=0, pos=(0, 0), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
distract_img = visual.ImageStim(
    win=win,
    name='distract_img',
    image='images/pop_1.png', mask=None,
    ori=0, pos=(0.3, 0), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
key_resp = keyboard.Keyboard()
text = visual.TextStim(win=win, name='text',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=-10.0);

# Initialize components for Routine "breakScr"
breakScrClock = core.Clock()
breakText = visual.TextStim(win=win, name='breakText',
    text='Press the SPACE key to continue.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);
breakResp = keyboard.Keyboard()

# Initialize components for Routine "goodbye"
goodbyeClock = core.Clock()
byeText = visual.TextStim(win=win, name='byeText',
    text='The experiment is now complete.\n\nThank you, and goodbye!',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instructions"-------
continueRoutine = True
# update component parameters for each repeat
instrResp.keys = []
instrResp.rt = []
_instrResp_allKeys = []
# keep track of which components have finished
instructionsComponents = [instrResp, instrText]
for thisComponent in instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions"-------
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *instrResp* updates
    waitOnFlip = False
    if instrResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instrResp.frameNStart = frameN  # exact frame index
        instrResp.tStart = t  # local t and not account for scr refresh
        instrResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instrResp, 'tStartRefresh')  # time at next scr refresh
        instrResp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instrResp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instrResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instrResp.status == STARTED and not waitOnFlip:
        theseKeys = instrResp.getKeys(keyList=['space'], waitRelease=False)
        _instrResp_allKeys.extend(theseKeys)
        if len(_instrResp_allKeys):
            instrResp.keys = _instrResp_allKeys[-1].name  # just the last key pressed
            instrResp.rt = _instrResp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False

    # *instrText* updates
    if instrText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instrText.frameNStart = frameN  # exact frame index
        instrText.tStart = t  # local t and not account for scr refresh
        instrText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instrText, 'tStartRefresh')  # time at next scr refresh
        instrText.setAutoDraw(True)

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if instrResp.keys in ['', [], None]:  # No response was made
    instrResp.keys = None
thisExp.addData('instrResp.keys',instrResp.keys)
if instrResp.keys != None:  # we had a response
    thisExp.addData('instrResp.rt', instrResp.rt)
thisExp.addData('instrResp.started', instrResp.tStartRefresh)
thisExp.addData('instrResp.stopped', instrResp.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('instrText.started', instrText.tStartRefresh)
thisExp.addData('instrText.stopped', instrText.tStopRefresh)
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
blocks = data.TrialHandler(nReps=1, method='sequential',
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('blocks.xlsx'),
    seed=None, name='blocks')
thisExp.addLoop(blocks)  # add the loop to the experiment
thisBlock = blocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock:
        exec('{} = thisBlock[paramName]'.format(paramName))

for thisBlock in blocks:
    currentLoop = blocks
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))

    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=2, method='random',
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('trial.xlsx'),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))

    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))

        # ------Prepare to start Routine "fixation"-------
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        # keep track of which components have finished
        fixationComponents = [fixationResp]
        for thisComponent in fixationComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        fixationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1

        # -------Run Routine "fixation"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = fixationClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=fixationClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame

            # *fixationResp* updates
            if fixationResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixationResp.frameNStart = frameN  # exact frame index
                fixationResp.tStart = t  # local t and not account for scr refresh
                fixationResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixationResp, 'tStartRefresh')  # time at next scr refresh
                fixationResp.setAutoDraw(True)
            if fixationResp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixationResp.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fixationResp.tStop = t  # not accounting for scr refresh
                    fixationResp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fixationResp, 'tStopRefresh')  # time at next scr refresh
                    fixationResp.setAutoDraw(False)

            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()

            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        # -------Ending Routine "fixation"-------
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('fixationResp.started', fixationResp.tStartRefresh)
        trials.addData('fixationResp.stopped', fixationResp.tStopRefresh)

        # ------Prepare to start Routine "flanker"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        target = randint(low = 0, high = load)
        png = ""
        stockSet = set()
        images = [
        image1,
        image2,
        image3,
        image4,
        image5,
        image6,
        image7,
        image8
        ]

        # if it is a popstar
        if (identity == "pop"):
            index = randint(low = 0, high = len(popstars) )
            png = popstars[index]

        # if it is a politician
        else:
            index = randint(low = 0, high = len(politicians) )
            png = politicians[index]

        def pos (index):
            return index * 0.1


        def setImage (file):
            return "images/" + file

        anchor = anchor_dict[load]


        #loops through load from 0, 1 ... load
        for i in range(load):
            cImage = images[i]
            cImage.pos = (0, anchor - pos(i))


            if i == target:
                cImage.image = setImage(png)
            else:
                index = randint(low = 0, high = len(stock))
                while stock[index] in stockSet:
                    index = randint(low = 0, high = len(stock))

                stockSet.add(stock[index])
                cImage.image = setImage(stock[index])


        if distractor == "inv":
            distract_img.ori = 180

        def setDist (l):
            index = randint(low = 0, high = len(l))

            while l[index] == png:
                index = randint(low = 0, high = len(l))
            distract_img.image = setImage(l[index])

        if congruency == "congruent":
            if identity == "pop":
                setDist(popstars)
            else:
                setDist(politicians)


        else:
            if identity == "pop":
                setDist(politicians)
            else:
                setDist(popstars)


        direction = randint(low = 0, high = 2)

        if direction == 0:
            distract_img.pos = (-0.3,0)
        else:
            distract_img.pos = (0.3,0)

         #Testing
        text.text = load

        # keep track of which components have finished
        flankerComponents = [image1, image2, image3, image4, image5, image6, image7, image8, distract_img, key_resp, text]
        for thisComponent in flankerComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        flankerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1

        # -------Run Routine "flanker"-------
        while continueRoutine:
            # get current time
            t = flankerClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=flankerClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame

            # *image1* updates
            if image1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image1.frameNStart = frameN  # exact frame index
                image1.tStart = t  # local t and not account for scr refresh
                image1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image1, 'tStartRefresh')  # time at next scr refresh
                image1.setAutoDraw(True)

            # *image2* updates
            if image2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image2.frameNStart = frameN  # exact frame index
                image2.tStart = t  # local t and not account for scr refresh
                image2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image2, 'tStartRefresh')  # time at next scr refresh
                image2.setAutoDraw(True)

            # *image3* updates
            if image3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image3.frameNStart = frameN  # exact frame index
                image3.tStart = t  # local t and not account for scr refresh
                image3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image3, 'tStartRefresh')  # time at next scr refresh
                image3.setAutoDraw(True)

            # *image4* updates
            if image4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image4.frameNStart = frameN  # exact frame index
                image4.tStart = t  # local t and not account for scr refresh
                image4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image4, 'tStartRefresh')  # time at next scr refresh
                image4.setAutoDraw(True)

            # *image5* updates
            if image5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image5.frameNStart = frameN  # exact frame index
                image5.tStart = t  # local t and not account for scr refresh
                image5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image5, 'tStartRefresh')  # time at next scr refresh
                image5.setAutoDraw(True)

            # *image6* updates
            if image6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image6.frameNStart = frameN  # exact frame index
                image6.tStart = t  # local t and not account for scr refresh
                image6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image6, 'tStartRefresh')  # time at next scr refresh
                image6.setAutoDraw(True)

            # *image7* updates
            if image7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image7.frameNStart = frameN  # exact frame index
                image7.tStart = t  # local t and not account for scr refresh
                image7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image7, 'tStartRefresh')  # time at next scr refresh
                image7.setAutoDraw(True)

            # *image8* updates
            if image8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image8.frameNStart = frameN  # exact frame index
                image8.tStart = t  # local t and not account for scr refresh
                image8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image8, 'tStartRefresh')  # time at next scr refresh
                image8.setAutoDraw(True)

            # *distract_img* updates
            if distract_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                distract_img.frameNStart = frameN  # exact frame index
                distract_img.tStart = t  # local t and not account for scr refresh
                distract_img.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(distract_img, 'tStartRefresh')  # time at next scr refresh
                distract_img.setAutoDraw(True)

            # *key_resp* updates
            waitOnFlip = False
            if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['f', 'k'], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
                    # was this correct?
                    if (key_resp.keys == str(correct)) or (key_resp.keys == correct):
                        key_resp.corr = 1
                    else:
                        key_resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False

            # *text* updates
            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                text.setAutoDraw(True)

            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()

            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in flankerComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        # -------Ending Routine "flanker"-------
        for thisComponent in flankerComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('image1.started', image1.tStartRefresh)
        trials.addData('image1.stopped', image1.tStopRefresh)
        trials.addData('image2.started', image2.tStartRefresh)
        trials.addData('image2.stopped', image2.tStopRefresh)
        trials.addData('image3.started', image3.tStartRefresh)
        trials.addData('image3.stopped', image3.tStopRefresh)
        trials.addData('image4.started', image4.tStartRefresh)
        trials.addData('image4.stopped', image4.tStopRefresh)
        trials.addData('image5.started', image5.tStartRefresh)
        trials.addData('image5.stopped', image5.tStopRefresh)
        trials.addData('image6.started', image6.tStartRefresh)
        trials.addData('image6.stopped', image6.tStopRefresh)
        trials.addData('image7.started', image7.tStartRefresh)
        trials.addData('image7.stopped', image7.tStopRefresh)
        trials.addData('image8.started', image8.tStartRefresh)
        trials.addData('image8.stopped', image8.tStopRefresh)
        trials.addData('distract_img.started', distract_img.tStartRefresh)
        trials.addData('distract_img.stopped', distract_img.tStopRefresh)
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
            # was no response the correct answer?!
            if str(correct).lower() == 'none':
               key_resp.corr = 1;  # correct non-response
            else:
               key_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for trials (TrialHandler)
        trials.addData('key_resp.keys',key_resp.keys)
        trials.addData('key_resp.corr', key_resp.corr)
        if key_resp.keys != None:  # we had a response
            trials.addData('key_resp.rt', key_resp.rt)
        trials.addData('key_resp.started', key_resp.tStartRefresh)
        trials.addData('key_resp.stopped', key_resp.tStopRefresh)
        trials.addData('text.started', text.tStartRefresh)
        trials.addData('text.stopped', text.tStopRefresh)



        for image in images:
            image.image = None
            image.pos = (0,0)

        distract_img.image = None
        distract_img.ori = 0
        distract_img.pos = (0,0)

        # the Routine "flanker" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()

    # completed 2 repeats of 'trials'


    # ------Prepare to start Routine "breakScr"-------
    continueRoutine = True
    # update component parameters for each repeat
    breakResp.keys = []
    breakResp.rt = []
    _breakResp_allKeys = []
    # keep track of which components have finished
    breakScrComponents = [breakText, breakResp]
    for thisComponent in breakScrComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    breakScrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "breakScr"-------
    while continueRoutine:
        # get current time
        t = breakScrClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=breakScrClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *breakText* updates
        if breakText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            breakText.frameNStart = frameN  # exact frame index
            breakText.tStart = t  # local t and not account for scr refresh
            breakText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(breakText, 'tStartRefresh')  # time at next scr refresh
            breakText.setAutoDraw(True)

        # *breakResp* updates
        waitOnFlip = False
        if breakResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            breakResp.frameNStart = frameN  # exact frame index
            breakResp.tStart = t  # local t and not account for scr refresh
            breakResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(breakResp, 'tStartRefresh')  # time at next scr refresh
            breakResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(breakResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(breakResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if breakResp.status == STARTED and not waitOnFlip:
            theseKeys = breakResp.getKeys(keyList=['space'], waitRelease=False)
            _breakResp_allKeys.extend(theseKeys)
            if len(_breakResp_allKeys):
                breakResp.keys = _breakResp_allKeys[-1].name  # just the last key pressed
                breakResp.rt = _breakResp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in breakScrComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "breakScr"-------
    for thisComponent in breakScrComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    blocks.addData('breakText.started', breakText.tStartRefresh)
    blocks.addData('breakText.stopped', breakText.tStopRefresh)
    # check responses
    if breakResp.keys in ['', [], None]:  # No response was made
        breakResp.keys = None
    blocks.addData('breakResp.keys',breakResp.keys)
    if breakResp.keys != None:  # we had a response
        blocks.addData('breakResp.rt', breakResp.rt)
    blocks.addData('breakResp.started', breakResp.tStartRefresh)
    blocks.addData('breakResp.stopped', breakResp.tStopRefresh)
    # the Routine "breakScr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1 repeats of 'blocks'


# ------Prepare to start Routine "goodbye"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
goodbyeComponents = [byeText]
for thisComponent in goodbyeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
goodbyeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "goodbye"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = goodbyeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=goodbyeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *byeText* updates
    if byeText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        byeText.frameNStart = frameN  # exact frame index
        byeText.tStart = t  # local t and not account for scr refresh
        byeText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(byeText, 'tStartRefresh')  # time at next scr refresh
        byeText.setAutoDraw(True)
    if byeText.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > byeText.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            byeText.tStop = t  # not accounting for scr refresh
            byeText.frameNStop = frameN  # exact frame index
            win.timeOnFlip(byeText, 'tStopRefresh')  # time at next scr refresh
            byeText.setAutoDraw(False)

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in goodbyeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "goodbye"-------
for thisComponent in goodbyeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('byeText.started', byeText.tStartRefresh)
thisExp.addData('byeText.stopped', byeText.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
