# Benchmark sample tooling

The Benchmark Before Choosing rule asks for a count across ten to fifteen
recent publications from the target venue. The `style_bench` tool supports
that count mechanically: pass each sampled entry as one argument and it
numbers the sample and reports its size, so the pattern across the set can
be recorded alongside the count itself.

Run it through the context resolver (`ctxmod tool run style_bench ...`);
the tool is read-only and takes no environment.
