# 구현·검증 보고서

작업일: 2026-11-03. 작업 디렉터리: `/workspace/Industrial-Engineer-Information-Processing-CBT`.

## 시작 상태와 표준

시작 HEAD `85b013aa2c33c196642aa1e3356efa21bd9b5073`, 작업 브랜치 `work`, 변경 없음, 파일 README.md 한 개. AGENTS.md·앱·기존 배포 workflow는 없었다.

최신 원본 main `76b990b8720adfa85c22a0a8f699b17094aa357b`의 표준 v1.4.0과 references 전부를 읽었다. 스킬 폴더 9개 파일을 바이트 단위로 비교해 복사를 확인했다. 기준 앱 `b9a682ccff1b460334b78d5bfad9375b7ec4fbb6`에서 소스·스타일·모델·테스트·빌드 설정·workflow·MIT 고지를 가져와 대상용으로 수정했다. 원본 저장소 원격 변경·기존 사이트 재배포는 수행하지 않았다.

## 로컬 결과

| 명령/검사 | 결과 |
| --- | --- |
| `npm ci` | 종료 0, 잠금 파일 사용 |
| `npm test` | 종료 0, 958개 통과. 940개 독립 계산 사례와 수량/중복/채점/시간/저장/가져오기 검사 포함 |
| `npm run build` | 종료 0, TypeScript 및 Vite 프로덕션 빌드 성공 |
| 데이터 재생성 | 동일 SHA-256, 1,000개 ID·fingerprint 고유 |
| 표준 폴더 비교 | 9개 파일 일치, AGENTS 연결 완료 |
| PC/모바일 기본 브라우저 검사 | 18개 통과 |
| 모바일 메뉴·저장 오류·상단 안내 회귀 | 12개 통과 |
| 주요 화면 캡처·가로 넘침 | 수정 후 종료 0, PC/모바일 2개 통과; 최종 사례 합계 32개 통과 |

브라우저 명령은 `PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH=/usr/bin/chromium npx playwright test`다. 시스템 Chromium을 사용한 Desktop Chrome과 Pixel 7 에뮬레이션이다. 실기기·Safari·Firefox·블로그 iframe은 미실행이다. 프로덕션 산출물을 `vite preview`로 실행해 검사했다. 대규모 JSON을 번들에 포함하므로 500 kB 초과 청크 경고가 있다(비압축 JS 약 1.30 MB, gzip 약 142 kB). 오류나 실패를 숨기기 위해 경고 임계값을 바꾸지 않았다.

추가 화면 검사 초기에 테스트가 랜덤 화면의 시작 버튼을 누르지 않아 2개가 시간 초과됐다. 앱 결함이 아니라 테스트 조작 누락으로 확인했고 해당 조작과 정확한 버튼명을 수정한 뒤 다시 검사했다. 배포 파이프라인은 실행하지 않았으므로 이 로컬 수정·재검증은 배포 재시도가 아니다.

## 기능 검사 범위

- 60문항 고유 추출·과목별 20개·기본 은행 family 중복 없음·검증 대기 제외.
- 평균 60점 양쪽 경계, 각 과목 40점 경계, 고평균이어도 과락 시 불합격.
- 실제 90분 설정·절대 종료 시각 유지·새로고침 복원·만료 자동 제출·중복 제출 방지·만료 후 답안 변경 차단.
- 실전 중 해설 비공개·제출 확인/취소·모든 해설·오답 필터·그 시험 오답만 재학습.
- 랜덤 즉시 채점 한 번·연속 정답·학습 이어하기·순회 내 중복 방지·오답 해제·북마크·통계.
- 두 모드 실제 키보드 keydown/keyup Space 이동·미응답 보호·마지막 문제 자동 제출 방지·답안/이동 후 본문 포커스·네이티브 버튼/입력/대화상자 보호. repeat는 별도 이벤트로 확인했다.
- JSON/CSV 등록·원자적 오류 처리·중복 제거·승인 근거·내보내기·초기화·기본 은행 보존.
- 손상 저장 원본 보존·실제 저장 실패 경고 유지·학습 기준 선택 메뉴 없음·상단 상시 면책 배너 없음.

## 모바일 메뉴: 실제 입력

390×480과 740×360에서 각각 wheel과 CDP touchStart/move/end 스와이프를 사용했다. 메뉴 애니메이션 완료 후 아래로 이동해 백업·초기화 버튼의 뷰포트 진입과 실제 클릭/탭·다운로드/대화상자를 확인하고, 위로 돌아와 대시보드 선택 및 메뉴 닫힘을 검사했다. `scrollTop` 강제 대입은 하지 않았다. 배경만 스크롤된 경우 통과하지 않으며 배경 위치 유지도 검사한다. 글자 확대 CSS와 480→400 높이 변화에서 상하단 접근도 확인했다. 이는 브라우저 터치 에뮬레이션이며 실기기 터치 검증은 아니다.

## 수량·출처

자체 제작 1,000 = 개념형 60 + 40 family × 총 940 숫자 조건. 기출/복원 0. 내부 검수 완료 1,000, 검증 대기 0, 제외 0, 부족 0. 외부 전문가 검수와 공식 출제기준 대조는 미완료다. 공식 규칙 조사는 Q-Net 프록시 403으로 차단됐다. 자세한 내용은 [SOURCES.md](SOURCES.md), [QUESTION_REVIEW.md](QUESTION_REVIEW.md).

## 배포 사전 확인: 첫 차단에서 중단

실행한 유일한 API 확인:

```text
gh api repos/YunSangYeong/Industrial-Engineer-Information-Processing-CBT
Get "https://api.github.com/repos/YunSangYeong/Industrial-Engineer-Information-Processing-CBT": Forbidden
exit 1
```

GitHub API 도메인은 관측한 현재 인터넷 허용 목록에 포함되지 않았다. 원인이 네트워크 정책인지 별도 권한인지 재시도로 판정하지 않았다. Pages 설정·관리 권한·기존 공개 여부는 확인하지 못했다. API 재시도·대체 API/배포·workflow 수동 실행·재실행·main push는 하지 않았다. 자동 실행도 시작하지 않았다.

main용 자동 검증→배포 workflow는 코드로 준비했다. PR은 검증만 하고 배포 job의 쓰기 권한은 `pages: write`, `id-token: write`로 제한했다. 이후 사용자가 직접 마무리한다. 현재 필요한 최소 단계는 클라우드 환경 인터넷 허용 도메인에 `api.github.com`을 추가하는 것이다. 이것이 인증이나 Pages 최초 설정 완료를 보장하지 않는다.

예정 주소 `https://YunSangYeong.github.io/Industrial-Engineer-Information-Processing-CBT/`. 이번 작업의 CI/Pages 실행 없음, 배포 성공 미확인, 공개 화면 미확인. 별도 보존 브랜치의 원격 커밋은 완료 응답에 보고하며 원격 확인 기록을 아래 추가한다.

최종 화면 검사는 `npx playwright test tests/e2e/visual.spec.ts` 종료 0, 2 passed다. PC 대시보드와 모바일 시험 캡처를 직접 열어 확인했다. 기본 18개·메뉴 회귀 12개·화면 검사 2개를 합쳐 최종 사례 결과는 32개 통과다. 한 번의 전체 실행에서 32개 전부가 통과했다고 기록한 것은 아니며, 추가 화면 검사 수정 후 영향받은 2개를 별도로 재검증했다.
