import js as p5

# - - - - - - - - - - - - - - - - - - - - - - - - - - - (INDEX) - - - - - - - - - - - - - - - - - - - - - - - - - 
# CTRL + F to quickly find main sections.

## 001 .   .   .   . Characters
   # a .   .   .   .   . Ground Movement
   # b .   .   .   .   . Air Movement
   # c .   .   .   .   . 'Player' Child
## 002 .   .   .   . Key/Mouse Events
## 003 .   .   .   . Environments
## 004 .   .   .   . UI
## 005 .   .   .   . Main Body


# - - - - - - - - - - - - - - - - - - - - - - - - - - - (GLOBAL VARIABLES) - - - - - - - - - - - - - - - - - - - - - - - - - 
## PLR / 'Player' variables
PLR_currentCharacter = 'luna' # Whether 'Player' is currently 'luna' or 'nox'
PLR_grounded = False # Whether 'Player' is grounded or not
PLR_jumpCharges = [] # Amount of times 'Player' can jump in succession
PLR_heldDirection = 'none' # Whether player is holding the left or right controls
PLR_movingDirection = 'none' # Checks what direction 'Player' is currently moving
PLR_initialJumpDirection = 'none' # Checks what direction 'Player' jumped
PLR_runSpeed = 10 # Run speed
PLR_xmoveTimer = 10 # Timer for x-movement
PLR_jumpSpeedy = 10 # Jump distance
PLR_jumpSpeedx = 10 # Horizontal Jump speed
PLR_ymoveTimer = 10 # Timer for y-movement
PLR_AirTurnaround = False # Whether 'Player' is turning around in the air
PLR_fallSpeed = 10 # Fall speed
PLR_fallSpeedMax = 10 # Maximum Fall speed
PLR_fallCheck = True # Check for whether 'Player' can still reset fallSpeed
PLR_fallTimer = 10 # Amount of time 'Player' has been falling
PLR_runStopSpeed = 10 # Run speed after letting go of run
PLR_runStopTimerCheck = 'none' # Checks if 'Player' has stopped running
PLR_runStopTimer = 10 # Timer for RunStop
PLR_jumpTurnSpeed = 10 # Jump TurnAround speed
PLR_jumpTurnTimeLength = 10
PLR_hitCharge = [1,2,3] 
PLR_landCheck = False
PLR_landTimer = 0
PLR_deathFlag = False
PLR_deathTimerCheck = False
PLR_deathTimer = 0
PLR_onWall = False

LUN_boostState = 'none'
LUN_boostGuidex = 0
LUN_boostGuidey = 0
LUN_xdiff = 0
LUN_ydiff = 0
LUN_boostTimer = 0
LUN_boostTimer02 = 0
LUN_boostTimerCheck = False
LUN_boostSpeedx = 10
LUN_boostSpeedy = 10
LUN_boostReleaseSpeedx = 10
LUN_boostReleaseSpeedy = 10
LUN_boostChargeTimerStart = 0
LUN_boostChargeTimerEnd = 0
LUN_disableBoost = True

## ENV / Environment variables
ENV_envState = 'exterior'
ENV_platformySpeed = 0
ENV_platformxSpeed = 0
ENV_boostGuidex = 0
ENV_boostGuidey = 0

## MSC / Miscellaneous variables
MSC_xborder = 300 # Horizontal game border (959 = normal gameplay)
MSC_yborder = 200 # Vertical game border
MSC_groundBorder = 540
MSC_keyboardA = False # Whether keyboard 'a' is being pressed
MSC_keyboardD = False # Whether keyboard 'd' is being pressed
MSC_keyboardW = False # Whether keyboard 'w' is being pressed
MSC_keyboardS = False
MSC_keyboardSpace = False
MSC_keyboardSpaceRelease = False
MSC_mouseL = False
MSC_listMechanics = False
MSC_pausePlay = 'play'
MSC_pausePlayerX = 0
MSC_pausePlayerY = 0
MSC_trackPlaying = 'none'
MSC_startedPlaying = False
MSC_startScreen = [1,2,3,4]

# RHT / Rhythm Variables
#RTH_gridMarkx = [220,250,280,310,340,370,400,430,460,490,520,550,580,610,640,670,700,730]
RTH_gridMarkx = [220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640,660,680,700,720,740]
#RTH_notex = [240,300,360,420,480,540,600,660,720]
RTH_barSpeedx = 0
RTH_disableBar = True
RTH_pauseBar = False
RTH_trackBPM = 1
RTH_beatTimer = 0
RTH_trackPlaying = 'none'
RTH_beatCount = []
RTH_noteStart = ['none','none','none','none']
RTH_noteStartx = [-1200,-1200,-1200,-1200]
RTH_noteEnd = ['none','none','none','none']
RTH_noteEndx = [-1200,-1200,-1200,-1200]
RTH_noteFillStart = ['none','none','none','none']
RTH_noteFillStartx = [-1200,-1200,-1200,-1200]
RTH_noteFillEnd = ['none','none','none','none']
RTH_noteFillEndx = [-1200,-1200,-1200,-1200]
RTH_startCheck_A = False
RTH_startCheck_B = False
RTH_startCheck_C = False
RTH_startCheck_D = False
RTH_endCheck_A = False
RTH_endCheck_B = False
RTH_endCheck_C = False
RTH_endCheck_D = False
RTH_failed_A = False
RTH_failed_B = False
RTH_failed_C = False
RTH_failed_D = False



# Initial Spawn Locations of all Assets
LUN_x = 300
LUN_y = 400
ENV_sect01_platform01x = -300
ENV_sect01_platform01y = 400
ENV_sect01_platform02x = 1350
ENV_sect01_platform02y = 300
ENV_sect01_platform03x = 3750
ENV_sect01_platform03y = 400
ENV_sect01_wall00x = -550
ENV_sect01_wall00y = 400
ENV_sect01_wall01x = 2100
ENV_sect01_wall01y = 690
ENV_sect01_wall02x = 4100
ENV_sect01_wall02y = 400
ENV_sect01_lavax = -2500
ENV_sect01_lavay = 520
UI_sect01_textInstructionsx = 1460
UI_sect01_textInstructionsy = 150

def resetGameToCheckpoint():
  global LUN_disableBoost, RTH_disableBar, RTH_barSpeedx, RTH_noteStart, RTH_noteEnd, RTH_noteStartx, RTH_noteEndx, RTH_trackPlaying
  player.x = LUN_x
  player.y = LUN_y
  fg_sect01_platform01.x = ENV_sect01_platform01x
  fg_sect01_platform01.y = ENV_sect01_platform01y
  fg_sect01_platform02.x = ENV_sect01_platform02x
  fg_sect01_platform02.y = ENV_sect01_platform02y
  fg_sect01_platform03.x = ENV_sect01_platform03x
  fg_sect01_platform03.y = ENV_sect01_platform03y
  fg_sect01_wall00.x = ENV_sect01_wall00x
  fg_sect01_wall00.y = ENV_sect01_wall00y
  fg_sect01_wall01.x = ENV_sect01_wall01x
  fg_sect01_wall01.y = ENV_sect01_wall01y
  fg_sect01_wall02.x = ENV_sect01_wall02x
  fg_sect01_wall02.y = ENV_sect01_wall02y
  fg_sect01_lava.x = ENV_sect01_lavax
  fg_sect01_lava.y = ENV_sect01_lavay
  ui_sect01_textInstructions.x = UI_sect01_textInstructionsx
  ui_sect01_textInstructions.y = UI_sect01_textInstructionsy
  LUN_disableBoost = True
  RTH_disableBar = True
  RTH_barSpeedx = 0
  if(RTH_trackPlaying == 'none' or RTH_trackPlaying == 'track01'):
    RTH_trackPlaying = 'track01'
  elif(RTH_trackPlaying == 'track00'):
    pass



# - - - - - - - - - - - - - - - - - - - - - - - - - - - (001 CHR - CHARACTERS) - - - - - - - - - - - - - - - - - - - - - - - - - 
#Classes:
class Movement: # Movement mechanics for 'Player' and 'Follower'
  x=0 # Starting pos x
  y=0 # Starting pos y
  def __init__(self):
    self.x = x
    self.y = y
    self.action_state = 'idleR' # Default 'action_state'
# 001a Ground Movement:
  def groundMovement(self): 
    global PLR_heldDirection, PLR_runSpeed, PLR_jumpSpeedx, PLR_jumpSpeedy, PLR_runStopTimerCheck, PLR_runStopTimer, PLR_runStopSpeed, PLR_movingDirection, PLR_grounded, PLR_fallCheck, PLR_AirTurnaround, PLR_landCheck, PLR_landTimer, LUN_boostState, LUN_disableBoost, ENV_platformySpeed, ENV_platformxSpeed, RTH_disableBar, RTH_pauseBar, RTH_trackPlaying
  # CONTROLS:
  ## RIGHT/LEFT RUNNING CONTROLS
    if(PLR_grounded == True):
      if(self.action_state != 'jumping' and self.action_state != 'falling'):
        if(MSC_keyboardD == True and MSC_keyboardA == False): 
          self.action_state = 'running' # Applies right run
          PLR_heldDirection = 'right'
        elif(MSC_keyboardA == True and MSC_keyboardD == False):
          self.action_state = 'running' # Applies left run
          PLR_heldDirection = 'left'
  ## GROUND TURNAROUND CONTROLS
        elif(MSC_keyboardA == True and MSC_keyboardD == True): # If both directions are pressed together, enter Turnaround state
          if(PLR_movingDirection == 'right'):
            self.action_state = 'turnAroundL' # Turnaround from right run to left run
            PLR_heldDirection = 'both'
          elif(PLR_movingDirection == 'left'):
            self.action_state = 'turnAroundR' # Turnaround from left run to right run
            PLR_heldDirection = 'both'
          else:
            pass
  ## GROUND IDLES
      if(self.action_state == 'idleL' and MSC_keyboardSpace == False): # When facing left, maintains left Idle state
        pass
      elif(MSC_keyboardD == False and MSC_keyboardA == False and MSC_keyboardW == False and self.action_state != 'idleL' and MSC_keyboardSpace == False):
        self.action_state = 'idleR' # Resets 'Player' to default IdleR state when grounded
        PLR_heldDirection = 'none'
  ## ENTER RUN AFTER LANDING A JUMP
      if(self.action_state == 'falling' and LUN_boostState != 'startup'):
        if(MSC_keyboardD == True and MSC_keyboardA == False and MSC_keyboardSpace == False): # Continues running right if holding D after a jump
          self.action_state = 'running'
          PLR_heldDirection = 'right'
        if(MSC_keyboardA == True and MSC_keyboardD == False and MSC_keyboardSpace == False): # Continues running left if holding A after a jump
          self.action_state = 'running'
          PLR_heldDirection = 'left'
        
  # VARIABLES:
    runStartup = 100 # Adjusts the startup time of 'Player' Run
    runSpeed = 1.5 # Run speed
    runStopTimeLength = 600 # Adjusts the length of time of RunStop
    runStopSpeed = 5 # RunStop speed
    runStopThreshold = 800 # Run time required for a full Runstop

  #MISC RULES:
  ## 'GROUNDED' RULES / DETERMINING GROUNDED STATE
    if(fg_sect01_platform01.plrGroundedFlag == True or \
       fg_sect01_platform02.plrGroundedFlag == True or \
       fg_sect01_platform03.plrGroundedFlag == True or \
       fg_sect01_wall01.plrGroundedFlag == True or \
       fg_sect01_wall02.plrGroundedFlag == True):
      PLR_grounded = True # Determines whether 'Player' is grounded. EVERY ground platform needs to be added to the plr.GroundedFlag==True checks above
      if(fg_sect01_platform03.plrGroundedFlag == True and MSC_pausePlay == 'play'):
        LUN_disableBoost = False
        RTH_disableBar = False
        RTH_pauseBar = False
        RTH_trackPlaying = 'track01'
      if(PLR_fallCheck == False):
        PLR_fallCheck = True
      if(PLR_landCheck == True):
        if(MSC_startedPlaying == True):
          self.landingJump01.setVolume(0.2)
          self.landingJump01.play()
          self.landingJump02.setVolume(0.05)
          self.landingJump02.play()
        PLR_landTimer = p5.millis()
        if(PLR_movingDirection == 'right' and MSC_keyboardD == False):
          PLR_runStopTimerCheck = 'right'
          PLR_runStopTimer = p5.millis()
        elif(PLR_movingDirection == 'left' and MSC_keyboardA == False):
          PLR_runStopTimerCheck = 'left'
          PLR_runStopTimer = p5.millis()
        PLR_landCheck = False
      for n in range(1,50,1):
        if(p5.millis()>PLR_landTimer + n*30):
          #if(LUN_boostState == 'none'):
            #ENV_platformySpeed = 6/n
          #else:
          ENV_platformySpeed = 13/n
      if(LUN_boostState == 'none' or LUN_boostState == 'release'):
        LUN_boostState = 'none'
      if(PLR_AirTurnaround == True):
        PLR_AirTurnaround = False
    else:
      PLR_grounded = False
      if(player.footstep.isPlaying() == True):
        player.footstep.stop()
      if(PLR_landCheck == False):
        PLR_landCheck = True
      self.y += PLR_fallSpeed # Applies Fall speed
      if(self.action_state == 'running' or self.action_state == 'runStopR'): # Fall off of platforms
        self.action_state = 'falling'
      if(len(PLR_jumpCharges) == 1): # Removes the ability to jump whenever Luna is not on the ground.
        PLR_jumpCharges.pop()
  ## RUNNING
    for n in range(0,6,1): # Gradual Run speed
      if(p5.millis()>PLR_xmoveTimer + runStartup*n):
        PLR_runSpeed = 1 + (runSpeed * n)
    if(self.action_state == 'running' and PLR_grounded == True):
      if(LUN_boostState == 'startup'): # Gradual decreasing speed during grounded Boost startup
        for n in range(1,12,1): 
          if(p5.millis()>PLR_runStopTimer + runStopTimeLength*2-100*(12/n)):
            PLR_runSpeed = (runSpeed/n)*4
      if(PLR_heldDirection == 'right' and MSC_keyboardA == False): # Applies right Run speed
        self.x += PLR_runSpeed
      if(PLR_heldDirection == 'left' and MSC_keyboardD == False): # Applies left Run speed
        self.x -= PLR_runSpeed
  ## RUNSTOP
    if(PLR_grounded == True):
      for n in range(1,10,1): # Gradual RunStop speed
        if(p5.millis()>PLR_runStopTimer + runStopTimeLength-60*(10/n)):
          PLR_runStopSpeed = (runStopSpeed/n)
      # if(PLR_runStopTimerCheck == 'right' or PLR_runStopTimerCheck == 'left'): # Extra camera movement during runStop
      #   for n in range(1,50,1):
      #     if(p5.millis()>PLR_runStopTimer + n*100):
      #       ENV_platformxSpeed = 10/n
      if(PLR_runStopTimerCheck=='right'): # Enables RunStop state after releasing right Run key
        if(MSC_keyboardW == True):
          player.action_state = 'jumping'
        else:
          player.action_state = 'runStopR'
          if(PLR_runStopTimer % PLR_xmoveTimer < runStopThreshold): # If Run time threshold was not met, RunStop is shortened and slowed.
            runStopTimeLength = 25 + runStopTimeLength*(PLR_runStopTimer % PLR_xmoveTimer / runStopThreshold) # Shortens RunStop
            if(runStopTimeLength > runStopTimeLength): # Applies max RunStop time
              runStopTimeLength = runStopTimeLength
            runStopSpeed = runStopSpeed * (PLR_runStopTimer % PLR_xmoveTimer / runStopThreshold) # Slows RunStop
          self.x += PLR_runStopSpeed # Applies right RunStop speed
          if(p5.millis()>PLR_runStopTimer + runStopTimeLength):
            player.action_state = 'idleR'
            PLR_runStopTimerCheck = 'none'
      elif(PLR_runStopTimerCheck == 'left'): # Enables RunStop state after releasing left Run key
        if(MSC_keyboardW == True):
          player.action_state = 'jumping'
        else:
          player.action_state = 'runStopL'
          if(PLR_runStopTimer % PLR_xmoveTimer < runStopThreshold): # If Run time-threshold was not met, RunStop is shortened and slowed.
            runStopTimeLength = 25 + runStopTimeLength*(PLR_runStopTimer % PLR_xmoveTimer / runStopThreshold) # Shortens RunStop
            if(runStopTimeLength > runStopTimeLength): # Applies max RunStop time
              runStopTimeLength = runStopTimeLength
            runStopSpeed = runStopSpeed * (PLR_runStopTimer % PLR_xmoveTimer / runStopThreshold) # Slows RunStop
          self.x -= PLR_runStopSpeed # Applies left RunStop speed
          if(p5.millis()>PLR_runStopTimer + runStopTimeLength):
            player.action_state = 'idleL'
            PLR_runStopTimerCheck = 'none'
  ## TURNAROUNDS
      elif(self.action_state == 'turnAroundL' or self.action_state == 'turnAroundR'): # TurnAround speed uses same formula as RunStop speed ^^
        if(PLR_runStopTimer % PLR_xmoveTimer < runStopThreshold):
          runStopTimeLength = 25 + runStopTimeLength*(PLR_runStopTimer % PLR_xmoveTimer / runStopThreshold)
          if(runStopTimeLength > runStopTimeLength):
            runStopTimeLength = runStopTimeLength
          runStopSpeed = runStopSpeed * (PLR_runStopTimer % PLR_xmoveTimer / 800) # Slows TurnAround
        if(self.action_state == 'turnAroundL'):
          self.x += PLR_runStopSpeed # Applies right>left TurnAround speed
          if(p5.millis()>PLR_runStopTimer + runStopTimeLength):
            player.action_state = 'idleR'
        elif(self.action_state == 'turnAroundR'):
          self.x -= PLR_runStopSpeed # Applies right>left TurnAround speed
          if(p5.millis()>PLR_runStopTimer + runStopTimeLength):
            player.action_state = 'idleL'
    if(player.action_state == 'idleR' or player.action_state == 'idleL'):
      PLR_runSpeed = 0
      PLR_runStopSpeed = 0
    if(PLR_grounded == True):
      if(PLR_runSpeed != 0 or PLR_runStopSpeed != 0 ): 
        if(player.action_state == 'running' and PLR_heldDirection == 'right'):
          PLR_movingDirection = 'right'
        if(player.action_state == 'runStopR'):
          if(MSC_keyboardA == False and MSC_keyboardD == False):
            PLR_movingDirection = 'right'
          if(MSC_keyboardA == True):
            PLR_movingDirection = 'turnLeft'
        if(player.action_state == 'running' and PLR_heldDirection == 'left'):
          PLR_movingDirection = 'left'
        if(player.action_state == 'runStopL'):
          if(MSC_keyboardA == False and MSC_keyboardD == False):
            PLR_movingDirection = 'left'
          if(MSC_keyboardD == True):
            PLR_movingDirection = 'turnRight'
      else:
        PLR_movingDirection = 'none'
  ## SOUNDS
    if(player.action_state == 'running'):
      if(player.footstep.isPlaying() == False):
        player.footstep.setVolume(0.03)
        player.footstep.loop()
      elif(player.footstep.isPlaying() == True):
        pass
      if(MSC_pausePlay == 'pause' and player.footstep.isPlaying()):
        player.footstep.pause()
      elif(MSC_pausePlay == 'play' and player.footstep.isPaused()):
        player.footstep.play()
    player.runStop.playMode('untilDone')
    if(player.action_state == 'runStopR' or player.action_state == 'runStopL'):
      if(PLR_grounded == True):
        player.runStop.setVolume(0.05)
        player.runStop.play()
  ## BORDERS BLOCK GROUND MOVEMENT
    if(self.x >= (p5.width-MSC_xborder*1.5)): # Stops movement through right border
      self.x = p5.width - MSC_xborder*1.5
    if(self.x <= MSC_xborder): # Stops movement through left border
      self.x = MSC_xborder

  
