import { utilFoo } from "util/foo";
import jsc from 'jsverify';

function lala(a) {
  return !a;
}

function xyz(x, y) {
  if (y == 0) {
    return 0;
  }
  return x / y;
}

function ccc(a, b) {
  return (a + b).toLowerCase();
}

describe( "utilFoo", () => {
  it( "returns intended value", () => {
    const t = jsc.forall('string', 'string', function(a, b) {
      return ccc(a, b) === a.toLowerCase() + b;
    });
    jsc.assert(t);
  });

  it("xyz divided two numbers", () => {
    const t = jsc.forall("integer", "integer", function(a, b) {
      return xyz(a, b) == a / b;
    })
      jsc.assert(t)
  })
});
