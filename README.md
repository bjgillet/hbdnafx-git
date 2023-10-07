# hbdnafx-git

Open Source Software to manage and edit Harley Benton DNAfx-git guitar multieffect

## Introduction and background

### About the device

Harley Benton DNAfx-git is a cheap but cool guitar multieffect.
It may provide up to 200 presets, each with a chain of 9 effects, amps and cab simulations.
thse are of good unit quality.

It comes with an integrated expression pedal, for controlling either an effect (ie. Wah) or Volume.
Factory presets are not all good, but they can be easily edited and some are cool anyway.

All in all I think that for the very low price it is a very good device with a very small footprint.

### About the free software Harley Benton provide

The edition software runs only on Windows or Mac, and has a lot of limitations.
- On Windows  admin rights are mandatory. That is just not possible, especially on Windows,. (suicide incitation ?)
- It cannot be used with device off-line.
- Rearranging effects order is painfull.
- Updating a preset require full import of the preset, going through disk save/re-load.
- It is not possible to prepare and save one-shot specific presets ranges (ie. having a list a Jazz/Blues presets pre-defined and saved one shot to device at a dedicated bank range).
- Device documentation is awfull. The software does not have any.
- ,.

Harley Benton is a music instruments and device producer, they have no dedicated software engineering department and experience and very probably used a contractor one shot.<br>
Therefore, I cannot really reproach them the Software issues, especially as they build pretty good (even if inexpensive) devices and guitars.<br>

### About this Project

This project intends to create a Python / GTK+ software, initially on Linux, to address those issues (Security, Functionnalities, etc,.).<br>
Theoretically, adopting it to Mac or even Windows should not be an issue (Python is multi-platform) but those OS specificities in terms of security (USB rw access) will require some spesific settings.

As in a device discovery phasis, the following process have been adopted :
1. Discovery by analysis. Discovery documentation creation.
2. Validation of discovered items by unit test codes - discovery documentation updates if required.
3. Publication of codes and dedicated doc.

## Project status at October 3, 2023.

This project is at early stage.<br>

Preset JSON and full backup binary files have been decoded and understood at about 90%.
USB protocol is currently understood at about 60 %.<br>

Items published so far :
- USB device discovery (doc/01_QualifyingtheUSBdeviceonLinux.pdf)
- System and Security constaints and setup.(doc/02_SystemandSecuritysettings.pdf)
- Device file discovery .(doc/03_DNAfx-git Files data structures.pdf)

To come next :

- Initial python classes for data (HbData, Effect) and their data configuration file (hb_data.json). (with test code)
- Documentation of initial classes and data structures within hbdna-edit.

Published documentation is accessible from [this index](./doc/00_INTRO_INDEX.md)
