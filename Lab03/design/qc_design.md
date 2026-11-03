## Problem
 - Input  
 The system will receive these inputs:
   - length (Length of the sequence)
   - n_count (Number of unknoen base)
   - gc (GC percentage)
   - quals (quality score)
   - thresohold (20)

 - Output 
 
 classify_read function will returns one of these three decisions:
   - "reject"
   - "review"
   - "pass"

 trim_low_quality function will return:
   - number of bases to keep after trimming the low quality 3' tail

 - Constraints
    - length < 500 (reject)
    - n_count > 10 (review)
    - gc must in gc_range equal or between  30 and 70
    - quality scores below threshold (20) at the 3 end are trimmed
    - empty quality list return 0

## Pseudocode
   - FUNCTION classify_read(length, n_count, gc):

            MIN_LEN = 500
            MAX_N = 10
            GC_LOW = 30.0
            GC_HIGH = 70.0

            IF length < MIN_LEN:
                RETURN "reject"

            IF n_count > MAX_N OR NOT (GC_LOW <= gc <= GC_HIGH):
                RETURN "review"

            RETURN "pass"

     END FUNCTION

   - FUNCTION trim_low_quality(quals, threshold):

            end = LENGTH(quals)   

            WHILE end > 0 AND quals[end - 1] < threshold:
                end = end - 1
            END WHILE

            RETURN end

     END FUNCTION

## Flowchart

                            +-------+
                            | Start |
                            +-------+
                                |
                                v
                         +---------------+
                         | length < 500? |
                         +---------------+
                                |
                             +--+--+
                             |     |
                            Yes    No
                           |         |
                           v         v
                    +--------+     +-----------------------------+
                    | Reject |     | N > 10 or GC outside 30-70? |
                    +--------+     +-----------------------------+
                                            |
                                        +---+---+
                                        |        |
                                       Yes       No
                                       |         |
                                       v         v
                                  +--------+   +------+
                                  | Review |   | Pass |
                                  +--------+   +------+
                                        |        |
                                        +----+---+
                                             |
                                             v
                                          +-----+
                                          | End |
                                          +-----+

## Trace

| sample | length | n_count |  gc  | length < 500? | N > 10 or GC outside 30-70? | decision |
|--------|--------|---------|------|---------------|-----------------------------|----------|
|  R03   |  420   |    0    | 68.5 |     Yes       |            No               |  Reject  |
|  R04   |  500   |   10    | 45.0 |     No        |            No               |  Pass    |
|  R05   |  640   |    3    | 72.4 |     No        |            Yes              |  Review  |
|  R07   |  499   |    0    | 50.0 |     Yes       |            No               |  Reject  |