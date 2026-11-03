"""Deterministic original educational items. No past-paper claims or external text."""
import csv
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SUBJECTS=['정보시스템 기반 기술','프로그래밍언어 활용','데이터베이스 활용']
SOURCE='https://github.com/YunSangYeong/Industrial-Engineer-Information-Processing-CBT/blob/main/docs/QUESTION_REVIEW.md'
# Each row: topic | prompt | correct choice | three distractors | reviewed explanation.
CONCEPTS=[
'''운영체제|프로세스와 스레드의 관계에 관한 설명으로 옳은 것은?|같은 프로세스의 스레드는 주소 공간을 공유할 수 있다|모든 프로세스는 반드시 주소 공간을 공유한다|스레드는 실행 흐름을 가질 수 없다|프로세스에는 자원이 할당되지 않는다|프로세스는 실행 중인 프로그램의 자원 관리 단위이고 스레드는 실행 흐름의 단위다. 같은 프로세스 내 스레드는 코드·데이터 등 주소 공간을 공유하지만 스택과 레지스터 상태는 개별적으로 유지한다.
교착상태|교착상태의 필요조건에 해당하지 않는 것은?|자원의 강제 선점 가능|상호 배제|점유 및 대기|순환 대기|교착상태의 네 필요조건은 상호 배제, 점유 및 대기, 비선점, 순환 대기다. 자원을 강제로 회수할 수 있는 선점은 비선점 조건을 깨므로 필요조건이 아니다.
가상기억장치|페이징에서 페이지 테이블의 주된 역할은?|가상 페이지와 물리 프레임의 대응 관리|파일의 저작권 관리|모든 프로세스의 실행 종료|인터넷 도메인 이름 등록|페이징은 가상 주소 공간을 일정 크기 페이지로 나눈다. 페이지 테이블은 가상 페이지가 어느 물리 프레임에 대응하는지와 접근 관련 정보를 관리한다.
스케줄링|라운드 로빈 스케줄링에서 사용하는 것은?|시간 할당량|데이터베이스 외래키|고정된 파일 확장자|오직 작업의 파일 크기|라운드 로빈은 준비 큐의 프로세스에 일정 시간 할당량을 순환 배정하는 선점형 정책이다. 할당량이 끝나면 미완료 프로세스는 준비 큐 뒤로 이동할 수 있다.
네트워크|IP 주소에서 목적지 네트워크로 패킷을 전달하는 장비는?|라우터|스캐너|키보드|단순 전원 분배기|라우터는 네트워크 계층에서 목적지 IP와 라우팅 정보를 이용해 패킷을 다음 홉으로 전달한다. 서로 다른 IP 네트워크를 연결하는 역할을 한다.
전송계층|TCP의 특징으로 옳은 것은?|연결 지향이며 순서 있는 바이트 스트림을 제공한다|수신 순서를 절대 관리하지 않는다|IP 주소를 MAC 주소로 바꾼다|항상 암호화를 필수 제공한다|TCP는 연결 지향 전송으로 순서 제어, 재전송, 흐름 제어 등을 제공한다. 암호화 자체는 TCP의 필수 기능이 아니며 TLS 같은 별도 계층을 사용한다.
DNS|DNS의 대표적인 역할은?|도메인 이름에 대응하는 IP 주소 조회|디스크 섹터 포맷|프로세스 강제 종료|CPU 명령어 해독|DNS는 계층적인 이름 체계에서 도메인 이름의 A·AAAA 등 자원 레코드를 조회한다. 웹 접근 시 이름을 IP 주소로 찾는 용도로 널리 사용한다.
보안|비밀번호 저장에 일반적으로 적합한 방법은?|솔트를 포함한 전용 비밀번호 해싱 함수 사용|평문으로 공개 저장|단순 Base64만 적용|모든 사용자가 같은 비밀번호 사용|비밀번호는 평문이나 가역 인코딩으로 보관하지 않는다. 개별 솔트와 비용 조절이 가능한 Argon2·scrypt·bcrypt 같은 전용 해싱 방식을 사용하면 사전 대입 공격 비용을 높일 수 있다.
접근통제|최소 권한 원칙의 의미는?|업무에 필요한 최소한의 권한만 부여한다|모든 사용자에게 관리자 권한을 준다|로그를 전혀 남기지 않는다|인증 없이 접근을 허용한다|최소 권한은 사용자나 프로세스에 업무 수행에 필요한 범위의 권한만 부여하는 원칙이다. 불필요한 권한을 줄여 실수와 침해 사고의 영향을 제한한다.
암호|대칭키 암호의 설명으로 옳은 것은?|암호화와 복호화에 같은 비밀키를 사용한다|비밀키 없이 항상 복호화한다|해시값을 반드시 원문으로 복원한다|공개키와 개인키 쌍만 사용한다|대칭키 방식은 송수신자가 공유한 비밀키로 암호화와 복호화를 수행한다. 공개키와 개인키 쌍을 사용하는 비대칭키 방식과 구별한다.
소프트웨어공학|형상 관리의 주요 목적은?|소프트웨어 변경 이력과 버전의 체계적 관리|화면 밝기의 자동 조정|CPU 주파수 고정|네트워크 선로 전압 증폭|형상 관리는 소스·문서 등 형상 항목의 식별과 변경 통제, 상태 기록을 수행한다. 누가 무엇을 변경했는지 추적하고 일관된 버전을 유지하는 데 필요하다.
요구사항|비기능 요구사항에 해당하는 것은?|동시 사용자 500명에서 응답시간 2초 이내|회원 가입 기능 제공|주문 취소 기능 제공|상품명 검색 기능 제공|비기능 요구사항은 성능·신뢰성·보안 등 시스템이 갖춰야 할 품질이나 제약을 기술한다. 회원 가입이나 검색처럼 수행하는 업무 기능과 구별한다.
테스트|경계값 분석의 기본 생각은?|입력 영역의 경계와 그 인접 값을 검사한다|항상 무작위 한 값만 검사한다|소스 코드 주석만 검사한다|결과와 무관하게 모두 통과시킨다|입력 범위의 경계 주변은 비교 연산이나 범위 처리 오류가 자주 나타나는 곳이다. 경계값 분석은 유효 범위의 끝값 및 그 바로 안팎 값을 골라 검사한다.
테스트수준|통합 테스트에서 중점적으로 확인하는 것은?|모듈 사이 인터페이스와 상호작용|오직 키보드 외형|직원의 근무시간|프린터 잉크 색상|단위 테스트는 개별 단위를 검사하고 통합 테스트는 결합한 모듈 사이 인터페이스와 데이터 흐름을 확인한다. 시스템 전체 요구사항 검사는 시스템 테스트의 범위다.
구조|클라이언트·서버 구조의 설명으로 옳은 것은?|클라이언트가 요청하고 서버가 서비스를 제공한다|서버에는 프로그램이 존재할 수 없다|요청과 응답은 반드시 같은 프로세스다|클라이언트는 사용자 입력을 받을 수 없다|클라이언트는 서비스를 요청하고 서버는 요청을 처리해 응답한다. 역할을 분리하는 구조이며 동일 장치 안에서도 서로 다른 프로세스로 구성할 수 있다.
자료구조|스택의 기본 접근 순서는?|후입선출|선입선출|항상 오름차순|항상 임의 접근만|스택은 마지막에 넣은 항목을 먼저 꺼내는 LIFO 구조다. push로 넣고 pop으로 제거하며 함수 호출 관리와 깊이 우선 탐색 등에 활용한다.
자료구조|큐의 기본 접근 순서는?|선입선출|후입선출|항상 내림차순|항상 가장 큰 값 우선|일반 큐는 먼저 들어온 항목을 먼저 꺼내는 FIFO 구조다. 대기 작업을 도착 순서대로 처리하는 데 사용하며 우선순위 큐와 구별한다.
검색|정렬된 배열에 이진 탐색을 적용하는 이유는?|비교할 때마다 후보 범위를 대략 절반으로 줄일 수 있어서|모든 값을 항상 하나씩만 읽어서|정렬 여부가 전혀 무관해서|비교 연산이 필요 없어서|이진 탐색은 중간값과 목표값을 비교해 정렬 순서에 따라 절반의 후보를 제외한다. 임의 접근 가능한 정렬 배열에서 탐색 비교 횟수는 O(log n)이다.
저장장치|휘발성 메모리의 대표적인 예는?|DRAM|읽기 전용 광디스크|전원이 꺼진 SSD의 플래시|자기 테이프|DRAM은 주기적 재충전이 필요하고 전원이 끊어지면 저장 내용이 유지되지 않는 휘발성 메모리다. 플래시나 자기 매체의 비휘발성 저장과 구별한다.
백업|랜섬웨어 피해 복구를 위해 유용한 백업 방식은?|운영 시스템과 분리된 검증 가능한 백업 유지|원본과 동일 권한으로만 연결된 복사본 하나|백업 파일을 항상 원본으로 덮어쓰기|복구 시험을 전혀 수행하지 않기|백업도 감염이나 삭제의 영향을 받을 수 있으므로 분리·오프라인·불변 보관 등을 고려한다. 보관 여부뿐 아니라 실제로 복구할 수 있는지 시험하는 것이 중요하다.''',
'''변수|변수의 유효 범위에 관한 설명으로 옳은 것은?|지역 변수는 선언된 범위의 규칙에 따라 접근이 제한된다|모든 변수는 반드시 전역 변수다|지역 변수는 어느 함수에서나 이름만으로 접근된다|변수의 범위는 언어와 무관하게 항상 같다|지역 변수의 이름은 함수나 블록 등 언어가 정한 범위에서만 유효하다. 전역 변수와 다르며 구체적 수명과 범위 규칙은 사용하는 언어를 확인해야 한다.
제어문|반복문을 즉시 종료하고 그 다음 문장으로 이동하는 일반적인 문장은?|break|continue|반복문의 조건식 삭제|변수 선언만 수행|break는 현재 반복문을 끝내는 데 사용한다. continue는 현재 반복의 남은 부분을 건너뛰고 다음 반복 조건이나 갱신 단계로 이동한다.
제어문|반복문의 현재 회차 나머지를 건너뛰는 일반적인 문장은?|continue|break|return으로 항상 다음 반복|함수 정의|continue는 현재 회차에서 남은 본문을 생략하고 다음 반복 단계로 이동한다. break는 반복 자체를 종료하므로 두 동작을 구별해야 한다.
함수|재귀 함수에서 종료 조건이 필요한 주된 이유는?|호출이 무한히 이어지는 것을 막기 위해|변수를 사용할 수 없게 하기 위해|모든 반복을 느리게 하기 위해|반환값을 항상 문자열로 만들기 위해|재귀는 작은 부분 문제로 자기 자신을 호출하는 방식이다. 적절한 기저 조건과 그 조건에 가까워지는 진행이 없으면 호출이 끝나지 않거나 스택 자원이 소진될 수 있다.
객체지향|캡슐화의 목적과 가장 가까운 것은?|내부 상태와 구현을 숨기고 정해진 인터페이스로 접근하게 한다|모든 필드를 반드시 공개한다|클래스 생성을 금지한다|동일 코드를 무조건 복제한다|캡슐화는 데이터와 동작을 묶고 외부의 무분별한 직접 접근을 제한한다. 내부 구현 변경의 영향을 줄이고 객체가 자신의 일관성을 유지하는 데 도움을 준다.
객체지향|상속에 대한 설명으로 옳은 것은?|기존 클래스의 특성을 바탕으로 새 클래스를 정의한다|모든 객체가 항상 같은 메모리 주소를 갖는다|함수 호출을 모두 금지한다|데이터를 반드시 파일로만 저장한다|상속은 기존 클래스의 속성이나 동작을 새 클래스가 이어받아 확장하는 기법이다. 개별 언어의 접근 제한과 재정의 규칙을 함께 고려해야 한다.
객체지향|다형성의 예로 적절한 것은?|같은 인터페이스 호출이 실제 객체에 따라 다른 동작을 한다|모든 객체가 반드시 같은 문자열을 출력한다|메서드를 전혀 정의하지 않는다|자료형 검사를 모두 없앤다|다형성은 공통 인터페이스를 통해 서로 다른 구현을 다룰 수 있게 한다. 재정의된 메서드가 실제 객체의 종류에 맞게 선택되는 동적 바인딩이 대표적 예다.
예외처리|try-finally에서 finally의 용도는?|예외 발생 여부와 관계없이 필요한 정리 작업 수행|항상 예외를 무시하기|컴파일 오류를 모두 수정하기|변수명을 자동 변경하기|finally는 정상 흐름이나 예외 처리 후 자원 정리 등을 수행하는 구문이다. 프로세스 강제 종료 같은 상황까지 무조건 실행을 보장한다는 뜻은 아니다.
컴파일|컴파일러의 대표적인 역할은?|소스 프로그램을 다른 실행 가능한 형태 등으로 변환한다|모니터의 픽셀 수를 늘린다|데이터베이스 행을 삭제한다|네트워크 케이블을 연결한다|컴파일러는 소스의 구문과 의미를 분석해 목적 코드나 중간 표현 등으로 변환한다. 코드 실행 방식은 컴파일·링크·가상머신·JIT 등 도구 체계에 따라 달라질 수 있다.
Python|Python의 리스트에 관한 설명으로 옳은 것은?|순서가 있고 원소를 변경할 수 있다|원소를 절대 변경할 수 없다|반드시 숫자 하나만 저장한다|항상 자동 정렬된다|Python 리스트는 순서가 있는 가변 시퀀스다. 인덱스로 원소를 읽고 바꾸거나 append로 추가할 수 있으며 튜플의 불변성과 구별한다.
Python|Python 튜플의 특징은?|튜플 자체의 원소 참조를 재할당할 수 없다|항상 리스트와 완전히 같은 가변 구조다|반드시 한 원소만 갖는다|인덱스로 읽을 수 없다|튜플은 불변 시퀀스이므로 생성 후 특정 위치의 원소 참조를 바꿀 수 없다. 다만 튜플 안에 가변 객체를 넣었다면 그 객체의 내부 상태까지 불변이 되는 것은 아니다.
Java|Java 문자열 내용의 동등성을 비교하는 일반적인 방법은?|equals 메서드|객체 참조에 대한 ==만 사용|항상 주소를 숫자로 변환|문자열 길이만 비교|Java에서 참조형의 ==는 참조 동일성을 비교한다. String의 equals는 문자열 내용을 비교하므로 서로 다른 객체에 같은 내용이 들어 있는 경우에도 참이 될 수 있다.
C언어|C언어 포인터의 기본 용도는?|객체나 함수 등의 주소를 다루기|모든 변수를 문자열로 바꾸기|데이터베이스만 접속하기|배열 길이를 항상 자동 기록하기|포인터는 주소를 표현하는 값으로 객체 간접 접근 등에 사용된다. 올바른 수명과 범위 안의 대상을 가리켜야 하며 잘못된 역참조는 정의되지 않은 동작을 일으킬 수 있다.
알고리즘|시간 복잡도 O(n)의 의미에 가장 가까운 것은?|입력 크기에 비례하는 차수의 증가를 나타낸다|실행시간이 항상 정확히 n초다|메모리를 전혀 사용하지 않는다|입력과 무관하게 항상 한 번만 실행한다|빅오 표기법은 입력 크기가 커질 때 자원 증가율의 점근적 상한을 나타낸다. O(n)은 선형 차수이며 실제 초 단위 시간이나 상수 계수를 그대로 뜻하지 않는다.
정렬|안정 정렬이 보존하는 것은?|같은 키를 가진 항목 사이의 기존 상대 순서|모든 항목의 원래 절대 위치|항상 파일 크기|중복 키의 삭제 여부|안정 정렬은 정렬 기준 키가 같은 항목들의 상대적인 순서를 유지한다. 여러 키에 대해 순서대로 정렬할 때 유용하며 중복 항목을 제거하는 기능은 아니다.
메모리|동적 할당 메모리를 더 이상 사용하지 않는데 해제하지 않아 누적되는 문제는?|메모리 누수|문법 강조|정상적인 정렬|프로토콜 협상|메모리 누수는 필요가 없어진 동적 메모리를 회수하지 못해 사용량이 누적되는 현상이다. 언어의 자동 메모리 관리가 있더라도 불필요한 참조 유지 등으로 발생할 수 있다.
자료형|불리언 자료형이 표현하는 대표적인 값은?|참과 거짓|임의 길이 그림|오직 정수 100만|파일 경로만|불리언은 논리적 참과 거짓을 표현하는 자료형이다. 조건식과 논리 연산에 사용하며 언어마다 암시적 변환 규칙이 다르므로 실제 규칙을 확인해야 한다.
논리연산|논리 AND의 결과가 참이 되는 조건은?|두 피연산자가 모두 참|적어도 하나만 참이면 항상 참|두 피연산자가 모두 거짓|두 값이 다를 때만 참|논리 AND는 양쪽 논리값이 모두 참일 때만 참이다. 하나 이상이 거짓이면 거짓이며 적어도 하나가 참이면 되는 OR와 구별한다.
코드품질|중복 코드를 함수로 추출할 때 기대하는 효과는?|같은 로직의 변경 지점을 줄인다|모든 오류가 자동으로 사라진다|테스트가 항상 불필요해진다|실행시간이 무조건 0이 된다|함수 추출은 반복되는 로직을 한 곳에서 관리하도록 해 유지보수성을 높일 수 있다. 하지만 인자·부작용·호출 비용을 검토해야 하며 별도 검증은 여전히 필요하다.
모듈|모듈 사이 결합도를 낮추는 방향은?|필요한 인터페이스만 공개하고 내부 의존을 줄인다|다른 모듈의 내부 전역 상태를 모두 직접 수정한다|모든 모듈을 서로 순환 참조시킨다|같은 코드를 모든 파일에 복제한다|낮은 결합도는 모듈 간 불필요한 의존을 줄여 변경 영향을 제한한다. 명확한 인터페이스와 책임 분리는 독립적인 이해와 테스트를 돕는다.''',
'''관계모델|관계형 데이터베이스에서 행을 부르는 용어는?|튜플|속성|도메인|인덱스 페이지|릴레이션의 한 행은 튜플이고 열은 속성이다. 도메인은 속성이 가질 수 있는 값의 집합을 뜻하며 행과 열을 혼동하지 않아야 한다.
키|기본키의 조건으로 옳은 것은?|각 행을 유일하게 식별하며 NULL을 허용하지 않는다|중복과 NULL을 모두 반드시 허용한다|반드시 문자열 하나여야 한다|항상 다른 테이블 전체를 복사한다|기본키는 행 식별을 위해 선택한 후보키다. 유일성과 NOT NULL 제약을 만족해야 하며 단일 속성뿐 아니라 복합 속성으로 구성할 수도 있다.
참조무결성|외래키의 주된 목적은?|관련 테이블 사이의 참조 무결성 유지|모든 행 자동 암호화|디스크 용량 무제한 확장|중복 행 무조건 삭제|외래키는 참조하는 값이 참조 대상 키에 존재하도록 관계를 제약한다. NULL 허용 여부와 삭제·갱신 시 동작은 정의된 제약과 정책에 따른다.
정규화|제1정규형의 핵심 조건은?|각 속성 값이 관계 모델에서 원자값을 갖는다|모든 속성이 기본키다|테이블에 반드시 1행만 존재한다|모든 문자열을 암호화한다|제1정규형은 각 셀의 속성 값이 원자값이어야 한다는 조건이다. 한 셀에 반복되는 값 목록을 넣는 구조와 구별하며 원자성은 사용 도메인의 관점에서 판단한다.
정규화|제2정규형에서 제거하는 대표적인 의존은?|비주요 속성의 후보키에 대한 부분 함수 종속|모든 기본키의 유일성|모든 외래키|모든 완전 함수 종속|제2정규형은 제1정규형을 만족하고 비주요 속성이 후보키 전체에 완전 함수 종속되어야 한다. 복합 후보키의 일부에만 의존하는 비주요 속성의 부분 종속을 제거한다.
정규화|이행적 종속을 분리하는 대표적인 목적은?|갱신 이상 등 데이터 중복 문제를 줄이기|모든 데이터 손실을 허용하기|키 제약을 없애기|항상 테이블을 하나로 합치기|정규화는 함수 종속에 따라 테이블을 분해해 중복과 삽입·삭제·갱신 이상을 줄인다. 분해 시 무손실 조인과 종속성 보존을 함께 고려해야 한다.
SQL|SELECT에서 행을 그룹으로 묶는 절은?|GROUP BY|ORDER BY|DROP TABLE|COMMIT|GROUP BY는 지정한 속성 값에 따라 행들을 그룹으로 나눈다. 집계 함수와 함께 사용하며 ORDER BY는 결과 정렬이므로 역할이 다르다.
SQL|집계 후 그룹에 조건을 적용하는 절은?|HAVING|WHERE만 가능|CREATE|ROLLBACK|WHERE는 그룹화 이전의 개별 행을 필터링하고 HAVING은 그룹화·집계 결과에 조건을 적용한다. 두 절은 실행 단계와 조건 대상이 다르다.
SQL|SQL에서 NULL 여부를 검사하는 표현은?|IS NULL|= NULL|NULL = NULL만 사용|COUNT = NULL|NULL은 값이 없거나 알려지지 않음을 나타낸다. 일반 비교 연산은 UNKNOWN을 만들 수 있으므로 NULL 여부는 IS NULL 또는 IS NOT NULL로 검사한다.
집계함수|COUNT(열명)이 세는 것은?|해당 열이 NULL이 아닌 행 수|항상 모든 NULL 행만|서로 다른 테이블 수|열 이름의 글자 수|COUNT(*)는 행 수를 세고 COUNT(열명)은 해당 열 값이 NULL이 아닌 행을 센다. DISTINCT를 함께 쓰면 중복 제거 대상과 범위를 따로 확인해야 한다.
트랜잭션|ACID의 원자성이 의미하는 것은?|트랜잭션의 작업을 전부 반영하거나 전부 취소한다|반드시 작업을 하나만 포함한다|모든 값을 원자로 변환한다|항상 동시에 한 사용자만 접속한다|원자성은 논리적 작업 단위의 전부 성공 또는 전부 취소를 뜻한다. 일부 변경만 남아 일관성이 깨지는 것을 방지하는 성질이다.
트랜잭션|성공적으로 끝난 트랜잭션을 확정하는 명령은?|COMMIT|ROLLBACK|DROP DATABASE|RENAME|COMMIT은 트랜잭션의 변경을 확정한다. ROLLBACK은 미확정 변경을 취소하는 명령으로 확정과 취소의 역할을 구별해야 한다.
동시성|다른 트랜잭션의 미확정 변경을 읽는 현상은?|더티 리드|무손실 조인|키 생성|정규화|더티 리드는 아직 커밋되지 않은 변경을 다른 트랜잭션이 읽는 현상이다. 그 변경이 롤백되면 유효하지 않은 값을 사용하게 될 수 있다.
인덱스|인덱스 사용에 관한 설명으로 옳은 것은?|검색을 빠르게 할 수 있지만 갱신 비용과 저장 공간이 필요하다|모든 쿼리가 반드시 빨라진다|저장 공간을 전혀 쓰지 않는다|삽입·삭제 시 유지 비용이 없다|인덱스는 조건에 맞는 행을 찾는 비용을 줄일 수 있다. 다만 별도 자료구조를 저장하고 데이터 변경 때 유지해야 하므로 모든 작업에 무조건 이득은 아니다.
뷰|일반적인 논리 뷰에 관한 설명으로 옳은 것은?|질의로 정의한 가상 테이블이다|항상 원본과 무관한 완전한 물리 복사본이다|정의할 때 SELECT를 사용할 수 없다|모든 뷰가 항상 수정 가능하다|일반 뷰는 질의로 정의한 가상 테이블로 결과를 표현한다. 물리화 뷰와 구별하며 갱신 가능 여부는 뷰의 구조와 DBMS 규칙에 달려 있다.
권한|테이블에 대한 권한을 부여하는 SQL 명령은?|GRANT|REVOKE|ROLLBACK|TRUNCATE|GRANT는 사용자 등에 접근 권한을 부여한다. REVOKE는 부여된 권한을 회수하며 트랜잭션 확정·취소나 데이터 삭제 명령과 구별한다.
삭제|조건에 맞는 행만 삭제할 때 사용하는 기본 명령은?|DELETE FROM 테이블 WHERE 조건|DROP DATABASE|CREATE TABLE|GRANT SELECT|DELETE는 테이블의 행을 삭제하며 WHERE로 대상을 제한할 수 있다. WHERE가 없으면 모든 행이 대상이 될 수 있으므로 조건을 확인해야 한다.
보안|SQL 삽입 공격을 줄이는 기본적인 방법은?|매개변수화된 질의 사용|사용자 입력을 SQL 문자열에 그대로 연결|오류 메시지에 비밀번호 표시|인증 기능 제거|매개변수화 질의는 SQL 구조와 데이터 값을 분리한다. 사용자 입력을 문자열로 직접 연결하는 방식보다 안전하며 권한 최소화와 입력 검증도 함께 적용한다.
ER모델|ER 모델에서 엔터티 사이 연관을 나타내는 것은?|관계|CPU 레지스터|컴파일 옵션|디스크 회전수|ER 모델은 엔터티와 속성 및 엔터티 사이 관계를 표현한다. 업무의 개념적 구조를 모델링하며 관계의 차수와 참여 제약 등을 함께 검토한다.
복구|체크포인트의 대표적인 목적은?|장애 복구 시 확인해야 할 로그 범위를 줄이는 데 도움을 준다|모든 로그를 항상 즉시 삭제한다|모든 트랜잭션을 무조건 취소한다|백업을 영원히 불필요하게 한다|체크포인트는 특정 시점의 처리 상태 등을 기록해 복구 작업량을 줄이는 데 이용한다. 구체적 절차는 DBMS에 따라 다르며 백업과 로그 관리가 여전히 필요하다.'''
]
bank=[]
def add(subject,topic,prompt,correct,wrong,explanation,family=None,calc=None):
 idx=len(bank)+1
 choices=[str(correct),*map(str,wrong)]; shift=idx%4
 choices=choices[shift:]+choices[:shift]
 q=dict(id=f'IP-{idx:04d}',subject=subject,topic=topic,question=prompt,choices=choices,answer=choices.index(str(correct))+1,explanation=explanation,difficulty='중' if family else '하',year=None,session=None,type='original',sourceUrl=SOURCE,verificationStatus='reviewed',reviewNote='AI 일반 지식 기반 자체 작성. 개념·문장 내부 검토; 외부 전문가 검수 및 공식 출제기준 대조 미완료. '+('독립 JavaScript 계산 검사. 숫자 조건 변형.' if family else '정답·오답 선택지 의미 내부 대조.'),version='main',rights='자체 제작 · CC BY 4.0 · 정보처리산업기사 CBT 기여자 표시. 외부 원문 전재 없음.')
 if family:q.update(family=family,calculation=calc)
 bank.append(q)
