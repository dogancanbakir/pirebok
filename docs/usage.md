# Usage

To use pirebok in a project

```
from pirebok.fuzzers import FuzzerBuilder
fuzzer_builder = FuzzerBuilder()
fuzzer = fuzzer_builder.choice("RandomGenericFuzzer").build()
fuzzer.fuzz("<script> ")
```

To use from CLI

```
pirebok --help
Usage: pirebok [OPTIONS]

Options:
  -f, --fuzzer [RandomGenericFuzzer|GuidedRandomSqlFuzzer|RandomSqlFuzzer]
                                  choose fuzzer  [required]
  -s, --steps INTEGER             Number of iteration
  -p, --payload TEXT              payload to fuzz  [required]
  --help                          Show this message and exit.
```
