# 2DGP Term Project

------



[TOC]

------

### 1. 게임 소개

> - 제목 : 메탈슬러그3 모작
> - 장르 : 2D 런앤건 액션게임
>
> <img src="https://github.com/honey1586/2DGP/blob/master/Term_Project/Images/title_screenshot.png?raw=true" alt="title" style="zoom:80%;" />  <img src="https://github.com/honey1586/2DGP/blob/master/Term_Project/Images/ingame_screenshot.jpg?raw=true" alt="ingame" style="zoom: 80%;" />
>
> <img src="https://github.com/honey1586/2DGP/blob/master/Term_Project/Images/%EC%BA%90%EB%A6%AD%ED%84%B0%EC%84%A0%ED%83%9D%EC%B0%BD.JPG?raw=true" style="zoom:80%;" /> <img src="https://github.com/honey1586/2DGP/blob/master/Term_Project/Images/%ED%98%88%EC%82%AC%ED%8F%AC.jpg?raw=true" style="zoom:300%;" />
>
> [^인-게임 스크린샷]:  메탈슬러그3 타이틀, 인-게임 , 캐릭터 선택창
>
> - 플레이 방법 : 상하좌우 입력을 받아 횡스크롤로 진행하는 게임이다. 바라보는 방향으로 총을 쏴서 맵의 곳곳에서 등장하는 적을 물리치면서 보스방까지 진행하는 게임이다. 조작은 상,하,좌,우,총알 발사,폭탄 던지기,점프가 있다.
>
>   적에게 공격을 당할 시 라이프가 하나 깎이면서 라이프가 남아 있을 시 그 자리에서 몇초 간 무적상태로 부활한다.
>
> - 공식 배경 스토리 : 
>
>   세계의 신질서를 파괴하기 위한 모덴 원수의 반란도 과거의 사건이 되고, 간신히 세계에 질서와 평온이 돌아오기 시작했다. 부활한 모덴은 새로운 쿠데타를 계획하고 있었지만, 사전에 계획을 탐지한 정규군의 전격적인 기습작전에 의하여, 제2쿠데타는 불발로 끝나 버렸다. 모덴 반란군 진압에 많은 공을 세웠던 페레그린 팰콘스(PF)의 마르코와 타마의 제대 소원을 받아들여, PF의 리더로서 임무를 수행하게 되었다. 모덴 원수는 행방불명이라고 여기고 있지만, 모덴군 잔당은 지금 여전히 세계 각지에 잠복하고 있고, 그들의 거점을 하나씩 파괴해 가는 와중이었으므로 그들의 능력과 경험이 필요하였기 때문이다. 잔당과의 격렬한 싸움 중에서, 마르코와 타마는 모덴의 그림자를, 세번째 야망을 느끼고 있었다. 모덴은 살아있었다. 그리고 그는 야망을 포기하지 않았다.
>
>   한편, 정규군정보부소속의 특무 기관 스패로우즈는, 모덴 원수의 추적과 병행해, 계속해서 일어나는 괴사건의 조사를 하고 있었다. 가축의 유괴 사건이나 요원의 행방불명, 생물의 이상한 변이 등의 해괴한 사건들이 계속해서 일어나고 있었다. 모덴 원수와는 다르다.다른 무엇인가가 있다. 정보부는 반강제적으로 스패로우즈와 PF의 공동 작전을 실행시킨다. 모덴군 잔당이 숨어있는 곳에 기습적으로 상륙하는 작전으로, 스패로우즈의 멤버를 참가시키겠다고 한 상태였다. 조사 결과, 모덴군 잔당과 괴사건 사이에 무엇인가 관련이 있다는 것이 밝혀졌지만, 정규군 상부는 기밀에 부쳤다. 이상 성장한 거대 생물과 모덴군과의 관계 등은 일반적인 현상으로는 생각되지 않기 때문이다. PF와 스패로우즈의 연합작전에 있어서 지휘계통의 혼란을 걱정한 대장 마르코는 당연히 반대하였다. 그러나 평소와 마찬가지로 그의 의견은 기각되었고, 상륙 작전은 개시되었다. 
>
> [출처]: https://namu.wiki/w/%EB%A9%94%ED%83%88%EC%8A%AC%EB%9F%AC%EA%B7%B8%203?from=%EB%A9%94%ED%83%88%EC%8A%AC%EB%9F%AC%EA%B7%B83



------

### 2. GameState

> - TitleState
> - CharacterselectionState
> - GameState
> - PauseState
> - EndingState

------

### 3. GameState 설명

> ![](https://github.com/honey1586/2DGP/blob/master/Term_Project/Images/%EB%8B%A4%EC%9D%B4%EC%96%B4%EA%B7%B8%EB%9E%A8.JPG?raw=true) 
>
> ​                                                 **< State 구조 다이어그램 >**
>
> - TitleState 
>
>   - 게임의 타이틀 화면을 관리하는 Scene이다.
>   - 객체목록 : 메탈슬러그3 타이틀 이미지
>   - 아무 키 입력 시 CharacterselectionState로 change_state를 이용하여 이동한다.
>
> - CharacterselectionState
>
>   - 캐릭터를 선택하는 Scene이다. 캐릭터 선택 시 게임으로 넘어간다.
>   - 객체목록 : Characters(선택되어진 캐릭터의 값을 인자로 받아서 원하는 캐릭터 선택)
>   - ←,→ 키로 캐릭터를 선택하여 공격키를 누를 시 캐릭터가 선택되고 change_state를 이용하여 GameState로 이동한다.
>
> - GameState
>
>   - 게임을 플레이 하는 State이다.
>
>   - 객체목록 : 플레이어 캐릭터 , 적 , 총 ,아이템, 폭탄 , 구조물 등의 객체
>
>   - ← , →  : 캐릭터가 좌우로 움직이게 한다.  
>
>     ↑ , ↓ : 위를 보게하거나 앉게 한다.
>
>     A  : 총알 발사
>
>     S  : 폭탄 투척 , 혈사포(좀비모드)
>
>     D  : 점프
>
>     ESC : GameState를 멈추고 push_state를 이용하여 PauseState로 이동한다. 
>
> - PauseState
>
>   - GameState에서 ESC키를 입력할 시에만 넘어올 수 있는 State이다.
>   - 게임 사운드 On/Off , 게임 종료 , 게임으로 돌아가기 세 가지 기능을 가지고 있다.
>
> - EndingState
>
>   - 라이프가 다 깎이거나 보스 스테이지를 클리어 할 시에 넘어가는 State이다.
>   - 5초 간 게임이 끝났다는 이미지를 넣고 change_state로 TitleState로 넘어간다. 

------

### 4. 필요한 기술

> - 충돌처리 : 적의 총알과 폭탄에 맞았을 때 캐릭터가 죽어야 하므로 충돌처리 기술이 필요하다.
>
>   ​                  적이 가까이에 있을 때에는 칼로 공격하는 모션이 있어서 충돌처리가 필요하다.
>
>   ​                  구조물에 막히면 진행을 못하거나 점프를 하여 구조물 위에 올라타야 하므로 충돌처리가 필요하다.
>
> - 총알,폭탄 : 배열에 담아서 안보이는 상태로 미리 그려놓은 다음에 좌표를 바꿔주는 기술과 화면에서 벗어나면 사라지도록 하는 기술이 필요하다.
>
> - 총 : 아이템을 먹으면 총의 종류가 달라지므로 총을 관리하는 매니저 스크립트가 필요하다.