for s,block in zip(SUBJECTS,CONCEPTS):
 for line in block.splitlines():
  topic,prompt,correct,*rest=line.split('|');add(s,topic,prompt,correct,rest[:3],rest[3])
# Each calculation family specifies explicit assumptions; all answers are exact integers.
# (subject index, kind, topic, prompt builder, result, explanation builder, unit)
families=[]
def family(si,kind,topic,prompt,fn,ex,unit=''):
 families.append((si,kind,topic,prompt,fn,ex,unit))
family(0,'bits','정보 표현',lambda a,b:f'{a}비트의 서로 다른 비트열은 총 몇 개인가?',lambda a,b:2**a,lambda a,b,r:f'각 비트에는 0과 1 두 값이 있다. 독립인 {a}비트의 조합은 2^{a} = {r}개다.','개')
family(0,'bytes','단위 변환',lambda a,b:f'1 KiB = 1024 byte일 때 {a} KiB는 몇 byte인가?',lambda a,b:a*1024,lambda a,b,r:f'KiB는 이진 접두 단위다. {a} × 1024 = {r} byte이며 십진 kB와 구별한다.','byte')
family(0,'rgb','영상 저장',lambda a,b:f'가로 {a}픽셀, 세로 {b}픽셀 RGB 영상이 픽셀당 3 byte이다. 압축·헤더·패딩 없이 영상 데이터는 몇 byte인가?',lambda a,b:a*b*3,lambda a,b,r:f'픽셀 수는 {a} × {b}이고 픽셀당 3 byte이므로 {a} × {b} × 3 = {r} byte이다.','byte')
family(0,'address','주소 공간',lambda a,b:f'바이트 주소 방식에서 주소선 {a}개로 표현 가능한 주소 수는?',lambda a,b:2**a,lambda a,b,r:f'주소선마다 0 또는 1을 표현하므로 주소 조합은 2^{a} = {r}개다. 여기서는 바이트마다 독립 주소를 부여한다.','개')
family(0,'subnet','IPv4 서브넷',lambda a,b:f'일반 IPv4 /{32-a} 서브넷에서 네트워크·브로드캐스트 주소 각 1개를 제외한 사용 가능 호스트 주소 수는? (/31·/32 예외 제외)',lambda a,b:2**a-2,lambda a,b,r:f'호스트 비트는 {a}개로 주소는 2^{a}개다. 예약된 네트워크·브로드캐스트 두 주소를 빼면 {r}개다.','개')
family(0,'transfer','전송 시간',lambda a,b:f'오버헤드 없는 회선에서 {a*b} Mbit를 {b} Mbit/s로 보낸다. 전송 시간은?',lambda a,b:a,lambda a,b,r:f'시간 = 데이터량 ÷ 전송률 = {a*b} Mbit ÷ {b} Mbit/s = {r}초다. 대기·전파 지연은 제외한 조건이다.','초')
family(0,'pagecount','페이징',lambda a,b:f'프로세스의 연속 가상 공간이 {a*b} KiB이고 페이지 크기가 {b} KiB이다. 필요한 페이지 수는?',lambda a,b:a,lambda a,b,r:f'가상 공간을 페이지 크기로 나눈다. {a*b} ÷ {b} = {r}개로 정확히 나누어지므로 올림으로 늘어나는 페이지가 없다.','개')
family(0,'offset','페이지 오프셋',lambda a,b:f'페이지 크기가 {2**a} byte인 바이트 주소 페이징에서 페이지 내 오프셋 비트 수는?',lambda a,b:a,lambda a,b,r:f'페이지 내 {2**a}개 바이트를 구분해야 한다. 2^{a} = {2**a}이므로 필요한 오프셋은 {r}비트다.','비트')
family(0,'fcfswait','CPU 스케줄링',lambda a,b:f'두 작업이 시각 0에 도착하고 FCFS 순서는 A, B다. A 실행시간 {a}, B 실행시간 {b}이며 전환 비용이 0일 때 B 대기시간은?',lambda a,b:a,lambda a,b,r:f'B는 자신보다 먼저 실행되는 A가 끝날 때까지 기다린다. A가 0부터 {a}까지 실행되므로 B의 대기시간은 {r}이다.','시간단위')
family(0,'turnaround','CPU 반환시간',lambda a,b:f'작업 도착 시각이 {a}, 완료 시각이 {a+b}이다. 반환시간은?',lambda a,b:b,lambda a,b,r:f'반환시간은 완료 시각에서 도착 시각을 뺀 값이다. ({a+b}) - ({a}) = {r}이다. CPU 실행시간만을 뜻하지 않는다.','시간단위')
family(0,'bitrate','직렬 전송',lambda a,b:f'초당 {a}개의 심벌을 보내고 심벌마다 {b}비트를 전달한다. 오버헤드가 없을 때 비트 전송률은?',lambda a,b:a*b,lambda a,b,r:f'비트 전송률 = 심벌 전송률 × 심벌당 비트 수 = {a} × {b} = {r} bit/s다.','bit/s')
family(0,'capacity','저장 용량',lambda a,b:f'레코드 {a}개를 각각 {b} byte로 연속 저장한다. 인덱스·헤더·패딩 없이 필요한 용량은?',lambda a,b:a*b,lambda a,b,r:f'전체 용량은 레코드 수와 레코드 크기의 곱이다. {a} × {b} = {r} byte이며 추가 메타데이터는 제외한다.','byte')
family(0,'serial','병렬화 한계',lambda a,b:f'총 실행시간 {a+b}초 중 직렬 부분 {a}초와 완전 병렬 부분 {b}초다. 병렬 부분 시간을 이상적으로 0으로 줄이면 최소 실행시간은?',lambda a,b:a,lambda a,b,r:f'이상적으로 병렬 부분을 제거해도 직렬 부분은 남는다. ({a+b}) - ({b}) = {r}초로 직렬 부분이 하한을 결정한다.','초')
family(0,'treeedges','트리',lambda a,b:f'노드 {a}개인 유한 연결 무방향 트리의 간선 수는?',lambda a,b:a-1,lambda a,b,r:f'연결되어 있고 사이클이 없는 유한 트리는 노드 n개에 간선 n-1개다. n={a}이므로 {r}개다.','개')
family(1,'sum','반복 추적',lambda a,b:f'Python: s = 0; 이후 for i in range(1, {a+1}): s += i 를 실행한다. 종료 후 s는?',lambda a,b:a*(a+1)//2,lambda a,b,r:f'range(1, {a+1})는 1부터 {a}까지다. 합은 n(n+1)/2 = {a}×{a+1}/2 = {r}이다.')
family(1,'nested','중첩 반복',lambda a,b:f'Python에서 range({a}) 반복 안에 range({b}) 반복을 두고 안쪽에서 매번 c += 1 한다. c 초깃값 0, 중간 탈출 없을 때 최종 c는?',lambda a,b:a*b,lambda a,b,r:f'바깥 반복 {a}회마다 안쪽 반복 {b}회가 모두 수행된다. 증가 횟수는 {a} × {b} = {r}회다.')
family(1,'quotient','정수 나눗셈',lambda a,b:f'Python 정수식 {a*b+b-1} // {b} 의 값은?',lambda a,b:a,lambda a,b,r:f'{a*b+b-1} = {b} × {a} + {b-1}이다. 양수의 //는 몫의 내림이므로 결과는 {r}이다.')
family(1,'mod','나머지',lambda a,b:f'Python 정수식 {a*b+b-1} % {b} 의 값은?',lambda a,b:b-1,lambda a,b,r:f'{a*b+b-1}을 {b}로 나누면 몫 {a}, 나머지 {b-1}이다. 나머지는 0 이상 {b} 미만이며 답은 {r}이다.')
family(1,'shift','비트 이동',lambda a,b:f'Python의 비음수 정수식 {a} << {b%4+1} 의 값은?',lambda a,b:a*2**(b%4+1),lambda a,b,r:f'Python 정수에서 왼쪽으로 k비트 이동하면 2^k를 곱한다. {a} × 2^{b%4+1} = {r}이며 고정 폭 오버플로는 없다.')
family(1,'xor','비트 XOR',lambda a,b:f'Python 정수식 {a} ^ {b} 의 값은? (^는 비트 XOR)',lambda a,b:a^b,lambda a,b,r:f'두 정수의 이진 표현 {a:b}와 {b:b}에서 같은 위치 비트가 다를 때 1이다. XOR 결과는 {r:b}, 십진수로 {r}이다.')
family(1,'and','비트 AND',lambda a,b:f'Python 정수식 {a} & {b} 의 값은?',lambda a,b:a&b,lambda a,b,r:f'이진수 {a:b}와 {b:b}에서 양쪽 비트가 모두 1인 위치만 남긴다. 결과 {r:b}를 십진수로 바꾸면 {r}이다.')
family(1,'or','비트 OR',lambda a,b:f'Python 정수식 {a} | {b} 의 값은?',lambda a,b:a|b,lambda a,b,r:f'이진수 {a:b}와 {b:b}에서 어느 한쪽 이상이 1인 위치를 1로 한다. 결과 {r:b}는 십진수 {r}이다.')
family(1,'range','반복 범위',lambda a,b:f'Python len(range(0, {a*b}, {b})) 의 값은?',lambda a,b:a,lambda a,b,r:f'0, {b}, …, {a*b-b}까지 {b} 간격으로 포함하고 끝값 {a*b}은 제외한다. 원소 수는 {a*b}/{b} = {r}이다.')
family(1,'array','배열 인덱스',lambda a,b:f'Python: x = list(range({a+b})); 이후 x[{a}] 의 값은?',lambda a,b:a,lambda a,b,r:f'range({a+b})는 0부터 시작하는 연속 정수다. 리스트 인덱스도 0부터이므로 인덱스 {a}의 값은 {r}이다.')
family(1,'recurrence','점화식',lambda a,b:f'정수 함수 f(0)={b}, f(n)=f(n-1)+{b} (n>=1)로 정의한다. f({a})는?',lambda a,b:(a+1)*b,lambda a,b,r:f'초깃값 {b}에서 {a}번 각각 {b}를 더한다. f({a})={b}+{a}×{b}={r}이다.')
family(1,'linear','대입 추적',lambda a,b:f'Python: x={a}; y={b}; x=x+y; y=x-y 를 순서대로 실행한다. 마지막 y는?',lambda a,b:a,lambda a,b,r:f'x 변경 후 x={a+b}이고 y는 아직 {b}다. 이어 y={a+b}-{b}={r}이므로 원래 x 값과 같다.')
family(1,'slice','슬라이스',lambda a,b:f'Python: x=list(range({a+b+5})); len(x[{a}:{a+b}]) 의 값은?',lambda a,b:b,lambda a,b,r:f'슬라이스는 시작 인덱스를 포함하고 끝 인덱스를 제외한다. 모두 유효 범위이므로 길이는 ({a+b})-({a})={r}이다.')
family(2,'cross','관계 연산',lambda a,b:f'행 수 {a}인 R과 행 수 {b}인 S의 카티션 곱의 행 수는?',lambda a,b:a*b,lambda a,b,r:f'R의 각 행을 S의 모든 행과 짝짓는다. 쌍의 수는 {a} × {b} = {r}행이다.','행')
family(2,'unionall','SQL 집합 연산',lambda a,b:f'결과 행이 각각 {a}개, {b}개인 두 SELECT를 UNION ALL로 연결한다. 총 행 수는?',lambda a,b:a+b,lambda a,b,r:f'UNION ALL은 중복을 제거하지 않고 두 결과를 이어 붙인다. 따라서 {a}+{b}={r}행이다.','행')
family(2,'countnull','집계',lambda a,b:f'테이블 T에 {a+b}행이 있고 열 c가 NULL인 행이 {b}개다. SELECT COUNT(c) FROM T 결과는?',lambda a,b:a,lambda a,b,r:f'COUNT(c)는 c가 NULL이 아닌 행만 센다. 전체 {a+b}행에서 NULL {b}행을 빼면 {r}이다.')
family(2,'selectivity','필터',lambda a,b:f'테이블 {a*b}행을 조건으로 걸렀더니 정확히 1/{b}이 남았다. 결과 행 수는?',lambda a,b:a,lambda a,b,r:f'전체 행 수에 조건 통과 비율을 곱한다. {a*b} × 1/{b} = {r}행이다.','행')
family(2,'join','조인',lambda a,b:f'부모 {a}행 각각에 자식 {b}행이 있고 다른 자식은 없다. 자식 외래키로 부모와 INNER JOIN하면 몇 행인가?',lambda a,b:a*b,lambda a,b,r:f'각 자식은 유일한 부모 한 행에 대응한다. 부모당 {b}개의 결과가 생겨 {a} × {b} = {r}행이다.','행')
family(2,'projection','관계 차수',lambda a,b:f'차수가 {a+b}인 릴레이션에서 서로 다른 속성 {b}개를 제거하고 나머지 전부를 투영한다. 결과 차수는?',lambda a,b:a,lambda a,b,r:f'차수는 속성의 수다. 전체 {a+b}개에서 {b}개를 제외하면 {r}개다. 투영에 따른 중복 제거는 행 수와 관계있다.','개')
family(2,'blocks','블록 저장',lambda a,b:f'한 블록에 고정 길이 레코드 {b}개가 들어가며 레코드가 {a*b+1}개다. 레코드 분할 없이 필요한 최소 블록 수는?',lambda a,b:a+1,lambda a,b,r:f'{a}개 블록에 {a*b}개를 저장하고 남은 1개에 추가 블록이 필요하다. ceil({a*b+1}/{b})={r}개다.','개')
family(2,'recordsize','레코드',lambda a,b:f'고정 길이 필드 크기가 각각 {a}, {b}, 4 byte다. 헤더·패딩·NULL 표시가 없다면 한 레코드 크기는?',lambda a,b:a+b+4,lambda a,b,r:f'조건상 추가 공간은 없으므로 필드 크기를 합산한다. {a}+{b}+4={r} byte이다.','byte')
family(2,'groups','그룹 집계',lambda a,b:f'테이블에 부서 {a}개가 있고 각 부서에 행이 {b}개씩 있다. 부서별 GROUP BY 결과의 그룹 수는?',lambda a,b:a,lambda a,b,r:f'GROUP BY는 서로 다른 부서 값마다 한 그룹을 만든다. 부서가 {a}개이므로 그룹 수도 {r}개이며 각 그룹의 행 수 {b}와 다르다.','개')
family(2,'update','갱신',lambda a,b:f'T의 모든 행에서 x={a}이다. UPDATE T SET x=x+{b} 실행 후 각 행의 x 값은?',lambda a,b:a+b,lambda a,b,r:f'각 행의 원래 x 값에 {b}를 더한다. {a}+{b}={r}이다. WHERE가 없으므로 모든 행이 갱신된다.')
family(2,'delete','삭제',lambda a,b:f'테이블에 {a+b}행이 있고 DELETE의 WHERE 조건을 만족하는 행이 정확히 {b}개다. 삭제 후 남은 행 수는?',lambda a,b:a,lambda a,b,r:f'조건을 만족한 {b}행만 삭제한다. 전체 {a+b}행에서 빼면 {r}행이 남는다.','행')
family(2,'sumcolumn','SUM 집계',lambda a,b:f'NULL이 없는 T.c 열에 {a}행 모두 정수 {b}가 들어 있다. SELECT SUM(c) FROM T 결과는?',lambda a,b:a*b,lambda a,b,r:f'같은 정수 {b}가 {a}번 더해진다. SUM(c)={a}×{b}={r}이며 NULL이나 빈 테이블은 없다.')
family(2,'distinct','중복 제거',lambda a,b:f'T.c에는 서로 다른 값 {a}개가 있고 각각 정확히 {b}회 나타나며 NULL은 없다. COUNT(DISTINCT c)는?',lambda a,b:a,lambda a,b,r:f'DISTINCT는 중복을 제거해 서로 다른 값만 남긴다. 각 값의 반복 횟수 {b}와 관계없이 {r}개다.')
assert len(families)==40
for fi,(si,kind,topic,prompt,fn,ex,unit) in enumerate(families):
 for j in range(24 if fi<20 else 23):
  # Unique pairs within every family. Small bounded bit exponents prevent overflow.
  a=j+2; b=j%7+2
  if kind in ['bits','address','offset']: a=j+2
  text=prompt(a,b)
  result=fn(a,b)
  # Avoid duplicate subnet families: use all prefix sizes /2 through /25, no /31 exception.
  if kind=='subnet':
   a=j+7; text=prompt(a,b);result=fn(a,b)
  mistakes={
   'bits':[2*a,2**(a-1),2**(a+1)], 'bytes':[a*1000,a*128,a*8192],
   'rgb':[a*b,a*b*8,a+b+3], 'address':[a*2,2**(a-1),2**(a+1)],
   'subnet':[2**a,2**a-1,2**(a-1)-2], 'offset':[2**a,a+1,a-1],
   'sum':[a*a,a*(a-1)//2,a*(a+1)], 'quotient':[a+1,b-1,a*b],
   'mod':[a,b,a*b+b-1], 'shift':[a*(b%4+1),a+2**(b%4+1),a],
   'blocks':[a,a*b+1,a+2], 'countnull':[a+b,b,0],
   'cross':[a+b,a,b], 'unionall':[a*b,a,b], 'distinct':[a*b,b,a+b],
  }.get(kind,[result-1,result+1,result*2,a+b,a*b])
  distractors=[]
  for candidate in [*mistakes,result+2,result+3,result+4]:
   if candidate>=0 and candidate!=result and candidate not in distractors:distractors.append(candidate)
   if len(distractors)==3:break
  calc=dict(kind=kind,values=[a,b],result=result,unit=unit)
  add(SUBJECTS[si],topic,text,f'{result}{unit}',[f'{x}{unit}' for x in distractors],ex(a,b,result),f'IP-{kind}',calc)
assert len(bank)==1000
(ROOT/'src/data/questions.json').write_text(json.dumps(bank,ensure_ascii=False,indent=2)+'\n')
example={**bank[0],'id':'IMPORT-EXAMPLE-001','question':'[직접 작성용] '+bank[0]['question'],'verificationStatus':'pending','reviewNote':'양식 예제: 등록 전 직접 검수 필요'}
(ROOT/'public/templates/questions.json').write_text(json.dumps([example],ensure_ascii=False,indent=2)+'\n')
row={k:v for k,v in example.items() if k!='choices'}
row.update({f'choice{i+1}':x for i,x in enumerate(example['choices'])})
with (ROOT/'public/templates/questions.csv').open('w') as f:
 writer=csv.DictWriter(f,fieldnames=row,lineterminator="\n");writer.writeheader();writer.writerow(row)
print(json.dumps({'total':len(bank),'subjects':{s:sum(q['subject']==s for q in bank) for s in SUBJECTS},'concepts':60,'numericVariants':940,'numericFamilies':len(families)},ensure_ascii=False))