# 001b Air Movement:
  def airMovement(self):
    global PLR_jumpSpeedy, PLR_movingDirection, PLR_jumpTurnSpeed, PLR_fallTimer, PLR_jumpSpeedx, PLR_fallSpeed, PLR_fallSpeedMax, PLR_jumpCharges, PLR_fallCheck, PLR_initialJumpDirection, PLR_jumpTurnTimeLength
  # CONTROLS:
  ## RIGHT/LEFT AIR CONTROLS
    if(PLR_grounded == False and LUN_boostState == 'none'): # Right and Left controls while 'Player' is in the air:
      if(MSC_keyboardW == True or MSC_keyboardA == True or MSC_keyboardD == True or MSC_keyboardSpace == True):
        if(MSC_keyboardD == True and MSC_keyboardA == False and PLR_AirTurnaround == False): 
          PLR_movingDirection = 'right'
        elif(MSC_keyboardA == True and MSC_keyboardD == False and PLR_AirTurnaround == False): 
          PLR_movingDirection = 'left'
        elif(MSC_keyboardW == True and MSC_keyboardA == False and MSC_keyboardD == False):
          pass
        if(MSC_keyboardA == True and MSC_keyboardD == True):
          PLR_heldDirection = 'both'
          PLR_movingDirection = 'none'
      else:
        if(PLR_deathFlag == False):
          self.action_state = 'falling' # Resets 'Player' to default Jump state
  # VARIABLES:
    jumpSpeed = 12 # Jump speed
    jumpSpeedMinx = 5 # Minimum horizontal Jump speed
    jumpMaxTime = 12 # Max time the Jump button can be held
    jumpTurnStartup = 400 # Adjusts the TurnAround startup time
    jumpTurnTimeLength = 800 # Adjusts the length of time of air TurnAround
    jumpTurnSpeed = 5 # Air TurnAround speed
    jumpTurnThreshold = 800 # Run time required for a full air TurnAround
    PLR_fallSpeedMax = 20 # Maximum Fall speed
    fallSpeed = 1
  # MISC RULES:
  ## UP/DOWN JUMP MOVEMENT
    for n in range(1,jumpMaxTime,1): # Decreases Jump speed over time
      if(p5.millis()>PLR_ymoveTimer + n*40):
        PLR_jumpSpeedy = jumpSpeed - n
        if(PLR_jumpSpeedy >= 12):
          PLR_jumpSpeedy = 12
        if(PLR_jumpSpeedy <= 0):
          PLR_jumpSpeedy = 0.1
    if(self.action_state == 'jumping'):
      self.y -= PLR_jumpSpeedy + PLR_fallSpeed # Applies up Jump speed
      if(p5.millis()>PLR_ymoveTimer + jumpMaxTime*40): # 'Player' starts falling after exceeding jumpMaxTime
        self.action_state = 'falling'
        PLR_jumpSpeedy = 0
        PLR_fallTimer = p5.millis()
      if(PLR_movingDirection == 'none'):
        self.x += 0
  ## RIGHT/LEFT AIR MOVEMENT
    if(self.action_state == 'jumping' or self.action_state == 'falling' or self.action_state == 'boostStartup'):
      if(PLR_movingDirection == 'right'): # Applies right Jump speed
        self.x += PLR_jumpSpeedx
      if(PLR_movingDirection == 'left'): # Applies left Jump speed
        self.x -= PLR_jumpSpeedx
      if(PLR_jumpSpeedx < jumpSpeedMinx): # Applies minimum Jump speed
        for n in range(1,jumpSpeedMinx,1): # Gradually decreasing minimum Jump speed
          if(p5.millis()>PLR_ymoveTimer + 100*n):
            PLR_jumpSpeedx = jumpSpeedMinx-n
  ## AIR TURNAROUND MOVEMENT
      for n in range(1,10,1): # Gradual jump TurnAround speed
        if(p5.millis()>PLR_runStopTimer + jumpTurnTimeLength-80*(10/n)):
          PLR_jumpTurnSpeed = (jumpTurnSpeed/n)
      if(PLR_runStopTimer % PLR_xmoveTimer < jumpTurnThreshold):
        PLR_jumpTurnTimeLength = 25 + jumpTurnTimeLength*(PLR_runStopTimer % PLR_xmoveTimer / jumpTurnThreshold)
        if(PLR_jumpTurnTimeLength > jumpTurnTimeLength):
          PLR_jumpTurnTimeLength = jumpTurnTimeLength
        jumpTurnSpeed = PLR_jumpSpeedx*0.8 * (PLR_runStopTimer % PLR_xmoveTimer / 800) # Slows TurnAround
      if(PLR_initialJumpDirection == 'right'):
        if(PLR_AirTurnaround == True):
          if(PLR_movingDirection == 'left'):
            self.x += PLR_jumpSpeedx # Cancels out standard left Jump speed
          self.x += PLR_jumpTurnSpeed # Applies the gradually decreasing right speed, slowing down movement to 0
          if(p5.millis()>PLR_runStopTimer + PLR_jumpTurnTimeLength and MSC_keyboardD == False and MSC_keyboardA == True):
            PLR_movingDirection = 'left'
            if(PLR_jumpTurnSpeed <= 1):
              for n in range(0,6,1): # Gradual jump turnaround speed
                if(p5.millis()>PLR_xmoveTimer + jumpTurnStartup*n):
                  PLR_jumpSpeedx = (jumpSpeed/1500 * n)*0.5
                self.x -= PLR_jumpSpeedx # Applies gradual jump speed after turnaround
      if(PLR_initialJumpDirection == 'left'):
        if(PLR_AirTurnaround == True):
          if(PLR_movingDirection == 'right'):
            self.x -= PLR_jumpSpeedx # Cancels out standard right Jump speed
          self.x -= PLR_jumpTurnSpeed # Applies the gradually decreasing left speed, slowing down movement to 0
          if(p5.millis()>PLR_runStopTimer + PLR_jumpTurnTimeLength and MSC_keyboardA == False and MSC_keyboardD == True):
            PLR_movingDirection = 'right'
            if(PLR_jumpTurnSpeed <= 1):
              for n in range(0,6,1): # Gradual jump turnaround speed
                if(p5.millis()>PLR_xmoveTimer + jumpTurnStartup*n):
                  PLR_jumpSpeedx = (jumpSpeed/15 * n)*0.5
                self.x += PLR_jumpSpeedx # Applies gradual jump speed after turnaround
  ## FALL SPEED / GRAVITY
    for n in range(0,10,1): # Gradual Fall speed
      if(p5.millis()>PLR_fallTimer + 150*n):
        PLR_fallSpeed = fallSpeed * n 
    if(PLR_fallSpeed >= PLR_fallSpeedMax): # Caps Fall speed
      PLR_fallSpeed = PLR_fallSpeedMax
  ## AIRTIME TIMER
    if(PLR_grounded == False and PLR_fallTimer == 0): # Checks how long 'Player' has been in the air
      PLR_fallTimer = p5.millis()
    if(PLR_grounded == True): 
      PLR_fallTimer = 0 # Resets fallTimer
  ## INITIAL JUMP DIRECTION
      if(PLR_movingDirection == 'none'): # Sets initial jump direction when not moving (for visual purposes)
        if(player.action_state == 'idleR'):
          PLR_initialJumpDirection = 'rightIdle'
        if(player.action_state == 'idleL'):
          PLR_initialJumpDirection = 'leftIdle'
  ## AMOUNT OF JUMPS ALLOWED
      if(len(PLR_jumpCharges) == 0 and self.action_state != 'jumping'):
        PLR_jumpCharges.append(1)
  ## BORDERS BLOCK AERIAL MOVEMENT
    if(self.x >= (p5.width-MSC_xborder*1.5)): # Stops movement through right border
      self.x = p5.width - MSC_xborder*1.5
    if(self.x <= MSC_xborder): # Stops movement through left border
      self.x = MSC_xborder
    #if(self.y >= (p5.height-(MSC_yborder)/2)):
      #self.y = p5.height - (MSC_yborder)/2
    #if(self.y < MSC_yborder):
      #self.y = MSC_yborder
      


# 001c 'Player' Child:
class Player(Movement):
  def __init__(self, envScale = 'exterior'):
    self.envScale = envScale
    self.action_state = 'idleR'
  ## IMAGE ASSETS
    self.LunaIdleL1 = p5.loadImage('CHR/CHR_Luna/CHR_Luna-IdleL1.png') # Idle
    self.LunaIdleL2 = p5.loadImage('CHR/CHR_Luna/CHR_Luna-IdleL2.png')
    self.LunaIdleL3 = p5.loadImage('CHR/CHR_Luna/CHR_Luna-IdleL3.png')
    self.LunaIdleR1 = p5.loadImage('CHR/CHR_Luna/CHR_Luna-IdleR1.png')
    self.LunaIdleR2 = p5.loadImage('CHR/CHR_Luna/CHR_Luna-IdleR2.png')
    self.LunaIdleR3 = p5.loadImage('CHR/CHR_Luna/CHR_Luna-IdleR3.png')
    self.LunaJumpL = p5.loadImage('CHR/CHR_Luna/CHR_Luna-JumpL.png') # Jump
    self.LunaJumpR = p5.loadImage('CHR/CHR_Luna/CHR_Luna-JumpR.png')
    self.LunaJumpLFX = p5.loadImage('CHR/CHR_Luna/CHR_Luna-JumpLFX.png') # Jump FX
    self.LunaJumpRFX = p5.loadImage('CHR/CHR_Luna/CHR_Luna-JumpRFX.png')
    self.LunaFallingL = p5.loadImage('CHR/CHR_Luna/CHR_Luna-FallingL.png') # Fall
    self.LunaFallingR = p5.loadImage('CHR/CHR_Luna/CHR_Luna-FallingR.png')
    self.LunaRunL1 = p5.loadImage('CHR/CHR_Luna/CHR_Luna-RunL1.png') # Run
    self.LunaRunL2 = p5.loadImage('CHR/CHR_Luna/CHR_Luna-RunL2.png')
    self.LunaRunL3 = p5.loadImage('CHR/CHR_Luna/CHR_Luna-RunL3.png')
    self.LunaRunR1 = p5.loadImage('CHR/CHR_Luna/CHR_Luna-RunR1.png')
    self.LunaRunR2 = p5.loadImage('CHR/CHR_Luna/CHR_Luna-RunR2.png')
    self.LunaRunR3 = p5.loadImage('CHR/CHR_Luna/CHR_Luna-RunR3.png')
    self.LunaRunStopL = p5.loadImage('CHR/CHR_Luna/CHR_Luna-RunStopL.png') # Runstop
    self.LunaRunStopR = p5.loadImage('CHR/CHR_Luna/CHR_Luna-RunStopR.png')
    self.LunaTurnAroundL = p5.loadImage('CHR/CHR_Luna/CHR_Luna-RunStopR.png') # Turnaround
    self.LunaTurnAroundR = p5.loadImage('CHR/CHR_Luna/CHR_Luna-RunStopL.png')
    self.LunaBoostStartupL = p5.loadImage('CHR/CHR_Luna/CHR_Luna-JumpL.png') # Boosts
    self.LunaBoostStartupR = p5.loadImage('CHR/CHR_Luna/CHR_Luna-JumpR.png')
    self.LunaBoostDnL = p5.loadImage('CHR/CHR_Luna/CHR_Luna-BoostDnL.png')
    self.LunaBoostDnR = p5.loadImage('CHR/CHR_Luna/CHR_Luna-BoostDnR.png')
    self.LunaBoostUpL = p5.loadImage('CHR/CHR_Luna/CHR_Luna-BoostUpL.png')
    self.LunaBoostUpR = p5.loadImage('CHR/CHR_Luna/CHR_Luna-BoostUpR.png')
    self.LunaBoostDnLFX = p5.loadImage('CHR/CHR_Luna/CHR_Luna-BoostDnLFX.png') # Boost FX
    self.LunaBoostDnRFX = p5.loadImage('CHR/CHR_Luna/CHR_Luna-BoostDnRFX.png')
    self.LunaBoostUpLFX = p5.loadImage('CHR/CHR_Luna/CHR_Luna-BoostUpLFX.png')
    self.LunaBoostUpRFX = p5.loadImage('CHR/CHR_Luna/CHR_Luna-BoostUpRFX.png')
    self.LunaDeathR0 = p5.loadImage('CHR/CHR_Luna/CHR_Luna-DeathR0.png') # Death
    self.LunaDeathR1 = p5.loadImage('CHR/CHR_Luna/CHR_Luna-DeathR1.png')
    self.LunaDeathR2 = p5.loadImage('CHR/CHR_Luna/CHR_Luna-DeathR2.png')
    self.LunaDeathL0 = p5.loadImage('CHR/CHR_Luna/CHR_Luna-DeathL0.png')
    self.LunaDeathL1 = p5.loadImage('CHR/CHR_Luna/CHR_Luna-DeathL1.png')
    self.LunaDeathL2 = p5.loadImage('CHR/CHR_Luna/CHR_Luna-DeathL2.png')
  ## SFX ASSETS
    self.footstep = p5.loadSound('SFX/Movement/Running/sfx_movement_footstepsloop4_slow.wav') # Ground Movement
    self.runStop = p5.loadSound('SFX/Movement/Boost/enchant2.ogg')
    self.initialJump01 = p5.loadSound('SFX/Movement/Jumping/sfx_movement_jump16.wav') # Jumps
    self.initialJump02 = p5.loadSound('SFX/Movement/Jumping/space shield sounds - 1.wav')
    self.landingJump01 = p5.loadSound('SFX/Movement/Jumping/sfx_movement_jump15_landing.wav')
    self.landingJump02 = p5.loadSound('SFX/Movement/Jumping/space shield sounds - 8.wav')
    self.boosting01 = p5.loadSound('SFX/Movement/Boost/Menu_Select_00.wav') # Boosting
    self.boosting02 = p5.loadSound('SFX/Music/magicfail2.ogg')
    self.boosting03 = p5.loadSound('SFX/Movement/Boost/Laser_00.wav')
    self.boosting04 = p5.loadSound('SFX/Movement/Boost/synth_laser_04.ogg')
    self.boostStartup01 = p5.loadSound('SFX/Music/magicfail.ogg')
    self.boostStartup02 = p5.loadSound('SFX/Movement/landingJump.wav')
    self.boostStartup03 = p5.loadSound('SFX/Movement/Jumping/space shield sounds - 1.wav')
    self.boostRelease = p5.loadSound('SFX/Movement/Boost/exit.wav')
    self.boostDirection01 = p5.loadSound('SFX/Movement/Boost/sfx_sounds_falling3.wav')
    self.boostDirection02 = p5.loadSound('SFX/Movement/Boost/sfx_sounds_falling6.wav')
    self.boostDirection03 = p5.loadSound('SFX/Movement/Boost/sfx_sounds_falling4.wav')
    self.boostDirection04 = p5.loadSound('SFX/Movement/Boost/sfx_sounds_falling5.wav')
    self.boostDirection05 = p5.loadSound('SFX/Movement/Boost/sfx_sounds_falling7.wav')
    self.boostDirection06 = p5.loadSound('SFX/Movement/Boost/sfx_sounds_falling5.wav')
    self.boostDirection07 = p5.loadSound('SFX/Movement/Boost/sfx_sounds_falling4.wav')
    self.boostDirection08 = p5.loadSound('SFX/Movement/Boost/sfx_sounds_falling6.wav')
    self.death = p5.loadSound('SFX/Death/plr_death.wav') # Death
    
    
