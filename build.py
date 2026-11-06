# -*- coding: utf-8 -*-
"""生成 5 套浅色系官网首页设计稿 + 方案总览画廊"""
import os
from design_data import (
    nav_html, hero_html, stats_html, ideas_html, products_html,
    experience_html, path_html, history_html, news_html, cta_html,
    footer_html, badge_html,
)

OUT = os.path.dirname(os.path.abspath(__file__))

FONT = '-apple-system, BlinkMacSystemFont, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Noto Sans SC", sans-serif'
SERIF = '"Songti SC", "STSong", "Noto Serif SC", "Source Han Serif SC", Georgia, serif'

BASE_CSS = r'''
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{font-family:FONT_PLACEHOLDER;background:var(--bg);color:var(--ink);line-height:1.6;-webkit-font-smoothing:antialiased;overflow-x:hidden}
a{text-decoration:none;color:inherit}
button{font:inherit;border:0;background:none;cursor:pointer}
img,svg{display:block}
.wrap{width:min(1180px,calc(100% - 64px));margin:0 auto}
.sec{padding:104px 0;position:relative}
.eyebrow{display:inline-block;font-size:12px;letter-spacing:.2em;font-weight:700;color:var(--acc);text-transform:uppercase}
h2{font-size:clamp(30px,3.6vw,50px);line-height:1.25;letter-spacing:-.03em;font-weight:700;margin:16px 0 18px}
.lead{font-size:16px;color:var(--ink-2);line-height:1.9;max-width:660px}
.sec-head{margin-bottom:52px}
.sec-head h2{margin-bottom:16px}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;padding:14px 26px;border-radius:999px;font-size:14px;font-weight:600;white-space:nowrap;transition:transform .25s,box-shadow .25s,background .25s}
.btn:hover{transform:translateY(-2px)}
.btn-primary{background:var(--acc);color:var(--acc-ink);box-shadow:0 10px 26px -10px var(--acc)}
.btn-primary:hover{box-shadow:0 16px 32px -10px var(--acc)}
.btn-ghost{background:var(--surface);color:var(--ink);border:1px solid var(--line)}
.arr{font-size:16px}
.nav{position:sticky;top:0;z-index:60;background:var(--nav-bg);border-bottom:1px solid var(--line);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px)}
.nav-in{width:min(1180px,calc(100% - 64px));margin:0 auto;height:72px;display:flex;align-items:center;gap:28px;position:relative}
.brand{display:flex;align-items:center;gap:10px;flex-shrink:0}
.brand-mark{width:34px;height:34px;border-radius:10px;background:var(--acc);color:var(--acc-ink);display:grid;place-items:center;font-size:17px;font-weight:700;font-family:SERIF_PLACEHOLDER}
.brand-txt{display:flex;flex-direction:column;line-height:1.15}
.brand-txt b{font-size:16px;letter-spacing:.04em}
.brand-txt small{font-size:9px;letter-spacing:.16em;color:var(--ink-3);margin-top:3px}
.nav-links{display:flex;gap:26px;margin-left:auto;align-items:center}
.nav-link{font-size:13.5px;color:var(--ink-2);transition:color .2s}
.nav-link:hover,.nav-link.is-active{color:var(--acc)}
.nav-cta{font-size:13px;font-weight:600;padding:10px 20px;border-radius:999px;background:var(--acc);color:var(--acc-ink);flex-shrink:0}
.nav-burger{display:none;flex-direction:column;gap:4px;margin-left:auto;padding:8px}
.nav-burger span{display:block;width:20px;height:2px;background:var(--ink)}
.dev{width:100%;height:auto;display:block}
.hero{position:relative;overflow:hidden;padding:96px 0 84px}
.hero-in{position:relative;z-index:2}
.hero-split{display:grid;grid-template-columns:1.05fr .95fr;gap:48px;align-items:center}
.hero-title{font-size:clamp(48px,6vw,86px);line-height:1.12;letter-spacing:-.04em;font-weight:700;margin:20px 0 24px}
.hero-desc{font-size:16.5px;color:var(--ink-2);line-height:1.9;max-width:620px}
.hero-btns{display:flex;gap:14px;flex-wrap:wrap;margin-top:34px}
.hero-note{font-size:11px;letter-spacing:.08em;color:var(--ink-3);margin-top:20px}
.hero-art{position:relative}
.stats{padding:0 0 20px}
.stats-grid{display:grid;grid-template-columns:repeat(4,1fr)}
.stat{padding:30px 24px;display:flex;flex-direction:column;gap:6px}
.stat b{font-size:clamp(22px,2.4vw,34px);font-weight:700;letter-spacing:-.03em}
.stat span{font-size:13px;color:var(--ink-2)}
.idea-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.idea-card{padding:34px 30px;border:1px solid var(--line);border-radius:var(--radius);background:var(--surface)}
.idea-no{display:block;font-size:13px;letter-spacing:.14em;color:var(--acc);font-weight:700;margin-bottom:26px}
.idea-card h3{font-size:20px;line-height:1.4;margin-bottom:14px;letter-spacing:-.01em}
.idea-card p{font-size:14px;color:var(--ink-2);line-height:1.85}
.prod-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:18px}
.prod-card{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);overflow:hidden;display:flex;flex-direction:column;transition:transform .3s,box-shadow .3s}
.prod-card:hover{transform:translateY(-6px)}
.prod-visual{background:var(--surface-2);min-height:238px;display:flex;align-items:center;justify-content:center;padding:32px 26px}
.prod-visual .dev-phone{max-width:118px}
.prod-visual .dev-tab{max-width:220px}
.prod-visual .dev-charge{max-width:140px}
.prod-info{padding:24px 22px 26px;display:flex;flex-direction:column;flex:1}
.prod-tag{font-size:11px;letter-spacing:.1em;color:var(--acc);font-weight:700}
.prod-info h3{font-size:17px;margin:12px 0 10px;letter-spacing:-.01em}
.prod-info p{font-size:13px;color:var(--ink-2);line-height:1.75;flex:1}
.prod-link{display:inline-flex;align-items:center;gap:8px;font-size:13px;font-weight:600;color:var(--acc);margin-top:22px}
.exp-body{display:grid;grid-template-columns:1.25fr .75fr;gap:56px;align-items:center}
.feat{padding:20px 0;border-bottom:1px solid var(--line);display:flex;gap:22px}
.feat:first-child{border-top:1px solid var(--line)}
.feat-no{font-size:12px;font-weight:700;color:var(--acc);letter-spacing:.1em;padding-top:6px}
.feat h3{font-size:17px;margin-bottom:7px}
.feat p{font-size:13.5px;color:var(--ink-2);line-height:1.75}
.exp-visual{position:relative;display:flex;justify-content:center}
.exp-visual .dev-phone{max-width:220px}
.exp-key{position:absolute;right:2%;top:42%;display:flex;align-items:center;gap:8px;font-size:12px;font-weight:600;color:var(--acc);background:var(--surface);border:1px solid var(--line);padding:8px 14px;border-radius:999px;box-shadow:0 8px 22px -12px var(--ink)}
.exp-key span{width:8px;height:8px;border-radius:50%;background:var(--acc)}
.steps-wrap{margin-top:70px}
.steps-title{font-size:20px;margin-bottom:26px}
.steps{display:grid;grid-template-columns:repeat(4,1fr);gap:18px}
.step{padding:24px 22px;border-radius:var(--radius);background:var(--surface-2)}
.step-no{display:grid;place-items:center;width:28px;height:28px;border-radius:50%;background:var(--acc);color:var(--acc-ink);font-size:13px;font-weight:700;margin-bottom:16px}
.step h4{font-size:16px;margin-bottom:8px}
.step p{font-size:13px;color:var(--ink-2);line-height:1.75}
.path-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}
.path-item{padding:34px 30px;border:1px solid var(--line);border-radius:var(--radius);background:var(--surface)}
.path-no{font-size:12px;letter-spacing:.14em;font-weight:700;color:var(--acc)}
.path-item h3{font-size:22px;margin:22px 0 12px}
.path-item p{font-size:14px;color:var(--ink-2);line-height:1.8}
.history-body{display:grid;grid-template-columns:1.35fr .75fr;gap:48px;align-items:start}
.time-row{display:grid;grid-template-columns:130px 1fr;gap:24px;padding:26px 0;border-bottom:1px solid var(--line)}
.time-row:first-child{border-top:1px solid var(--line)}
.time-row b{font-size:20px;letter-spacing:-.02em;color:var(--acc)}
.time-row p{font-size:14.5px;color:var(--ink-2);line-height:1.85}
.promise{padding:34px 30px;background:var(--surface-2);border-radius:var(--radius)}
.promise h3{font-size:20px;margin-bottom:20px}
.promise ul{list-style:none;display:flex;flex-direction:column;gap:16px}
.promise li{font-size:14px;color:var(--ink-2);line-height:1.7;padding-left:20px;position:relative}
.promise li:before{content:"";position:absolute;left:0;top:9px;width:7px;height:7px;border-radius:50%;background:var(--acc)}
.news-body{display:grid;grid-template-columns:1.35fr .75fr;gap:48px;align-items:start}
.news-row{display:grid;grid-template-columns:96px 1fr 20px;gap:22px;padding:22px 0;border-bottom:1px solid var(--line);align-items:start}
.news-row:first-child{border-top:1px solid var(--line)}
.news-row time{font-size:13px;color:var(--acc);font-weight:700;letter-spacing:.04em;padding-top:4px}
.news-row h3{font-size:16px;margin-bottom:6px}
.news-row p{font-size:13px;color:var(--ink-2);line-height:1.7}
.news-arr{color:var(--ink-3);font-size:15px}
.quote{padding:36px 32px;background:var(--surface-2);border-radius:var(--radius)}
.quote-mark{font-size:56px;line-height:.7;color:var(--acc);font-family:Georgia,serif;display:block;margin-bottom:16px}
.quote h3{font-size:19px;margin-bottom:14px}
.quote p{font-size:14.5px;color:var(--ink-2);line-height:1.9}
.cta{padding:104px 0;text-align:center;background:var(--surface-2);position:relative;overflow:hidden}
.cta-in{position:relative;z-index:2}
.cta h2{font-size:clamp(30px,4vw,54px);margin:18px 0 14px}
.cta p{font-size:16px;color:var(--ink-2)}
.cta-btns{display:flex;gap:14px;justify-content:center;margin-top:34px;flex-wrap:wrap}
.foot{padding:64px 0 30px;background:var(--bg-2);border-top:1px solid var(--line)}
.foot-top{display:grid;grid-template-columns:1fr 1.4fr;gap:48px;padding-bottom:44px}
.foot-brand{display:flex;gap:12px;align-items:flex-start}
.foot-brand b{font-size:18px;display:block}
.foot-brand small{font-size:11.5px;color:var(--ink-3);display:block;margin-top:4px}
.foot-cols{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}
.foot-col h4{font-size:13px;margin-bottom:16px}
.foot-col a{display:block;font-size:13px;color:var(--ink-2);margin-bottom:10px}
.foot-col a:hover{color:var(--acc)}
.foot-bottom{display:flex;justify-content:space-between;gap:20px;padding-top:22px;border-top:1px solid var(--line);font-size:12px;color:var(--ink-3);flex-wrap:wrap}
.foot-note{font-size:11px;color:var(--ink-3);margin-top:14px;opacity:.8}
.draft-badge{position:fixed;right:20px;bottom:20px;z-index:99;display:flex;align-items:center;gap:10px;background:rgba(255,255,255,.94);border:1px solid rgba(0,0,0,.09);box-shadow:0 8px 30px rgba(0,0,0,.10);border-radius:14px;padding:9px 14px 9px 9px;backdrop-filter:blur(10px)}
.badge-idx{width:30px;height:30px;border-radius:9px;background:var(--acc);color:var(--acc-ink);display:grid;place-items:center;font-size:12px;font-weight:700}
.badge-txt{display:flex;flex-direction:column;line-height:1.3}
.badge-txt b{font-size:12px;color:#1b1b1f}
.badge-txt small{font-size:10px;color:#777}
@media(max-width:1000px){
  .wrap,.nav-in{width:calc(100% - 40px)}
  .sec{padding:76px 0}
  .nav-links{display:none}
  .nav-burger{display:flex}
  .nav-cta{margin-left:0}
  .hero-split{grid-template-columns:1fr;gap:40px}
  .hero{padding:70px 0 60px}
  .prod-grid{grid-template-columns:repeat(2,1fr)}
  .exp-body,.history-body,.news-body{grid-template-columns:1fr;gap:36px}
  .exp-visual{order:-1}
  .exp-visual .dev-phone{max-width:190px}
  .steps{grid-template-columns:repeat(2,1fr)}
  .idea-grid,.path-grid{grid-template-columns:1fr 1fr}
  .foot-top{grid-template-columns:1fr}
}
@media(max-width:640px){
  .wrap,.nav-in{width:calc(100% - 32px)}
  .sec{padding:58px 0}
  .hero-title{font-size:40px}
  h2{font-size:28px}
  .stats-grid,.idea-grid,.prod-grid,.path-grid,.steps{grid-template-columns:1fr}
  .time-row{grid-template-columns:1fr;gap:8px}
  .news-row{grid-template-columns:1fr;gap:6px}
  .news-arr{display:none}
  .foot-cols{grid-template-columns:1fr 1fr}
  .draft-badge{right:12px;bottom:12px;padding:7px 10px 7px 7px}
  .badge-txt small{display:none}
}
'''.replace("FONT_PLACEHOLDER", FONT).replace("SERIF_PLACEHOLDER", SERIF)


