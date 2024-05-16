
#!/usr/bin/env python3

# Import the subprocess and time modules
import subprocess
import time

# List of commands to run
commands = [
    # Run the Micro XRCE-DDS Agent
    "MicroXRCEAgent udp4 -p 8888",

    # Run the PX4 SITL simulation
    "cd && cd ~/PX4-Autopilot && PX4_GZ_WORLD=default PX4_GZ_MODEL_POSE='-13,0,0,0,0,0' PX4_SIM_MODEL=gz_x500_depth ./build/px4_sitl_default/bin/px4",

    # Run QGroundControl
    "cd && cd QGroundControl.AppImage && ./QGroundControl.AppImage"
]

# Loop through each command in the list
for command in commands:
    # Each command is run in a new tab of the gnome-terminal
    subprocess.run(["gnome-terminal", "--tab", "--", "bash", "-c", command + "; exec bash"])
    
    # Pause between each command
    time.sleep(1)
