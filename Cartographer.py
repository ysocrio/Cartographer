#Top Level
if __name__ == '__main__':
    # TODO: Launch control, motor, sensor modules.
    import control_module.WASD_control as WASD_control
    controller = WASD_control()
    while(1):
        print(controller.getch())
