# Industrial-Engineer-Information-Processing-CBT

정보처리산업기사 필기 CBT. React + TypeScript + Vite 기반 비공식 학습 도구다. 서버·로그인·유료 API 없이 브라우저에 학습 기록을 저장한다.

## 구현

네이비·청록 반응형 화면, 실전 모의시험·랜덤 문제풀이, 과목별 선택, 오답노트·북마크·통계, 최근 시험, 답안·시험 시간 복원, 자동 제출, 과락 채점, 결과·전체 해설, 오답 재학습을 제공한다. 두 모드 모두 답안 선택/채점 후 **Space**로 다음 문제를 연다. 마지막 시험 문제에서는 Space로 제출하지 않는다. 학습 기준·연도 선택 메뉴는 없다.

JSON/CSV 가져오기·양식 다운로드·검색·검증 대기·근거 입력 후 로컬 승인·중복 제거·문항 내보내기를 제공한다. 개인 등록은 공용 저장소에 게시되지 않는다. 잘못된 파일은 일부만 등록하지 않고 전체를 거부한다.

모바일 메뉴는 전체가 독립 스크롤 영역이며 작은 세로 화면과 가로 모드에서 상하단 메뉴에 접근할 수 있다. 상단 상시 면책 배너는 없으며 비공식 표시는 사이드바/푸터, 출처·한계는 문제은행 관리에 둔다. 저장 실패·손상 경고는 유지한다.

## 시험 규칙과 자료의 한계

**공식 원문 확인은 미완료**다. Q-Net 조사 요청이 프록시 `403`으로 차단됐다. 설정은 3과목 각 20문항·총 60문항·90분·4지선다·평균 60점 및 과목별 40점 이상인 학습용 잠정 규칙이다. 과목은 정보시스템 기반 기술 / 프로그래밍언어 활용 / 데이터베이스 활용이다. 미응답은 오답이며 과락과 평균을 반올림 전 값으로 판정한다. 자세한 조사 URL·오류·배점은 [공식 자료 확인 기록](docs/SOURCES.md)을 참고한다. 이번 작업에서 공식 규칙을 읽고 검증했다고 주장하지 않는다.

기본 JSON에 **내부 검수 1,000문항**을 등록했다. 기출 0·복원 0·자체 제작 1,000이며 연도·회차는 전부 미확인(null)이다.

| 과목 | 개념형 | 숫자 조건 변형 | 합계 |
| --- | ---: | ---: | ---: |
| 정보시스템 기반 기술 | 20 | 336 | 356 |
| 프로그래밍언어 활용 | 20 | 305 | 325 |
| 데이터베이스 활용 | 20 | 299 | 319 |
| 합계 | 60 | 940 | 1,000 |

숫자 변형은 **40유형의 940조건**이다. 독립 학습 유형은 개념형을 합쳐 100개이며 1,000개 독립 개념이라는 뜻이 아니다. 문자열/보기 순서 중복 제거와 940개 독립 재계산·개념/문장 내부 검토를 수행했다. 외부 전문가 검수·공식 출제기준 대조는 미완료다. [제작·검수·재생성 기록](docs/QUESTION_REVIEW.md)에 범위와 한계를 공개한다. 기본 목표 대비 부족 0이지만, 공식 검증/전문가 검수 완료 은행으로 표현하지 않는다.

## 실행과 검사

Node.js 24.19.0 (`.node-version`), npm 잠금 파일을 사용한다. 저장소 루트에서:

```sh
npm ci
npm run dev
npm test
npm run build
npx playwright install --with-deps chromium
npm run test:e2e
```

이 클라우드의 시스템 Chromium을 사용하려면 브라우저 다운로드 대신:

```sh
PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH=/usr/bin/chromium npm run test:e2e
```

생성 원고를 바꾸면 `python3 scripts/generate_bank.py`로 JSON과 가져오기 양식을 재생성한다. 실제 실행 결과와 기기 범위는 [검증 보고서](docs/VALIDATION.md)를 참고한다.

## 기록 보존

자격증별 저장 키 `industrial-engineer-information-processing-cbt:v1`. 최근 응답 5,000개·시험 30회를 보존하며 대시보드 통계는 보존된 응답 범위다. JSON 기록 백업은 내보내기만 제공하며 백업 UI 복원은 제공하지 않는다. 초기화는 확인 후 개인 기록·로컬 등록분을 지우고 기본 은행은 유지한다. 손상된 저장 원본은 자동 덮어쓰지 않는다. 다른 브라우저·origin·시크릿 모드·iframe 저장 제한에 따라 기록이 분리되거나 저장이 차단될 수 있다. iframe 실사용은 이번 작업에서 검증하지 않았다.

## 표준과 라이선스

[CBT 표준 스킬](.agents/skills/cbt-site-standard/SKILL.md) 전체와 references를 복사하고 AGENTS.md에 연결했다. 기존 AGENTS.md는 없었다. 계정 공통 스킬 설치를 뜻하지 않는다.

- 최신 정책: `YunSangYeong/electrician-cbt` main `76b990b8720adfa85c22a0a8f699b17094aa357b`, 스킬 v1.4.0.
- 재사용 앱: 스킬 지정 커밋 `b9a682ccff1b460334b78d5bfad9375b7ec4fbb6`. 앱 소스·스타일·모델·테스트·빌드 설정·배포 workflow를 출발점으로 수정했다.
- 원본 전기기능사 데이터·생성 원고·학습 기록은 가져오지 않았다. 다른 프로젝트의 원격 저장소나 배포는 수정하지 않았다.
- 앱 코드 MIT 원본 고지 보존. 자체 문항 CC BY 4.0. [LICENSE](LICENSE)와 [출처 기록](docs/SOURCES.md) 참고.

## 배포 상태

기본 workflow는 **main push → 단위·빌드·PC/모바일 검증 성공 → Pages 자동 배포**, PR은 검증만 수행한다. `base`는 `/Industrial-Engineer-Information-Processing-CBT/`다.

배포 사전 확인 첫 요청에서 `gh api repos/YunSangYeong/Industrial-Engineer-Information-Processing-CBT`가 `Get "https://api.github.com/repos/YunSangYeong/Industrial-Engineer-Information-Processing-CBT": Forbidden`으로 실패했다. 원인을 권한 부족으로 단정하지 않는다. 정책상 API 접근과 Pages 설정을 다시 조회하지 않았고, main push·수동 실행·workflow 재실행·대체 배포를 하지 않았다. 이번 작업의 CI/Pages 실행은 없으며 기존 공개 상태는 확인하지 못했다. 코드는 배포 트리거가 없는 별도 브랜치에 보존한다. 이후 배포는 사용자가 직접 마무리한다.

예정 기본 주소: `https://YunSangYeong.github.io/Industrial-Engineer-Information-Processing-CBT/` — 배포 성공 및 공개 화면 모두 미확인.

현재 필요한 최소 환경 조치는 클라우드 환경의 인터넷 허용 도메인에 `api.github.com`을 추가하는 것이다. 공식 자료 조사를 위해서는 `www.q-net.or.kr` 접근도 필요하다. 이 설정이 인증·Pages 활성화까지 보장하지 않는다. Pages 상태를 확인하지 못했으므로 최초 설정 필요 여부나 승인 대기를 만들어 보고하지 않는다.