# Determining the image used to draw 'Player' based on their current 'action_state':
  def draw(self):
  # LUNA
  ## ENVIRONMENT-BASED SCALING
    if(self.envScale == 'exterior'):
      scale = 0.75*0.7 # The second number is a quick fix modifier, since I needed the character to be smaller overall.
    if(self.envScale == 'interior'):
      scale = 1*0.7
  ## IDLE
    if(self.action_state == 'idleL' and LUN_boostState == 'none'):
      if(MSC_pausePlay == 'play'):
        if(p5.millis() % 2000 < 500): 
          p5.image(self.LunaIdleL1,self.x,(self.y - self.LunaIdleL1.height*scale/2),self.LunaIdleL1.width*scale,self.LunaIdleL1.height*scale)
        elif((p5.millis() % 2000 < 1000) and (p5.millis() % 2000 > 499)):
          p5.image(self.LunaIdleL2,self.x,(self.y - self.LunaIdleL2.height*scale/2),self.LunaIdleL2.width*scale,self.LunaIdleL2.height*scale)
        elif((p5.millis() % 2000 < 1500) and (p5.millis() % 2000 > 999)):
          p5.image(self.LunaIdleL1,self.x,(self.y - self.LunaIdleL1.height*scale/2),self.LunaIdleL1.width*scale,self.LunaIdleL1.height*scale)
        elif((p5.millis() % 2000 <= 2000) and (p5.millis() % 2000 > 1499)):
          p5.image(self.LunaIdleL3,self.x,(self.y - self.LunaIdleL3.height*scale/2),self.LunaIdleL3.width*scale,self.LunaIdleL3.height*scale)
      if(MSC_pausePlay == 'pause'):
        p5.image(self.LunaIdleL1,self.x,(self.y - self.LunaIdleL1.height*scale/2),self.LunaIdleL1.width*scale,self.LunaIdleL1.height*scale)
    elif(self.action_state == 'idleR' and LUN_boostState == 'none'):
      if(MSC_pausePlay == 'play'):
        if(p5.millis() % 2000 < 500): 
          p5.image(self.LunaIdleR1,self.x,(self.y - self.LunaIdleR1.height*scale/2),self.LunaIdleR1.width*scale,self.LunaIdleR1.height*scale)
        elif((p5.millis() % 2000 < 1000) and (p5.millis() % 2000 > 499)):
          p5.image(self.LunaIdleR2,self.x,(self.y - self.LunaIdleR2.height*scale/2),self.LunaIdleR2.width*scale,self.LunaIdleR2.height*scale)
        elif((p5.millis() % 2000 < 1500) and (p5.millis() % 2000 > 999)):
          p5.image(self.LunaIdleR1,self.x,(self.y - self.LunaIdleR1.height*scale/2),self.LunaIdleR1.width*scale,self.LunaIdleR1.height*scale)
        elif((p5.millis() % 2000 <= 2000) and (p5.millis() % 2000 > 1499)):
          p5.image(self.LunaIdleR3,self.x,(self.y - self.LunaIdleR3.height*scale/2),self.LunaIdleR3.width*scale,self.LunaIdleR3.height*scale)
      if(MSC_pausePlay == 'pause'):
        p5.image(self.LunaIdleR1,self.x,(self.y - self.LunaIdleR1.height*scale/2),self.LunaIdleR1.width*scale,self.LunaIdleR1.height*scale)
  ## JUMPING
    elif(self.action_state == 'jumping'):
      if(PLR_movingDirection == 'none' and LUN_boostState == 'none'):
        if(PLR_initialJumpDirection == 'right' or PLR_initialJumpDirection == 'rightIdle'):
          p5.image(self.LunaJumpR,self.x,(self.y - self.LunaJumpR.height*scale/2),self.LunaJumpR.width*scale,self.LunaJumpR.height*scale)
        if(PLR_initialJumpDirection == 'left' or PLR_initialJumpDirection == 'leftIdle'):
          p5.image(self.LunaJumpL,self.x,(self.y - self.LunaJumpL.height*scale/2),self.LunaJumpL.width*scale,self.LunaJumpL.height*scale)
      if(PLR_movingDirection == 'right' and LUN_boostState == 'none'):
        p5.image(self.LunaJumpR,self.x,(self.y - self.LunaJumpR.height*scale/2),self.LunaJumpR.width*scale,self.LunaJumpR.height*scale)
      if(PLR_movingDirection == 'left' and LUN_boostState == 'none'):
        p5.image(self.LunaJumpL,self.x,(self.y - self.LunaJumpL.height*scale/2),self.LunaJumpL.width*scale,self.LunaJumpL.height*scale)
    if(LUN_boostState == 'startup'):
      if(p5.mouseX > self.x):
        p5.image(self.LunaJumpRFX,self.x,(self.y - self.LunaJumpRFX.height*scale/2),self.LunaJumpRFX.width*scale,self.LunaJumpRFX.height*scale)
        p5.image(self.LunaBoostStartupR,self.x,(self.y - self.LunaBoostStartupR.height*scale/2),self.LunaBoostStartupR.width*scale,self.LunaBoostStartupR.height*scale)
      elif(p5.mouseX < self.x):
        p5.image(self.LunaJumpLFX,self.x,(self.y - self.LunaJumpLFX.height*scale/2),self.LunaJumpLFX.width*scale,self.LunaJumpLFX.height*scale)
        p5.image(self.LunaBoostStartupL,self.x,(self.y - self.LunaBoostStartupL.height*scale/2),self.LunaBoostStartupL.width*scale,self.LunaBoostStartupL.height*scale)
    if(LUN_boostState == 'boosting' or LUN_boostState == 'release'): # Boost and release
      if(plr_boostGuide.x >= self.x and plr_boostGuide.y <= self.y-100):
        p5.image(self.LunaBoostUpRFX,self.x,(self.y - self.LunaBoostUpRFX.height*scale/2),self.LunaBoostUpRFX.width*scale,self.LunaBoostUpRFX.height*scale)
        p5.image(self.LunaBoostUpR,self.x,(self.y - self.LunaBoostUpR.height*scale/2),self.LunaBoostUpR.width*scale,self.LunaBoostUpR.height*scale)
      elif(plr_boostGuide.x < self.x and plr_boostGuide.y < self.y-100):
        p5.image(self.LunaBoostUpLFX,self.x,(self.y - self.LunaBoostUpLFX.height*scale/2),self.LunaBoostUpLFX.width*scale,self.LunaBoostUpLFX.height*scale)
        p5.image(self.LunaBoostUpL,self.x,(self.y - self.LunaBoostUpL.height*scale/2),self.LunaBoostUpL.width*scale,self.LunaBoostUpL.height*scale)
      elif(plr_boostGuide.x >= self.x and plr_boostGuide.y >= self.y-100):
        p5.image(self.LunaBoostDnRFX,self.x,(self.y - self.LunaBoostDnRFX.height*scale/2),self.LunaBoostDnRFX.width*scale,self.LunaBoostDnRFX.height*scale)
        p5.image(self.LunaBoostDnR,self.x,(self.y - self.LunaBoostDnR.height*scale/2),self.LunaBoostDnR.width*scale,self.LunaBoostDnR.height*scale)
      elif(plr_boostGuide.x < self.x and plr_boostGuide.y > self.y-100):
        p5.image(self.LunaBoostDnLFX,self.x,(self.y - self.LunaBoostDnLFX.height*scale/2),self.LunaBoostDnLFX.width*scale,self.LunaBoostDnLFX.height*scale)
        p5.image(self.LunaBoostDnL,self.x,(self.y - self.LunaBoostDnL.height*scale/2),self.LunaBoostDnL.width*scale,self.LunaBoostDnL.height*scale)
  ## FALLING
    elif(self.action_state == 'falling'):
      if(p5.millis()<PLR_fallTimer+300):
        if(PLR_movingDirection == 'none' and LUN_boostState == 'none'):
          if(PLR_initialJumpDirection == 'right' or PLR_initialJumpDirection == 'rightIdle'):
            p5.image(self.LunaJumpR,self.x,(self.y - self.LunaJumpR.height*scale/2),self.LunaJumpR.width*scale,self.LunaJumpR.height*scale)
          if(PLR_initialJumpDirection == 'left' or PLR_initialJumpDirection == 'leftIdle'):
            p5.image(self.LunaJumpL,self.x,(self.y - self.LunaJumpL.height*scale/2),self.LunaJumpL.width*scale,self.LunaJumpL.height*scale)
        if(PLR_movingDirection == 'right' and LUN_boostState == 'none'):
          p5.image(self.LunaJumpR,self.x,(self.y - self.LunaJumpR.height*scale/2),self.LunaJumpR.width*scale,self.LunaJumpR.height*scale)
        if(PLR_movingDirection == 'left' and LUN_boostState == 'none'):
          p5.image(self.LunaJumpL,self.x,(self.y - self.LunaJumpL.height*scale/2),self.LunaJumpL.width*scale,self.LunaJumpL.height*scale)
      elif(p5.millis()>=PLR_fallTimer+300):
        if(PLR_movingDirection == 'none' and LUN_boostState == 'none'):
          if(PLR_initialJumpDirection == 'right' or PLR_initialJumpDirection == 'rightIdle'):
            p5.image(self.LunaFallingR,self.x,(self.y - self.LunaFallingR.height*scale/2),self.LunaFallingR.width*scale,self.LunaFallingR.height*scale)
          if(PLR_initialJumpDirection == 'left' or PLR_initialJumpDirection == 'leftIdle'):
            p5.image(self.LunaFallingL,self.x,(self.y - self.LunaFallingL.height*scale/2),self.LunaFallingL.width*scale,self.LunaFallingL.height*scale)
        if(PLR_movingDirection == 'right' and LUN_boostState == 'none'):
          p5.image(self.LunaFallingR,self.x,(self.y - self.LunaFallingR.height*scale/2),self.LunaFallingR.width*scale,self.LunaFallingR.height*scale)
        if(PLR_movingDirection == 'left' and LUN_boostState == 'none'):
          p5.image(self.LunaFallingL,self.x,(self.y - self.LunaFallingL.height*scale/2),self.LunaFallingL.width*scale,self.LunaFallingL.height*scale)
  ## BOOSTING
      if(LUN_boostState == 'startup'): # Boost startup
        if(p5.mouseX > self.x):
          p5.image(self.LunaJumpRFX,self.x,(self.y - self.LunaJumpRFX.height*scale/2),self.LunaJumpRFX.width*scale,self.LunaJumpRFX.height*scale)
          p5.image(self.LunaBoostStartupR,self.x,(self.y - self.LunaBoostStartupR.height*scale/2),self.LunaBoostStartupR.width*scale,self.LunaBoostStartupR.height*scale)
        elif(p5.mouseX < self.x):
          p5.image(self.LunaJumpLFX,self.x,(self.y - self.LunaJumpLFX.height*scale/2),self.LunaJumpLFX.width*scale,self.LunaJumpLFX.height*scale)
          p5.image(self.LunaBoostStartupL,self.x,(self.y - self.LunaBoostStartupL.height*scale/2),self.LunaBoostStartupL.width*scale,self.LunaBoostStartupL.height*scale)
      if(LUN_boostState == 'boosting' or LUN_boostState == 'release'): # Boost and release
        if(plr_boostGuide.x >= self.x and plr_boostGuide.y <= self.y):
          p5.image(self.LunaBoostUpRFX,self.x,(self.y - self.LunaBoostUpRFX.height*scale/2),self.LunaBoostUpRFX.width*scale,self.LunaBoostUpRFX.height*scale)
          p5.image(self.LunaBoostUpR,self.x,(self.y - self.LunaBoostUpR.height*scale/2),self.LunaBoostUpR.width*scale,self.LunaBoostUpR.height*scale)
        elif(plr_boostGuide.x < self.x and plr_boostGuide.y < self.y):
          p5.image(self.LunaBoostUpLFX,self.x,(self.y - self.LunaBoostUpLFX.height*scale/2),self.LunaBoostUpLFX.width*scale,self.LunaBoostUpLFX.height*scale)
          p5.image(self.LunaBoostUpL,self.x,(self.y - self.LunaBoostUpL.height*scale/2),self.LunaBoostUpL.width*scale,self.LunaBoostUpL.height*scale)
        elif(plr_boostGuide.x >= self.x and plr_boostGuide.y >= self.y):
          p5.image(self.LunaBoostDnRFX,self.x,(self.y - self.LunaBoostDnRFX.height*scale/2),self.LunaBoostDnRFX.width*scale,self.LunaBoostDnRFX.height*scale)
          p5.image(self.LunaBoostDnR,self.x,(self.y - self.LunaBoostDnR.height*scale/2),self.LunaBoostDnR.width*scale,self.LunaBoostDnR.height*scale)
        elif(plr_boostGuide.x < self.x and plr_boostGuide.y > self.y):
          p5.image(self.LunaBoostDnLFX,self.x,(self.y - self.LunaBoostDnLFX.height*scale/2),self.LunaBoostDnLFX.width*scale,self.LunaBoostDnLFX.height*scale)
          p5.image(self.LunaBoostDnL,self.x,(self.y - self.LunaBoostDnL.height*scale/2),self.LunaBoostDnL.width*scale,self.LunaBoostDnL.height*scale)
  ## RUNNING
    elif(self.action_state == 'running' and LUN_boostState == 'none'):
      if(PLR_heldDirection == 'left'): #Run Left 3-frame Animation
        if(MSC_pausePlay == 'play'):
          if(p5.millis() % 1000 < 250): 
            p5.image(self.LunaRunL1,self.x,(self.y - self.LunaRunL1.height*scale/2),self.LunaRunL1.width*scale,self.LunaRunL1.height*scale)
          elif((p5.millis() % 1000 < 500) and (p5.millis() % 1000 > 249)):
            p5.image(self.LunaRunL2,self.x,(self.y - self.LunaRunL2.height*scale/2),self.LunaRunL2.width*scale,self.LunaRunL2.height*scale)
          elif((p5.millis() % 1000 < 750) and (p5.millis() % 1000 > 499)):
            p5.image(self.LunaRunL3,self.x,(self.y - self.LunaRunL3.height*scale/2),self.LunaRunL3.width*scale,self.LunaRunL3.height*scale)
          elif((p5.millis() % 1000 <= 1000) and (p5.millis() % 1000 > 749)):
            p5.image(self.LunaRunL2,self.x,(self.y - self.LunaRunL2.height*scale/2),self.LunaRunL2.width*scale,self.LunaRunL2.height*scale)           
        if(MSC_pausePlay == 'pause'):
          p5.image(self.LunaRunL2,self.x,(self.y - self.LunaRunL2.height*scale/2),self.LunaRunL2.width*scale,self.LunaRunL2.height*scale)
      if(PLR_heldDirection == 'right'): #Run Right 3-frame Animation
        if(MSC_pausePlay == 'play'):
          if(p5.millis() % 1000 < 250): 
            p5.image(self.LunaRunR1,self.x,(self.y - self.LunaRunR1.height*scale/2),self.LunaRunR1.width*scale,self.LunaRunR1.height*scale)
          elif((p5.millis() % 1000 < 500) and (p5.millis() % 1000 > 249)):
            p5.image(self.LunaRunR2,self.x,(self.y - self.LunaRunR2.height*scale/2),self.LunaRunR2.width*scale,self.LunaRunR2.height*scale)
          elif((p5.millis() % 1000 < 750) and (p5.millis() % 1000 > 499)):
            p5.image(self.LunaRunR3,self.x,(self.y - self.LunaRunR3.height*scale/2),self.LunaRunR3.width*scale,self.LunaRunR3.height*scale)
          elif((p5.millis() % 1000 <= 1000) and (p5.millis() % 1000 > 749)):
            p5.image(self.LunaRunR2,self.x,(self.y - self.LunaRunR2.height*scale/2),self.LunaRunR2.width*scale,self.LunaRunR2.height*scale)
        if(MSC_pausePlay == 'pause'):
          p5.image(self.LunaRunR2,self.x,(self.y - self.LunaRunR2.height*scale/2),self.LunaRunR2.width*scale,self.LunaRunR2.height*scale)
  ## DEATH
    elif(self.action_state == 'dead'):
      if(p5.millis()<PLR_deathTimer+300):
        if(PLR_movingDirection == 'left'):
          p5.image(self.LunaDeathL0,self.x,(self.y - self.LunaDeathL0.height*scale/2),self.LunaDeathL0.width*scale,self.LunaDeathL0.height*scale)
        if(PLR_movingDirection == 'right' or PLR_movingDirection == 'none'):
          p5.image(self.LunaDeathR0,self.x,(self.y - self.LunaDeathR0.height*scale/2),self.LunaDeathR0.width*scale,self.LunaDeathR0.height*scale)
      if(p5.millis()>=PLR_deathTimer+300):
        if(PLR_movingDirection == 'left'):
          p5.image(self.LunaDeathL1,self.x,(self.y - self.LunaDeathL1.height*scale/2),self.LunaDeathL1.width*scale,self.LunaDeathL1.height*scale)
          # if(p5.millis() % 1000 < 500): 
          #   p5.image(self.LunaDeathL1,self.x,(self.y - self.LunaDeathL1.height*scale/2),self.LunaDeathL1.width*scale,self.LunaDeathL1.height*scale)
          # elif((p5.millis() % 1000 <= 1000) and (p5.millis() % 1000 > 499)):
          #   p5.image(self.LunaDeathL2,self.x,(self.y - self.LunaDeathL2.height*scale/2),self.LunaDeathL2.width*scale,self.LunaDeathL2.height*scale)
        if(PLR_movingDirection == 'right' or PLR_movingDirection == 'none'):
          p5.image(self.LunaDeathR1,self.x,(self.y - self.LunaDeathR1.height*scale/2),self.LunaDeathR1.width*scale,self.LunaDeathR1.height*scale)
          # if(p5.millis() % 1000 < 500): 
          #   p5.image(self.LunaDeathR1,self.x,(self.y - self.LunaDeathR1.height*scale/2),self.LunaDeathR1.width*scale,self.LunaDeathR1.height*scale)
          # elif((p5.millis() % 1000 <= 1000) and (p5.millis() % 1000 > 499)):
          #   p5.image(self.LunaDeathR2,self.x,(self.y - self.LunaDeathR2.height*scale/2),self.LunaDeathR2.width*scale,self.LunaDeathR2.height*scale)
  ## RUNSTOP
    elif(self.action_state == 'runStopL' and LUN_boostState == 'none'):
      p5.image(self.LunaRunStopL,self.x,(self.y - self.LunaRunStopL.height*scale/2),self.LunaRunStopL.width*scale,self.LunaRunStopL.height*scale)
    elif(self.action_state == 'runStopR' and LUN_boostState == 'none'):
      p5.image(self.LunaRunStopR,self.x,(self.y - self.LunaRunStopR.height*scale/2),self.LunaRunStopR.width*scale,self.LunaRunStopR.height*scale)
  ## TURNAROUND
    elif(self.action_state == 'turnAroundL' and LUN_boostState == 'none'):
      p5.image(self.LunaTurnAroundL,self.x,(self.y - self.LunaTurnAroundL.height*scale/2),self.LunaTurnAroundL.width*scale,self.LunaTurnAroundL.height*scale)
    elif(self.action_state == 'turnAroundR' and LUN_boostState == 'none'):
      p5.image(self.LunaTurnAroundR,self.x,(self.y - self.LunaTurnAroundR.height*scale/2),self.LunaTurnAroundR.width*scale,self.LunaTurnAroundR.height*scale)
        
    self.groundMovement()
    self.airMovement()
    self.boost()
    self.deathState()

  
  def boost(self):
      global PLR_hitCharge, PLR_fallSpeed, PLR_jumpSpeedx, PLR_jumpSpeedy, PLR_runSpeed, PLR_movingDirection, LUN_boostSpeedx, LUN_boostSpeedy, LUN_boostState, LUN_boostTimer, LUN_boostTimer02, LUN_boostTimerCheck, LUN_xdiff, LUN_ydiff, LUN_boostReleaseSpeedx, LUN_boostReleaseSpeedy
  ## VARIABLES
      boostTime = 1000
      boostReleaseSpeedx = 9
      boostReleaseSpeedy = 12
      maxBoostDistance = 110**2
  ## BOOST CHARGE
      #LUN_boostChargeTimer
      
  ## BOOST STARTUP
      if(LUN_boostState == 'startup'):
        PLR_fallSpeed = PLR_fallSpeed*0.5
        PLR_jumpSpeedx = PLR_jumpSpeedx*0.8
        PLR_jumpSpeedy = PLR_jumpSpeedy*0.5
        PLR_runSpeed = PLR_runSpeed*0.1
        #p5.ellipse(p5.mouseX,p5.mouseY,15,15)
        #p5.fill(255)
        #p5.textSize(8)
        #p5.text('AIMING HERE', p5.mouseX, p5.mouseY-15)
  ## BOOST MOVEMENT
      if(LUN_boostState == 'boosting'):
        LUN_xdiff = LUN_boostGuidex - self.x
        LUN_ydiff = LUN_boostGuidey - self.y
        # if(LUN_ydiff < 50):
        #   LUN_ydiff = -50
        # elif(LUN_ydiff > -50):
        #   LUN_ydiff = 50
        # if(LUN_xdiff < -50):
        #   LUN_xdiff = -50
        # elif(LUN_xdiff > 50):
        #   LUN_xdiff = 50
        if(LUN_ydiff > 0 and PLR_grounded == True):
          LUN_ydiff = 0
          player.y = self.y
        if(LUN_xdiff > 0):
          PLR_movingDirection = 'right'
        elif(LUN_xdiff < 0):
          PLR_movingDirection = 'left'
        # boostDistance = ((LUN_xdiff**2) + (LUN_ydiff**2))**1/2 # Restricting the boost distance to a certain max
        # if(boostDistance > maxBoostDistance or boostDistance < -maxBoostDistance):
        #   LUN_xdiff = LUN_xdiff * (maxBoostDistance/boostDistance)
        #   LUN_ydiff = LUN_ydiff * (maxBoostDistance/boostDistance)
        for n in range(1,10,1):
          if(p5.millis()>LUN_boostTimer + boostTime-100*(10/n)):
            LUN_boostSpeedx = (LUN_xdiff/(n*50))
            LUN_boostSpeedy = (LUN_ydiff/(n*50))
          self.x += LUN_boostSpeedx
          self.y += LUN_boostSpeedy
        if(p5.millis()>LUN_boostTimer + 200):
          LUN_boostState = 'release'
          LUN_boostTimerCheck = True    
        if(len(PLR_jumpCharges) == 1):
          PLR_jumpCharges.pop()
  ## BOOST RELEASE
      if(LUN_boostState == 'release'):
        if(LUN_boostTimerCheck == True): # Starts a second timer for the duration of boost release
          LUN_boostTimerCheck = False
          LUN_boostTimer02 = p5.millis()
          #player.boostRelease.setVolume(0.8)
          #player.boostRelease.play()
        PLR_fallSpeed = PLR_fallSpeed/0.5
        PLR_jumpSpeedx = PLR_jumpSpeedx/0.8
        PLR_jumpSpeedy = PLR_jumpSpeedy/0.5
        LUN_boostReleaseSpeedx = boostReleaseSpeedx
        LUN_boostReleaseSpeedy = boostReleaseSpeedy
        if(LUN_ydiff < 0):
          if(LUN_xdiff == 0):
            self.x += 0
          elif(LUN_xdiff > 0 and LUN_xdiff < 40):
            self.x += boostReleaseSpeedx * 0.5
          elif(LUN_xdiff < 0 and LUN_xdiff > -40):
            self.x -= boostReleaseSpeedx * 0.5
          elif(LUN_xdiff >= 40 and LUN_xdiff < 250):
            self.x += boostReleaseSpeedx
          elif(LUN_xdiff <= -40 and LUN_xdiff > -250):
            self.x -= boostReleaseSpeedx
          elif(LUN_xdiff >= 250):
            self.x += boostReleaseSpeedx * 1.5
          elif(LUN_xdiff <= -250):
            self.x -= boostReleaseSpeedx * 1.5
        if(LUN_ydiff >= 0):
          self.y -= 0
        elif(LUN_ydiff < 0 and LUN_ydiff > -150):
          self.y -= boostReleaseSpeedy * 0.5
        elif(LUN_ydiff <= -150 and LUN_ydiff > -400):
          self.y -= boostReleaseSpeedy
        elif(LUN_ydiff <= -400):
          self.y -= boostReleaseSpeedy * 1.5
        if(p5.millis()>LUN_boostTimer02 + 2000):
          LUN_boostState = 'none'
    ## BORDERS BLOCK BOOST MOVEMENT
      if(self.x >= (p5.width-MSC_xborder*1.5)): # Stops movement through right border
        self.x = p5.width - MSC_xborder*1.5
      if(self.x <= (MSC_xborder)): # Stops movement through left border
        self.x = MSC_xborder
      #if(self.y <= MSC_yborder and LUN_boostState == 'release'):
        #self.y = MSC_yborder
  
  def enterBoostStartup(self):
    global LUN_boostChargeTimerStart, LUN_boostState, PLR_runStopTimer
    LUN_boostChargeTimerStart = p5.millis()
    player.boostStartup01.setVolume(0.5)
    player.boostStartup01.play()
    player.boostStartup02.setVolume(0.1)
    player.boostStartup02.play()
    LUN_boostState = 'startup'
    if(PLR_grounded == True):
      PLR_runStopTimer = p5.millis()

  def exitBoostStartup(self):
    global LUN_boostState
    LUN_boostState = 'none'
    PLR_fallSpeed = PLR_fallSpeed/0.5
    PLR_jumpSpeedx = PLR_jumpSpeedx/0.8
    PLR_jumpSpeedy = PLR_jumpSpeedy/0.5
    PLR_runSpeed = PLR_runSpeed/0.1
    

  def enterBoostBoosting(self):
    global LUN_boostChargeTimerEnd, LUN_boostGuidex, LUN_boostGuidey, ENV_boostGuidex, ENV_boostGuidey, MSC_keyboardSpaceRelease, LUN_boostState, LUN_boostTimer, PLR_fallTimer
    LUN_boostChargeTimerEnd = p5.millis()
    LUN_boostGuidex = p5.mouseX
    LUN_boostGuidey = p5.mouseY
    if(MSC_keyboardSpaceRelease == False):
      ENV_boostGuidex = p5.mouseX
      ENV_boostGuidey = p5.mouseY
      MSC_keyboardSpaceRelease = True
    LUN_boostState = 'boosting'
    LUN_boostTimer = p5.millis()
    player.boosting01.setVolume(0.05)
    player.boosting01.play()
    player.boosting02.setVolume(0.8)
    player.boosting02.play()
    player.boosting03.setVolume(0.05)
    player.boosting03.play()
    player.boosting04.setVolume(0.01)
    if(player.boosting04.isPlaying()):
      player.boosting04.stop()
      player.boosting04.play()
    else:
      player.boosting04.play()
    PLR_fallTimer = p5.millis()
    # if(LUN_ydiff < 0):
    #   if(LUN_xdiff > -40 and LUN_xdiff < 40):
    #     player.boosting01.rate()
    #   elif(LUN_xdiff >= 40 and LUN_xdiff < 250):
    #     player.boostDirection02.setVolume(0.05)
    #     player.boostDirection02.play()
    #   elif(LUN_xdiff <= -40 and LUN_xdiff > -250):
    #     player.boostDirection08.setVolume(0.05)
    #     player.boostDirection08.play()
    #   elif(LUN_xdiff >= 250):
    #     player.boostDirection03.setVolume(0.05)
    #     player.boostDirection03.play()
    #   elif(LUN_xdiff <= -250):
    #     player.boostDirection07.setVolume(0.05)
    #     player.boostDirection07.play()
    # if(LUN_ydiff >= 0):
    #   if(LUN_xdiff > -40 and LUN_xdiff < 40):
    #     player.boostDirection05.setVolume(0.05)
    #     player.boostDirection05.play()
    #   elif(LUN_xdiff >= 40 and LUN_xdiff < 250):
    #     player.boostDirection04.setVolume(0.05)
    #     player.boostDirection04.play()
    #   elif(LUN_xdiff <= -40 and LUN_xdiff > -250):
    #     player.boostDirection06.setVolume(0.05)
    #     player.boostDirection06.play()
    #   elif(LUN_xdiff >= 250):
    #     player.boostDirection03.setVolume(0.05)
    #     player.boostDirection03.play()
    #   elif(LUN_xdiff <= -250):
    #     player.boostDirection07.setVolume(0.05)
    #     player.boostDirection07.play()
    # if(LUN_ydiff < 0):
    #   if(LUN_xdiff > -40 and LUN_xdiff < 40):
    #     player.boostDirection01.setVolume(0.05)
    #     player.boostDirection01.play()
    #   elif(LUN_xdiff >= 40 and LUN_xdiff < 250):
    #     player.boostDirection02.setVolume(0.05)
    #     player.boostDirection02.play()
    #   elif(LUN_xdiff <= -40 and LUN_xdiff > -250):
    #     player.boostDirection08.setVolume(0.05)
    #     player.boostDirection08.play()
    #   elif(LUN_xdiff >= 250):
    #     player.boostDirection03.setVolume(0.05)
    #     player.boostDirection03.play()
    #   elif(LUN_xdiff <= -250):
    #     player.boostDirection07.setVolume(0.05)
    #     player.boostDirection07.play()
    # if(LUN_ydiff >= 0):
    #   if(LUN_xdiff > -40 and LUN_xdiff < 40):
    #     player.boostDirection05.setVolume(0.05)
    #     player.boostDirection05.play()
    #   elif(LUN_xdiff >= 40 and LUN_xdiff < 250):
    #     player.boostDirection04.setVolume(0.05)
    #     player.boostDirection04.play()
    #   elif(LUN_xdiff <= -40 and LUN_xdiff > -250):
    #     player.boostDirection06.setVolume(0.05)
    #     player.boostDirection06.play()
    #   elif(LUN_xdiff >= 250):
    #     player.boostDirection03.setVolume(0.05)
    #     player.boostDirection03.play()
    #   elif(LUN_xdiff <= -250):
    #     player.boostDirection07.setVolume(0.05)
    #     player.boostDirection07.play()

  def deathState(self):
    global PLR_fallSpeed, PLR_jumpSpeedx, PLR_jumpSpeedy, PLR_runSpeed, PLR_runStopSpeed, PLR_deathTimerCheck, PLR_deathTimer, PLR_ymoveTimer, PLR_fallTimer, LUN_boostSpeedx, LUN_boostSpeedy, LUN_boostState, LUN_boostTimer, LUN_boostReleaseSpeedx, LUN_boostReleaseSpeedy, MSC_trackPlaying, RTH_barSpeedx, RTH_trackPlaying
    if(PLR_deathFlag == True):
      if(PLR_deathTimerCheck == True):
        PLR_deathTimer = p5.millis()
        PLR_ymoveTimer = p5.millis()
        PLR_fallTimer = p5.millis()
        player.death.setVolume(0.3)
        player.death.play()
        PLR_deathTimerCheck = False
      self.action_state = 'dead'
      PLR_jumpSpeedx = 0
      PLR_runSpeed = 0
      PLR_runStopSpeed = 0
      LUN_boostSpeedx = 0
      LUN_boostSpeedy = 0
      LUN_boostReleaseSpeedx = 0
      LUN_boostReleaseSpeedy = 0
      LUN_boostState = 'none'
      # if(RTH_disableBar == False and RTH_pauseBar == False):
      #   RTH_barSpeedx = RTH_barSpeedx/2
      #RTH_trackPlaying = 'none'
      if(MSC_startedPlaying == True):
        for n in range(15):
          if(p5.millis()>PLR_deathTimer + n*300):
            p5.fill(0,n)
            p5.rect(p5.width/2,p5.height/2, p5.width, p5.height)
            #p5.filter(p5.GRAY)
        for n in range(255):
          if(p5.millis()>PLR_deathTimer + 1500 + n*30):
            p5.noStroke()
            p5.fill(255,n)
            p5.textFont(ui_pauseScreen.font_Coco)
            p5.textSize(30)
            p5.text('LUNA DIED..', p5.width/2, p5.height/2)
        for n in range(255):
          if(p5.millis()>PLR_deathTimer + 3000 + n*30):
            p5.noStroke()
            p5.fill(255,n)
            p5.textFont(ui_pauseScreen.font_CocoSemilight)
            p5.textSize(12)
            p5.text('(ESC to try again)', p5.width/2, p5.height/2 + 35)
    if(self.action_state == 'dead'):
      if(PLR_movingDirection == 'right'):
        self.y -= PLR_jumpSpeedy*2
        self.x += 3
      if(PLR_movingDirection == 'left'):
        self.y -= PLR_jumpSpeedy*2
        self.x -= 3
        


