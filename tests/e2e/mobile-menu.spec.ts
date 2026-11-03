import { expect, test, type Page } from '@playwright/test';
test.use({hasTouch:true});
async function open(page:Page) {
  await page.getByRole('button',{name:'메뉴 열기',exact:true}).click();
  await expect(page.locator('.sidebar')).toHaveClass(/open/);
  await page.waitForTimeout(350); // Wait for transform transition before pointer coordinates.
}
async function swipe(page:Page, direction:'down'|'up') {
  const cdp=await page.context().newCDPSession(page);
  await cdp.send('Emulation.setTouchEmulationEnabled',{enabled:true,maxTouchPoints:1});
  const height=page.viewportSize()!.height;
  const lo=105,hi=height-55;
  const start=direction==='down'?hi:lo,end=direction==='down'?lo:hi;
  await cdp.send('Input.dispatchTouchEvent',{type:'touchStart',touchPoints:[{x:140,y:start}]});
  for(let i=1;i<=12;i++) {
    await cdp.send('Input.dispatchTouchEvent',{type:'touchMove',touchPoints:[{x:140,y:start+(end-start)*i/12}]});
    await page.waitForTimeout(18);
  }
  await cdp.send('Input.dispatchTouchEvent',{type:'touchEnd',touchPoints:[]});
  await page.waitForTimeout(250);
  await cdp.detach();
}
for(const size of [{width:390,height:480},{width:740,height:360}]) {
 for(const input of ['wheel','touch'] as const) {
  test(`${size.width}×${size.height} 메뉴 ${input} 실제 입력으로 하단 도구→상단 대시보드`,async({page})=>{
   await page.setViewportSize(size); await page.goto(''); await open(page);
   const menu=page.locator('.sidebar');
   expect(await menu.evaluate(el=>el.scrollHeight>el.clientHeight)).toBe(true);
   const background=await page.evaluate(()=>scrollY);
   const scroll=async(direction:'down'|'up')=>{
    if(input==='touch') await swipe(page,direction);
    else {await page.mouse.move(140,size.height/2);await page.mouse.wheel(0,direction==='down'?500:-500);await page.waitForTimeout(150);}
   };
   for(let i=0;i<8;i++) {
    await scroll('down');
    if(await menu.evaluate(el=>el.scrollTop+el.clientHeight>=el.scrollHeight-2))break;
   }
   expect(await menu.evaluate(el=>el.scrollTop)).toBeGreaterThan(0);
   const backup=page.getByRole('button',{name:'학습 기록 백업',exact:true});
   const reset=page.getByRole('button',{name:'데이터 초기화',exact:true});
   await expect(backup).toBeInViewport(); await expect(reset).toBeInViewport();
   const download=page.waitForEvent('download');
   if(input==='touch') await backup.tap(); else await backup.click();
   expect((await download).suggestedFilename()).toBe('information-processing-study-backup.json');
   if(input==='touch') await reset.tap(); else await reset.click();
   await expect(page.getByRole('dialog')).toBeVisible();
   await page.getByRole('button',{name:'돌아가기',exact:true}).click();
   for(let i=0;i<8;i++){await scroll('up');if(await menu.evaluate(el=>el.scrollTop<2))break;}
   await expect.poll(()=>menu.evaluate(el=>el.scrollTop)).toBeLessThan(2);
   const home=page.getByRole('navigation').getByRole('button',{name:'학습 대시보드',exact:true});
   await expect(home).toBeInViewport();
   expect(await page.evaluate(()=>scrollY)).toBe(background);
   await page.screenshot({path:test.info().outputPath(`menu-${input}-${size.width}.png`)});
   if(input==='touch')await home.tap();else await home.click();
   await expect(menu).not.toHaveClass(/open/);
   await expect(page.getByRole('heading',{name:'정보처리산업기사 필기 CBT',exact:true})).toBeVisible();
  });
 }
}
test('글자 확대·뷰포트 높이 변화 후에도 메뉴 상하단 접근',async({page})=>{
 await page.setViewportSize({width:390,height:480});await page.goto('');
 await page.addStyleTag({content:'.sidebar nav button,.sidebar .text-button{font-size:24px;line-height:1.5}.sidebar nav button{min-height:72px}'});
 await open(page);await page.setViewportSize({width:390,height:400});
 for(let i=0;i<4;i++){await page.mouse.move(150,200);await page.mouse.wheel(0,700);await page.waitForTimeout(100);}
 await expect(page.getByRole('button',{name:'데이터 초기화',exact:true})).toBeInViewport();
 for(let i=0;i<4;i++){await page.mouse.wheel(0,-700);await page.waitForTimeout(100);}
 await expect(page.getByRole('navigation').getByRole('button',{name:'학습 대시보드',exact:true})).toBeInViewport();
});
test('각 화면에 상단 상시 안내가 없고 저장 실패 경고는 유지',async({page})=>{
 await page.goto('');
 for(const label of ['학습 대시보드','실전 모의시험','랜덤 문제풀이','오답노트','북마크','학습 통계','문제은행 관리']) {
   if(await page.getByRole('button',{name:'메뉴 열기',exact:true}).isVisible())await page.getByRole('button',{name:'메뉴 열기',exact:true}).click();
   await page.getByRole('navigation').getByRole('button',{name:label,exact:true}).click();
   await expect(page.locator('.criteria-note')).toHaveCount(0);
   if(label!=='문제은행 관리')await expect(page.locator('main')).not.toContainText(/공식 출제기준 대조 대기|기출 미제공|잠정 규칙/);
 }
 await page.addInitScript(()=>{Storage.prototype.setItem=function(){throw new DOMException('Full','QuotaExceededError')};});
 await page.reload();await expect(page.getByRole('alert')).toContainText('기록을 저장하지 못했습니다');
});
