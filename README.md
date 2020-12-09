# ShellProfiler

## Description

ShellProfiler is a simple and quick way to automate the starting of your shell. You can automate all these commands you launch everyday when you start working. To do so, just fulfill the profile.yaml file and call the executable.

## Usage

After cloning the project and fulfilling `profiles.yaml`, just do :
`python3 profiler.py [profileName]`
or
`python3 profiler.py` and then type the profile id to load it.

## Syntax
```
ProfileName:
  Instruction:
    Service:
      Arguments
```

See `profiles.syntax` for an example.

#### Valid Instructions

- `shell`
  - Arguments:
    - `True|False` : if `true`, the profile will be loaded in a shell opened in the `dir` directory (cf. dir). It will be launch during the `dir` instruction.

- `dir`
  - Arguments:
    - `Path` :  a string representing an absolute path to the directory you want to open your shell if `shell` instruction is `True`. If `shell` is false, all the instructions that will be launch after the `dir` instruction will be execute in the `dir` context anyway which allow absolute path for those commands.

- `process`
  - Arguments:
    - `cmd` : a string designing the command to call
    - `args` : list of string containing the arguments of the command
    - `silent` : `True|False`, if the command should write on stdout and stderr or not

#### Common arguments

`depends_on` :
  - `string|list` Force the command/step to be call after the command/name. Call it with the dir argument to launch a contextual command (eg. with a relative path).