# - - - - - - - - - - - - - - - - - - - - - - - - - - - (002 KEY/MOUSE EVENTS) - - - - - - - - - - - - - - - - - - - - - - - - - 
#Key Press:
def keyPressed(event):
  global PLR_currentCharacter, PLR_jumpCharges, PLR_runSpeed, PLR_fallSpeed, PLR_jumpSpeedx, PLR_jumpSpeedy, PLR_fallSpeedMax, PLR_xmoveTimer, PLR_ymoveTimer, PLR_runStopSpeed, PLR_runStopTimer, PLR_movingDirection, PLR_initialJumpDirection, PLR_airTurnTimer, PLR_fallTimer, PLR_AirTurnaround, PLR_deathFlag, LUN_boostState, LUN_boostTimer, LUN_boostTimer02, LUN_boostGuidey, LUN_boostGuidex, LUN_boostChargeTimerStart, LUN_xdiff, LUN_ydiff, LUN_boostSpeedx, LUN_boostSpeedy, LUN_boostReleaseSpeedx, LUN_boostReleaseSpeedy, LUN_disableBoost, MSC_keyboardD, MSC_keyboardA, MSC_keyboardW, MSC_keyboardS, MSC_keyboardSpace, MSC_listMechanics, MSC_pausePlay, MSC_pausePlayerX, MSC_pausePlayerY, MSC_pauseActState, MSC_pauseKeyboardA, MSC_pauseKeyboardW, MSC_pauseKeyboardD, MSC_pauseKeyboardS, MSC_pauseKeyboardSpace, MSC_pauseFallSpeed, MSC_pauseFallTimer, MSC_pauseXMoveTimer, MSC_pauseYMoveTimer, MSC_pauseHeldDir, MSC_pauseMovingDir, MSC_pauseInitialJumpDir, MSC_pauseRunSpeed, MSC_pauseRunStopSpeed, MSC_pauseRunStopTimerCheck, MSC_pauseJumpSpeedX, MSC_pauseJumpSpeedY, MSC_pauseLunBoostState, MSC_pauseLunBoostXDiff, MSC_pauseLunBoostYDiff, MSC_pauseLunBoostTimer, MSC_pauseLunBoostTimer02, MSC_pauseLunBoostSpeedX, MSC_pauseLunBoostSpeedY, MSC_pauseLunBoostRelSpeedX, MSC_pauseLunBoostRelSpeedY, MSC_pauseLunBoostChargeTimerStart, MSC_pauseLunBoostChargeTimerEnd, MSC_trackPlaying, MSC_startedPlaying, RTH_disableBar, RTH_trackPlaying, RTH_noteStart, RTH_startCheck_A, RTH_startCheck_B, RTH_startCheck_C, RTH_startCheck_D
  if(MSC_startedPlaying == True and MSC_pausePlay == 'play' and PLR_deathFlag == False):
