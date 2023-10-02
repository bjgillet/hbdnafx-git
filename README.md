# hbdnafx-git

Open Source Software to manage and edit Harley Benton DNAfx-git guitar multieffect

## Introduction and background
Harley Benton DNAfx-git is a cheap but cool guitar multieffect.
It may provide up to 200 presets, each with a chain of 9 effects, amps and cab simulations.
thse are of good unit quality.

It comes with an integrated expression pedal, for controlling either an effect (ie. Wah) or Volume.
Default presets are not all good, but there are some that are cool.
All in all I think that for the very low price it is a very good device with a very small footprint.

However, the edition software runs only on Windows or Mac, and has a lot of limitations.
- On Windows it admin rights are mandatory. That is just not possible, especially on Windows... (suicide incitation ?)
- It cannot be used with device off-line.
- Rearranging effects order is painfull.
- Updating a preset require full import of the preset, going through disk save/re-load.
- It is not possible to prepare and save one-shot specific presets ranges (ie. having a list a Jazz/Blues presets pre-defined and saved one shot to device at a dedicated bank range).
- Device documentation is awfull. The software does not have any.
- ...

Harley Benton is a music instruments and device producer, they have no dedicated software engineering department and experience and very probably used a contractor one shot.<br>
Therefore, I cannot really reproach them the Software issues, especially as they build pretty good (even if inexpensive) devices and guitars.<br>
This project intends to create a Python / GTK+ software, initially on Linux, to address those issues (Security, Functionnalities, etc...).<br>
Theoretically, adopting it to Mac or even Windows should not be an issue (Python is multi-platform) but those OS specificities in terms of security (USB rw access) will require some spesific settings.

## Project status at October 2, 2023.
This project is at early stage.<br>
Preset JSON and binary files have been decoded and understood at about 90%.

USB protocol is currently understood at about 60 %.<br>
Initial documentations for those are quite ready. <br>
Unit code exist to validate backup save/restore. 

This repo has been created in advance.<br>
First content will be published soon.