CLOUD_CSS = r'''
body{background:radial-gradient(120% 60% at 50% 0%,#ffffff 0%,var(--bg) 60%)}
.nav{--nav-bg:rgba(255,255,255,.78)}
.hero-cloud{text-align:center;padding-top:78px;padding-bottom:56px}
.hero-glow{position:absolute;width:900px;height:600px;left:50%;top:-180px;transform:translateX(-50%);background:radial-gradient(ellipse,rgba(150,165,200,.18),transparent 65%);pointer-events:none}
.hero-cloud .hero-title{font-size:clamp(52px,8vw,104px);font-weight:650;letter-spacing:-.055em;background:linear-gradient(160deg,#101116 25%,#4a4e5c 75%,#8a8f9e);-webkit-background-clip:text;background-clip:text;color:transparent}
.hero-cloud .hero-desc{margin:0 auto}
.hero-cloud .hero-btns{justify-content:center}
.hero-stage{margin-top:52px;display:flex;align-items:flex-end;justify-content:center;gap:18px;min-height:390px}
.stage-main{width:220px;flex-shrink:0;filter:drop-shadow(0 40px 50px rgba(40,45,65,.20))}
.stage-side{width:290px;flex-shrink:0;opacity:.82;filter:drop-shadow(0 30px 40px rgba(40,45,65,.14))}
.stage-side.right{width:140px}
.stage-side.left{transform:translateY(26px)}
.stage-side.right{transform:translateY(34px)}
.stats-grid{border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.stat{border-right:1px solid var(--line)}
.stat:last-child{border-right:0}
.idea-card{box-shadow:0 16px 44px -30px rgba(20,24,40,.35);border-color:rgba(0,0,0,.045)}
.idea-no{font-size:32px;letter-spacing:-.04em;color:var(--ink-3);opacity:.45;font-weight:600;margin-bottom:20px}
.products{background:var(--bg-2)}
.prod-card{box-shadow:0 18px 44px -34px rgba(20,24,40,.4)}
.prod-visual{background:linear-gradient(180deg,#f6f7fa,#eceef3)}
.experience{background:var(--bg-2)}
.exp-visual:before{content:"";position:absolute;width:340px;height:340px;border-radius:50%;background:radial-gradient(circle,rgba(140,155,190,.16),transparent 70%);left:50%;top:50%;transform:translate(-50%,-50%)}
.step{background:#f4f5f8;border:1px solid var(--line)}
.path-item{border-color:transparent;background:#f4f5f8}
.path-no{font-size:30px;letter-spacing:-.04em;color:var(--ink-3);opacity:.5}
.cta{background:var(--bg-2);border-top:1px solid var(--line)}
@media(max-width:1000px){.hero-stage{min-height:auto;flex-wrap:wrap;gap:8px;margin-top:48px}.stage-main{width:190px}.stage-side{width:150px}.stage-side.left,.stage-side.right{transform:none;width:120px}.idea-grid{grid-template-columns:1fr 1fr}}
@media(max-width:640px){.hero-stage{flex-direction:column;align-items:center}.stage-side{display:none}.stage-main{width:210px}}
'''

