import {expect,test,type Page} from '@playwright/test';
async function capture(page:Page,name:string) {
 expect(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth)).toBe(true);
 await page.screenshot({path:test.info().outputPath(`${name}.png`),fullPage:true});
}
test('PC·모바일 주요 화면과 결과의 가로 넘침·표시 검증',async({page})=>{
 await page.goto('');await capture(page,'home');
 await page.getByRole('button',{name:'모의시험 시작하기',exact:true}).click();
 await capture(page,'exam');
 await page.getByRole('button',{name:'시험 종료 및 제출',exact:true}).click();
 await page.getByRole('button',{name:'제출하고 결과 보기',exact:true}).click();
 await capture(page,'result');
 if(await page.getByRole('button',{name:'메뉴 열기',exact:true}).isVisible())await page.getByRole('button',{name:'메뉴 열기',exact:true}).click();
 await page.getByRole('navigation').getByRole('button',{name:'랜덤 문제풀이',exact:true}).click();
 await page.getByRole('button',{name:'문제풀이 시작',exact:true}).click();
 await page.getByRole('group',{name:'답안 선택'}).getByRole('button').first().click();
 await capture(page,'practice');
 for(const label of ['오답노트','북마크','학습 통계','문제은행 관리']) {
  if(await page.getByRole('button',{name:'메뉴 열기',exact:true}).isVisible())await page.getByRole('button',{name:'메뉴 열기',exact:true}).click();
  await page.getByRole('navigation').getByRole('button',{name:label,exact:true}).click();await capture(page,label);
 }
});
