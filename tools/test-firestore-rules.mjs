#!/usr/bin/env node
// Rules tests against the Firestore emulator. Does not talk to the live project.
//   npx firebase-tools emulators:exec --only firestore --project q-bank-cache \
//     "node tools/test-firestore-rules.mjs"
import { createHash, randomBytes } from 'crypto';

const project = 'q-bank-cache';
const emu = process.env.FIRESTORE_EMULATOR_HOST || '127.0.0.1:8080';
if (!/^(127\.0\.0\.1|localhost):(\d+)$/.test(emu)) {
  console.error('Refusing to run rules tests against', emu);
  process.exit(1);
}
const root = `http://${emu}/v1/projects/${project}/databases/(default)`;
const docs = `${root}/documents`;
const docName = path => `projects/${project}/databases/(default)/documents/${path}`;

const sha = s => createHash('sha256').update(s).digest('hex').toUpperCase();
const hex = (n, upper) => {
  const s = randomBytes(n).toString('hex');
  return upper ? s.toUpperCase() : s.slice(0, n * 2);
};
const secret = () => hex(32, true);
const pid = () => hex(16, false);
const ts = () => new Date().toISOString();
const S = v => ({ stringValue: v });
const I = v => ({ integerValue: String(v) });
const B = v => ({ booleanValue: v });
const A = values => ({ arrayValue: { values } });
const M = fields => ({ mapValue: { fields } });

let failed = 0;
async function call(method, url, body) {
  const res = await fetch(url, {
    method,
    headers: { 'Content-Type': 'application/json' },
    body: body === undefined ? undefined : JSON.stringify(body),
  });
  const text = await res.text();
  return { status: res.status, text };
}
function check(name, cond, extra) {
  if (cond) console.log('  ok', name);
  else { failed++; console.error('FAIL', name, extra || ''); }
}
async function expectStatus(name, method, url, body, status) {
  const res = await call(method, url, body);
  check(name, res.status === status, `got ${res.status} ${res.text.slice(0, 300)}`);
  return res;
}

function progressFields(block) {
  return {
    [`${block}_flags_v1`]: S('{}'),
    [`${block}_progress_v1`]: S('{"sdl-1":{"last":null,"best":null}}'),
    [`${block}_attempts_v1`]: S('[]'),
    [`${block}_settings_v1`]: S('{"hyOnly":false}'),
    _updatedAt: { timestampValue: ts() },
  };
}

