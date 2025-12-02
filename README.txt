You'll need to follow these steps in order to run format builder!

First, make sure you have python installed
Next, you'll want to make sure you have all of the repo's cloned:

- Voyager
- Format-Builder
- Voyager-Indexes
- Silver-MSE-2.5.6
- Voyager-mtg.github.io
- Voyager-Field-Builder

MAKE SURE ALL REPO's ARE IN ONE FOLDER, FORMAT BUILDER WILL NOT WORK OTHERWISE.

If you don't know how to clone a repo, GO BACK AND LEARN

Go to your GitHub folder, then find your Silver MSE folder. Open that folder, and within you'll see "Silver MSE" and
"git-updater.bat" etc...
From here, right click the Silver MSE folder, choose the option "copy as path"

Next, you'll want to, in your WINDOWS SEARCHBAR, search "environment variables". 
You'll choose "edit environment variables for your account"

On this new window, within the first list, you'll want to click on "Path" then "Edit..."
From here, choose "New" then paste the path that you copied earlier within. Click "OK" and close the Environment
Variables window.

Return to this folder (Format-Builder), right click, and choose "Open in terminal"

As a test, write out "mse" in the terminal, it should open mse.

Finally, to RUN format builder, simply type "python build.py"

Note: It may ask you to login to GitHub when it begins to push the changes, this is fine, simply finish 
authentication and it will continue with the push after you've finished logging in.

Congratulations! You've now setup and run Format Builder!