## Movement WAD
    if(p5.key=='w'):
      MSC_keyboardW = True # More reliable check for p5.key=='w'
      if(len(PLR_jumpCharges) > 0):
        PLR_jumpCharges.pop()
        player.action_state = 'jumping'
        player.initialJump01.setVolume(0.05)
        player.initialJump01.play()
        player.initialJump02.setVolume(0.05)
        player.initialJump02.play()
        PLR_ymoveTimer = p5.millis()
      elif(len(PLR_jumpCharges) == 0):
        pass   
      if(PLR_grounded == True):
        if(PLR_movingDirection == 'right'):
          PLR_jumpSpeedx = PLR_runSpeed # Sets jump speed to the final run speed before jumping (to account for the changing runspeed)
          PLR_initialJumpDirection = 'right' # Sets initial jump direction to right
        if(PLR_movingDirection == 'left'):
          PLR_jumpSpeedx = PLR_runSpeed # Sets jump speed to the final run speed before jumping (to account for the changing runspeed)
          PLR_initialJumpDirection = 'left' # Sets initial jump direction to left
    if(p5.key=='d'):
      MSC_keyboardD = True # More reliable for p5.key=='d'
      if(PLR_grounded == True):
        if(MSC_keyboardA == False):
          PLR_xmoveTimer = p5.millis() # Starts run timer for run startup
        if(MSC_keyboardA == True):
          PLR_runStopTimer = p5.millis() # Starts turnaround timer
      if(PLR_initialJumpDirection == 'left' and PLR_grounded == False):
        PLR_runStopTimer = p5.millis() # Starts air turnaround timer
        PLR_AirTurnaround = True #Sets air turnaround check to true
        PLR_xmoveTimer = p5.millis()
    if(p5.key=='a'):
      MSC_keyboardA = True # More reliable for p5.key=='d'
      if(PLR_grounded == True):
        if(MSC_keyboardD == False):
          PLR_xmoveTimer = p5.millis() # Starts run timer for run startup
        if(MSC_keyboardD == True):
          PLR_runStopTimer = p5.millis() # Starts turnaround timer
      if(PLR_initialJumpDirection == 'right' and PLR_grounded == False):
        PLR_runStopTimer = p5.millis() # Starts air turnaround timer
        PLR_AirTurnaround = True #Sets air turnaround check to true
        PLR_xmoveTimer = p5.millis()
## Character Abilities
    if(p5.key==' ' and LUN_disableBoost == False):
      MSC_keyboardSpace = True # More reliable for p5.key==' '
      if(RTH_noteFillStart[3] == 'none' and RTH_noteStart[3] == 'D'):
        if(p5.width/2 >= RTH_noteStartx[3]-11 and p5.width/2 <= RTH_noteStartx[3]+11):
          RTH_noteFillStart.pop(3)
          RTH_noteFillStart.insert(3,'D')
          RTH_noteFillStartx.pop(3)
          RTH_noteFillStartx.insert(3,RTH_noteStartx[3])
          player.enterBoostStartup()
          RTH_startCheck_D = True
      if(RTH_noteFillStart[2] == 'none' and RTH_noteStart[2] == 'C'):
        if(p5.width/2 >= RTH_noteStartx[2]-11 and p5.width/2 <= RTH_noteStartx[2]+11):
          RTH_noteFillStart.pop(2)
          RTH_noteFillStart.insert(2,'C')
          RTH_noteFillStartx.pop(2)
          RTH_noteFillStartx.insert(2,RTH_noteStartx[2])
          player.enterBoostStartup()
          RTH_startCheck_C = True
      if(RTH_noteFillStart[1] == 'none' and RTH_noteStart[1] == 'B'):
        if(p5.width/2 >= RTH_noteStartx[1]-11 and p5.width/2 <= RTH_noteStartx[1]+11):
          RTH_noteFillStart.pop(1)
          RTH_noteFillStart.insert(1,'B')
          RTH_noteFillStartx.pop(1)
          RTH_noteFillStartx.insert(1,RTH_noteStartx[1])
          player.enterBoostStartup()
          RTH_startCheck_B = True
      if(RTH_noteFillStart[0] == 'none' and RTH_noteStart[0] == 'A'):
        if(p5.width/2 >= RTH_noteStartx[0]-11 and p5.width/2 <= RTH_noteStartx[0]+11):
          RTH_noteFillStart.pop(0)
          RTH_noteFillStart.insert(0,'A')
          RTH_noteFillStartx.pop(0)
          RTH_noteFillStartx.insert(0,RTH_noteStartx[0])
          player.enterBoostStartup()
          RTH_startCheck_A = True
      if(RTH_noteStart[0] == 'A' and RTH_noteStart[1] == 'B' and RTH_noteStart[2] == 'C' and RTH_noteStart[3] == 'D'):
        pass
      elif(RTH_noteStart[0] == 'A' and RTH_noteStart[1] == 'B' and RTH_noteStart[2] == 'C' and RTH_noteStart[3] == 'none'):
        RTH_noteStart.pop(3)
        RTH_noteStart.insert(3,'D')
        RTH_noteStartx.pop(3)
        RTH_noteStartx.insert(3,p5.width/2)
        player.enterBoostStartup()
      elif(RTH_noteStart[0] == 'A' and RTH_noteStart[1] == 'B' and RTH_noteStart[2] == 'none' and RTH_noteStart[3] == 'none'):
        RTH_noteStart.pop(2)
        RTH_noteStart.insert(2,'C')
        RTH_noteStartx.pop(2)
        RTH_noteStartx.insert(2,p5.width/2)
        player.enterBoostStartup()
      elif(RTH_noteStart[0] == 'A' and RTH_noteStart[1] == 'none' and RTH_noteStart[2] == 'none' and RTH_noteStart[3] == 'none'):
        RTH_noteStart.pop(1)
        RTH_noteStart.insert(1,'B')
        RTH_noteStartx.pop(1)
        RTH_noteStartx.insert(1,p5.width/2)
        player.enterBoostStartup()
      if(RTH_noteStart[0] == 'none' and RTH_noteStart[1] == 'none' and RTH_noteStart[2] == 'none' and RTH_noteStart[3] == 'none'):
        RTH_noteStart.pop(0)
        RTH_noteStart.insert(0,'A')
        RTH_noteStartx.pop(0)
        RTH_noteStartx.insert(0,p5.width/2)
        player.enterBoostStartup()

    if(p5.key=='s'):
      MSC_keyboardS = True
      if(LUN_boostState == 'startup'):
        LUN_boostState = 'none'
    # if(p5.keyCode==p5.SHIFT):
    #   if(PLR_currentCharacter == 'luna'):
    #     PLR_currentCharacter = 'nox'
    #   elif(PLR_currentCharacter == 'nox'):
    #     PLR_currentCharacter = 'luna'
## Menu / Misc
    if(p5.key=='t'): 
      LUN_disableBoost = False
      RTH_disableBar = False
    if(p5.key=='f'):
      if(LUN_disableBoost == False):
        if(RTH_trackPlaying == 'track01'):
          RTH_trackPlaying = 'track00'
          p5.print("now playing 'City Pop x 80s Funk Type Beat - Foolish Love' by emilybeats")
        elif(RTH_trackPlaying == 'track00'):
          RTH_trackPlaying = 'track01'
          p5.print("now playing metronome")
    if(p5.key=='c'): #quick check variables
      print('plr_boostGuide.x,y =', plr_boostGuide.x, plr_boostGuide.y)
      print('player.action_state =', player.action_state)
      print('PLR_grounded =', PLR_grounded)
      print('PLR_initialJumpDirection =', PLR_initialJumpDirection)
      print('LUN_boostState =', LUN_boostState)
      print('LUN_boostGuidex,y =', LUN_boostGuidex, LUN_boostGuidey)
      print('PLR_movingDirection =', PLR_movingDirection)
      print('PLR_heldDirection =', PLR_heldDirection)
      print('player.x,y =', player.x, player.y)
      print('PLR_landTimer =', PLR_landTimer)
      print('PLR_deathFlag =', PLR_deathFlag)
      print('PLR_onWall =', PLR_onWall)
      print('LUN_ydiff =', LUN_ydiff)
  if(MSC_startedPlaying == True and PLR_deathFlag == False):
    if(p5.keyCode==p5.ESCAPE):
      if(MSC_pausePlay == 'play'):
        MSC_pausePlay = 'pause'
        MSC_pausePlayerX = player.x
        MSC_pausePlayerY = player.y
        MSC_pauseActState = player.action_state
        MSC_pauseKeyboardA = MSC_keyboardA
        MSC_pauseKeyboardW = MSC_keyboardW
        MSC_pauseKeyboardD = MSC_keyboardD
        MSC_pauseKeyboardS = MSC_keyboardS
        MSC_pauseKeyboardSpace = MSC_keyboardSpace
        MSC_pauseFallSpeed = PLR_fallSpeed
        MSC_pauseFallTimer = p5.millis() - PLR_fallTimer
        MSC_pauseXMoveTimer = p5.millis() - PLR_xmoveTimer
        MSC_pauseYMoveTimer = p5.millis() - PLR_ymoveTimer
        MSC_pauseHeldDir = PLR_heldDirection
        MSC_pauseMovingDir = PLR_movingDirection
        MSC_pauseInitialJumpDir = PLR_initialJumpDirection
        MSC_pauseRunSpeed = PLR_runSpeed
        MSC_pauseRunStopSpeed = PLR_runStopSpeed
        MSC_pauseRunStopTimerCheck = PLR_runStopTimerCheck
        MSC_pauseJumpSpeedX = PLR_jumpSpeedx
        MSC_pauseJumpSpeedY = PLR_jumpSpeedy
        MSC_pauseLunBoostState = LUN_boostState
        MSC_pauseLunBoostXDiff = LUN_xdiff
        MSC_pauseLunBoostYDiff = LUN_ydiff
        MSC_pauseLunBoostTimer = p5.millis() - LUN_boostTimer
        MSC_pauseLunBoostTimer02 = p5.millis() - LUN_boostTimer02
        MSC_pauseLunBoostSpeedX = LUN_boostSpeedx
        MSC_pauseLunBoostSpeedY = LUN_boostSpeedy
        MSC_pauseLunBoostRelSpeedX = LUN_boostReleaseSpeedx
        MSC_pauseLunBoostRelSpeedY = LUN_boostReleaseSpeedy
        MSC_pauseLunBoostChargeTimerStart = LUN_boostChargeTimerStart
        MSC_pauseLunBoostChargeTimerEnd = LUN_boostChargeTimerEnd
      elif(MSC_pausePlay == 'pause'):
        MSC_pausePlay = 'play'
        player.action_state = MSC_pauseActState
        PLR_fallSpeed = MSC_pauseFallSpeed
        PLR_runSpeed = MSC_pauseRunSpeed
        PLR_runStopSpeed = MSC_pauseRunStopSpeed
        PLR_jumpSpeedx = MSC_pauseJumpSpeedX
        PLR_jumpSpeedy = MSC_pauseJumpSpeedY
        LUN_boostSpeedx = MSC_pauseLunBoostSpeedX
        LUN_boostSpeedy = MSC_pauseLunBoostSpeedY
        LUN_boostReleaseSpeedx = MSC_pauseLunBoostRelSpeedX
        LUN_boostReleaseSpeedy = MSC_pauseLunBoostRelSpeedY
        PLR_fallTimer = p5.millis() - MSC_pauseFallTimer
        PLR_xmoveTimer = p5.millis() - MSC_pauseXMoveTimer
        PLR_ymoveTimer = p5.millis() - MSC_pauseYMoveTimer
        LUN_boostTimer = p5.millis() - MSC_pauseLunBoostTimer
        LUN_boostTimer02 = p5.millis() - MSC_pauseLunBoostTimer02
  if(MSC_startedPlaying == False and p5.key==' '):
    if(len(MSC_startScreen)==1):
      MSC_startedPlaying = True
      if(PLR_deathFlag == True):
        MSC_pausePlay = 'play'
        PLR_deathFlag = False
      resetGameToCheckpoint()
    elif(len(MSC_startScreen)==2):
      MSC_startScreen.pop()
    elif(len(MSC_startScreen)==3):
      MSC_startScreen.pop()
    elif(len(MSC_startScreen)==4):
      MSC_startScreen.pop()
    else:
      pass
  if(MSC_startedPlaying == True and PLR_deathFlag == True):
    if(p5.keyCode==p5.ESCAPE):
      PLR_deathFlag = False
      player.action_state == 'idleR'
      player.x = LUN_x
      player.y = LUN_y
      resetGameToCheckpoint()
      

