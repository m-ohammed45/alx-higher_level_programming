#!/usr/bin/node

function repeat(func, times) {
  if (times > 0) {
    func();
    repeat(func, times - 1);
  }
}