WARM_CSS = r'''
body{background-color:var(--bg);background-image:repeating-linear-gradient(0deg,rgba(160,130,90,.025) 0 1px,transparent 1px 5px)}
h2,.hero-title,.idea-card h3,.path-item h3,.cta h2,.promise h3,.quote h3{font-family:SERIF_PLACEHOLDER;letter-spacing:.01em}
.nav{--nav-bg:rgba(255,253,248,.9);border-bottom:1px solid var(--line)}
.brand-mark{border-radius:6px;background:var(--acc);font-size:18px}
.nav-in:after{content:"";position:absolute;left:0;right:0;bottom:-1px;height:1px;background:linear-gradient(90deg,transparent,var(--acc-2),transparent);opacity:.6}
.hero-warm{padding:88px 0 70px}
.hero-warm:before{content:"";position:absolute;right:-140px;top:-120px;width:620px;height:620px;border:1px solid rgba(166,96,60,.13);border-radius:50%}
.hero-warm:after{content:"";position:absolute;right:-60px;top:-40px;width:460px;height:460px;border:1px solid rgba(166,96,60,.10);border-radius:50%}
.hero-copy{position:relative}
.warm-seal{position:absolute;right:8%;top:-22px;width:62px;height:62px;border:2px solid var(--acc);border-radius:50%;color:var(--acc);display:grid;place-items:center;font-family:SERIF_PLACEHOLDER;font-size:19px;line-height:1.05;text-align:center;transform:rotate(-8deg);opacity:.85}
.hero-warm .hero-title{font-size:clamp(44px,5vw,68px);font-weight:600;letter-spacing:.02em}
.warm-rule{display:block;width:66px;height:2px;background:var(--acc-2);margin:0 0 24px}
.hero-warm .hero-desc{font-size:16px}
.hero-art{min-height:520px;display:flex;align-items:center;justify-content:center}
.warm-halo{position:absolute;width:400px;height:400px;border-radius:50%;background:radial-gradient(circle,rgba(201,162,39,.20),rgba(201,162,39,.04) 60%,transparent 72%);left:50%;top:50%;transform:translate(-50%,-50%)}
.vtext{position:absolute;right:0;top:8%;writing-mode:vertical-rl;font-size:11px;letter-spacing:.32em;color:var(--ink-3)}
.art-tab{position:absolute;width:390px;left:0;bottom:56px;transform:rotate(-3deg);filter:drop-shadow(0 26px 34px rgba(90,60,30,.20))}
.art-phone{position:absolute;width:180px;right:24px;top:10px;transform:rotate(5deg);filter:drop-shadow(0 26px 34px rgba(90,60,30,.24))}
.hero-warm .hero-note{position:absolute;bottom:10px;left:0;right:0;text-align:center}
.stats-grid{gap:14px;padding-top:14px}
.stat{background:var(--surface);border:1px solid var(--line);border-top:2px solid var(--acc-2);text-align:center;align-items:center;position:relative}
.stat:before{content:"◇";position:absolute;top:8px;right:12px;font-size:11px;color:var(--acc-2)}
.stat b{font-family:SERIF_PLACEHOLDER;color:var(--acc)}
.idea-card{position:relative;border-radius:4px;background:var(--surface);box-shadow:0 12px 28px -24px rgba(80,50,20,.5)}
.idea-card:before{content:"";position:absolute;top:0;left:0;width:38px;height:2px;background:var(--acc)}
.idea-no{font-family:Georgia,serif;color:var(--acc-2)}
.prod-card{border-radius:4px;border-color:var(--line)}
.prod-visual{background:linear-gradient(160deg,#f8f0e3,#f1e5d2)}
.prod-tag{color:var(--acc)}
.feat{border-color:var(--line)}
.feat-no{font-family:Georgia,serif;color:var(--acc-2)}
.exp-visual{background:radial-gradient(circle,rgba(201,162,39,.14),transparent 68%);padding:30px;border-radius:50%}
.step{background:var(--surface);border:1px solid var(--line);border-top:2px solid var(--acc-2);border-radius:4px}
.step-no{background:var(--acc-2);border-radius:50%}
.path-item{border-radius:4px;background:var(--surface)}
.path-no{font-family:Georgia,serif;color:var(--acc-2)}
.promise{border:1px solid var(--line);border-radius:4px;background:var(--surface)}
.quote{border-left:3px solid var(--acc);border-radius:0;background:var(--surface)}
.quote-mark{color:var(--acc-2)}
.cta{background:var(--surface-2);border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.cta:before{content:"幸";position:absolute;right:6%;top:50%;transform:translateY(-50%);font-family:SERIF_PLACEHOLDER;font-size:280px;color:rgba(166,96,60,.055);line-height:1}
.btn-ghost{border-color:var(--acc-2)}
@media(max-width:1000px){.hero-art{min-height:420px}.art-tab{width:300px;left:2%}.art-phone{width:140px;right:6%}.warm-seal{right:2%}}
@media(max-width:640px){.hero-art{min-height:340px}.art-tab{width:230px}.art-phone{width:110px}.vtext{display:none}}
'''.replace("SERIF_PLACEHOLDER", SERIF)