#Key Release:
def keyReleased(event):
  global PLR_currentCharacter, PLR_runStopTimerCheck, PLR_runStopTimer, PLR_fallTimer, PLR_fallCheck, PLR_jumpCharges, PLR_fallSpeed, PLR_heldDirection, LUN_boostState, PLR_lunaBoostSpots, LUN_boostTimer, LUN_boostGuidex, LUN_boostGuidey, LUN_boostChargeTimerEnd, LUN_boostState, ENV_boostGuidex, ENV_boostGuidey, MSC_keyboardD, MSC_keyboardA, MSC_keyboardW, MSC_keyboardSpace, MSC_keyboardSpaceRelease, RTH_noteEnd, RTH_endCheck_A, RTH_endCheck_B, RTH_endCheck_C, RTH_endCheck_D
  if(MSC_startedPlaying == True and MSC_pausePlay == 'play' and PLR_deathFlag == False):
## Movement WAD
    if(p5.key=='w'):
      MSC_keyboardW = False
      if(PLR_fallCheck == True and player.action_state == 'jumping' and PLR_deathFlag == False): 
          if((PLR_currentCharacter == 'luna' and len(PLR_jumpCharges) < 1) or (PLR_currentCharacter == 'nox' and len(PLR_jumpCharges) < 3)):
            PLR_fallTimer = p5.millis()
          PLR_fallCheck = False
          player.action_state = 'falling'
          PLR_fallTimer = p5.millis()
    if(p5.key=='d'):
      MSC_keyboardD = False
      if(PLR_movingDirection == 'right'):
        PLR_runStopTimerCheck = 'right'
        PLR_runStopTimer = p5.millis()
      if(PLR_heldDirection == 'both'):
        PLR_xmoveTimer = p5.millis()
    if(p5.key=='a'):
      MSC_keyboardA = False
      if(PLR_movingDirection == 'left'):
        PLR_runStopTimerCheck = 'left'
        PLR_runStopTimer = p5.millis()
    if(p5.key=='a' or p5.key=='d'):
      if(PLR_grounded == True):
        if(player.footstep.isPlaying() == True):
          player.footstep.stop()
## Character Abilities
    if(p5.key==' ' and LUN_disableBoost == False):
      MSC_keyboardSpace = False
      if(RTH_noteFillEnd[3] == 'none' and RTH_noteEnd[3] == 'D' and RTH_startCheck_D == True):
        if(p5.width/2 >= RTH_noteEndx[3]-11 and p5.width/2 <= RTH_noteEndx[3]+11):
          RTH_noteFillEnd.pop(3)
          RTH_noteFillEnd.insert(3,'D')
          RTH_noteFillEndx.pop(3)
          RTH_noteFillEndx.insert(3,RTH_noteEndx[3])
          player.enterBoostBoosting()
          RTH_endCheck_D = True
        else:
          player.exitBoostStartup()
          RTH_startCheck_D == False
      if(RTH_noteFillEnd[2] == 'none' and RTH_noteEnd[2] == 'C' and RTH_startCheck_C == True):
        if(p5.width/2 >= RTH_noteEndx[2]-11 and p5.width/2 <= RTH_noteEndx[2]+11):
          RTH_noteFillEnd.pop(2)
          RTH_noteFillEnd.insert(2,'C')
          RTH_noteFillEndx.pop(2)
          RTH_noteFillEndx.insert(2,RTH_noteEndx[2])
          player.enterBoostBoosting()
          RTH_endCheck_C = True
        else:
          player.exitBoostStartup()
          RTH_startCheck_C == False
      if(RTH_noteFillEnd[1] == 'none' and RTH_noteEnd[1] == 'B' and RTH_startCheck_B == True):
        if(p5.width/2 >= RTH_noteEndx[1]-11 and p5.width/2 <= RTH_noteEndx[1]+11):
          RTH_noteFillEnd.pop(1)
          RTH_noteFillEnd.insert(1,'B')
          RTH_noteFillEndx.pop(1)
          RTH_noteFillEndx.insert(1,RTH_noteEndx[1])
          player.enterBoostBoosting()
          RTH_endCheck_B = True
        else:
          player.exitBoostStartup()
          RTH_startCheck_B == False
      if(RTH_noteFillEnd[0] == 'none' and RTH_noteEnd[0] == 'A' and RTH_startCheck_A == True):
        if(p5.width/2 >= RTH_noteEndx[0]-11 and p5.width/2 <= RTH_noteEndx[0]+11):
          RTH_noteFillEnd.pop(0)
          RTH_noteFillEnd.insert(0,'A')
          RTH_noteFillEndx.pop(0)
          RTH_noteFillEndx.insert(0,RTH_noteEndx[0])
          player.enterBoostBoosting()
          RTH_endCheck_A = True
        else:
          player.exitBoostStartup()
          RTH_startCheck_A == False
      
      if(RTH_noteEnd[0] == 'A' and RTH_noteEnd[1] == 'B' and RTH_noteEnd[2] == 'C' and RTH_noteEnd[3] == 'D'):
        pass
      elif(RTH_noteEnd[0] == 'A' and RTH_noteEnd[1] == 'B' and RTH_noteEnd[2] == 'C' and RTH_noteEnd[3] == 'none'):
        RTH_noteEnd.pop(3)
        RTH_noteEnd.insert(3,'D')
        RTH_noteEndx.pop(3)
        RTH_noteEndx.insert(3,p5.width/2)
        player.enterBoostBoosting()
      elif(RTH_noteEnd[0] == 'A' and RTH_noteEnd[1] == 'B' and RTH_noteEnd[2] == 'none' and RTH_noteEnd[3] == 'none'):
        RTH_noteEnd.pop(2)
        RTH_noteEnd.insert(2,'C')
        RTH_noteEndx.pop(2)
        RTH_noteEndx.insert(2,p5.width/2)
        player.enterBoostBoosting()
      elif(RTH_noteEnd[0] == 'A' and RTH_noteEnd[1] == 'none' and RTH_noteEnd[2] == 'none' and RTH_noteEnd[3] == 'none'):
        RTH_noteEnd.pop(1)
        RTH_noteEnd.insert(1,'B')
        RTH_noteEndx.pop(1)
        RTH_noteEndx.insert(1,p5.width/2)
        player.enterBoostBoosting()
      elif(RTH_noteEnd[0] == 'none' and RTH_noteEnd[1] == 'none' and RTH_noteEnd[2] == 'none' and RTH_noteEnd[3] == 'none'):
        RTH_noteEnd.pop(0)
        RTH_noteEnd.insert(0,'A')
        RTH_noteEndx.pop(0)
        RTH_noteEndx.insert(0,p5.width/2)
        player.enterBoostBoosting()
      else:
        LUN_boostState = 'none'


    
    if(p5.key=='s'):
      MSC_keyboardS = False
  
#Mouse Press:
def mousePressed(event):
  global PLR_hitCharge, PLR_deathFlag, MSC_mouseL, MSC_startedPlaying, MSC_pausePlay
  if(MSC_startedPlaying == True and MSC_pausePlay == 'play' and PLR_deathFlag == False):
    # if(p5.mouseButton == 'left'):
    #   MSC_mouseL = True
    #   if(PLR_currentCharacter == 'nox'):
    #     if(p5.mouseButton==p5.LEFT and len(PLR_hitCharge)>0):
    #       PLR_hitCharge.pop()
    pass
  if(MSC_startedPlaying == False and p5.mouseButton == 'left'):
    if(len(MSC_startScreen)==1):
      MSC_startedPlaying = True
      if(PLR_deathFlag == True):
        MSC_pausePlay = 'play'
        PLR_deathFlag = False
      resetGameToCheckpoint()
    elif(len(MSC_startScreen)==2):
      MSC_startScreen.pop()
    elif(len(MSC_startScreen)==3):
      MSC_startScreen.pop()
    elif(len(MSC_startScreen)==4):
      MSC_startScreen.pop()
    else:
      pass

#Mouse Release:
def mouseReleased(event):
  global MSC_mouseL
  if(MSC_startedPlaying == True and MSC_pausePlay == 'play' and PLR_deathFlag == False):
## Character Combat
    if(p5.mouseButton == 'left'):
      MSC_mouseL = False






# - - - - - - - - - - - - - - - - - - - - - - - - - - - (003 ENV - ENVIRONMENTS) - - - - - - - - - - - - - - - - - - - - - - - - - 
#Classes:
class EnvironmentMechanics(): # Mechanics applied to Environments
  def __init__(self, x=0, y=0, leftEdge = 0, rightEdge = 0, groundLength = 1, trackingSpeed = 0, plyrOnTileX = False, plyrOnTileY = False, plrGroundedFlag = False):
    self.x = x
    self.y = y
    self.leftEdge = leftEdge
    self.rightEdge = rightEdge
    self.groundLength = groundLength
    self.trackingSpeed = trackingSpeed 
    self.plyrOnTileX = plyrOnTileX # Checks if 'Player' is within ground width
    self.plyrOnTileY = plyrOnTileY # Checks if 'Player' is on top of ground
    self.plrGroundedFlag = plrGroundedFlag

# Moves environment according to 'Player' movement:
  def trackPlayer(self):
    if(MSC_startedPlaying == True and MSC_pausePlay == 'play' and PLR_deathFlag == False):
      if(PLR_grounded == True): # Env speed while 'Player' is grounded
        if(PLR_onWall == False):
          if(MSC_keyboardA == True and MSC_keyboardD == True):
            if(player.x >= (p5.width-MSC_xborder*1.5) and PLR_movingDirection == 'right'): # Grounded turnaround right>left
              self.x -= PLR_runStopSpeed * self.trackingSpeed/100
            if(player.x <= MSC_xborder and PLR_movingDirection == 'left'): # Grounded turnaround left>right
              self.x += PLR_runStopSpeed * self.trackingSpeed/100
          if(player.x <= MSC_xborder):
            if(PLR_movingDirection == 'left'):
              if(MSC_keyboardA == True and MSC_keyboardD == False): # Grounded left run
                self.x += PLR_runSpeed * self.trackingSpeed/100
              if(player.action_state == 'runStopL'): # Grounded left runstop
                self.x += PLR_runStopSpeed * self.trackingSpeed/100
            if(PLR_movingDirection == 'turnRight'):
              if(MSC_keyboardA == False and MSC_keyboardD == True): # Grounded left runstop while turning right
                self.x += PLR_runStopSpeed * self.trackingSpeed/100
          if(player.x >= (p5.width-MSC_xborder*1.5)):
            if(PLR_movingDirection == 'right'):
              if(MSC_keyboardA == False and MSC_keyboardD == True): # Grounded right run
                self.x -= PLR_runSpeed * self.trackingSpeed/100
              if(player.action_state == 'runStopR'): # Grounded right runstop
                self.x -= PLR_runStopSpeed * self.trackingSpeed/100
            if(PLR_movingDirection == 'turnLeft'):
              if(MSC_keyboardA == True and MSC_keyboardD == False): # Grounded right runstop while turning left
                self.x -= PLR_runStopSpeed * self.trackingSpeed/100
        if(player.y >= (p5.height-MSC_yborder) and fg_sect01_lava.y>520):
          self.y -= ENV_platformySpeed * self.trackingSpeed/100
        #if(player.y < MSC_yborder):
          #self.y += ENV_platformySpeed * self.trackingSpeed/100
          #player.y += ENV_platformySpeed/2 * self.trackingSpeed/100
          
      
      if(PLR_grounded == False): # Env speed while 'Player' is in the air
        if(PLR_onWall == False):
          if(player.x <= MSC_xborder):
            if(LUN_boostState == 'none' or LUN_boostState == 'startup'):
              if(PLR_movingDirection == 'left'):
                if(MSC_keyboardA == True and MSC_keyboardD == False): # Left jump
                  self.x += PLR_jumpSpeedx * self.trackingSpeed/100
                if(MSC_keyboardA == False and MSC_keyboardD == False): # Left jump w/ no right/left keys held
                  self.x += PLR_jumpSpeedx * self.trackingSpeed/100
              if(PLR_movingDirection == 'right'):
                if(MSC_keyboardD == True): # Left jump w/ right key held
                  self.x += PLR_jumpTurnSpeed * self.trackingSpeed/100
                if(PLR_AirTurnaround == True): # Left jump turnaround startup
                  self.x += PLR_jumpTurnSpeed*0.5 * self.trackingSpeed/100
              if(PLR_movingDirection == 'none'):
                if(PLR_initialJumpDirection != 'rightIdle' and PLR_initialJumpDirection != 'leftIdle'):
                  self.x += PLR_jumpTurnSpeed * self.trackingSpeed/100
            if(LUN_boostState == 'boosting'):
              self.x += 11 * self.trackingSpeed/100
            if(LUN_boostState == 'release'):
              self.x += LUN_boostReleaseSpeedx * self.trackingSpeed/100
          if(player.x >= (p5.width-MSC_xborder*1.5)):
            if(LUN_boostState == 'none' or LUN_boostState == 'startup'):
              if(PLR_movingDirection == 'right'):
                if(MSC_keyboardA == False and MSC_keyboardD == True): # Right jump
                  self.x -= PLR_jumpSpeedx * self.trackingSpeed/100
                if(MSC_keyboardA == False and MSC_keyboardD == False): # Right jump w/ no right/left keys held
                  self.x -= PLR_jumpSpeedx * self.trackingSpeed/100
              if(PLR_movingDirection == 'left' and PLR_initialJumpDirection != 'none'):
                if(MSC_keyboardA == True): # Right jump w/ left key held
                  self.x -= PLR_jumpTurnSpeed * self.trackingSpeed/100
                if(PLR_AirTurnaround == True): # Right jump turnaround startup
                  self.x -= PLR_jumpTurnSpeed*0.5 * self.trackingSpeed/100
              if(PLR_movingDirection == 'none'):
                if(PLR_initialJumpDirection != 'rightIdle' and PLR_initialJumpDirection != 'leftIdle'):
                  self.x -= PLR_jumpTurnSpeed * self.trackingSpeed/100
            if(LUN_boostState == 'boosting'):
              self.x -= 11 * self.trackingSpeed/100
            if(LUN_boostState == 'release'):
              self.x -= LUN_boostReleaseSpeedx * self.trackingSpeed/100
  
        #if(player.action_state == 'falling'):
          #if(player.y > MSC_yborder and fg_sect01_lava.y>520):
            #self.y -= PLR_fallSpeed * self.trackingSpeed/100
        if(player.y >= (p5.height-(MSC_yborder)) and fg_sect01_lava.y>520):
          self.y -= PLR_fallSpeed*0.35 * self.trackingSpeed/100
          if(LUN_boostState == 'release'):
            self.y -= LUN_boostReleaseSpeedy * self.trackingSpeed/100
            self.y += PLR_fallSpeed*0.5 * self.trackingSpeed/100
        if(player.y < MSC_yborder):
          self.y -= PLR_fallSpeed*0.35 * self.trackingSpeed/100
          if(LUN_boostState == 'boosting'):
            #self.y += 5 * self.trackingSpeed/100
            LUN_ydiff = LUN_boostGuidey - player.y
            for n in range(1,10,1):
              if(p5.millis()>LUN_boostTimer + 1000-100*(10/n)):
                LUN_boostSpeedy = (LUN_ydiff/(n*50))
            self.y += LUN_boostSpeedy * self.trackingSpeed/100
          if(LUN_boostState == 'release'):
            self.y += LUN_boostReleaseSpeedy*0.5 * self.trackingSpeed/100
          if(LUN_boostState == 'none'):
            if(player.action_state == 'jumping'):
              self.y += (PLR_jumpSpeedy) * self.trackingSpeed/100
        if(player.y < (p5.height-MSC_yborder) and player.action_state == 'falling' and fg_sect01_lava.y>520):
          if(LUN_boostState == 'release' or LUN_boostState == 'none'):
            self.y -= PLR_fallSpeed*0.5 * self.trackingSpeed/100
      
    if(PLR_deathFlag == True and PLR_onWall == False):
      if(player.x >= (p5.width-MSC_xborder*1.5)):
        if(PLR_movingDirection == 'right' and player.y < p5.height+player.LunaDeathR0.height/2):
          self.x -= 3 * self.trackingSpeed/100
      if(player.x <= MSC_xborder):
        if(PLR_movingDirection == 'left' and player.y < p5.height+player.LunaDeathR0.height/2):
          self.x += 3 * self.trackingSpeed/100

        
  # Defines the Ground space of an environment piece, which 'Player' can stand on:
  def createGround(self):
    global LUN_ydiff
    if(player.x >= self.leftEdge and player.x <= self.rightEdge):
      self.plyrOnTileX = True
    else:
      self.plyrOnTileX = False
    if(player.y >= self.y and player.y <= self.y+PLR_fallSpeedMax*2 and LUN_boostState != 'boosting'): # Snaps 'Player' on top of Platform if within platform's y threshold
      self.plyrOnTileY = True
    elif(player.y >= self.y and player.y <= self.y+PLR_fallSpeedMax*2 and LUN_boostState == 'boosting' and LUN_ydiff >= 0):
      self.plyrOnTileY = True
    else:
      self.plyrOnTileY = False
    if(self.plyrOnTileX == True and self.plyrOnTileY == True and PLR_deathFlag == False):
      self.plrGroundedFlag = True
      if(player.action_state == 'falling' and player.action_state != 'jumping'):
        player.y = self.y
      elif(player.action_state == 'idleR' or player.action_state == 'idleL' or player.action_state == 'running' or player.action_state == 'runStopR' or player.action_state == 'runStopL'):
        player.y = self.y
    else:
      self.plrGroundedFlag = False
    #if(self.plrGroundedFlag == True):


