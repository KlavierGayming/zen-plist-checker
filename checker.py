import datetime

def printlog(text):
    print(text)
    log += "\n" + text

def check(p):
    log = ""
    booterquirks = p["Booter"]["Quirks"]
    count = 0

    # Show SMBIOS. Not checking anything, just needed to know...

    print("\nSMBIOS is: " + p["PlatformInfo"]["Generic"]["SystemProductName"] + " Check if correct according to hw configuration and OS version.")
    print("Current Boot Arguments: " + p["NVRAM"]["Add"]["7C436110-AB2A-4BBB-A880-FE41995C9F82"]["boot-args"] + "\n\n")

    log += "SMBIOS is: " + p["PlatformInfo"]["Generic"]["SystemProductName"] + " Check if correct according to hw configuration and OS version.\nCurrent Boot Arguments: " + p["NVRAM"]["Add"]["7C436110-AB2A-4BBB-A880-FE41995C9F82"]["boot-args"] + "\n\n"

    #checks booter quirks section. in this file for single reason of the main script looking tidier, lmao

    if booterquirks == True:
        printlog("Booter > Quirks > DevirtualiseMmio is set to TRUE when it should be FALSE.")
        count += 1

    if booterquirks["EnableWriteUnprotector"] == True:
        printlog("Booter > Quirks > EnableWriteUnprotector is set to TRUE when it should be FALSE")
        count += 1

    if booterquirks["RebuildAppleMemoryMap"] == False:
        printlog("Booter > Quirks > RebuildAppleMemoryMap is set to FALSE when it should be TRUE")
        count += 1
    
    if booterquirks["ResizeAppleGpuBars"] == 0:
        printlog("ReBar is set to 0. Check if ReBar is enabled in BIOS.")

    if booterquirks["SetupVirtualMap"] == False:
        printlog("Booter > Quirks > SetupVirtualMap is set to FALSE. If on X570, B550, A520, X470 or B450 you can try to leave this disabled. If not, should be TRUE")
        count += 1

    if booterquirks["SyncRuntimePermissions"] == False:
        printlog("Booter > Quirks > SyncRuntimePermissions is FALSE when it should be TRUE.")
        count += 1

    # Check kernel emulate and patch core count.
    
    if p["Kernel"]["Emulate"]["DummyPowerManagement"] == False:
        printlog("Kernel > Emulate > DummyPowerManagement is set to FALSE when it should be TRUE.")
        count += 1

    kpatch = p["Kernel"]["Patch"]


    i = 0
    while i < 4:
        printlog(str(kpatch[i]["Replace"]) + " Is replace value of patch " + str(i) + ". Check if this is correct.")
        i += 1

    # Kernel quirks check. God this is an inefficient way of doing this and it is annoying.
    
    kquirks = p["Kernel"]["Quirks"]

    if kquirks["PanicNoKextDump"] == False:
        printlog("Kernel > Quirks > PanicNoKextDump is set to FALSE when it should be TRUE.")
        count += 1
    
    if kquirks["PowerTimeoutKernelPanic"] == False:
        printlog("Kernel > Quirks > PowerTimeoutKernelPanic is set to FALSE when it should be TRUE.")
        count += 1

    if kquirks["ProvideCurrentCpuInfo"] == False:
        printlog("Kernel > Quirks > ProvideCurrentCpuInfo is set to FALSE when it should be TRUE.")
        count += 1

    if kquirks["XhciPortLimit"] == True:
        printlog("Kernel > Quirks > XhciPortLimit is set to TRUE. Check with plist creator what version they're running. If above 11.3, disable.")
        count += 1

    
    # Misc debug and security.

    miscdebug = p["Misc"]["Debug"]

    if miscdebug["AppleDebug"] == False:
        printlog("Misc > Debug > AppleDebug is set to FALSE, when it should be TRUE.")
        count += 1


    if miscdebug["ApplePanic"] == False:
        printlog("Misc > Debug > ApplePanic is set to FALSE, when it should be TRUE.")
        count += 1


    if miscdebug["DisableWatchDog"] == False:
        printlog("Misc > Debug > DisableWatchDog is set to FALSE, when it should be TRUE.")
        count += 1


    if miscdebug["Target"] != 67:
        printlog("Misc > Debug > Target isn't set to 67. Set to 67 for debug logs.")
        count += 1



    miscsecurity = p["Misc"]["Security"]

    if miscsecurity["AllowSetDefault"] == False:
        printlog("Misc > Security > AllowSetDefault is set to FALSE when it should be TRUE.")
        count += 1


    if miscsecurity["BlacklistAppleUpdate"] == False:
        printlog("Misc > Security > BlacklistAppleUpdate is set to FALSE when it should be TRUE.")
        count += 1


    if miscsecurity["ScanPolicy"] != 0:
        printlog("Misc > Security > ScanPolicy should be set to 0.")
        count += 1


    if miscsecurity["SecureBootModel"] != "Default":
        printlog("SecureBootModel isn't default. Current value is " + miscsecurity["SecureBootModel"] + ". Check if it is correct with the SMBIOS or can be disabled.")
        count += 1


    if miscsecurity["Vault"] != "Optional":
        printlog("Vault isn't set to optional. Check if vault is provided and everything is signed properly.")
        count += 1


    # NVRAM.

    if p["NVRAM"]["Add"]["7C436110-AB2A-4BBB-A880-FE41995C9F82"]["run-efi-updater"] == True:
        printlog("NVRAM > Add > 7... > run-efi-updater is set to TRUE when it should be FALSE.")
        count += 1

    time = datetime.datetime.now().strftime(" %d-%m-%Y %H:%M:%S ")
    logtxt = open("check" + str(time) + ".txt", "w")
    logtxt.write(log)
    logtxt.close()

    printlog("Finished config.plist sanity check. Found " + str(count) + " issues. Saved to text file in opened terminal dir.")


    # This is the most overly annoying to write way i've ever done anything. At least quicker than manually checking every time. This code is an eyesore though.
    