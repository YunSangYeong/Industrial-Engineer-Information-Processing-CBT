// Official page could not be read in this environment. See docs/SOURCES.md.
export const SUBJECTS = ["정보시스템 기반 기술", "프로그래밍언어 활용", "데이터베이스 활용"] as const;
export const PROFILE = {
  name: "정보처리산업기사", bankId: "main", rulesVerificationStatus: "pending",
  questionCount: 60, questionsPerSubject: 20, durationMinutes: 90,
  choiceCount: 4, passScore: 60, subjectCutoff: 40,
  officialUrl: "https://www.q-net.or.kr/crf005.do?id=crf00503&jmCd=2290",
  storageNamespace: "industrial-engineer-information-processing-cbt:v1",
} as const;
