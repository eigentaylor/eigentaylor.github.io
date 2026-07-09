#!/usr/bin/env node
// PostToolUse hook (Write|Edit): auto-formats .liquid/.html files with prettier
// so we don't hit CI's `npx prettier . --check` formatting failures.
let data = "";
process.stdin.on("data", (c) => (data += c));
process.stdin.on("end", () => {
  let input;
  try {
    input = JSON.parse(data);
  } catch {
    process.exit(0);
  }

  const filePath = input.tool_input && input.tool_input.file_path;
  if (!filePath || !/\.(liquid|html)$/i.test(filePath)) process.exit(0);

  const { execFileSync } = require("child_process");
  try {
    execFileSync("npx", ["prettier", "--write", filePath], {
      stdio: "inherit",
      shell: true,
    });
  } catch {
    // non-blocking: don't fail the tool call if prettier errors
  }
  process.exit(0);
});