class FG_Platform(EnvironmentMechanics): 
  def __init__(self, x = 2000, y = 2000, leftEdge = 0, rightEdge = 0, groundLength = 1, trackingSpeed = 100, plyrOnTileX = False, plyrOnTileY = False, plrGroundedFlag = False):
    self.x = x
    self.y = y
    self.leftEdge = leftEdge
    self.rightEdge = rightEdge
    self.groundLength = groundLength
    self.trackingSpeed = trackingSpeed 
    self.plyrOnTileX = plyrOnTileX # Checks if 'Player' is within ground width
    self.plyrOnTileY = plyrOnTileY # Checks if 'Player' is on top of ground
    self.plrGroundedFlag = plrGroundedFlag
    self.PlatformLeft = p5.loadImage('ENV/ENV_Foreground/ENV_Foreground-PlatformLeftSection.png')
    self.PlatformMid = p5.loadImage('ENV/ENV_Foreground/ENV_Foreground-PlatformMidSection.png')
    self.PlatformRight = p5.loadImage('ENV/ENV_Foreground/ENV_Foreground-PlatformRightSection.png')
  def draw(self):
    p5.image(self.PlatformLeft, (self.x-self.PlatformLeft.width/2), self.y+843)
    p5.image(self.PlatformRight, (self.x+self.PlatformRight.width/2 + self.PlatformMid.width*(self.groundLength)), self.y+843)
    self.leftEdge = self.x - self.PlatformLeft.width + 10
    self.rightEdge = self.x + self.PlatformRight.width + self.PlatformMid.width*self.groundLength - 10
    for n in range(self.groundLength):
      p5.image(self.PlatformMid, (self.x+self.PlatformMid.width/2 + self.PlatformMid.width*n), self.y+843)
    self.createGround()
    self.trackPlayer()


class FG_Wall(EnvironmentMechanics):
  def __init__(self, x = 2000, y = 2000, leftEdge = 0, rightEdge = 0, groundLength = 1, wallHeight = 1, trackingSpeed = 100, plyrOnTileX = False, plyrOnTileY = False, plrGroundedFlag = False, plyrOnWall = False):
    self.x = x
    self.y = y
    self.leftEdge = leftEdge
    self.rightEdge = rightEdge
    self.groundLength = groundLength
    self.wallHeight = wallHeight
    self.trackingSpeed = trackingSpeed 
    self.plyrOnTileX = plyrOnTileX # Checks if 'Player' is within ground width
    self.plyrOnTileY = plyrOnTileY # Checks if 'Player' is on top of ground
    self.plrGroundedFlag = plrGroundedFlag
    self.plyrOnWall = plyrOnWall
    self.WallLeftBot = p5.loadImage('ENV/ENV_Foreground/ENV_Foreground-WallLeftBot.png')
    self.WallLeftMid = p5.loadImage('ENV/ENV_Foreground/ENV_Foreground-WallLeftMid.png')
    self.WallLeftTop = p5.loadImage('ENV/ENV_Foreground/ENV_Foreground-WallLeftTop.png')
    self.WallMidBot = p5.loadImage('ENV/ENV_Foreground/ENV_Foreground-WallMidBot.png')
    self.WallMidMid = p5.loadImage('ENV/ENV_Foreground/ENV_Foreground-WallMidMid.png')
    self.WallMidTop = p5.loadImage('ENV/ENV_Foreground/ENV_Foreground-WallMidTop.png')
    self.WallRightBot = p5.loadImage('ENV/ENV_Foreground/ENV_Foreground-WallRightBot.png')
    self.WallRightMid = p5.loadImage('ENV/ENV_Foreground/ENV_Foreground-WallRightMid.png')
    self.WallRightTop = p5.loadImage('ENV/ENV_Foreground/ENV_Foreground-WallRightTop.png')
    
  def draw(self):
    self.leftEdge = self.x - self.WallLeftTop.width
    self.rightEdge = self.x + self.WallRightTop.width + self.WallMidTop.width*self.groundLength
    p5.image(self.WallLeftBot, (self.x-self.WallLeftBot.width/2), (self.y+self.WallLeftBot.height/2))
    p5.image(self.WallLeftTop, (self.x-self.WallLeftTop.width/2), (self.y-self.WallLeftTop.height/2 - self.WallLeftMid.height*self.wallHeight))
    p5.image(self.WallRightBot, (self.x+self.WallRightBot.width/2 + self.WallMidBot.width*self.groundLength), (self.y+self.WallRightBot.height/2))
    p5.image(self.WallRightTop, (self.x+self.WallRightTop.width/2 + self.WallMidTop.width*self.groundLength), (self.y-self.WallRightTop.height/2 - self.WallRightMid.height*self.wallHeight))
    for i in range(self.groundLength):
      for n in range(self.wallHeight):
        p5.image(self.WallLeftMid, (self.x-self.WallLeftMid.width/2), (self.y-self.WallLeftMid.height/2 - self.WallLeftMid.height*n))
        p5.image(self.WallRightMid, (self.x+self.WallRightMid.width/2 + self.WallMidMid.width*self.groundLength), (self.y-self.WallRightMid.height/2 - self.WallRightMid.height*n))
        p5.image(self.WallMidBot, (self.x+self.WallMidBot.width/2 + self.WallMidBot.width*i), (self.y+self.WallMidBot.height/2))
        p5.image(self.WallMidTop, (self.x+self.WallMidTop.width/2 + self.WallMidTop.width*i), (self.y-self.WallMidTop.height/2 - self.WallMidMid.height*self.wallHeight))
        p5.image(self.WallMidMid, (self.x+self.WallMidMid.width/2 + self.WallMidMid.width*i), (self.y-self.WallMidMid.height/2 - self.WallMidMid.height*n))
    self.createGround()
    self.createWall()
    self.trackPlayer()
  
  def createGround(self):
    if(player.x >= self.leftEdge and player.x <= self.rightEdge):
      self.plyrOnTileX = True
    else:
      self.plyrOnTileX = False
    if(player.y >= (self.y-self.WallMidTop.height/2 - self.WallMidMid.height*self.wallHeight - 19) and player.y <= (self.y-self.WallMidTop.height/2 - self.WallMidMid.height*self.wallHeight)+PLR_fallSpeedMax*2 - 19): # Snaps 'Player' on top of Platform if within platform's y threshold
      self.plyrOnTileY = True
    elif(player.y >= (self.y-self.WallMidTop.height/2 - self.WallMidMid.height*self.wallHeight - 19) and player.y <= (self.y-self.WallMidTop.height/2 - self.WallMidMid.height*self.wallHeight)+PLR_fallSpeedMax*2 - 19 and LUN_boostState == 'boosting' and LUN_ydiff >= 0):
      self.plyrOnTileY = True
    else:
      self.plyrOnTileY = False
    if(self.plyrOnTileX == True and self.plyrOnTileY == True and PLR_deathFlag == False):
      self.plrGroundedFlag = True
      if(player.action_state == 'falling' and player.action_state != 'jumping'):
        player.y = self.y-self.WallMidTop.height/2 - self.WallMidMid.height*self.wallHeight - 19
      elif(player.action_state == 'idleR' or player.action_state == 'idleL' or player.action_state == 'running' or player.action_state == 'runStopR' or player.action_state == 'runStopL'):
        player.y = self.y-self.WallMidTop.height/2 - self.WallMidMid.height*self.wallHeight - 19
    else:
      self.plrGroundedFlag = False
  
  def createWall(self):
    global PLR_onWall
    if(player.x >= self.leftEdge-10 and player.x <= self.rightEdge+10 and player.y > (self.y-self.WallMidTop.height/2 - self.WallMidMid.height*self.wallHeight)+PLR_fallSpeedMax*3 - 19):
      if(player.x >= self.leftEdge-10 and player.x <= self.leftEdge + 100):
        #PLR_onWall = True
        self.plyrOnWall = True
        player.x = self.leftEdge-10
      elif(player.x <= self.rightEdge+10 and player.x >= self.rightEdge - 100):
        #PLR_onWall = True
        self.plyrOnWall = True
        player.x = self.rightEdge+10
    else:
      #PLR_onWall = False
      self.plyrOnWall = False
    if(fg_sect01_wall00.plyrOnWall == True or \
       fg_sect01_wall01.plyrOnWall == True or \
       fg_sect01_wall02.plyrOnWall == True):
      PLR_onWall = True
    else:
      PLR_onWall = False
      

class FG_Lava(EnvironmentMechanics):
  def __init__(self, x = 2000, y = 2000, leftEdge = 0, rightEdge = 0, groundLength = 1, trackingSpeed = 110, plyrOnTileX = False, plyrOnTileY = False):
    self.x = x
    self.y = y
    self.leftEdge = leftEdge
    self.rightEdge = rightEdge
    self.groundLength = groundLength
    self.trackingSpeed = trackingSpeed 
    self.plyrOnTileX = plyrOnTileX # Checks if 'Player' is within ground width
    self.plyrOnTileY = plyrOnTileY # Checks if 'Player' is on top of ground
    self.Lava01 = p5.loadImage('ENV/ENV_Foreground/ENV_Foreground-Lava01.png')
    self.Lava02 = p5.loadImage('ENV/ENV_Foreground/ENV_Foreground-Lava02.png')
  
  def draw(self):
    self.leftEdge = self.x - self.Lava01.width/2
    self.rightEdge = self.x + self.Lava01.width/2 + self.Lava01.width*(self.groundLength)
    if(MSC_pausePlay == 'play'):
      for n in range(self.groundLength):
        if(p5.millis() % 1000 < 500): 
          p5.image(self.Lava01,(self.x + self.Lava01.width*n),self.y-105)
        elif((p5.millis() % 1000 <= 1000) and (p5.millis() % 1000 > 499)):
          p5.image(self.Lava02,(self.x + self.Lava02.width*n),self.y-105)
    elif(MSC_pausePlay == 'pause'):
      for n in range(self.groundLength): 
        p5.image(self.Lava01,(self.x + self.Lava01.width*n),self.y-105)
    self.createGround()
    self.trackPlayer()
  
  def createGround(self): #polymorphism, changing createGround to set player to death state rather than grounded state
    global PLR_deathFlag, PLR_deathTimerCheck
    if(player.x >= self.leftEdge and player.x <= self.rightEdge):
      self.plyrOnTileX = True
    else:
      self.plyrOnTileX = False
    if(player.y >= self.y):
      self.plyrOnTileY = True
    else:
      self.plyrOnTileY = False
    if(self.plyrOnTileX == True and self.plyrOnTileY == True and MSC_startedPlaying == True):
      if(PLR_deathTimerCheck == False and PLR_deathFlag == False):
        PLR_deathTimerCheck = True
      PLR_deathFlag = True


class BG_Backdrop(EnvironmentMechanics): # Background assets that don't track player movement
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y
    self.BgBackdrop = p5.loadImage('ENV/ENV_Background/ENV_Background-SkyBackdrop.jpg')
  def draw(self):
    p5.image(self.BgBackdrop,p5.width/2,p5.height/2,)      

class BG_Stars(EnvironmentMechanics):
  def __init__(self, x=p5.width/2, y=(p5.height)/2, trackingSpeed=0.25):
    self.x = x
    self.y = y
    self.trackingSpeed = trackingSpeed
    self.BgStars = p5.loadImage('ENV/ENV_Background/ENV_Background-Stars.png')
  def draw(self):
    for n in range(5):
      p5.image(self.BgStars,(self.x + self.BgStars.width*n),270)
    self.trackPlayer()

class BG_City02(EnvironmentMechanics):
  def __init__(self, x=p5.width/2, y=(p5.height)/2, trackingSpeed=0.5):
    self.x = x
    self.y = y
    self.trackingSpeed = trackingSpeed
    self.BgCity02 = p5.loadImage('ENV/ENV_Background/ENV_Background-Cityline02.png')
  def draw(self):
    for n in range(5):
      p5.image(self.BgCity02,(self.x + self.BgCity02.width*n),270)
    self.trackPlayer()

class BG_CityLights(EnvironmentMechanics):
  def __init__(self, x=p5.width/2, y=(p5.height)/2, trackingSpeed=1.5):
    self.x = x
    self.y = y
    self.trackingSpeed = trackingSpeed
    self.BgCityLights = p5.loadImage('ENV/ENV_Background/ENV_Background-CityLightsBack.png')
  def draw(self):
    for n in range(5):
      p5.image(self.BgCityLights,(self.x + self.BgCityLights.width*n),270)
    self.trackPlayer()

class BG_City01(EnvironmentMechanics):
  def __init__(self, x=p5.width/2, y=(p5.height)/2, trackingSpeed=2):
    self.x = x
    self.y = y
    self.trackingSpeed = trackingSpeed
    self.BgCity = p5.loadImage('ENV/ENV_Background/ENV_Background-Cityline.png')
  def draw(self):
    for n in range(5):
      p5.image(self.BgCity,(self.x + self.BgCity.width*n),270)
    self.trackPlayer()


class PLR_BoostGuide(EnvironmentMechanics):
  def __init__(self, x = 0, y = 0, trackingSpeed = 100):
    self.x = x
    self.y = y
    self.trackingSpeed = trackingSpeed 
  def update(self):
    global MSC_keyboardSpaceRelease
    if(MSC_keyboardSpaceRelease == True):
      self.x = ENV_boostGuidex
      self.y = ENV_boostGuidey
      MSC_keyboardSpaceRelease = False
    self.trackPlayer()


class UI_TextInstructions(EnvironmentMechanics):
  def __init__(self, x = 0, y = 0, trackingSpeed = 100):
    self.x = x
    self.y = y
    self.trackingSpeed = trackingSpeed 
  def draw(self):
    p5.textFont(ui_pauseScreen.font_CocoSemilight)
    p5.textSize(13)
    p5.fill(255)
    p5.text("If you're feeling tired *lagging*, take a moment to breathe...it'll help your jumps.",self.x,self.y)
    p5.print('yo')
    #p5.text("It'll help your jumps.",500,434)
    self.trackPlayer()





# - - - - - - - - - - - - - - - - - - - - - - - - - - - (004 UI - INTERFACE) - - - - - - - - - - - - - - - - - - - - - - - - - 
#Classes:
class DirectionArrows:
  scale = 0.25
  def __init__(self):
    self.ArrowOff = p5.loadImage('UI/UI_DirectionArrows/UI_DirectionArrows-Off.png')
    self.ArrowOnL = p5.loadImage('UI/UI_DirectionArrows/UI_DirectionArrows-OnL.png')
    self.ArrowOnR = p5.loadImage('UI/UI_DirectionArrows/UI_DirectionArrows-OnR.png')
    self.ArrowOnU = p5.loadImage('UI/UI_DirectionArrows/UI_DirectionArrows-OnU.png')
  def draw(self):
    p5.image(self.ArrowOff, self.ArrowOff.width/2-130, self.ArrowOff.height/2-100, self.ArrowOff.width*self.scale, self.ArrowOff.height*self.scale)
    if(MSC_keyboardD == True):
      p5.image(self.ArrowOnR, self.ArrowOnR.width/2-130, self.ArrowOnR.height/2-100, self.ArrowOnR.width*self.scale, self.ArrowOnR.height*self.scale)
    if(MSC_keyboardA == True):
      p5.image(self.ArrowOnL, self.ArrowOnL.width/2-130, self.ArrowOnL.height/2-100, self.ArrowOnL.width*self.scale, self.ArrowOnL.height*self.scale)
    if(MSC_keyboardW == True):
      p5.image(self.ArrowOnU, self.ArrowOnU.width/2-130, self.ArrowOnU.height/2-100, self.ArrowOnU.width*self.scale, self.ArrowOnU.height*self.scale)


class TextOverlay:
  def __init__(self, x=100, y=330):
    self.x = x
    self.y = y
    self.font_Roboto = p5.loadFont('UI/UI_Fonts/Roboto-Black.ttf')
  def cursor(self):
    p5.fill(255)  
    p5.textFont(self.font_Roboto)
    p5.textSize(10)
    p5.noStroke()
    cursor_xy = (int(p5.mouseX), int(p5.mouseY))
    p5.text(cursor_xy, 30, 15)


