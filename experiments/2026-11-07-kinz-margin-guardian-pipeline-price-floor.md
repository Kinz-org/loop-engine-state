# Idea: price floor and headroom for kinz-margin-guardian-pipeline

The pipeline says *after the fact* that a margin fell below the threshold, but never
answers the question a pricing decision needs first: "how low can the competitor price
go before this product alerts, and how much room do we have today?" Add a pure
`src/price_floor.py` (the lowest competitor price that keeps both the B2C and the B2B
margin at or above the threshold, given COGS and the B2B discount) and a
`scripts/price_floor.py` CLI that prints the floor and today's headroom for the demo
catalogue or for one product given on the command line.

Repo: Kinz-org/kinz-margin-guardian-pipeline. Branch: `claude/loop-creative-20261107-price-floor`.

## Success checks

1. `pytest tests/test_price_floor.py -q` passes and contains at least 8 tests.
2. **The floor agrees with the real engine.** For each of the 5 products in
   `scripts/demo.py`'s `DEMO_PRODUCTS`, with the default threshold (40%) and B2B
   discount (0.85): passing the computed floor price as `competitor_price` to
   `src.margin_engine.compute_product_margins` gives `b2c_alert == False` and
   `b2b_alert == False`, and passing `floor - 0.001` gives at least one alert.
   (Confirm with a short Python snippet, not only by reading the tests.)
3. `python scripts/price_floor.py --seed 42` exits 0 and prints a table with exactly
   5 product rows that includes a floor column and a headroom column. The products it
   marks as below the floor are exactly the ones `python scripts/demo.py --seed 42`
   marks `ALERT`.
4. `python scripts/price_floor.py --cogs 30` prints a floor of `58.819` TND.
   *(Amended before any code was written, see the note below. Originally `58.824`.)*
5. `python scripts/price_floor.py --cogs 30 --threshold 100` exits non-zero with a
   one-line error message and no Python traceback.
6. `ruff check .` is clean and `pytest tests/ -q` passes on the branch (no new failures
   or skips compared with `main`).

### Amendment to check 4 (made before any code was written)

Checking the arithmetic against the engine showed that checks 2 and 4 contradicted each
other. `compute_product_margins` rounds margins to 2 decimals before comparing them with
the threshold, so at COGS 30 the engine raises no alert down to 58.819 TND, below the
exact 30 / 0.6 / 0.85 = 58.8235…. A floor of 58.824 would fail check 2's
`floor - 0.001 alerts` half. Check 2 is the one that matters (the floor must agree with
the engine that actually raises the alerts), so check 4's expected number was corrected
to the engine-consistent value. The original text is kept above for the record.
