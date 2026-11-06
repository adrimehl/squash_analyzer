// Misst die automatische Ballwechsel-Erkennung gegen die von Hand geprüften Ballwechsel.
const fs = require('fs');
const lib = require(process.argv[2]);
const j = JSON.parse(fs.readFileSync(process.argv[3], 'utf8'));
const res = { own: true, dur: j.dauer_s, t0: j.t0, vid: j.video, cal: j.kalibrierung, noAudio: j.ton_ignoriert,
  tracks: j.tracks.map(tr => tr.map(([t, x, y]) => ({ t, x, y }))), pose: j.pose, hits: j.ballgeraeusche, hitSwing: j.schlagbewegung_bei_geraeusch,
  swings: j.schwuenge, swingWin: j.schwung_fenster, dense: j.positionen_20fps, rallyFix: {} };
const EX = lib.computeExcl(res), D = lib.deepAnalysis(res, EX), F = lib.FPS, t0 = EX.t0;
const auto = D.rallies.map(r => ({ a: t0 + r.a / F, b: t0 + r.b / F }));
const truth = j.ballwechsel.map(r => ({ a: r.beginn, b: r.ende }));
const ov = (p, q) => Math.max(0, Math.min(p.b, q.b) - Math.max(p.a, q.a));
const used = new Set(), pairs = [];
truth.forEach((g, i) => { let best = -1, bo = 0; auto.forEach((r, k) => { const o = ov(g, r); if (!used.has(k) && o > bo) { bo = o; best = k; } });
  if (best >= 0 && bo >= 0.3 * (g.b - g.a)) { used.add(best); pairs.push([i, best]); } });
const fn = truth.filter((_, i) => !pairs.some(p => p[0] === i)), fp = auto.filter((_, k) => !used.has(k));
const dA = pairs.map(([i, k]) => auto[k].a - truth[i].a), dB = pairs.map(([i, k]) => auto[k].b - truth[i].b);
const med = a => { const s = [...a].sort((x, y) => x - y); return s.length ? s[s.length >> 1] : null; }, f1 = v => v == null ? '–' : (v > 0 ? '+' : '') + v.toFixed(1);
console.log(`gefunden ${pairs.length}/${truth.length} | fehlen ${fn.length} [${fn.map(g => g.a.toFixed(0)).join(',')}] | falsch ${fp.length} [${fp.map(r => r.a.toFixed(0)).join(',')}]`);
console.log(`Beginn: Median ${f1(med(dA))} s | Ende: Median ${f1(med(dB))} s, mittl. Betrag ${(dB.reduce((s, v) => s + Math.abs(v), 0) / Math.max(1, dB.length)).toFixed(1)} s, max ${f1(dB.length ? dB.reduce((m, v) => Math.abs(v) > Math.abs(m) ? v : m, 0) : null)}`);
if (process.argv[4] === '-v') { console.log('Ende-Abweichung je Ballwechsel:', pairs.map(([i, k], n) => `${truth[i].a.toFixed(0)}:${f1(dB[n])}`).join(' '));
  console.log('Aufschläge:', D.serves.map(s => s.t).join(', '), '| Quelle:', D.rallySrc); }
module.exports = {};
