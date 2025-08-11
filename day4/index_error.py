# IndexError
# 인덱스 범위 초과 오류(list index out of range)
#Index Error
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
                     "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
                     "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
                     "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
                     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                     "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
                     "New Mexico", "Arizona", "Alaska", "Hawaii"] # 0~49인덱스, 총 50개의 아이템

print(len(states_of_america)) # 50

print(states_of_america[49]) # Hawaii
# print(states_of_america[50]) # IndexError: list index out of range

index_num_states : int = len(states_of_america)
# print(states_of_america[index_num_states]) # IndexError: list index out of range

print(states_of_america[index_num_states - 1]) # Hawaii