MINT_CSS = r'''
body{background:linear-gradient(175deg,#f4faf8 0%,#ffffff 42%,#f6fbf9 100%)}
.blob{position:absolute;border-radius:50%;filter:blur(80px);pointer-events:none}
.blob-a{width:520px;height:520px;background:rgba(111,207,184,.30);top:-180px;right:-120px}
.blob-b{width:420px;height:420px;background:rgba(120,190,220,.22);top:260px;left:-180px}
.nav{--nav-bg:transparent;border-bottom:0;background:transparent;backdrop-filter:none}
.nav-in{margin-top:14px;height:60px;background:rgba(255,255,255,.68);border:1px solid rgba(255,255,255,.9);border-radius:999px;padding:0 22px;width:min(1140px,calc(100% - 48px));box-shadow:0 8px 30px -18px rgba(20,90,75,.4);backdrop-filter:blur(18px);-webkit-backdrop-filter:blur(18px)}
.nav-cta{border-radius:999px}
.hero-mint{padding-top:76px}
.hero-mint .hero-title{font-size:clamp(46px,5.6vw,76px);font-weight:750;color:var(--ink)}
.hero-mini{margin-top:30px;font-size:12.5px;letter-spacing:.06em;color:var(--acc);background:rgba(255,255,255,.7);border:1px solid var(--line);display:inline-block;padding:10px 18px;border-radius:999px}
.glass-hero{background:rgba(255,255,255,.58);border:1px solid rgba(255,255,255,.95);border-radius:30px;padding:34px 30px 22px;min-height:480px;box-shadow:0 26px 60px -34px rgba(20,100,85,.5);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);display:flex;flex-direction:column;align-items:center}
.ai-chip{align-self:flex-start;display:inline-flex;align-items:center;gap:8px;font-size:12px;font-weight:600;color:var(--acc);background:rgba(255,255,255,.85);padding:8px 14px;border-radius:999px;border:1px solid var(--line)}
.ai-chip .dot{width:7px;height:7px;border-radius:50%;background:var(--acc);box-shadow:0 0 0 4px rgba(33,127,108,.14)}
.ai-bubble{align-self:flex-end;max-width:78%;font-size:12.5px;background:var(--acc);color:#fff;padding:11px 16px;border-radius:16px 16px 4px 16px;margin-top:20px}
.ai-reply{align-self:flex-start;background:rgba(255,255,255,.9);color:var(--ink-2);border:1px solid var(--line);border-radius:16px 16px 16px 4px;margin-top:10px}
.glass-hero .art-phone{width:160px;margin-top:-6px}
.glass-hero .hero-note{margin-top:8px;text-align:center}
.stats-grid{gap:14px}
.stat{background:rgba(255,255,255,.66);border:1px solid rgba(255,255,255,.9);border-radius:22px;box-shadow:0 14px 36px -28px rgba(20,100,85,.55);backdrop-filter:blur(14px)}
.stat b{color:var(--acc)}
.stats{padding-top:8px}
.idea-card{background:rgba(255,255,255,.68);border-color:rgba(255,255,255,.95);backdrop-filter:blur(16px);box-shadow:0 18px 40px -30px rgba(20,100,85,.5)}
.prod-card{background:rgba(255,255,255,.7);border-color:rgba(255,255,255,.95);backdrop-filter:blur(14px);box-shadow:0 18px 40px -32px rgba(20,100,85,.5)}
.prod-visual{background:rgba(232,245,241,.65)}
.prod-card:hover{box-shadow:0 28px 50px -30px rgba(20,100,85,.55)}
.feat-list{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.feat{border:1px solid rgba(255,255,255,.95);background:rgba(255,255,255,.68);border-radius:20px;padding:22px;backdrop-filter:blur(14px);display:block}
.feat:first-child{border-top:1px solid rgba(255,255,255,.95)}
.feat-no{display:block;margin-bottom:12px}
.exp-visual{background:radial-gradient(circle,rgba(111,207,184,.26),transparent 68%);padding:28px}
.step{background:rgba(255,255,255,.7);border:1px solid rgba(255,255,255,.95);backdrop-filter:blur(12px)}
.step-no{background:linear-gradient(135deg,var(--acc),var(--acc-2))}
.path-item{background:rgba(255,255,255,.7);border-color:rgba(255,255,255,.95);backdrop-filter:blur(14px)}
.promise,.quote{background:rgba(255,255,255,.7);border:1px solid rgba(255,255,255,.95);backdrop-filter:blur(14px)}
.cta{background:linear-gradient(140deg,rgba(204,238,228,.8),rgba(226,244,240,.6));border-top:1px solid rgba(255,255,255,.9)}
@media(max-width:1000px){.blob-a{width:340px;height:340px}.glass-hero{min-height:auto}.feat-list{grid-template-columns:1fr 1fr}}
@media(max-width:640px){.feat-list{grid-template-columns:1fr}.nav-in{width:calc(100% - 24px)}.ai-bubble{max-width:92%}}
'''

