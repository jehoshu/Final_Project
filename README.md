# Final_Project
README of how to use the image
how to run a python script in a Docker container. 
The script is a merge script that receives a git URL 
and branch name from environment variables.

Prerequisites
    - Install Docker

Build the image
    - Clone this repository
    - Navigate to the directory where the Dockerfile is located
    - Run the following command:

        docker build -t merge-image .

Run the image
    - Run the image and pass in the environment variables 
    for the repository URL and branch to merge, use the following command:

    docker run -e REPO_TO_CLONE=<GIT_URL> -e BRANCH_TO_MERGE=<BRANCH_NAME> merge-image

    - Replace <GIT_URL> with the actual URL of the repository 
    and <BRANCH_NAME> with the actual name of the branch you want to merge.

Notes
    - This is an example of how to run a python script in a Docker container.
    - The script is a merge script that receives a git URL 
    and branch name from environment variables.
    - Make sure to use Github link only.

Author
    - Jehoshua Yefah
   

Date
    - Jan - Fab 2023