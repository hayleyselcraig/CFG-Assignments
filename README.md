# CFG Assignment 1

## Contents
[About Me](#about-me)\
[Coding Experience](#coding-experience)\
[Assignment One Task List](#assignment-task-list)\
[Formatting Feautures](#formatting-features)\
[Git Commands](#git-commands)\
[Screenshots](#screenshot-process)\
[Adding a .gitignore & requirements.txt](#git-ignore-and-requirements)



## About Me <a name="about-me"></a>
Hello! My name is Hayley Selcraig.\
My hobbies include photography, reading and walking my Maltese dog called Ellie.\
I have done photography for charity events, weddings and personal shoots.\
You can view my online gallery [here](https://hayleyselcraigphotography.pixieset.com/).\
I am a big Disney fan and my favourite movie is Lilo & Stitch.

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠏⠀⠀⠀⠀⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠀⠀⠀⠀⠀⠀⠀⢠⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⡞⠸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠤⠀
⠀⠀⠀⠀⠀⠀⢀⣶⠀⠀⠸⡄⠀⠀⠀⠀⠀⢰⠃⠀⡇⠀⠀⠀⢀⣤⣔⣚⣛⠛⠟⠛⠛⠉⠉⠙⠛⠻⢭⡿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀⡄
⠀⠀⣾⣦⣀⢰⡿⢿⡆⣀⣠⣷⡄⠀⠀⠀⠀⣼⠀⠀⢹⣀⣴⡿⠟⠋⠉⠉⠉⠛⠷⡄⠀⠀⠀⠀⠤⠤⢤⣙⢦⡉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀⠀⠀⠃
⠀⠀⠸⣅⠈⠛⠁⠈⠳⠏⢙⡇⠙⣦⣀⠀⠀⢿⠀⢀⡞⢡⠞⠀⠀⠀⠀⠀⠀⠀⠀⣷⠀⠀⠀⠀⠀⠀⠀⠀⠙⠳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠋⠀⠀⠀⠀⠀⢠⠀
⢠⣤⡤⡟⠀⡼⠋⢹⠀⠀⣿⠀⠀⠘⣎⠓⠦⢼⣤⠎⢠⡏⠀⣠⣾⣿⣿⢶⡄⠀⢀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡄⠀⠀⠀⠀⠀⠀⠀⢀⡞⠁⠀⠀⠀⠀⠀⠀⡌⠀
⠀⠻⢧⣴⡀⠛⠦⠼⠂⠰⠛⠲⢤⡀⠘⢦⡀⢠⠏⠀⢸⠀⣰⣿⣿⣿⣇⣼⡇⠀⡾⠀⠀⠀⢀⠀⣀⠀⠀⠀⢀⣐⡲⣷⠀⠀⠀⠀⠀⠀⢠⠏⠀⠀⠀⠀⠀⠀⠀⣸⠁⠀
⠀⠀⠀⠈⠛⢶⠶⠚⠁⠀⠀⠀⠀⠉⠳⣄⠙⡿⠀⠀⠸⡄⢿⣿⣿⣿⣿⡿⠀⡼⢁⣀⣼⣗⣚⡯⣾⣗⠀⣠⠋⠉⠻⣿⡇⠀⠀⠀⠀⣰⠃⠀⠀⠀⠀⠀⠀⠀⡰⠃⠀⠀
⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⡇⠴⢶⡆⠹⣌⣛⠿⢿⣿⡁⠞⣴⠋⠀⠀⠀⠈⠙⢾⣳⣤⠇⠀⠀⠀⢸⡇⠀⢀⡤⢺⠃⠀⠀⠀⠀⠀⠀⠀⡴⠃⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⠀⢸⡙⠢⣄⡉⢛⣺⠿⠃⢰⢷⡆⠀⠀⠀⠀⠀⠀⢹⣏⣴⣿⣿⣷⢸⣅⡴⠋⢠⠏⠀⠀⠀⠀⠀⠀⢀⡞⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣇⠀⢧⠀⣀⣹⣷⡦⣄⡀⠈⢻⣧⠀⠀⠀⠀⠀⣀⣿⣿⣿⣼⣿⡟⡼⠁⠀⢠⠏⠀⠀⠀⠀⠀⠀⣠⠏⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠹⣦⡀⠀⠀⠀⠀⠀⠀⠀⠘⣆⠈⢿⣡⡀⠀⠙⠶⠬⢿⠲⢯⣷⣤⣤⣶⠿⣿⠿⣿⣿⣿⡟⢱⠃⠀⡴⠋⠀⠀⠀⣄⣀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠦⣄⡀⠸⡆⠀⠀⢀⣼⡷⣄⠙⢿⡒⣆⠀⠀⠘⣟⠒⠮⣝⠲⡦⣄⡘⢦⣉⣋⣉⡠⢋⣠⣞⠁⠀⠀⠀⣼⠁⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⣇⠀⣰⢫⠎⠀⠈⠓⠦⣍⠻⠤⣄⣀⠈⠀⠀⣸⡆⠙⠒⣛⢶⣌⡽⠛⠛⠫⠦⠚⠛⠛⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣶⠇⡏⠀⠀⠀⢀⣤⠎⠉⠒⠦⣬⣉⠓⠛⠓⠛⢋⣭⣵⡊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢰⠇⠀⠀⢻⣷⠏⠀⠀⠀⠀⠀⢨⠿⡍⠉⠉⠉⠀⠀⠙⠲⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⢸⠀⠀⠀⢸⣏⠀⠀⠀⠀⠀⢰⠋⠀⢹⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠇⢸⠀⠀⠀⠈⠛⠀⠀⠀⠀⠀⡏⠀⠀⠈⢧⣀⣠⠤⠒⠲⢤⡀⠀⠸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠏⠀⡼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⣤⠟⠁⠀⠀⠀⠀⠉⠀⠀⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⠀⢀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢧⠀⠀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣆⠀⡇⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣆⢧⡀⠀⠀⠀⠤⢖⣚⣿⣾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⣧⠀⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⠀⠙⠦⣄⣀⡀⠈⠋⢈⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠏⠀⠘⣆⠘⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠀⠀⠀⠀⠀⣯⣉⢉⢉⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

## Coding Experience <a name="coding-experience"></a>
I have done the following Kickstarter and Tech Taster courses through CFG which I really enjoyed:
- C#
- JavaScript
- Introduction to coding
- Python

### Using Git & Github 
**This is my first time using Git & Github.**
I am going to use this private repository for my CFG assignments.

## Assignment One Task List <a name="assignment-task-list"></a>

For this assignment I will complete the following steps:
- [x] Create a GitHub account
- [x] Create a private Repository
- [x] Create a README.md file including information about me and what I will use GitHub for in this assignment
- [x] Use at least six different markdown text [formatting features](#formatting-features)
- [x] Demonstrate the following commands:\
         - Checking the status\
         - Creating a branch\
         - Adding files to a branch\
         - Adding commits with meaningful messages\
         - Opening a pull request\
         - Merging and deploying to main branch
- [x] Take screenshots of the process and add to my README.md file
- [x] Create .gitignore and briefly explain what it is for
- [x] Create requirements.txt and briefly explain what it is
for
- [x] Add Asmaa as a collaborator to your individual
repository for marking and review purposes
- [x] All tasks complete! :tada:

## Formatting Features
<a name="formatting-features"></a>
I have used the following formatting features in this assignment:
1. Headings
2. Bold text
3. Website Link
4. Custom Anchor
5. Lists
6. Task List
7. Quoting Code

## Git Commands <a name="git-commands"></a>
Some basic Git commands that I used throughout this assignment:

```git clone``` Makes a copy of the remote repository to a local machine.<br/>
<br/>
```git status``` Provides an overview of your repository by showing which files have been modified, which changes are ready to be committed, and which files are not currently tracked by Git.<br/>
<br/>
```git add``` Tells Git which files we want to be included in our next save.<br/>
<br/>
```git commit``` Saves a snapshot of your changes in the local repository. These changes are stored locally and are not shared with the remote repository until you push them.<br/>
<br/>
```git push``` Sends our changes from the local repository to the remote repository.<br/>
<br/>
```git pull``` To get the most up-to-date version of the remote repository in our local repository.


## Screenshots <a name="screenshot-process"></a>
Here is screenshots of the process<br/>

**1. Checking the status**<br/>
In this step I used this git command, which listed which files are staged, unstaged, and untracked.
```
git status
```

<img width="564" height="252" alt="Screenshot of checking status of the readme.md file" src="https://github.com/user-attachments/assets/e9b6e78a-b8c2-42c3-a026-e9263971c57d" /><br/>
<br/>

**2. Creating a branch**<br/>
In this step, I created a new branch and named it ***Screenshots*** this allowed me to work on this new part of the readme.md file without affecting the main.<br/>
<br/>
<img width="349" height="342" alt="Screenshot of Creating a branch" src="https://github.com/user-attachments/assets/49a54128-4ff4-4158-a5a9-e45ef6e76eb0" /><br/>
<br/>

**3. Adding files to a branch**<br/>
In this step, I added image files to the branch. I have added screenshots of the steps I took and added accurate alt text which gives context to the screenshots.<br/>
<br/>
<img width="1129" height="216" alt="Screenshot of Adding files to a branch" src="https://github.com/user-attachments/assets/21fd0988-3919-4729-bd71-49806c058df4" /><br/>
<br/>

**4. Adding commits with meaningful messages**<br/>
In this step, I commited the changes and added a detailed description of the new section I added.<br/>
<br/>
<img width="357" height="385" alt="Screenshot of Commit Changes and description of the updates." src="https://github.com/user-attachments/assets/5e060b83-ca7f-48fc-a270-a34dd4f81e3b" /><br/>
<br/>

**5. Opening a pull request**<br/>
In this step. I opened the new pull request and compared the changes of this new branch against the main.<br/>
<br/>
<img width="937" height="666" alt="Screenshot of comparing the changes of the new branch and the main." src="https://github.com/user-attachments/assets/bd9bee31-c693-462a-9f7d-7c03f34f7c64" /><br/>
<br/>

**6. Merging and deploying to main branch**<br/>\
In this step, I seen that there was no conflict issues and proceeded to merge to the main branch. I then confirmed the merge and the pull request was complete.<br/>
<br/>
<img width="663" height="125" alt="Screenshot of no conflict issues and proceed to merge to main branch." src="https://github.com/user-attachments/assets/f4ce320d-1717-4aea-9c01-43634bd7e82c" /><br/>
<br/>
<br/>
<img width="658" height="279" alt="Screenshot of confirming the merge." src="https://github.com/user-attachments/assets/417f9b8b-9fa4-4fd0-b4e0-9d39b1aaf287" /><br/>
<br/>
<br/>
<img width="658" height="72" alt="Screenshot of Pull request complete." src="https://github.com/user-attachments/assets/3b04929e-91eb-4696-b642-763b11cba4b1" />


## Adding a .gitignore and requirements.txt file <a name="git-ignore-and-requirements"></a>

A .gitignore file tells Git which files or folders to ignore when tracking changes
<br/>
-It mainly affects new/untracked files
<br/>
-It helps prevent committing:
system files (like macOS hidden files)
IDE configs
temporary or sensitive files<br/>
<br/>
<br/>
A requirements.txt file lists all the packages or libraries required for a project.
It allows them to be installed in one step, ensuring a consistent environment and supporting easier collaboration.<br/>
<br/>