LILAC_CSS = r'''
body{background:linear-gradient(180deg,#fdfaff 0%,#f8f3ff 55%,#fff 100%)}
.lilac-orb{position:absolute;border-radius:50%;filter:blur(70px);pointer-events:none}
.orb-1{width:460px;height:460px;background:rgba(180,145,235,.30);top:-160px;left:-120px}
.orb-2{width:400px;height:400px;background:rgba(240,170,205,.28);top:60px;right:-130px}
.nav{--nav-bg:transparent;border-bottom:0;background:transparent;backdrop-filter:none}
.nav-in{margin-top:14px;height:62px;background:rgba(255,255,255,.86);border-radius:999px;padding:0 22px;width:min(1140px,calc(100% - 48px));box-shadow:0 12px 34px -20px rgba(90,60,150,.45);backdrop-filter:blur(18px)}
.hero-lilac{text-align:center;padding-top:70px}
.lucky-badge{display:inline-flex;align-items:center;gap:8px;padding:9px 18px;border-radius:999px;background:#fff;box-shadow:0 10px 26px -16px rgba(110,70,180,.6);font-size:12.5px;font-weight:700;color:var(--acc)}
.lucky-badge span{font-size:10px;letter-spacing:.14em;color:var(--ink-3);font-weight:600}
.hero-lilac .eyebrow{display:block;margin-top:18px}
.hero-lilac .hero-title{font-size:clamp(52px,7.4vw,96px);font-weight:800;letter-spacing:-.05em;background:linear-gradient(100deg,#4b3285,#7c5bd6 45%,#e8a0c8);-webkit-background-clip:text;background-clip:text;color:transparent}
.title-dot{color:var(--acc-2);-webkit-text-fill-color:var(--acc-2)}
.hero-lilac .hero-desc{margin:0 auto}
.hero-lilac .hero-btns{justify-content:center}
.btn-primary{background:linear-gradient(110deg,var(--acc),#a173e8);box-shadow:0 14px 30px -12px var(--acc)}
.hero-collage{display:flex;align-items:flex-end;justify-content:center;gap:18px;margin-top:66px;min-height:330px}
.collage-card{background:#fff;border-radius:30px;padding:22px;box-shadow:0 24px 50px -28px rgba(80,50,140,.55);border:1px solid rgba(255,255,255,.9)}
.collage-card.c1{width:300px;transform:translateY(20px) rotate(-5deg)}
.collage-card.c2{width:190px;transform:translateY(-16px);z-index:2}
.collage-card.c3{width:180px;transform:translateY(28px) rotate(6deg)}
.collage-card .dev-tab{width:100%}
.stats-grid{gap:16px}
.stat{border-radius:26px;text-align:center;align-items:center;padding:28px 18px}
.stat:nth-child(1){background:#f0e9ff}.stat:nth-child(2){background:#ffecf4}.stat:nth-child(3){background:#fff5dc}.stat:nth-child(4){background:#e7f4ff}
.stat b{color:var(--acc)}
.idea-card{border-radius:30px;border:0;position:relative;overflow:hidden;padding:40px 30px 34px}
.idea-card:nth-child(1){background:#f2ecff}.idea-card:nth-child(2){background:#ffeff6}.idea-card:nth-child(3){background:#fff4e4}
.idea-card:before{content:"";position:absolute;width:130px;height:130px;border-radius:50%;right:-40px;top:-46px;background:rgba(255,255,255,.55)}
.idea-no{position:relative;font-size:12px}
.idea-card h3,.idea-card p{position:relative}
.prod-card{border-radius:30px;border:0;box-shadow:0 20px 46px -32px rgba(80,50,140,.5)}
.prod-card:nth-child(even){transform:translateY(18px)}
.prod-card:hover{transform:translateY(-2px)}
.prod-visual{background:linear-gradient(160deg,#f7f1ff,#fdf3fa);min-height:230px}
.feat{border-color:var(--line);border-radius:22px;padding:20px 22px;margin-bottom:12px;background:#fff}
.feat:first-child{border-top:1px solid var(--line)}
.feat-no{background:var(--surface-2);color:var(--acc);width:30px;height:30px;border-radius:50%;display:grid;place-items:center;flex-shrink:0;font-size:12px}
.exp-visual{background:radial-gradient(circle,rgba(180,145,235,.24),transparent 68%);padding:26px;border-radius:50%}
.step{background:#fff;border:1px solid var(--line)}
.step-no{background:linear-gradient(135deg,var(--acc),var(--acc-2));width:34px;height:34px}
.path-item{border:0;border-radius:30px;background:#fff;box-shadow:0 18px 40px -32px rgba(80,50,140,.5);text-align:center}
.path-no{display:grid;place-items:center;width:52px;height:52px;border-radius:50%;background:var(--surface-2);margin:0 auto;font-size:16px}
.path-item h3{margin-top:20px}
.promise{border-radius:30px;background:#f2ecff}
.quote{border-radius:30px;background:linear-gradient(140deg,#f0e7ff,#ffeaf4);position:relative}
.quote-mark{color:var(--acc)}
.cta{background:linear-gradient(125deg,#ede4ff,#ffe9f4 60%,#fff3df)}
.cta .btn-ghost{background:rgba(255,255,255,.8)}
@media(max-width:1000px){.hero-collage{min-height:auto;margin-top:44px}.collage-card.c1{width:220px}.collage-card.c2{width:140px}.collage-card.c3{width:130px}.prod-card:nth-child(even){transform:none}}
@media(max-width:640px){.hero-collage{flex-direction:column;align-items:center}.collage-card{width:230px !important;transform:none !important}.lilac-orb{display:none}}
'''

