###########
# Here is a document on how to collaberate on GitHub
#
###########

#Create a new Repository in GitHub
#Add a collaborator

#On your personal computer, where you want the file in

git clone <url.git>
cd <FolderName>

#This adds your repository to your computer, and moves you into it
#Then add some files
#Start with pull in case something has changed

git pull

#make your changes

git add <filename>
#putting into staging area

git commit -m "message here"
#this puts your files into the repository

git push
#moves everything up to GitHub


###################

#If you want to add your folder without cloning you can also do:

git remote add origin <url.git>
