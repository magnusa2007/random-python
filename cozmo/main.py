import pygame,pycozmo,time

size = 2

cozmo = pycozmo.Client()
cozmo.start()
cozmo.connect()
time.sleep(1)
cozmo.enable_camera(enable=True, color=False)
angle = (pycozmo.robot.MAX_HEAD_ANGLE.radians - pycozmo.robot.MIN_HEAD_ANGLE.radians) / 2.0
cozmo.set_head_angle(angle)
cozmo.set_volume(65535)
text = {}
def Main():
    pygame.init()
    pygame.joystick.init()
    surface = pygame.display.set_mode((320*size, 240*size)) 
    pygame.display.set_caption('Cozmo')
    clock = pygame.time.Clock()
    joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
    font = pygame.font.Font('freesansbold.ttf', 16)
    text[1] = font.render(f'power: {cozmo.battery_voltage}' , True, (0, 255, 0) , (0, 0, 128))
    surface.blit(pygame.transform.scale(pygame.image.load('camera.png'),(320*size,240*size)),(0,0))

    x = 0
    y = 0
    head = 0.5
    speedboost = 1
    light = False
    def on_camera_image(cozmo, image):
        image.save("camera.png", "PNG")
        surface.blit(pygame.transform.scale(pygame.image.load('camera.png'),(320*size,240*size)),(0,0))
        
    while True:
        clock.tick(10)
        for event in pygame.event.get():    
            #print(pygame.event.event_name(event.type))
            if event.type == pygame.QUIT:
                cozmo.disconnect() 
                pygame.quit()  
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    cozmo.drive_wheels(lwheel_speed=50.0, rwheel_speed=50.0, duration=2.0)
                elif event.key == pygame.K_t:
                    print('> ')
                    eval(input())

            elif event.type == pygame.JOYAXISMOTION:
                if event.axis <= 2: #WHEELS
                    if event.axis == 1:
                        y = -event.value
                    elif event.axis == 0:
                        x = -event.value
                    if abs(x)+abs(y) > 0.1:
                        cozmo.drive_wheels(lwheel_speed=(y-x)*100*speedboost, rwheel_speed=(y+x)*100*speedboost)
                    else:
                        cozmo.drive_wheels(lwheel_speed=0, rwheel_speed=0)

                elif event.axis == 3: # HEAD
                    if abs(event.value) > 0.05:
                        head=head+0.1*-event.value
                        if head > 1:
                            head = 1
                        elif head < 0:
                            head = 0
                        cozmo.set_head_angle((pycozmo.MAX_HEAD_ANGLE.radians-pycozmo.MIN_HEAD_ANGLE.radians)*(-head)+(pycozmo.MIN_HEAD_ANGLE.radians))
                        cozmo.move_head(round(-event.value*2,2))
                    else:
                        cozmo.move_head(0)

                elif event.axis in [4, 5]: #LIFT
                    if event.value > -0.95:
                        cozmo.move_lift((event.axis-4.5)*(event.value+1)*speedboost)
                    else:
                        cozmo.move_lift(0)
            elif event.type == pygame.JOYBUTTONDOWN:
                if event.button == 3:
                    light = not light
                    cozmo.set_head_light(light)
            elif event.type == pygame.JOYHATMOTION:
                speedboost=speedboost+event.value[1]


        cozmo.add_handler(pycozmo.event.EvtNewRawCameraImage, on_camera_image, one_shot=True)
        text[1] = font.render(f'Power: {round(cozmo.battery_voltage,5)}' , True, (0, 255, 0))
        text[2] = font.render(f'Speed: {speedboost}' , True, (255, 255, 255))
        surface.blit(text[1],(0,0))
        surface.blit(text[2],(0,240*size-25))
        pygame.display.update()  


        
    

