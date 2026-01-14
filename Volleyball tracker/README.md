What can it do:
- display text main menu
- go through main menu options
- start and go through a whole game
- assign basic stats to each team
- save game result in json file
- load saved games from json file
- display statistics for each game and each team in that game

What I want it to be able to do:
- display lineup
- display teams on correct halves of the field
- perform rotations
- substitutions
- display proper field
- increment points & sets by one using a button
- display a box in the center that is supposed to be playing field
- ~~end the set automatically when one team scores >= 25 points while having having 2 point advantage over opposite team; add +1 set to winning team~~
- ~~display points~~
- ~~display team names~~
- ~~display sets~~

Current vision:

<img width="869" height="554" alt="{4889C13D-9770-4E48-8787-D993CF5E6EFA}" src="https://github.com/user-attachments/assets/a1c57dcd-aef9-4df9-9090-f201fdc09078" />

Current status (updated as of 14/01/26):

<img width="1275" height="824" alt="image" src="https://github.com/user-attachments/assets/8a5bd271-8b1b-4423-ac0e-9803d50edd1b" />

@Update 24/11/25
I have scrapped previous project and remodeled it using OOP. Works how I want it to work.
Things to do:
- fix 5th set to finish after 15 points scored
- calculate and display stats after each set

@Update 16/12/25
Things done:
- fix 5th set to finish after 15 points scored

@Update 14/01/26
I started creating GUI using PyQt5. For now it displays a picture, three clickable buttons that change color of the window below them.

Things to do:
- calculate and display stats after each set
- display detailed stats post-game
- add freeballs during rally
- add blocks
- fix spike kill feature (doesnt add stats, because there is no code for that)
- better stats handling (game indexing, remove games history through menu, plot charts)
