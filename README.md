# SimpleVirtualBackground
python과 일렉트론을 사용한 웹캠 가상배경 프로그램
<hr/>

## 프로젝트 소개
이 프로젝트는 UnityCaptureFilter를 사용하여 가상 웹캠을 생성하고 python으로 웹캠의 비디오를 받아와서 프레임을 수정하여 가상배경을 넣어 가상웹캠에 전송하고 이 과정들 중간에 배경의 이미지를 바꾸거나 그 외의 컨트롤을 할 수 있는 인터페이스를 일렉트론js로 만드는 것이 목표입니다
<hr/>

### 개발 환경
- OS: windows
- development language: python(3.10), Javascript
- Framework: Electron.js, Node.js
- Connection: FastAPI
<hr/>

### 기능

#### Electron.js UI
(예정)
- 가상 캠화면 불러오기
- 가상 배경: on/off
- 가상 배경 이미지 변경
<hr/>

### 설치 및 사용방법
#### Windows
(제대로 설치가 가능한 패키지는 Electron.js 연동 후 패키징 할 예정)

(FastAPI 적용중이라 코드 작동 안함)
1. UnityCaptureFilter 폴더에 있는 InstallCustomName.bat을 실행하고 만들 가상캠의 이름을 설정 후 Enter를 하면 설치되었다는 alert창이 뜸
alert창 확인 후 캠목록을 확인하면 설정한 이름을 가진 가상캠 확인 가능
2. opencv_pyvirtualcam.py에 있는 모듈 설치 후
python opencv_pyvirtualcam.py 실행
3. 종료는 ESC키를 입력하면 됨

## 프로젝트 진행 사항
python만 사용하여서 캠을 컨트롤 하는 부분은 성공하였으나 Electron.js를 사용하여 웹 연동하는 부분에 에러 때문에 upload 하지 않았음