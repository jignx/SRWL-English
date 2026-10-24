/** Verify a patch with an independently supplied xdelta-wasm decoder.
 * Usage: node tools/verify_web_patch.mjs decoder.js decoder.wasm source.nds patch.xdelta expected-sha256
 * Obtain the decoder from the upstream xdelta-wasm project; binaries are not bundled.
 */
import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import crypto from 'node:crypto';

const [decoder, wasm, source, patch, expected] = process.argv.slice(2);
if (!expected || !/^[a-f0-9]{64}$/i.test(expected)) {
  console.error('Usage: node tools/verify_web_patch.mjs decoder.js decoder.wasm source.nds patch.xdelta expected-sha256');
  process.exit(2);
}
const {default: createModule} = await import(pathToFileURL(path.resolve(decoder)).href);
const sourceFd = fs.openSync(source, 'r');
const patchFd = fs.openSync(patch, 'r');
const hash = crypto.createHash('sha256');
let size = 0;
let error;
try {
  const module = await createModule({wasmBinary: fs.readFileSync(wasm), noExitRuntime: true});
  function read(fd, pointer, offset, length) {
    return fs.readSync(fd, new Uint8Array(module.HEAP8.buffer, pointer, length), 0, length, Number(offset));
  }
  module.readSource = (...args) => read(sourceFd, ...args);
  module.readPatch = (...args) => read(patchFd, ...args);
  module.outputFile = (pointer, length) => {
    hash.update(new Uint8Array(module.HEAP8.buffer, pointer, length));
    size += length;
  };
  module.reportError = pointer => { error = module.UTF8ToString(pointer); };
  const code = module.callMain(['4194304', '32', '0']);
  const sha256 = hash.digest('hex');
  console.log(JSON.stringify({checksumEnabled: true, code, error, size, sha256}));
  if (code !== 0 || sha256 !== expected.toLowerCase()) process.exitCode = 1;
} finally {
  fs.closeSync(sourceFd);
  fs.closeSync(patchFd);
}
