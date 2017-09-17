import buildIarProj

if __name__ == '__main__':
    target_dir = r"E:\SmithMedical\trunk"

    target_safety = target_dir + "\\" + "SafetyFirmware\IAR_Project\GrasebyC9_Safety.ewp"

    target_main_boot = target_dir + "\\" + "MainBootloader\IAR_project\GrasebyC9_Main_Bootloader.ewp"
    target_main = target_dir + "\\" + "MainFirmware\IAR_project\GrasebyC9_Main.ewp"

    target_ui_boot = target_dir + "\\" + "UIBootloader\IAR_project\GrasebyC9_UI_Bootloader.ewp"
    target_ui_gui = target_dir + "\\" + "UIFirmware\Lib\\uC-GUI\IAR_project\\uC-GUI.ewp"
    target_ui_lib = target_dir + "\\" + "UIFirmware\Lib\libqrencode\IAR_project\libqrencode.ewp"
    target_ui = target_dir + "\\" + "UIFirmware\IAR_project\GrasebyC9_UI.ewp"

    buildIarProj.build(target_safety, "Debug")
    # buildIarProj.build(target_main_boot, "Release")
    buildIarProj.build(target_main, "Release")
    # buildIarProj.build(target_ui_boot, "Release")
    # buildIarProj.build(target_ui_gui, "Release")
    # buildIarProj.build(target_ui_lib, "Release")
    # buildIarProj.build(target_ui, "Release")