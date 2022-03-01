Suppose you have created a social networking application, in which users can sign-up and be friends with other users. Your application has 3 APIs:
add_user(email) - adds user to the system.
befriend(email1, email2) - creates a friendship between the two given users.
check_friendship(email1, email2) - checks whether the two given users are directly or indirectly friends. Indirect friends meaning they have a connectivity via their friends of friends of... friends.
Constraint: The check_friendship API should take O(1) time.


{email1: [(email3, email2), (email4)],
 email2: [(email4, email1), (email3)],
 email3: [{email1, email4}, (email2, email5)],
 email4: [{(email2, email3, email5})],
 email5: [{email4}]}


{email2: [(email1), ()]}

1 is friend with 2 and 3.
2 is friend with 1 and 4
3 is friend with 1 and 4
4 is friend with 2, 3 and 5
5 is friend with 4.
1, 5 - None
1, 2 - directly
1, 4 - indirect