class PausePlay:
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y
    self.font_CocoLight = p5.loadFont('UI/UI_Fonts/Cocogoose Pro Light-trial.ttf')
    self.font_CocoSemilight = p5.loadFont('UI/UI_Fonts/Cocogoose Pro Semilight-trial.ttf')
    #self.font_CocoThin = p5.loadFont('UI/UI_Fonts/Cocogoose Pro Thin-trial.ttf')
    #self.font_CocoUltralight = p5.loadFont('UI/UI_Fonts/Cocogoose Pro Ultralight-trial.ttf')
    self.font_Coco = p5.loadFont('UI/UI_Fonts/Cocogoose Pro-trial.ttf')
  def pause(self):
    global MSC_keyboardA, MSC_keyboardW, MSC_keyboardD, MSC_keyboardS, MSC_keyboardSpace, PLR_heldDirection, PLR_movingDirection, PLR_initialJumpDirection, LUN_boostState, PLR_fallSpeed, PLR_runSpeed, PLR_runStopSpeed, PLR_jumpSpeedx, PLR_jumpSpeedy, LUN_boostSpeedx, LUN_boostSpeedy, LUN_boostReleaseSpeedx, LUN_boostReleaseSpeedy, RTH_pauseBar
    if(MSC_pausePlay == 'play'):
      pass
    elif(MSC_pausePlay == 'pause' and MSC_startedPlaying == True):
    # Graphic:
    ## BG
      p5.fill(0,155)
      p5.rect(p5.width/2,p5.height/2,p5.width,p5.height)
      p5.fill(255)
      p5.noStroke()
      p5.textSize(30)
      p5.textFont(self.font_Coco)
      p5.text('- PAUSED -',p5.width/2,p5.height/2)
      p5.textFont(self.font_CocoSemilight)
      p5.textSize(10)
      p5.text('(press ESC to return)',p5.width/2,p5.height/2 + 30)
    # Gameplay:
    ## PLAYER
      player.x = MSC_pausePlayerX
      player.y = MSC_pausePlayerY
      player.action_state = MSC_pauseActState
      MSC_keyboardA = MSC_pauseKeyboardA
      MSC_keyboardW = MSC_pauseKeyboardW
      MSC_keyboardD = MSC_pauseKeyboardD
      MSC_keyboardS = MSC_pauseKeyboardS
      MSC_keyboardSpace = MSC_pauseKeyboardSpace
      PLR_heldDirection = MSC_pauseHeldDir
      PLR_movingDirection = MSC_pauseMovingDir
      PLR_initialJumpDirection = MSC_pauseInitialJumpDir
      PLR_runStopTimerCheck = MSC_pauseRunStopTimerCheck
      LUN_boostState = MSC_pauseLunBoostState
      PLR_fallSpeed = 0
      PLR_runSpeed = 0
      PLR_runStopSpeed = 0
      PLR_jumpSpeedx = 0
      PLR_jumpSpeedy = 0
      LUN_boostSpeedx = 0
      LUN_boostSpeedy = 0
      LUN_boostReleaseSpeedx = 0
      LUN_boostReleaseSpeedy = 0
      RTH_pauseBar = True


class DialogueOverlay:
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y
    self.DialogueBase01 = p5.loadImage('UI/UI_DialogueOverlay/UI_DialogueOverlay-Base01.png')
    self.DialogueBase02 = p5.loadImage('UI/UI_DialogueOverlay/UI_DialogueOverlay-Base02.png')
    self.DialogueSmile01 = p5.loadImage('UI/UI_DialogueOverlay/UI_DialogueOverlay-Smile01.png')
    self.DialogueSmile02 = p5.loadImage('UI/UI_DialogueOverlay/UI_DialogueOverlay-Smile02.png')
    self.font_Coco = p5.loadFont('UI/UI_Fonts/Cocogoose Pro-trial.ttf')
  def startScreen(self):
    if(MSC_startedPlaying == False):
      if(len(MSC_startScreen) == 4):
        if(p5.millis() % 1000 < 500): 
          p5.image(self.DialogueSmile01,p5.width/2,p5.height/2)
        elif((p5.millis() % 1000 <= 1000) and (p5.millis() % 1000 > 499)):
          p5.image(self.DialogueSmile02,p5.width/2,p5.height/2)
        p5.textFont(self.font_Coco)
        p5.textSize(13)
        p5.noStroke()
        p5.text('Hi! Welcome to StarStruck,',500,414)
        p5.text('a rhythm-platformer!',500,434)
      elif(len(MSC_startScreen) == 3):
        if(p5.millis() % 1000 < 500): 
          p5.image(self.DialogueBase01,p5.width/2,p5.height/2)
        elif((p5.millis() % 1000 <= 1000) and (p5.millis() % 1000 > 499)):
          p5.image(self.DialogueBase02,p5.width/2,p5.height/2)
        p5.textFont(self.font_Coco)
        p5.textSize(13)
        p5.text("The goal's simple: run, jump, and",500,414)
        p5.text('boost your way through to the end.',500,434)
      elif(len(MSC_startScreen) == 2):
        if(p5.millis() % 1000 < 500): 
          p5.image(self.DialogueBase01,p5.width/2,p5.height/2)
        elif((p5.millis() % 1000 <= 1000) and (p5.millis() % 1000 > 499)):
          p5.image(self.DialogueBase02,p5.width/2,p5.height/2)
        p5.textFont(self.font_Coco)
        p5.textSize(10)
        p5.text("...",500,424)
      elif(len(MSC_startScreen) == 1):
        if(p5.millis() % 1000 < 500): 
          p5.image(self.DialogueSmile01,p5.width/2,p5.height/2)
        elif((p5.millis() % 1000 <= 1000) and (p5.millis() % 1000 > 499)):
          p5.image(self.DialogueSmile02,p5.width/2,p5.height/2)
        p5.textFont(self.font_Coco)
        p5.textSize(10)
        p5.text("..and don't let me die!",500,424)



class RhythmBar:
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y
    self.Bar = p5.loadImage('UI/UI_RhythmBar/UI_RhythmMeter-MeterV2.png')
    self.GridMark = p5.loadImage('UI/UI_RhythmBar/UI_RhythmMeter-GridSingle.png')
    self.track01 = p5.loadSound('SFX/Music/City Pop X 80s Funk Type Beat - .mp3')
    self.beat01a = p5.loadSound('SFX/Movement/Jumping/sfx_movement_jump9_landing.wav')
    self.beat01b = p5.loadSound('SFX/Movement/Jumping/space shield sounds - 1.wav')
    self.beat02a = p5.loadSound('SFX/Movement/Running/sfx_movement_footsteps1b.wav')
    self.beat02b = p5.loadSound('SFX/Movement/part.wav')
    self.beat02c = p5.loadSound('SFX/Movement/magnet_start.wav')
    
  def draw(self):
    if(RTH_disableBar == False):
      p5.image(self.Bar,p5.width/2,38)
      for n in range(len(RTH_gridMarkx)):
        p5.image(self.GridMark,RTH_gridMarkx[n],43)
    self.barGridLoop()

  def playBaseTrack(self):
    global RTH_trackBPM, RTH_beatTimer, RTH_beatCount, RTH_barSpeedx
    if(RTH_trackPlaying == 'track01'):
      RTH_trackBPM = 95
      RTH_barSpeedx = 0.5
      if(PLR_deathFlag == True):
        self.track01.rate(0.5)
        RTH_trackBPM = RTH_trackBPM/2
        RTH_barSpeedx = RTH_barSpeedx/2
      elif(PLR_deathFlag == False):
        self.track01.rate(1)
      if(MSC_startedPlaying == True):
        self.track01.playMode('untilDone')
        self.track01.setVolume(0.02)
        self.track01.loop()
      if(MSC_pausePlay == 'pause' and self.track01.isPlaying()):
        self.track01.pause()
      elif(MSC_pausePlay == 'play' and self.track01.isPaused()):
        self.track01.play()
    else:
      self.track01.stop()
    if(RTH_trackPlaying == 'track00' and RTH_pauseBar == False):
      RTH_trackBPM = 110
      RTH_barSpeedx = 0.5
      if(p5.millis() >= RTH_beatTimer + 500/(RTH_trackBPM/120)):
        if(len(RTH_beatCount)==3):
          RTH_beatCount.pop()
          RTH_beatCount.pop()
          RTH_beatCount.pop()
          pass
        elif(len(RTH_beatCount)==2):
          RTH_beatCount.append(2)
          self.beat02a.setVolume(0.04)
          self.beat02a.play()
          self.beat02b.setVolume(0.01)
          self.beat02b.play()
          self.beat02c.setVolume(0.01)
          self.beat02c.play()
        elif(len(RTH_beatCount)==1):
          RTH_beatCount.append(2)
          self.beat01a.setVolume(0.1)
          self.beat01a.play()
          self.beat01b.setVolume(0.002)
          self.beat01b.play()
        elif(len(RTH_beatCount)==0):
          RTH_beatCount.append(1)
          self.beat01a.setVolume(0.1)
          self.beat01a.play()
          self.beat01b.setVolume(0.002)
          self.beat01b.play()
        RTH_beatTimer = p5.millis()
    else:
      RTH_beatTimer = 0
            
  def barGridLoop(self):
    global RTH_gridmarkx, RTH_notex
    if(RTH_disableBar == False and RTH_pauseBar == False):
      for n in range(len(RTH_gridMarkx)):
        RTH_gridMarkx[n] -= RTH_barSpeedx
        if(RTH_gridMarkx[n] < p5.width/2-self.Bar.width/2):
          RTH_gridMarkx[n] += self.Bar.width


class RhythmNotes:
  def __init__(self, startx=0, endx=0, y=43):
    self.startx = startx
    self.endx = endx
    self.y = y
    self.NoteEmpty = p5.loadImage('UI/UI_RhythmBar/UI_RhythmMeter-NoteEmpty.png')
    self.NoteFilled = p5.loadImage('UI/UI_RhythmBar/UI_RhythmMeter-NoteFilled.png')
    
  def draw(self):
    if(RTH_disableBar == False):
      for n in range(len(RTH_noteStart)):
        p5.image(self.NoteEmpty,RTH_noteStartx[n],self.y)
      for n in range(len(RTH_noteEnd)):
        p5.image(self.NoteEmpty,RTH_noteEndx[n],self.y)
        p5.fill(222,237,255,80)
        p5.noStroke()
        if(RTH_noteEndx[n] > RTH_noteStartx[n] and RTH_noteEndx[n] > -1100):
          p5.rect((RTH_noteEndx[n]+RTH_noteStartx[n])/2,41,(RTH_noteEndx[n]-11)-(RTH_noteStartx[n]+11),3)  
      for n in range(len(RTH_noteFillStart)):
        p5.image(self.NoteFilled,RTH_noteFillStartx[n],self.y)
      for n in range(len(RTH_noteFillEnd)):
        p5.image(self.NoteFilled,RTH_noteFillEndx[n],self.y)
        p5.fill(222,237,255,80)
        p5.noStroke()
        if(RTH_noteFillEndx[n] > RTH_noteFillStartx[n] and RTH_noteFillEndx[n] > -1100):
          p5.rect((RTH_noteFillEndx[n]+RTH_noteFillStartx[n])/2,41,(RTH_noteFillEndx[n]-11)-(RTH_noteFillStartx[n]+11),3)  
      self.barNoteLoop()
        
  def barNoteLoop(self):
    global RTH_startCheck_D, RTH_startCheck_C, RTH_startCheck_B, RTH_startCheck_A
    if(RTH_disableBar == False and RTH_pauseBar == False):
      for n in range(len(RTH_noteStartx)):
        if(RTH_noteStartx[n] > -1100):
          RTH_noteStartx[n] -= RTH_barSpeedx
          if(RTH_noteStartx[n] < p5.width/2-ui_rhythmBar.Bar.width/2):
            RTH_noteStartx[n] += ui_rhythmBar.Bar.width
      for n in range(len(RTH_noteEndx)):
        if(RTH_noteStartx[n] > -1100):
          RTH_noteEndx[n] -= RTH_barSpeedx
          if(RTH_noteEndx[n] < p5.width/2-ui_rhythmBar.Bar.width/2 ):
            RTH_noteEndx[n] += ui_rhythmBar.Bar.width
      for n in range(len(RTH_noteFillStartx)):
        RTH_noteFillStartx[n] -= RTH_barSpeedx
        if(RTH_noteFillStartx[n] < p5.width/2-ui_rhythmBar.Bar.width/2):
          RTH_noteFillStartx.pop(n)
          RTH_noteFillStartx.insert(n,-110)
      for n in range(len(RTH_noteFillEndx)):
        RTH_noteFillEndx[n] -= RTH_barSpeedx
        if(RTH_noteFillEndx[n] < p5.width/2-ui_rhythmBar.Bar.width/2):
          RTH_noteFillEndx.pop(n)
          RTH_noteFillEndx.insert(n,-110)

      if(RTH_noteFillStart[0] == 'A'):
        if(RTH_noteEndx[0]+11 <= p5.width/2 and RTH_endCheck_A == False):
          RTH_noteFillStart.pop(0)
          RTH_noteFillStart.insert(0,'none')
          RTH_startCheck_A = False
      if(RTH_noteFillStart[1] == 'B'):
        if(RTH_noteEndx[1]+11 <= p5.width/2 and RTH_endCheck_B == False):
          RTH_noteFillStart.pop(1)
          RTH_noteFillStart.insert(1,'none')
          RTH_startCheck_B = False
      if(RTH_noteFillStart[2] == 'C'):
        if(RTH_noteEndx[2]+11 <= p5.width/2 and RTH_endCheck_C == False):
          RTH_noteFillStart.pop(2)
          RTH_noteFillStart.insert(2,'none')
          RTH_startCheck_C = False
      if(RTH_noteFillStart[3] == 'D'):
        if(RTH_noteEndx[3]+11 <= p5.width/2 and RTH_endCheck_D == False):
          RTH_noteFillStart.pop(3)
          RTH_noteFillStart.insert(3,'none')
          RTH_startCheck_D = False





# - - - - - - - - - - - - - - - - - - - - - - - - - - - (005 MAIN BODY) - - - - - - - - - - - - - - - - - - - - - - - - - 
# Instances:
## ENVIRONMENTS
bg_extBackdrop = BG_Backdrop()
bg_stars = BG_Stars()
bg_city02 = BG_City02()
bg_cityLights = BG_CityLights()
bg_city01 = BG_City01()
fg_sect01_platform01 = FG_Platform(groundLength = 4)
fg_sect01_platform02 = FG_Platform(groundLength = 1)
fg_sect01_platform03 = FG_Platform(groundLength = 5)
fg_sect01_wall00 = FG_Wall(groundLength = 3, wallHeight = 5)
fg_sect01_wall01 = FG_Wall(groundLength = 2, wallHeight = 5)
fg_sect01_wall02 = FG_Wall(groundLength = 4, wallHeight = 2)
fg_sect01_lava = FG_Lava(groundLength = 15)

## UI
ui_directionArrows = DirectionArrows()
ui_cursor = TextOverlay()
ui_sect01_textInstructions = UI_TextInstructions()
ui_pauseScreen = PausePlay()
ui_dialogue = DialogueOverlay()
ui_rhythmBar = RhythmBar()
ui_rhythmNotes = RhythmNotes()

## CHARACTERS
player = Player()
plr_boostGuide = PLR_BoostGuide()


# Setup:
def setup():
  p5.createCanvas(960, 540)
  p5.imageMode(p5.CENTER)
  p5.textAlign(p5.CENTER, p5.CENTER)
  p5.rectMode(p5.CENTER)
  print('CONTROLS: W / A / D for movement. Hold SPACE to charge boost, then aim mouse and release SPACE. F to change track to metronome. ESC to pause.')
  print('                                  ^^SPACE and F only work after you reach a certain platform. Or, press T to access early.')
  print('When you Boost, you create a looping note. After 4 Boosts, can only boost again during those notes. Goal is to create a game that has you use abilities to create your own songs.')
  print('artwork by me, music by emilybeats, various sfx files by rubberduck/legoluft/Little Robot Sound Factory/bart/p0ss/Juhani Junkala/yd (OpenGameArt.org)')
def draw():
  p5.background(255)
  
# Environment:
  bg_extBackdrop.draw()
  bg_stars.draw()
  bg_city02.draw()
  bg_cityLights.draw()
  bg_city01.draw()
  fg_sect01_platform01.draw()
  fg_sect01_platform02.draw()
  fg_sect01_platform03.draw()
  fg_sect01_wall00.draw()
  fg_sect01_wall01.draw()
  fg_sect01_wall02.draw()
  fg_sect01_lava.draw()
  
# UI:
  ui_directionArrows.draw()
  ui_sect01_textInstructions.draw()
  ui_cursor.cursor()
  
# Characters:
  plr_boostGuide.update()
  player.draw()
  #player.deathState()
  
# UI2:
  ui_rhythmBar.draw()
  ui_rhythmBar.playBaseTrack()
  ui_rhythmNotes.draw()
  ui_pauseScreen.pause()
  ui_dialogue.startScreen()
