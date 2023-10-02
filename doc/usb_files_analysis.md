# USB protocol and Files format analysis

## Introduction

Here is the current status of those analysis.
Anything has not been totally understood yet, but current understanding makes it usable for the following :

1. Loading and interpreting a backup file from original Software regarding presets.
2. Reading from device to get "live" settings and to interpret them.  

Just a beginning, but WIP.
As creating md complex tables is a hassle, all informations are detailed in the **pdf docs** section in the same directory than this file.<br>
Here is just an introduction.

## File structures

Backup files have a **.bhb** extension.Those are binary files.<br>
Unit preset files have a **.phb** extension. Those are in JSON format, so easier to understand.

Understanding their format is important as **.bhb** sections are really close to the device memory setup per section, and **.phb** enlight some obscure settings in the PRESETS **.bhb** section. They both help to understand later structured exchange to have with the device through USB (read or write), in addition of providing backward compatible files with original softwares (PC and Mac).<br>
Also, from simplest JSON **.phb** files, binary **.bhb** files are easier to understand.

### Unit preset files (.phb)

Each preset may be exported through original provided software.<br>
Resulting files are easy to understand JSON files.
They contain the following sections :

- **EXP** : Describes expression pedal associated to this preset.
- **effectModule** : This is a section for all of the 9 items in a single preset. They are presented in the following order :
  - **AMP**
  - **CAB**
  - **DELAY** : Warning - This is not the same name than the one commonly used as just **DLY**
  - **DS/OD** : Warning - This is not the same name than the one commonly used as just **DS**
  - **EQ**
  - **FX/COMP** : Warning - This is not the same name than the one commonly used as just **FX**
  - **MOD**
  - **NS/GATE** : Warning - This is not the same name than the one commonly used as just **NS**
  - **REVERB** : Warning - This is not the same name than the one commonly used as just **RV**
- **fileInfo** : Contains release informations for compatibility insurance.

Thing to note is that the structure of this file do not reflect the device settings organization, nor its memory mapping neither its USB exchange protocol.<br>
Why is not understandable but this will have to be preserved between different sections for backward compatibility.<br>

See **pdf docs** for full details.

### Device backup/restore files (.bhb)

Those files may be initially generated through original software.<br>
They are a full device dump.<br>
Despite the JSON **.php** files, they exactly match the data structures of the device and USB exchanges done with it.<br>
When retrieving or saving presets or part of them through USB, it totally matches the device expectations. Same for restoring.

This is binary file, encoded little endian.<br>
Key sections are :
- **Header** (0x48 bytes long) - Contains product and release informations.
- **Buffer** (0x3B8 bytes long) - *Not investigated yet*
- **HB100_PRESETS** (0x110 + (200 * 0xC2) - total size) :
  - Header info (0x110 bytes long)
  - List of the 200 presets each being as foolows (each is 0xC2 fixed bytes size):
    - preset number (2 bytes)
    - preset name (16 bytes - String padded at 14 bytes)
    - for each of the 9 effects in chain :
      - is_on (0/1 - 2 bytes)
      - Effect type in section : ( 2 bytes )
      - Parameters of the effect (1 to 6 params ) : each is 2 bytes - size is variable.<br>
       **warning** : *Effects are written sequentially, with no padding per effect. It means the full chain is written but could have variable size between two different presets. Padding is applied at the end of the preset to fill the fixed size of the preset. (0xC2)*
      - Exp pedal settings for preset+ Padding to fill in a 0xC2 size per preset.
  - **HB100_SYSTEM** (0x12C bytes long) - *Not investigated yet*
  - **HB100_Rythm** (0x128 bytes long) - *Not investigated yet*


For more details, look at the **pdf doc**.<br>
There, you will find codes for effects and simulations per chain section, full list of possible number and type of parameters per effect, and some more stuff.<br>

Note that the initial backup from the windows software is too short in size by 32 bytes.<br>
This is the reason why device returns an error on the device when last preset is trying to be restored.<br>
Perhaps a too short buffer size somewhere...

So, here we are (currently) with file analysis.
Soon to come, some POC code as well as USB protocol analysis.