EDIT_CSS = r'''
body{background:#fff}
h2,.hero-title,.sec-head,.idea-card h3,.path-item h3,.cta h2,.quote h3,.prod-info h3,.step h4,.promise h3{font-family:SERIF_PLACEHOLDER}
.eyebrow{font-family:FONT_PLACEHOLDER;letter-spacing:.24em;color:var(--acc)}
.nav{--nav-bg:#fff;border-bottom:2px solid var(--ink);border-radius:0;backdrop-filter:none}
.brand-mark{border-radius:0;background:var(--ink)}
.nav-link{font-size:12.5px;letter-spacing:.02em}
.nav-cta{background:var(--ink);border-radius:0;padding:10px 18px}
.edit-strip{display:flex;justify-content:space-between;gap:16px;font-size:10.5px;letter-spacing:.2em;color:var(--ink-3);border-bottom:1px solid var(--line);padding:12px 0;margin-bottom:34px}
.hero-edit{padding:40px 0 0}
.hero-edit .hero-split{gap:60px;align-items:start}
.hero-edit .hero-title{font-size:clamp(56px,7.6vw,108px);line-height:1.03;letter-spacing:-.06em;font-weight:700;margin:22px 0 26px}
.edit-ink{color:var(--acc)}
.edit-rule{display:block;width:100%;max-width:190px;height:5px;background:var(--ink);margin:0 0 26px}
.hero-edit .hero-desc{font-size:15.5px;max-width:480px}
.hero-edit .btn{border-radius:0}
.hero-edit .btn-primary{background:var(--acc);box-shadow:none}
.hero-edit .btn-primary:hover{box-shadow:none;background:var(--ink)}
.edit-art{padding-top:20px}
.edit-frame{background:var(--surface-2);border:1px solid var(--ink);padding:46px 30px 30px;position:relative;display:flex;justify-content:center}
.edit-frame .dev-phone{max-width:230px}
.frame-tag{position:absolute;left:16px;top:16px;font-size:10px;letter-spacing:.16em;color:var(--ink-2);font-family:FONT_PLACEHOLDER}
.edit-marquee{margin-top:56px;border-top:1px solid var(--line);border-bottom:1px solid var(--line);padding:16px 0;white-space:nowrap;overflow:hidden;font-family:FONT_PLACEHOLDER;font-size:clamp(24px,3.6vw,46px);font-weight:800;letter-spacing:-.02em;color:transparent;-webkit-text-stroke:1px #b6b6ad}
.stats{padding-top:6px}
.stats-grid{gap:0}
.stat{border-top:3px solid var(--ink);padding:26px 20px 26px 0;border-right:0}
.stat b{font-family:SERIF_PLACEHOLDER;font-size:30px}
.sec-head{border-bottom:1px solid var(--line);padding-bottom:26px;margin-bottom:44px}
.idea-grid{gap:0}
.idea-card{border:0;border-right:1px solid var(--line);border-radius:0;padding:0 28px 0 0;background:transparent}
.idea-card:last-child{border-right:0}
.idea-card:not(:first-child){padding-left:28px}
.idea-no{font-family:Georgia,serif;font-size:14px;color:var(--acc);margin-bottom:22px}
.idea-card h3{font-size:22px}
.prod-grid{gap:0}
.prod-card{border:0;border-top:1px solid var(--line);border-radius:0;background:transparent}
.prod-card:hover{transform:none}
.prod-card:before{content:"0" counter(pcard);counter-increment:pcard;font-family:Georgia,serif;font-size:12px;color:var(--acc)}
.prod-grid{counter-reset:pcard}
.prod-visual{background:var(--surface-2);min-height:250px}
.prod-info{padding:22px 20px 26px 0}
.prod-info h3{font-size:18px}
.prod-link{color:var(--ink);border-bottom:1px solid var(--ink);align-self:flex-start;padding-bottom:3px;margin-top:20px}
.feat{border-color:var(--line);gap:26px;padding:22px 0}
.feat:first-child{border-top:1px solid var(--ink)}
.feat-no{font-family:Georgia,serif;color:var(--acc)}
.feat h3{font-family:SERIF_PLACEHOLDER;font-size:20px}
.exp-visual{background:var(--surface-2);border:1px solid var(--ink);padding:34px}
.steps-title{font-family:SERIF_PLACEHOLDER;font-size:24px;border-bottom:1px solid var(--ink);padding-bottom:14px}
.steps{gap:0}
.step{border-radius:0;border-top:1px solid var(--line);background:transparent;padding:24px 20px 24px 0}
.step-no{border-radius:0;background:var(--ink);width:26px;height:26px}
.step h4{font-size:18px}
.path-grid{gap:0}
.path-item{border-radius:0;border:0;border-top:1px solid var(--ink);background:transparent;padding:28px 26px 28px 0}
.path-no{font-family:Georgia,serif;font-size:40px;color:var(--acc);line-height:1}
.path-item h3{font-size:24px;margin:18px 0 10px}
.time-row{border-color:var(--line)}
.time-row:first-child{border-top:1px solid var(--ink)}
.time-row b{font-family:Georgia,serif;color:var(--ink)}
.promise{border-radius:0;border:1px solid var(--ink);background:var(--surface-2)}
.promise h3{font-size:22px}
.news-row{border-color:var(--line);grid-template-columns:110px 1fr 20px}
.news-row:first-child{border-top:1px solid var(--ink)}
.news-row time{font-family:Georgia,serif;color:var(--acc)}
.news-row h3{font-family:SERIF_PLACEHOLDER;font-size:19px}
.quote{border-radius:0;border:1px solid var(--ink);background:var(--surface-2)}
.quote-mark{color:var(--acc)}
.cta{background:#fff;border-top:1px solid var(--ink)}
.cta h2{font-size:clamp(34px,5.2vw,68px);letter-spacing:-.05em}
.cta .btn{border-radius:0}
.cta .btn-ghost{border:1px solid var(--ink)}
.foot{background:#fff;border-top:2px solid var(--ink)}
@media(max-width:1000px){.edit-strip span:nth-child(2){display:none}.hero-edit .hero-split{gap:36px}.edit-marquee{font-size:26px}.idea-card{border-right:0;border-bottom:1px solid var(--line);padding:20px 0}.idea-card:not(:first-child){padding-left:0}}
@media(max-width:640px){.edit-strip span:last-child{display:none}}
'''.replace("SERIF_PLACEHOLDER", SERIF).replace("FONT_PLACEHOLDER", FONT)


