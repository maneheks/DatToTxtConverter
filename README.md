## Dat to Txt Converter
### Available for Windows and MacOS

Converts one or many .dat files into .txt files named after each player and formats the data in an easy-to-read format.

**Visit [releases](https://github.com/maneheks/DatToTxtConverter/releases) to download the latest release.**

How it works:
* The program asks for a file path to the folder containing .dat files
* The program will only process files with a .dat extension so the folder does not need to contain exclusively .dat files
* The program will display the path cleaned of any disallowed characters
* As the program goes through each file, it will display the path and name of the file it is processing, any errors it encounters, and the path and name of the saved .txt file
* If a particular item is not found in the .dat file, the program will output an index error.

Future improvements:
* Make error messages more user friendly
* Improve readability of the log (spacing mostly)
* Ask user to confirm the path they entered is correct to give them a chance to re-enter if a mistake was made
* Resolve inventory and Enderchest formatting issues including replacing the wall of replace() statements
* Better format number outputs (remove brackets and apostrophes)
* Create a UI to run the program instead of running from console

_Note: Inventory and Enderchest data may be broken in some cases, especially where plugins have been used to create custom items/attributes (e.g. custom enchants applied to items)._
