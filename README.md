# Summary

|№ | String        | Result              |
|- | :-----------: | :-----------------: |
|1 |    (())       |     valid           |
|2 |     ""        |     valid           |
|3 |     (()       |     invalid         |
|4 |     )(()      |     invalid         |
|5 |     (((       |     invalid         |
|6 |     )))       |     invalid         |
|7 |    [{()}]     |     valid           |
|8 |    {[(])}     |     invalid         |
|9 |    ({]}       |     invalid         |
|10|    ({)}       |     invalid         |
