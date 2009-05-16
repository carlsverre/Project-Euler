#!/usr/bin/python

merged_list = map(lambda x: 3*x, range(1,334))
merged_list.extend(
    filter(lambda x: not x%3==0,
        map(lambda x: 5*x, range(1,200))
    )
)
print sum(merged_list)
