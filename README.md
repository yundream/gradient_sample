## Gradient API를 이용한 LLM 파인튜닝 예제코드 
이 예제코드는 Joinc EDU 유튜브 채널의 **일상이 AI 시리즈 #4 Gradient.ai API를 이용해서 LLM 파인튜닝 해보기** 영상에서 사용한 Python 코드입니다.
 * [일상이 AI 시리즈 #4 Gradient.ai API를 이용해서 LLM 파인튜닝 해보기](https://youtu.be/G_ZCczGe0AI)

테스트 환경은 아래와 같습니다.
```
python --version 
Python 3.11.6
```

아래의 패키지를 설치하면 됩니다.
```shell
 pip install gradientai --upgrade
 pip install python-dotenv
```

이 코드를 실행하기 위해서는 [https://gradient.ai/](https://gradient.ai/)에 가입한 후 Workspace를 만들고 Access Token을 발급 받아서 **.env** 파일을 설정해줘야 합니다. 자세한 내용은 영상을 참고해 주세요.
```
GRADIENT_ACCESS_TOKEN=<gradient.ai api를 호출하기 위한 access token>
GRADIENT_WORKSPACE_ID=<생성한 workspace의 ID>

```