THEMES = [
    dict(key="cloud", idx=1, name="云白 · 极简", en="CLOUD WHITE / MINIMAL",
         desc="大留白、无彩灰阶、居中构图，产品为唯一主角",
         css=CLOUD_CSS, vars=dict(
             bg="#fafafc", bg2="#ffffff", surface="#ffffff", surface2="#f4f5f8",
             ink="#16161a", ink2="#55565f", ink3="#9a9ca6", line="#e7e8ee",
             acc="#2f3542", acc2="#8e94a8", accink="#ffffff", navbg="rgba(255,255,255,.78)",
             dev1="#f3f4f7", dev2="#d9dce4", devline="#bfc3cd", devhi="#ffffff", devshadow="#8a8fa0",
             scr1="#2b2e38", scr2="#4b5162", scrcard="rgba(255,255,255,.10)", scrink="#ffffff", radius="18px")),
    dict(key="warm", idx=2, name="暖米 · 东方", en="WARM RICE / ORIENTAL",
         desc="米色纸感、赤陶朱印、衬线排版，呼应东方美学点缀",
         css=WARM_CSS, vars=dict(
             bg="#faf5ec", bg2="#fffdf8", surface="#fffdf8", surface2="#f5eddf",
             ink="#2c2620", ink2="#6a5c4c", ink3="#9b8c79", line="#e7dbc7",
             acc="#a6603c", acc2="#c9a227", accink="#fffdf8", navbg="rgba(255,253,248,.9)",
             dev1="#efe2ce", dev2="#d9c3a5", devline="#c2a883", devhi="#fffbf2", devshadow="#a98d6a",
             scr1="#3e342a", scr2="#6b5540", scrcard="rgba(255,246,230,.12)", scrink="#fff6e8", radius="6px")),
    dict(key="mint", idx=3, name="薄荷 · 轻盈科技", en="MINT GLASS / AI",
         desc="淡青绿渐变、玻璃拟态与 AI 对话气泡，突出科技感",
         css=MINT_CSS, vars=dict(
             bg="#f4faf8", bg2="#ffffff", surface="rgba(255,255,255,.72)", surface2="#e8f5f1",
             ink="#12322c", ink2="#4c6b64", ink3="#7c9b93", line="#d8ebe5",
             acc="#217f6c", acc2="#6fcfb8", accink="#ffffff", navbg="transparent",
             dev1="#effffb", dev2="#c8e9e0", devline="#9ccfbe", devhi="#ffffff", devshadow="#6fae9b",
             scr1="#12483e", scr2="#1e7a67", scrcard="rgba(255,255,255,.14)", scrink="#f2fffb", radius="22px")),
    dict(key="lilac", idx=4, name="柔紫 · 幸运感", en="LILAC / LUCKY",
         desc="柔紫粉光晕、圆润卡片与错落产品拼贴，面向年轻人群",
         css=LILAC_CSS, vars=dict(
             bg="#fbf8ff", bg2="#ffffff", surface="#ffffff", surface2="#f3edff",
             ink="#2a2140", ink2="#635b7e", ink3="#948bae", line="#e9e1f7",
             acc="#7c5bd6", acc2="#e8a0c8", accink="#ffffff", navbg="transparent",
             dev1="#f6eeff", dev2="#dcc9f5", devline="#bfa5e8", devhi="#ffffff", devshadow="#9b84cd",
             scr1="#4b3285", scr2="#8b5bc7", scrcard="rgba(255,255,255,.16)", scrink="#ffffff", radius="30px")),
    dict(key="editorial", idx=5, name="杂志 · 编辑排版", en="EDITORIAL / PRINT",
         desc="黑白网格、超大衬线标题与朱红点缀，画册式信息编排",
         css=EDIT_CSS, vars=dict(
             bg="#ffffff", bg2="#f5f5f2", surface="#ffffff", surface2="#f1f1ee",
             ink="#111111", ink2="#4a4a4a", ink3="#8a8a8a", line="#dcdcd7",
             acc="#c8382b", acc2="#111111", accink="#ffffff", navbg="#ffffff",
             dev1="#f0f0ec", dev2="#d6d6d0", devline="#b9b9b2", devhi="#ffffff", devshadow="#9a9a92",
             scr1="#1a1a1a", scr2="#3a3a3a", scrcard="rgba(255,255,255,.10)", scrink="#ffffff", radius="0px")),
]


def root_vars(v):
    return ":root{" + ";".join([
        f"--bg:{v['bg']}", f"--bg-2:{v['bg2']}", f"--surface:{v['surface']}",
        f"--surface-2:{v['surface2']}", f"--ink:{v['ink']}", f"--ink-2:{v['ink2']}",
        f"--ink-3:{v['ink3']}", f"--line:{v['line']}", f"--acc:{v['acc']}",
        f"--acc-2:{v['acc2']}", f"--acc-ink:{v['accink']}", f"--nav-bg:{v['navbg']}",
        f"--dev-1:{v['dev1']}", f"--dev-2:{v['dev2']}", f"--dev-line:{v['devline']}",
        f"--dev-hi:{v['devhi']}", f"--dev-shadow:{v['devshadow']}",
        f"--scr-1:{v['scr1']}", f"--scr-2:{v['scr2']}", f"--scr-card:{v['scrcard']}",
        f"--scr-ink:{v['scrink']}", f"--radius:{v['radius']}",
    ]) + ";}"


def build_theme(t):
    k = t["key"]
    body = "".join([
        nav_html(t["name"], t["idx"]),
        hero_html(k), stats_html(k), ideas_html(k), products_html(k),
        experience_html(k), path_html(k), history_html(k), news_html(k),
        cta_html(k), footer_html(), badge_html(t["idx"], t["name"], t["en"]),
    ])
    css = root_vars(t["vars"]) + BASE_CSS + t["css"] + MOBILE_FIX_CSS
    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="theme-color" content="{t["vars"]["bg"]}">
