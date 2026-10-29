# Motion audit
| Item | Duration / ease | Verdict |
|---|---|---|
| Hero line rise | 1.1s, ease-out, 80ms stagger | Keep (one-off brand moment) |
| Hero photo settle | 1.6s scale 1.08 to 1 | Keep |
| Section reveal | .9s, 24px rise | Keep; add 60ms list stagger |
| Buttons | 160 to 250ms, press .97 | Keep |
| Menu open | 300ms fade + 8px | Keep |
| Burger morph | 300ms | Keep |
| Floating card | 300ms | Keep; hide over forms |
| FAQ icon | 300ms rotate | Keep |
| Guide image hover | .6s scale 1.03, hover devices only | Keep |
| Reduced motion | fades only, hero static | Pass |
All triggered by IntersectionObserver; no scroll listeners.
