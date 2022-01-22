# git push origin master
error: failed to push some refs to .... 
위의 명령어를 통해 push할 때 reject가 걸림

원인: 원인은 .gitignore 파일 또는 README.md 파일로 인해 발생한다고 한다.

해결: git push origin +master 명령어 입력하면 해결