<title>幸运无限官网设计稿 {t["idx"]:02d} · {t["name"]} · Lucky Infinite</title>
<style>
{css}
</style>
</head>
<body class="t-{k}">
{body}
<script>
document.querySelectorAll('.nav-link,.prod-link,.btn,.foot-col a').forEach(function(a){{
  a.addEventListener('click',function(e){{
    var h=this.getAttribute('href')||'';
    if(h.startsWith('#')){{e.preventDefault();var el=document.querySelector(h);if(el)el.scrollIntoView({{behavior:'smooth',block:'start'}});}}
  }});
}});
var burger=document.querySelector('.nav-burger');
if(burger)burger.addEventListener('click',function(){{
  var n=document.querySelector('.nav-links');
  if(!n)return;
  var open=n.style.display==='flex';
  n.style.display=open?'':'flex';
  if(!open)Object.assign(n.style,{{position:'absolute',top:'72px',left:'0',right:'0',background:'var(--bg-2)',flexDirection:'column',padding:'18px 24px',gap:'14px',borderBottom:'1px solid var(--line)',boxShadow:'0 20px 30px -20px rgba(0,0,0,.3)'}});
}});
</script>
</body>
</html>'''
    path = os.path.join(OUT, f"design-{t['idx']:02d}-{k}.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    return path


MOBILE_FIX_CSS = """
/* 主题里的 .hero-xxx .hero-title 特异性高于基础媒体查询，需在最后用更高特异性覆盖 */
@media(max-width:640px){
  body.t-cloud .hero-title{font-size:40px}
  body.t-warm .hero-title{font-size:38px}
  body.t-mint .hero-title{font-size:40px}
  body.t-lilac .hero-title{font-size:40px}
  body.t-editorial .hero-title{font-size:42px}
  body .hero-desc{font-size:15px}
  body .hero{padding-top:48px}
  body .hero-mini{font-size:11px;max-width:100%;white-space:normal;line-height:1.7}
  body .hero-btns .btn{padding:12px 20px;font-size:13px}
  body .edit-marquee{font-size:20px}
  body .lucky-badge{font-size:11px}
  body .hero-stage{margin-top:36px}
  body .hero-collage{gap:10px}
  body .glass-hero{padding:24px 18px 18px}
  body .stat{padding:22px 20px}
  body .idea-card,body .path-item,body .promise,body .quote{padding:26px 22px}
}
"""

GALLERY_CSS = r'''
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:-apple-system,BlinkMacSystemFont,"PingFang SC","Microsoft YaHei",sans-serif;background:#f2f3f6;color:#1b1c20;height:100vh;display:flex;overflow:hidden}
a{text-decoration:none;color:inherit}
.side{width:296px;flex-shrink:0;background:#fff;border-right:1px solid #e4e5ea;display:flex;flex-direction:column;overflow-y:auto}
.side-top{padding:24px 22px 18px;border-bottom:1px solid #eef0f3}
.side-top .kicker{font-size:10.5px;letter-spacing:.22em;color:#9a9ca6;font-weight:700}
.side-top h1{font-size:20px;margin:10px 0 6px;letter-spacing:-.02em}
.side-top p{font-size:12px;color:#787a85;line-height:1.7}
.tag{display:inline-block;margin-top:12px;font-size:10.5px;background:#eef1f8;color:#4b5673;padding:5px 10px;border-radius:6px;font-weight:600}
.list{padding:14px;display:flex;flex-direction:column;gap:8px}
.item{display:flex;gap:12px;align-items:flex-start;padding:14px;border:1px solid #ebecf0;border-radius:12px;cursor:pointer;transition:.2s;background:#fff}
.item:hover{border-color:#c8cbd6;background:#fafbfe}
.item.on{border-color:#2f3542;background:#f7f8fb;box-shadow:0 6px 18px -12px #2f3542}
.num{width:28px;height:28px;flex-shrink:0;border-radius:8px;background:#eef0f4;color:#5a5d68;display:grid;place-items:center;font-size:11px;font-weight:700}
.item.on .num{background:#2f3542;color:#fff}
.item b{font-size:13.5px;display:block;line-height:1.3}
.item small{display:block;font-size:10px;color:#9a9ca6;letter-spacing:.08em;margin:4px 0 6px}
.item p{font-size:11.5px;color:#787a85;line-height:1.55}
.side-foot{margin-top:auto;padding:16px 22px 22px;border-top:1px solid #eef0f3;font-size:11px;color:#9a9ca6;line-height:1.7}
.main{flex:1;display:flex;flex-direction:column;min-width:0}
.bar{height:62px;background:#fff;border-bottom:1px solid #e4e5ea;display:flex;align-items:center;gap:14px;padding:0 22px;flex-shrink:0}
.bar .now{font-size:14px;font-weight:700}
.bar .now span{font-size:11px;font-weight:500;color:#9a9ca6;margin-left:8px;letter-spacing:.06em}
.devs{display:flex;gap:4px;margin-left:auto;background:#f2f3f6;padding:4px;border-radius:9px}
.devs button{font-size:11.5px;padding:7px 13px;border-radius:6px;color:#6b6d78;cursor:pointer;transition:.2s}
.devs button.on{background:#fff;color:#1b1c20;font-weight:700;box-shadow:0 2px 8px rgba(0,0,0,.07)}
.open{font-size:11.5px;border:1px solid #dfe1e8;padding:8px 13px;border-radius:8px;color:#4b4d58;cursor:pointer}
.open:hover{background:#f7f8fb}
.stage{flex:1;background:#e9ebf0;display:flex;align-items:flex-start;justify-content:center;padding:20px;overflow:auto}
.frame{background:#fff;box-shadow:0 20px 60px rgba(20,24,40,.14);border-radius:8px;overflow:hidden;transition:width .3s;flex-shrink:0}
.frame iframe{width:100%;height:100%;border:0;display:block}
@media(max-width:900px){body{flex-direction:column;height:auto;overflow:auto}.side{width:100%;border-right:0;border-bottom:1px solid #e4e5ea}.list{flex-direction:row;overflow-x:auto}.item{min-width:220px}.side-foot{display:none}.main{height:82vh}.stage{padding:10px}}
'''

GALLERY_JS = r'''
var themes=THEMES_JSON;
var frame=document.getElementById('frame'),iframe=document.getElementById('preview'),now=document.getElementById('now');
function show(i,w){
  var t=themes[i];
  iframe.src=t.file;
  now.innerHTML=t.name+'<span>'+t.en+'</span>';
  document.querySelectorAll('.item').forEach(function(el,j){el.classList.toggle('on',j===i)});
  setW(w||'desktop');
}
function setW(mode){
  document.querySelectorAll('.devs button').forEach(function(b){b.classList.toggle('on',b.dataset.m===mode)});
  if(mode==='desktop'){frame.style.width='100%';frame.style.height='100%';frame.style.maxWidth='none';}
  if(mode==='tablet'){frame.style.width='834px';frame.style.height='100%';frame.style.maxWidth='100%';}
  if(mode==='phone'){frame.style.width='390px';frame.style.height='100%';frame.style.maxWidth='100%';}
}
document.querySelectorAll('.item').forEach(function(el,i){el.addEventListener('click',function(){show(i)})});
document.querySelectorAll('.devs button').forEach(function(b){b.addEventListener('click',function(){setW(b.dataset.m)})});
document.getElementById('openBtn').addEventListener('click',function(){window.open(iframe.src,'_blank')});
show(0,'desktop');
'''


def build_gallery(themes):
    items = "".join(
        f'''<div class="item{' on' if i == 0 else ''}"><span class="num">{t['idx']:02d}</span>
        <div><b>{t['name']}</b><small>{t['en']}</small><p>{t['desc']}</p></div></div>'''
        for i, t in enumerate(themes)
    )
    import json
    payload = json.dumps([
        dict(file=f"design-{t['idx']:02d}-{t['key']}.html", name=t["name"], en=t["en"])
        for t in themes
    ], ensure_ascii=False)
    html = f'''<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>幸运无限官网 · 5 套浅色系设计稿</title>
<style>{GALLERY_CSS}</style></head><body>
<aside class="side">
  <div class="side-top"><div class="kicker">LUCKY INFINITE · WEB DESIGN</div>
  <h1>官网首页设计稿</h1><p>5 套浅色系视觉方向，信息架构与公开版文案完全一致，可直接对比挑选。</p>
  <span class="tag">浅色系 · 响应式 · 5 案</span></div>
  <div class="list">{items}</div>
  <div class="side-foot">文案来源：幸运无限官网公开版文案稿 v1.0<br>设备图形为 SVG 示意图，待替换产品实拍图。</div>
</aside>
<main class="main">
  <div class="bar"><div class="now" id="now"></div>
    <div class="devs"><button data-m="desktop" class="on">桌面</button><button data-m="tablet">平板</button><button data-m="phone">手机</button></div>
    <div class="open" id="openBtn">单独打开 ↗</div>
  </div>
  <div class="stage"><div class="frame" id="frame"><iframe id="preview" title="设计稿预览"></iframe></div></div>
</main>
<script>{GALLERY_JS.replace("THEMES_JSON", payload)}</script>
</body></html>'''
    path = os.path.join(OUT, "index.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    return path


if __name__ == "__main__":
    paths = [build_theme(t) for t in THEMES]
    paths.append(build_gallery(THEMES))
    for p in paths:
        print(os.path.basename(p), os.path.getsize(p), "bytes")