async function main() {
  console.log('emulator', emu);

  // ----- syncs: no list, exact id, shape -----
  await expectStatus('list syncs denied', 'GET', `${docs}/syncs?pageSize=5`, undefined, 403);
  await expectStatus('query syncs denied', 'POST', `${docs}:runQuery`, {
    structuredQuery: { from: [{ collectionId: 'syncs' }] },
  }, 403);

  const pin = 'MGVMZA';
  await expectStatus('create block doc', 'PATCH', `${docs}/syncs/${pin}_psych`, { fields: progressFields('psych') }, 200);
  const got = await expectStatus('get block doc', 'GET', `${docs}/syncs/${pin}_psych`, undefined, 200);
  check('block doc round-trips', got.text.includes('psych_flags_v1'));
  await expectStatus('bad block field denied', 'PATCH', `${docs}/syncs/${pin}_psych`, {
    fields: { ...progressFields('psych'), evil: S('x') },
  }, 403);
  await expectStatus('short pin denied', 'PATCH', `${docs}/syncs/ABC`, { fields: progressFields('psych') }, 403);
  await expectStatus('wrong block key denied', 'PATCH', `${docs}/syncs/${pin}_psych`, {
    fields: {
      neuro_flags_v1: S('{}'),
      _updatedAt: { timestampValue: ts() },
    },
  }, 403);
  await expectStatus('atlas doc', 'PATCH', `${docs}/syncs/${pin}_atlas`, {
    fields: { 'mla-progress': S('{"rev":{}}'), _updatedAt: { timestampValue: ts() } },
  }, 200);
  await expectStatus('legacy marker', 'PATCH', `${docs}/syncs/${pin}`, {
    fields: { _migratedAt: { timestampValue: ts() } },
  }, 200);
  await expectStatus('legacy progress still accepted', 'PATCH', `${docs}/syncs/ABC120`, {
    fields: {
      psych_flags_v1: S('{"1":true}'),
      _updatedAt: { timestampValue: ts() },
    },
  }, 200);
  await expectStatus('non-json progress denied', 'PATCH', `${docs}/syncs/${pin}_nephro`, {
    fields: { nephro_flags_v1: S('hello'), _updatedAt: { timestampValue: ts() } },
  }, 403);

  const big = 'x'.repeat(1100000);
  // A single field this large is rejected by the API itself (400), before rules.
  const huge = await call('PATCH', `${docs}/syncs/${pin}_gastro`, {
    fields: { gastro_attempts_v1: S('[' + JSON.stringify(big) + ']'), _updatedAt: { timestampValue: ts() } },
  });
  check('oversize doc denied', huge.status === 400 || huge.status === 403, `got ${huge.status} ${huge.text.slice(0, 180)}`);

  const reportId = 'QREPORT-nephro-1763000000000-ab12cd';
  const report = {
    fields: {
      kind: S('question-report'), block: S('nephro'), qid: S('sdl01_q01'), reason: S('typo'),
      note: S('page 3'), exam: S('1'), sdl: S('1'), picked: S('A'), stem: S('A short stem'),
      _createdAt: { timestampValue: ts() },
    },
  };
  await expectStatus('create report', 'PATCH', `${docs}/syncs/${reportId}`, report, 200);
  await expectStatus('overwrite report denied', 'PATCH', `${docs}/syncs/${reportId}`, report, 403);
  await expectStatus('get report by id', 'GET', `${docs}/syncs/${reportId}`, undefined, 200);
  await expectStatus('delete report by id', 'DELETE', `${docs}/syncs/${reportId}`, undefined, 200);
  await expectStatus('other collection denied', 'PATCH', `${docs}/notes/x`, { fields: { a: S('b') } }, 403);

  // ----- live: create, no token on the room, host proof, join, answer, score -----
  const code = 'K7QRT';
  const host = secret();
  const roomFields = {
    block: S('psych'), status: S('lobby'), currentIndex: I(0), revealed: B(false), locked: B(false),
    questionIds: A([S('sdl01_q01'), S('sdl01_q02')]),
    autoAdvanceSeconds: I(0), createdAt: I(Date.now()),
    participantIds: A([]), joinPid: S(''),
  };
  await expectStatus('room without secret denied', 'POST', `${docs}:commit`, { writes: [
    { update: { name: docName(`live_sessions/${code}`), fields: roomFields }, currentDocument: { exists: false } },
  ]}, 403);
  await expectStatus('create room + secret', 'POST', `${docs}:commit`, { writes: [
    { update: { name: docName(`live_sessions/${code}`), fields: roomFields }, currentDocument: { exists: false } },
    { update: { name: docName(`live_sessions/${code}/private/host`), fields: { token: S(host) } }, currentDocument: { exists: false } },
  ]}, 200);
  const room = await expectStatus('get room', 'GET', `${docs}/live_sessions/${code}`, undefined, 200);
  check('room has no hostToken', !room.text.includes('hostToken') && !room.text.includes(host));
  await expectStatus('secret unreadable', 'GET', `${docs}/live_sessions/${code}/private/host`, undefined, 403);
  await expectStatus('list rooms denied', 'GET', `${docs}/live_sessions?pageSize=5`, undefined, 403);
  await expectStatus('list players denied', 'GET', `${docs}/live_sessions/${code}/participants?pageSize=5`, undefined, 403);
  await expectStatus('query answers denied', 'POST', `${docs}/live_sessions/${code}:runQuery`, {
    structuredQuery: { from: [{ collectionId: 'answers' }], where: { fieldFilter: { field: { fieldPath: 'qIndex' }, op: 'EQUAL', value: I(0) } } },
  }, 403);

  const reveal = (token, status, extra) => ({ writes: [
    { update: { name: docName(`live_sessions/${code}/private/host`), fields: { token: S(token) } }, updateMask: { fieldPaths: ['token'] }, currentDocument: { exists: true } },
    { update: { name: docName(`live_sessions/${code}`), fields: Object.assign({ status: S(status), currentIndex: I(0), revealed: B(false), locked: B(false) }, extra || {}) },
      updateMask: { fieldPaths: ['status', 'currentIndex', 'revealed', 'locked'].concat(extra ? Object.keys(extra) : []) },
      currentDocument: { exists: true } },
  ]});
  await expectStatus('host update without proof denied', 'PATCH', `${docs}/live_sessions/${code}?updateMask.fieldPaths=status`, {
    fields: { status: S('active') },
  }, 403);
  await expectStatus('wrong host token denied', 'POST', `${docs}:commit`, reveal('A'.repeat(64), 'active'), 403);
  let token = sha(host);
  await expectStatus('host can start', 'POST', `${docs}:commit`, reveal(token, 'active'), 200);
  await expectStatus('host cannot rewrite question list', 'POST', `${docs}:commit`, reveal(sha(token), 'active', {
    questionIds: A([S('other')]),
  }), 403);

  const player = pid();
  const psec = secret();
  const roomNow = await call('GET', `${docs}/live_sessions/${code}`);
  const updateTime = JSON.parse(roomNow.text).updateTime;
  await expectStatus('join', 'POST', `${docs}:commit`, { writes: [
    { update: { name: docName(`live_sessions/${code}`), fields: { participantIds: A([S(player)]), joinPid: S(player) } },
      updateMask: { fieldPaths: ['participantIds', 'joinPid'] }, currentDocument: { updateTime } },
    { update: { name: docName(`live_sessions/${code}/participants/${player}`), fields: {
      name: S('Sam'), score: I(0), joinedAt: I(Date.now()), scored: M({}),
    } }, currentDocument: { exists: false } },
    { update: { name: docName(`live_sessions/${code}/participants/${player}/secret/key`), fields: { token: S(psec) } }, currentDocument: { exists: false } },
  ]}, 200);
  await expectStatus('player secret unreadable', 'GET', `${docs}/live_sessions/${code}/participants/${player}/secret/key`, undefined, 403);
  const pub = await expectStatus('host can get player by id', 'GET', `${docs}/live_sessions/${code}/participants/${player}`, undefined, 200);
  check('player name visible', pub.text.includes('Sam'));
  check('player token not on profile', !pub.text.includes(psec));

  let ptoken = sha(psec);
  const answer = (tok, choice) => ({ writes: [
    { update: { name: docName(`live_sessions/${code}/participants/${player}/secret/key`), fields: { token: S(tok) } }, updateMask: { fieldPaths: ['token'] }, currentDocument: { exists: true } },
    { update: { name: docName(`live_sessions/${code}/answers/0_${player}`), fields: { choice: S(choice), qIndex: I(0), ts: I(Date.now()) } } },
  ]});
  await expectStatus('answer', 'POST', `${docs}:commit`, answer(ptoken, 'C'), 200);
  ptoken = sha(ptoken);
  await expectStatus('change answer', 'POST', `${docs}:commit`, answer(ptoken, 'A'), 200);
  await expectStatus('get answer by id', 'GET', `${docs}/live_sessions/${code}/answers/0_${player}`, undefined, 200);

  token = sha(token);
  await expectStatus('host reveals', 'POST', `${docs}:commit`, { writes: [
    { update: { name: docName(`live_sessions/${code}/private/host`), fields: { token: S(token) } }, updateMask: { fieldPaths: ['token'] }, currentDocument: { exists: true } },
    { update: { name: docName(`live_sessions/${code}`), fields: { revealed: B(true) } }, updateMask: { fieldPaths: ['revealed'] }, currentDocument: { exists: true } },
  ]}, 200);

  await expectStatus('answer after reveal denied', 'POST', `${docs}:commit`, answer(sha(ptoken), 'B'), 403);
  const me = JSON.parse((await call('GET', `${docs}/live_sessions/${code}/participants/${player}`)).text);
  ptoken = sha(ptoken);
  await expectStatus('score once', 'POST', `${docs}:commit`, { writes: [
    { update: { name: docName(`live_sessions/${code}/participants/${player}/secret/key`), fields: { token: S(ptoken) } }, updateMask: { fieldPaths: ['token'] }, currentDocument: { exists: true } },
    { update: { name: docName(`live_sessions/${code}/participants/${player}`), fields: { score: I(1), scored: M({ '0': B(true) }) } },
      updateMask: { fieldPaths: ['score', 'scored'] }, currentDocument: { exists: true } },
  ]}, 200);
  ptoken = sha(ptoken);
  await expectStatus('score twice denied', 'POST', `${docs}:commit`, { writes: [
    { update: { name: docName(`live_sessions/${code}/participants/${player}/secret/key`), fields: { token: S(ptoken) } }, updateMask: { fieldPaths: ['token'] }, currentDocument: { exists: true } },
    { update: { name: docName(`live_sessions/${code}/participants/${player}`), fields: { score: I(2), scored: M({ '0': B(true) }) } },
      updateMask: { fieldPaths: ['score', 'scored'] }, currentDocument: { exists: true } },
  ]}, 403);

  // someone who is not the host cannot delete, even naming every doc
  await expectStatus('delete room without proof denied', 'DELETE', `${docs}/live_sessions/${code}`, undefined, 403);

  token = sha(token);
  await expectStatus('host cleanup', 'POST', `${docs}:commit`, { writes: [
    { update: { name: docName(`live_sessions/${code}/private/host`), fields: { token: S(token) } }, updateMask: { fieldPaths: ['token'] }, currentDocument: { exists: true } },
    { delete: docName(`live_sessions/${code}/answers/0_${player}`) },
    { delete: docName(`live_sessions/${code}/answers/1_${player}`) },
    { delete: docName(`live_sessions/${code}/participants/${player}/secret/key`) },
    { delete: docName(`live_sessions/${code}/participants/${player}`) },
    { delete: docName(`live_sessions/${code}`) },
  ]}, 200);
  await expectStatus('room gone', 'GET', `${docs}/live_sessions/${code}`, undefined, 404);
  await expectStatus('delete leftover secret', 'DELETE', `${docs}/live_sessions/${code}/private/host`, undefined, 200);

  // locked room rejects a new player. Build a fresh room.
  const alphabet = 'ABCDEFGHJKMNPQRSTUVWXYZ23456789';
  const code2 = Array.from(randomBytes(5), b => alphabet[b % alphabet.length]).join('');
  const host2 = secret();
  await expectStatus('second room', 'POST', `${docs}:commit`, { writes: [
    { update: { name: docName(`live_sessions/${code2}`), fields: roomFields }, currentDocument: { exists: false } },
    { update: { name: docName(`live_sessions/${code2}/private/host`), fields: { token: S(host2) } }, currentDocument: { exists: false } },
  ]}, 200);
  await expectStatus('host locks room', 'POST', `${docs}:commit`, { writes: [
    { update: { name: docName(`live_sessions/${code2}/private/host`), fields: { token: S(sha(host2)) } }, updateMask: { fieldPaths: ['token'] }, currentDocument: { exists: true } },
    { update: { name: docName(`live_sessions/${code2}`), fields: { locked: B(true) } }, updateMask: { fieldPaths: ['locked'] }, currentDocument: { exists: true } },
  ]}, 200);
  const p2 = pid();
  await expectStatus('join locked room denied', 'POST', `${docs}:commit`, { writes: [
    { update: { name: docName(`live_sessions/${code2}`), fields: { participantIds: A([S(p2)]), joinPid: S(p2) } },
      updateMask: { fieldPaths: ['participantIds', 'joinPid'] }, currentDocument: { exists: true } },
    { update: { name: docName(`live_sessions/${code2}/participants/${p2}`), fields: { name: S('Jo'), score: I(0), joinedAt: I(Date.now()), scored: M({}) } }, currentDocument: { exists: false } },
    { update: { name: docName(`live_sessions/${code2}/participants/${p2}/secret/key`), fields: { token: S(secret()) } }, currentDocument: { exists: false } },
  ]}, 403);
  await expectStatus('host removes locked room', 'POST', `${docs}:commit`, { writes: [
    { update: { name: docName(`live_sessions/${code2}/private/host`), fields: { token: S(sha(sha(host2))) } }, updateMask: { fieldPaths: ['token'] }, currentDocument: { exists: true } },
    { delete: docName(`live_sessions/${code2}`) },
  ]}, 200);
  await call('DELETE', `${docs}/live_sessions/${code2}/private/host`);

  void me;

  await expectStatus('research block doc', 'PATCH', `${docs}/syncs/${pin}_research`, { fields: progressFields('research') }, 200);
  await expectStatus('settings updatedAt stays inside the JSON', 'PATCH', `${docs}/syncs/${pin}_research`, {
    fields: {
      research_settings_v1: S('{"hyOnly":false,"updatedAt":' + Date.now() + '}'),
      _updatedAt: { timestampValue: ts() },
    },
  }, 200);
  const researchDoc = JSON.parse((await call('GET', `${docs}/syncs/${pin}_research`)).text);
  const precondition = await call('POST', `${docs}:commit`, { writes: [{
    update: { name: docName(`syncs/${pin}_research`), fields: progressFields('research') },
    currentDocument: { updateTime: researchDoc.updateTime },
  }] });
  check('updateTime precondition patch', precondition.status === 200, `${precondition.status} ${precondition.text.slice(0, 200)}`);
  const stale = await call('POST', `${docs}:commit`, { writes: [{
    update: { name: docName(`syncs/${pin}_research`), fields: progressFields('research') },
    currentDocument: { updateTime: '2000-01-01T00:00:00.000Z' },
  }] });
  check('stale updateTime rejected', stale.status === 400 || stale.status === 409, `${stale.status} ${stale.text.slice(0, 180)}`);

  const code3 = 'HJKM3';
  const host3 = secret();
  const oldFields = Object.assign({}, roomFields, { block: S('research'), createdAt: I(Date.now() - 25 * 60 * 60 * 1000) });
  await expectStatus('create day-old research room', 'POST', `${docs}:commit`, { writes: [
    { update: { name: docName(`live_sessions/${code3}`), fields: oldFields }, currentDocument: { exists: false } },
    { update: { name: docName(`live_sessions/${code3}/private/host`), fields: { token: S(host3) } }, currentDocument: { exists: false } },
  ]}, 200);
  await expectStatus('expired room deletes without host token', 'POST', `${docs}:commit`, { writes: [
    { delete: docName(`live_sessions/${code3}/private/host`) },
    { delete: docName(`live_sessions/${code3}`) },
  ]}, 200);

  if (failed) {
    console.error(`\n${failed} failed`);
    process.exit(1);
  }
  console.log('\nall rules checks passed');
}

main().catch(err => { console.error(err); process.exit(1); });
