#Top Level
if __name__ == '__main__':
    # TODO: Launch control, motor, sensor modules.
    import control_module.WASD_control as control
    controller = control.WASD_control()
    while(1):
        a = controller.getch()
